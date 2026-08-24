# Tailscale WSL потік підключення для віддалених swarm-нод

Статус: VERIFIED-LIVE 2026-08-24 (усі команди й адреси з робочої сесії;
топологія знята через `tailscale status`).

## Топологія (цей tailnet)

| Пристрій | Tailnet IP | ОС | Роль |
|---|---|---|---|
| `desktop-1` | `100.88.228.63` | linux (WSL2) | локальна дев-машина; **tailscaled працює всередині WSL** |
| `desktop` | `100.120.29.6` | windows | Windows-хост (окремий пристрій) |
| `ubuntu-s-1vcpu-512mb-10gb-ams3` | `100.113.68.50` | linux дроплет | **bootstrap node-1 :9101** |

WSL — самостійний пристрій tailnet: tailscaled запущений у WSL-неймспейсі;
Windows-хост того ж tailnet — інша нода.

## Правило loopback (чому віддалені піри тебе не бачать)

За замовчуванням кожна swarm-node слухає **тільки 127.0.0.1**:

```
ss -tln | grep <порт>   # -> 127.0.0.1:<порт>
```

Loopback-ноди невидимі для всього tailnet. Віддалені піри не можуть
дзвонити тобі; працює лише твій вихідний `--connect`.

## Робочий патерн: outbound-only join (верифіковано сьогодні)

```bash
cd ~/GitHub/my-lisp-panini
setsid ./target/debug/swarm-node \
  --port 9106 --node-id my-lisp-panini-1 --project my-lisp-panini \
  --data-dir ~/.swarm-node/my-lisp-panini-1 \
  --connect 100.113.68.50:9101 </dev/null >> /шлях/до/log 2>&1 & disown
```

- Bootstrap — дроплет :9101 (завжди увімкнений). Gossip знаходить решту mesh.
- Верифікація: `ss -tln | grep <порт>`, потім лог на предмет peer joins.

## Рецепт inbound (якщо віддалена нода має дзвонити у WSL напряму)

```bash
--bind 100.88.228.63 --port <порт>   # tailnet-інтерфейс цього WSL
```

Додатково поза WSL:

1. Windows firewall: дозволити порт на Tailscale-інтерфейсі.
2. Тримати tailscaled у WSL запущеним (помирає при рестарті WSL без
   boot-сервісу).

Нотатка про trade-off: loopback — це також поточний безпековий дефолт;
inbound-bounding вмикай тільки для нод, які мають бути адресовані.

## Обмеження, спостережені сьогодні

- Завжди запускай через `setsid ... </dev/null >> log 2>&1 & disown` —
  діти plain `&` помирають разом із батьківським шеллом.
- Під важким навантаженням боксу (FPGA synthesis, RAM ~300 MB вільних)
  ноди ріже OOM/reaper неодноразово — перезапускай після нормалізації.
- `/tmp` на цьому боксі волатильний: логи й чекпоінти тримай у
  `/home/agents/logs` та `/home/agents/backups`.

## Попередження health

- `tailscale status`: `/etc/resolv.conf overwritten` (DNS-fight) — тут
  косметика, але повернись, якщо знадобляться magic-DNS імена.
