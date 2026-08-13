# Swarm-agent connection guide / Підключення агента до рою / Anleitung zur Verbindung eines Schwarm-Agenten

## English

This repository is worked on through **WSL2**, under its dedicated Linux user
`my-lisp-panini`. The physical Windows checkout stays at
`C:\GitHub\my-lisp-panini`; its WSL path is `/mnt/c/GitHub/my-lisp-panini`.
Use the repository's declared **Guix environment** for builds, tests, and
tooling. Git itself does not require Guix.

### Enter the working environment

From Windows, run a Git command through WSL as follows:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc 'cd /mnt/c/GitHub/my-lisp-panini && git status'
```

For a build, test, or validator that needs declared dependencies:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc 'cd /mnt/c/GitHub/my-lisp-panini && guix shell -m manifest.scm -- bash -lc "<command>"'
```

For an interactive session:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc 'cd /mnt/c/GitHub/my-lisp-panini && guix shell -m manifest.scm'
```

### Start a local swarm node

Choose an unoccupied port and a durable, unique node id. The usual bootstrap
peer is `my-lisp-1` on port `9101`. Do not send control commands to the
bootstrap peer: send them to the port of the node you started.

Example for this project’s second node (`9107`):

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc 'nohup /mnt/c/GitHub/my-lisp/target/debug/swarm-node --port 9107 --node-id my-lisp-panini-2 --project my-lisp-panini --data-dir ~/.swarm-node/my-lisp-panini-2 --connect 127.0.0.1:9101 > /tmp/swarm-node-my-lisp-panini-2.log 2>&1 &'
```

Inspect the startup log:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc 'cat /tmp/swarm-node-my-lisp-panini-2.log'
```

The node process is deliberately outside the Guix shell: it is the shared
coordination binary. Repository commands still run in `guix shell -m
manifest.scm` where applicable.

### Join, synchronize, and inspect

Replace `9107` only if you started the node on another port. Capabilities must
describe real expertise, not aspirational work.

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc "printf '%s\n' '(join (capabilities (sanskrit panini slp1 documentation)) (roles (worker voter)))' | timeout 8 nc 127.0.0.1 9107"
```

Synchronize durable tasks using an **absolute** path:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc "printf '%s\n' '(sync-tasks (file \"/mnt/c/GitHub/my-lisp-panini/tasks.my\"))' | timeout 8 nc 127.0.0.1 9107"
```

Check peers and task state:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc "printf '%s\n' '(status)' | timeout 8 nc 127.0.0.1 9107"
```

An `(ok ...)` response is success even if `nc`/`timeout` returns a nonzero
exit status after the server closes the connection.

### Operating rules

- Keep `tasks.my` under version control; it is the durable shared plan.
- After a node restart, repeat `join` and `sync-tasks`: presence and claims are
  ephemeral even when the node journal survives.
- Claim tasks before editing, complete them with the assigned generation, and
  do not touch files already claimed by another agent.
- Do not put `IAST` or Devanāgarī identifiers into VM internals; canonical IDs
  remain SLP1.

## Українська

У цьому репозиторії працюють через **WSL2** під окремим Linux-користувачем
`my-lisp-panini`. Фізичний checkout Windows лишається в
`C:\GitHub\my-lisp-panini`; шлях із WSL — `/mnt/c/GitHub/my-lisp-panini`.
Для збирання, тестів та інструментів використовуйте задеклароване
**Guix-оточення** репозиторію. Для самого Git Guix не потрібен.

### Вхід у робоче середовище

З Windows Git-команду запускайте через WSL так:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc 'cd /mnt/c/GitHub/my-lisp-panini && git status'
```

Для збирання, тесту або валідатора, що потребує задекларованих залежностей:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc 'cd /mnt/c/GitHub/my-lisp-panini && guix shell -m manifest.scm -- bash -lc "<command>"'
```

Для інтерактивної сесії:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc 'cd /mnt/c/GitHub/my-lisp-panini && guix shell -m manifest.scm'
```

### Запуск локального вузла рою

Виберіть вільний порт і сталий унікальний node id. Звичний bootstrap-peer —
`my-lisp-1` на порту `9101`. Не надсилайте команди керування bootstrap-вузлу:
надсилайте їх на порт власного запущеного вузла.

Приклад для другого вузла цього проєкту (`9107`):

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc 'nohup /mnt/c/GitHub/my-lisp/target/debug/swarm-node --port 9107 --node-id my-lisp-panini-2 --project my-lisp-panini --data-dir ~/.swarm-node/my-lisp-panini-2 --connect 127.0.0.1:9101 > /tmp/swarm-node-my-lisp-panini-2.log 2>&1 &'
```

Перегляд логу запуску:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc 'cat /tmp/swarm-node-my-lisp-panini-2.log'
```

Процес вузла навмисно запускається поза Guix shell: це спільний бінарник
координації. Команди репозиторію, де це потрібно, усе одно виконуються в
`guix shell -m manifest.scm`.

### Приєднання, синхронізація та перевірка

Замініть `9107`, лише якщо запустили вузол на іншому порту. Capabilities мають
описувати реальну компетенцію, а не бажану майбутню роботу.

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc "printf '%s\n' '(join (capabilities (sanskrit panini slp1 documentation)) (roles (worker voter)))' | timeout 8 nc 127.0.0.1 9107"
```

Синхронізуйте durable tasks за **абсолютним** шляхом:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc "printf '%s\n' '(sync-tasks (file \"/mnt/c/GitHub/my-lisp-panini/tasks.my\"))' | timeout 8 nc 127.0.0.1 9107"
```

Перевірте peers і стан задач:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc "printf '%s\n' '(status)' | timeout 8 nc 127.0.0.1 9107"
```

Відповідь `(ok ...)` означає успіх, навіть якщо `nc`/`timeout` повернув
ненульовий exit status після закриття з’єднання сервером.

### Робочі правила

- Тримайте `tasks.my` під контролем версій: це durable спільний план.
- Після рестарту вузла повторіть `join` і `sync-tasks`: presence та claims
  тимчасові, навіть якщо journal вузла збережено.
- Claim задачу до редагування, завершуйте її з виданим generation і не
  торкайтеся файлів, які вже взяв інший агент.
- Не вносьте IAST або Devanāgarī-ідентифікатори у внутрішності VM: канонічні ID
  лишаються SLP1.

## Deutsch

In diesem Repository wird über **WSL2** unter dem eigenen Linux-Benutzer
`my-lisp-panini` gearbeitet. Der physische Windows-Checkout bleibt unter
`C:\GitHub\my-lisp-panini`; der WSL-Pfad lautet
`/mnt/c/GitHub/my-lisp-panini`. Für Build, Tests und Werkzeuge ist die
deklarierte **Guix-Umgebung** des Repositories zu verwenden. Git selbst
benötigt Guix nicht.

### Arbeitsumgebung betreten

Eine Git-Anweisung von Windows aus über WSL ausführen:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc 'cd /mnt/c/GitHub/my-lisp-panini && git status'
```

Für Build, Test oder Validator mit deklarierten Abhängigkeiten:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc 'cd /mnt/c/GitHub/my-lisp-panini && guix shell -m manifest.scm -- bash -lc "<command>"'
```

Für eine interaktive Sitzung:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc 'cd /mnt/c/GitHub/my-lisp-panini && guix shell -m manifest.scm'
```

### Lokalen Schwarmknoten starten

Einen freien Port und eine dauerhafte eindeutige Node-ID wählen. Der übliche
Bootstrap-Peer ist `my-lisp-1` auf Port `9101`. Steuerbefehle nicht an den
Bootstrap-Knoten senden, sondern an den Port des eigenen gestarteten Knotens.

Beispiel für den zweiten Knoten dieses Projekts (`9107`):

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc 'nohup /mnt/c/GitHub/my-lisp/target/debug/swarm-node --port 9107 --node-id my-lisp-panini-2 --project my-lisp-panini --data-dir ~/.swarm-node/my-lisp-panini-2 --connect 127.0.0.1:9101 > /tmp/swarm-node-my-lisp-panini-2.log 2>&1 &'
```

Startprotokoll prüfen:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc 'cat /tmp/swarm-node-my-lisp-panini-2.log'
```

Der Knotenprozess läuft absichtlich außerhalb der Guix-Shell: Er ist das
gemeinsame Koordinationsprogramm. Repository-Befehle werden, wo erforderlich,
weiterhin in `guix shell -m manifest.scm` ausgeführt.

### Beitreten, synchronisieren und prüfen

`9107` nur ersetzen, wenn der Knoten auf einem anderen Port läuft.
Capabilities müssen tatsächliche Kompetenz beschreiben, nicht geplante Arbeit.

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc "printf '%s\n' '(join (capabilities (sanskrit panini slp1 documentation)) (roles (worker voter)))' | timeout 8 nc 127.0.0.1 9107"
```

Dauerhafte Aufgaben mit einem **absoluten** Pfad synchronisieren:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc "printf '%s\n' '(sync-tasks (file \"/mnt/c/GitHub/my-lisp-panini/tasks.my\"))' | timeout 8 nc 127.0.0.1 9107"
```

Peers und Aufgabenstatus prüfen:

```sh
wsl -d Ubuntu -u my-lisp-panini -- bash -lc "printf '%s\n' '(status)' | timeout 8 nc 127.0.0.1 9107"
```

Eine Antwort `(ok ...)` bedeutet Erfolg, auch wenn `nc`/`timeout` nach dem
Schließen der Verbindung durch den Server einen Exit-Status ungleich null
liefert.

### Betriebsregeln

- `tasks.my` unter Versionskontrolle halten: Es ist der dauerhafte gemeinsame
  Plan.
- Nach einem Neustart des Knotens `join` und `sync-tasks` wiederholen:
  Presence und Claims sind flüchtig, selbst wenn das Node-Journal erhalten
  bleibt.
- Aufgaben vor dem Editieren claimen, mit der zugewiesenen Generation
  abschließen und keine Dateien berühren, die bereits ein anderer Agent
  geclaimt hat.
- Keine IAST- oder Devanāgarī-Identifikatoren in VM-Interna einbringen:
  Kanonische IDs bleiben SLP1.
