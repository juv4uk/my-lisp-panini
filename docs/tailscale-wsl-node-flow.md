# Tailscale WSL connection flow for remote swarm nodes

Status: VERIFIED-LIVE 2026-08-24 (all commands and addresses from a working
session; topology captured via `tailscale status`).

## Topology (this tailnet)

| Device | Tailnet IP | OS | Role |
|---|---|---|---|
| `desktop-1` | `100.88.228.63` | linux (WSL2) | local dev box; **tailscaled runs inside WSL** |
| `desktop` | `100.120.29.6` | windows | Windows host (separate device) |
| `ubuntu-s-1vcpu-512mb-10gb-ams3` | `100.113.68.50` | linux droplet | **bootstrap node-1 :9101** |

WSL is its own tailnet device — tailscaled (PID started at boot) runs inside
the WSL namespace; the Windows host on the same tailnet is a different node.

## The loopback rule (why remote peers can't see you)

By default every swarm-node binds **127.0.0.1 only**:

```
ss -tln | grep <port>   # -> 127.0.0.1:<port>
```

Loopback-bound nodes are invisible to the whole tailnet. Remote peers cannot
dial in; only your **outbound** `--connect` reaches them.

## Working pattern: outbound-only join (verified today)

```bash
cd ~/GitHub/my-lisp-panini
setsid ./target/debug/swarm-node \
  --port 9106 --node-id my-lisp-panini-1 --project my-lisp-panini \
  --data-dir ~/.swarm-node/my-lisp-panini-1 \
  --connect 100.113.68.50:9101 </dev/null >> /path/to/log 2>&1 & disown
```

- Bootstrap = the droplet's :9101 (always-on). Gossip discovers the rest.
- Verify: `ss -tln | grep <port>` then check the log for peer joins.

## Inbound recipe (remote must dial WSL directly)

```bash
--bind 100.88.228.63 --port <port>   # tailnet interface of this WSL
```

Also required outside WSL:

1. Windows firewall allowance for that port on the Tailscale interface.
2. Keep tailscaled inside WSL running (it dies with WSL restarts unless
   configured as a boot service).

Trade-off note: loopback binding is also the current security default;
enable inbound binding only for nodes that must be dialed.

## Operational constraints observed today

- Always launch via `setsid ... </dev/null >> log 2>&1 & disown` — plain `&`
  children die when the parent shell is torn down.
- Under heavy box load (e.g., FPGA synthesis, RAM ~300 MB free) nodes get
  reaped repeatedly — launch/relaunch after load normalizes.
- `/tmp` is volatile on this box: logs and checkpoints belong under
  `/home/agents/logs` and `/home/agents/backups`.

## Health warnings seen

- `tailscale status` health block: `/etc/resolv.conf overwritten`
  (DNS-fight) — cosmetic here, but revisit if magic-DNS names are needed.
