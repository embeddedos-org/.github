# MCP layer + API layer — org audit (2026-10-24)

The 2026-10-24 standing directives require EmbeddedOS to present
two org-wide layers: an **MCP layer** (agents reach platform
capabilities as tools) and an **API layer** (stable, versioned
programmatic surface — ROS 2 nodes, MQTT brokers and third-party
apps integrate without an agent). This audit is the first
written map of what the org actually exposes on each layer.

**Method.** Every row below comes from a tree or file read at
the repo's HEAD on 2026-10-24 (evening): file trees for all
repos in the org, plus content reads of every `server.json`,
MCP server implementation, and contract named. Cells that could
not be evidenced from a read say "not yet assessed" — nothing
here is carried forward from plan prose. Where a fact is
external (the MCP specification), it was fetched first-party
from modelcontextprotocol.io on 2026-10-24 and is marked as
such. No issues are filed from this audit alone: a gap becomes
an issue on the day its slice is taken.

## 1. MCP-layer inventory

Exactly **three** repos carry a `server.json`, and exactly
**two** carry a working MCP tool server. The rest of the org's
MCP surface is policy, analysis, and third-party bridges.

| Repo | server.json | MCP server | Tools / surface | Transport |
| --- | --- | --- | --- | --- |
| EoSim | yes — `io.github.embeddedos-org/eosim`, v3.1.0 | yes — `eosim/mcp/` (stdio, `python -m eosim.mcp`) | 8 tools: `list_platforms`, `sim_launch`, `sim_build`, `sim_flash`, `sim_status`, `console_tail`, `gpio_poke`, `net_capture` (mutating tools dry-run by default) | stdio |
| eFlow | yes — `io.github.embeddedos-org/eflow`, v0.1.0 | yes — `eflow/mcp_server.py` + `eflow/mcp_tools.py` | 1 tool: `eflow_validate` — validates a flow document, executes nothing, `readOnlyHint: true`; input is the document, never a host path | stdio |
| eosllm | yes — `io.github.embeddedos-org/eosllm`, v0.1.0 | **no MCP tool server** — the card declares an SSE remote at `127.0.0.1:7777`, but the implementation (`tools/eosllm-server`, `docs/server.md`) is an HTTP/SSE **API-layer daemon** (`/healthz`, `/caps`, `/generate`) | see §3 — a classification gap, recorded in §5 | HTTP/SSE (API layer) |
| the on-device agent repo (private; unnamed here per this repo's canon rule) | no | no server — a **tool-use policy** instead: `vera/safety/mcp_policy.py` + `docs/mcp-tool-use-policy.md` (server allowlist, pinned identity, no commands from config) | policy surface | — |
| eSec | no | no — the **normative source**: `docs/mcp-hostile-protocol-hardening.md`, Controls 1–9 | controls | — |
| eIPC | no | no — analysis only: `docs/mcp-attack-classes-ipc.md` maps the six MCP attack classes onto the IPC surface | analysis | — |
| eNet | no | no — third-party bridge evaluation: `docs/mcp-bridge-evaluation.md` + `docs/mcp-bridge-trial-plan.md` (mcp2mqtt / mcp2tcp / modbus-mcp); the trial is environment-blocked (no broker in the sandbox) | bridges (external) | — |
| eApps | no | no server — a roadmap statement: `docs/ai-tool-policy.md` says agent tools should be wrapped as MCP tools in a future iteration, deferred until real tool execution exists | policy / roadmap | — |
| all other repos | no | no MCP surface found in tree reads (filename census cross-checked by a full-text MCP search in the architect pass) | — | — |

All three `server.json` files are validated by this repo's
reusable workflow (`docs/reusable-server-json-standard.md`);
each of the three repos carries a `server-json.yml` caller.
One stale cell found while auditing: that standard's
worked-examples table lists EoSim's `expected_version` as
`3.0.2`; EoSim's live caller pins `3.1.0`, matching its
`server.json`. The table is the stale side.

### The protocol-version axis (first-party spec read)

Both stdio servers declare `PROTOCOL_VERSION = "2026-07-28"`
in code and answer the `initialize` handshake with it. The
specification fetched first-party on 2026-10-24 says the
2026-07-28 revision **removed** that handshake: it is the
stateless revision (no protocol sessions, no
`Mcp-Session-Id`, version carried per-request in `_meta`, a
mandatory `server/discover` RPC), superseding 2025-11-25,
which was the stateful handshake era. The org's servers
therefore carry a **new-era version label on an old-era wire
shape**. This audit records that as a fact to resolve at
gateway evaluation time — which behaviour a gateway must
speak to these servers is an empirical question (record what
each endpoint actually negotiates), not something either
label settles. The claimed 2026-11-25 revision sometimes
cited for the spec is **unverified** — no first-party page
announces it.

A question this surfaces for eSec Control 9 (responses bound
to the connection that created them): in the stateless era
there is no protocol session to bind to, so binding — where
it exists — is to the authenticated connection or an explicit
server-minted handle. Recorded here as a question for the
gateway evaluation and the control's next revision; this
audit does not rewrite the control.

## 2. Entry requirements — eSec Controls as the gate

Anything exposed on the MCP layer must meet eSec's controls.
The load-bearing four for exposure:

- **Control 6** — no executable commands from configuration;
  tool registration declares exact command allowlists.
- **Control 7** — authorization-server identity is pinned,
  never discovered from the counterparty.
- **Control 8** — authentication has **no fallback path**; a
  failed or absent credential is terminal; sessions are a
  bounded resource.
- **Control 9** — responses and tasks are bound to the
  connection that created them: routing keyed by
  (connection, id), never by id alone.

Assessment against the inventoried servers, only where a read
evidences it: EoSim and eFlow are **stdio** servers — the
trust boundary is the local process launch, they run no OAuth
or network session surface, so Controls 7–9 do not reach them
as built (the standing exposure assessment in eSec's own doc
agrees). What *is* evidenced: eFlow's tool is validate-only
with document-not-path input (Control 6's spirit, by design);
EoSim's mutating tools are dry-run by default. The moment
either server is exposed over a network transport — which is
what a gateway does — Controls 7–9 apply in full and every
cell becomes "not yet assessed" until the gateway's behaviour
is measured. eosllm's HTTP daemon already listens on a socket
(localhost): its authentication posture against Control 8 is
**not yet assessed**.

## 3. API-layer inventory

| Surface | Contract | Implementation state (read at HEAD) |
| --- | --- | --- |
| eos sockets / DNS | `net/include/eos/net.h` socket API | **Real** on the Compute profile (`net/src/net_posix.c`, POSIX mapping per ADR-014); freestanding fallback in `net.c` returns -1 honestly until lwIP lands (Nano/Edge, ADR-014) |
| eos MQTT client | `net.h` MQTT section (config struct + 6 functions) | **Stub** — every function returns -1 / `EOS_MQTT_INVALID`; no POSIX variant (ADR-014 point 5 reserved the decision). Design doc landed today in eos (`docs/eos-mqtt-client-design.md`, commit `c313e66d`); tracker eos#199 |
| eos HTTP client / mDNS | `net.h` HTTP + mDNS sections | **Stub**, same ADR-014 point 5 reservation; separate future decisions |
| eNI ROS 2 package | `integrations/ros2/` — rclc package (`package.xml` depends on `rclc`, `std_msgs`, `sensor_msgs`), node + `NeuralIntent` / `NeuralSignal` messages | **Real but partial** — a genuine rclc node package; micro-ROS itself exists nowhere in eos yet |
| EoSim ROS 2 bridge | `eosim/integrations/ros2.py` (rclpy) | **Partial** — `connect()` works; `publish` / `subscribe` raise `NotImplementedError` |
| ebuild backends | backend implementations for freertos / nuttx / zephyr / buildroot / kbuild (plus cmake / meson / ninja / cargo / make / autotools) | **Real** as build targets; documented install/interop paths on top of them are the interop directive's open work, not yet written |
| ebuild eAI connector framework | `layers/eai/framework/` connector ops (incl. `connector_mqtt.c`) | **Framework real, transports stub** — the MQTT connector logs publishes and returns canned reads; it integrates against the eos client once eos#199 lands |
| eosllm daemon | `docs/server.md` — `GET /healthz`, `GET /caps`, `POST /generate` on localhost:7777 | **Real** — an API-layer HTTP/SSE surface (mis-carded as an MCP remote, §1) |

## 4. Gateway state

**Selected, not stood up.** EoSim's `docs/mcp-gateway-eval.md`
records the decision (2026-10-05): **Klavis Strata** —
open-source, self-hostable, progressive tool discovery.
sdys666/mcp-gateway is retained as a pattern reference
(SKILL.md validation, allow/confirm/deny policies), not a
dependency. No gateway code exists in any tree read today;
the eval doc's step 1 ("stand up Strata in front of the EoSim
MCP server") has not been taken.

Standing evaluation criteria the stand-up will be judged
against:

1. **Control 9 routing** — does it route by (connection, id),
   never by a client-supplied session id alone?
2. **protocolVersion recording** — what each backend actually
   negotiates, measured per server (§1's era split is why this
   is a measurement, not an assumption).
3. **Espressif ESP-IDF MCP Server interop** — ESP-IDF v6.0
   ships a vendor MCP server (Espressif, first-party); it is
   the first non-org server the gateway should be tested
   against.
4. Neither candidate's negotiated protocol version was
   verified for this audit — gateway version claims stay
   **unverified** until measured at stand-up.

## 5. Gap table — in dependency order

| # | Gap | Owning repo | Next daily-sized slice |
| --- | --- | --- | --- |
| 1 | MQTT client declared, unimplemented | eos (eos#199) | Slice 1 of the design doc: codec core + byte fixtures |
| 2 | micro-ROS not scoped | eos / eNI | Scoping doc after gap 1's design — the next API-layer scoping |
| 3 | EoSim ROS bridge publish/subscribe unimplemented | EoSim | Implement against a live rclpy in the sim environment, or scope the socket fallback the class already names |
| 4 | eosllm card classifies an API daemon as an MCP remote | eosllm | Decide: a real MCP wrapper over the daemon, or a corrected card — one slice, either way |
| 5 | Gateway selected, not stood up | EoSim (fabric) | Stand Strata up in front of EoSim's server; record negotiated versions per §4 |
| 6 | Interop install paths undocumented (ROS / Zephyr / FreeRTOS / NuttX / embedded Linux) | ebuild | Backend-by-backend install/interop docs on the existing backends |
| 7 | Home-systems surfaces undesigned | eNet (eNet#7) | Scoping doc landed today in eNet (`docs/home-systems-plan.md`, commit `744aa995`); next: its slice 1, the BLE commissioning-bearer audit |
| 8 | Reusable-server-json standard's EoSim version cell stale (3.0.2 vs live 3.1.0) | .github | **Corrected in the commit that lands this audit** (one cell, §1) |

## 6. Modular-adoption lens

Per surface: could a third party lift this piece alone today?

- **EoSim MCP server** — yes: standalone stdio server, own
  `server.json`, own CI caller. The org's cleanest lift.
- **eFlow MCP server** — yes, same shape, smaller surface.
- **eos `net.h` contracts** — the socket contract yes; the
  MQTT contract is liftable as a *contract* today and as code
  only once gap 1 lands — the design doc's codec is scoped to
  depend on nothing beyond the socket API for exactly this
  reason.
- **eNI rclc package** — yes as a ROS 2 package; its value
  without the rest of eNI is the messages + node skeleton.
- **eosllm daemon** — yes as a local service; its registry
  card currently oversells what it is (gap 4).
- **The MCP layer as a whole** — not yet: with no gateway
  stood up, "the layer" is two stdio servers and a policy
  set. That is the honest state, and gap 5 is the slice that
  changes it.
