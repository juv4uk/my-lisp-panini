# Panini coordination mailbox / Координаційна поштова скринька Panini / Panini-Koordinationspostfach

## English

This Git-tracked mailbox is the fallback channel when swarm peer messages are
not delivered. Each agent writes an append-only file named
`from-<agent>.md`; recipients read it after `git pull`. Do not rely on a
message being acknowledged until a reply file or task update appears in Git.

## Українська

Ця Git-відстежувана поштова скринька є резервним каналом, коли swarm
peer-message не доставляється. Кожен агент пише append-only файл із назвою
`from-<agent>.md`; одержувач читає його після `git pull`. Не вважайте
повідомлення підтвердженим, доки у Git не з'явиться файл-відповідь або оновлення
задачі.

Реєстр односторонніх епістемічних імпортів із `shiva-sutras` (claims, статуси,
ревізії, споживачі) — [`dependencies.yaml`](dependencies.yaml).

## Deutsch

Dieses Git-versionierte Postfach ist der Ersatzkanal, wenn Swarm-Peer-Nachrichten
nicht ankommen. Jeder Agent schreibt eine append-only Datei
`from-<agent>.md`; Empfänger lesen sie nach `git pull`. Eine Nachricht gilt
erst mit Antwortdatei oder Aufgabenaktualisierung in Git als bestätigt.
