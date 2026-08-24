#!/usr/bin/env python3
"""Verify panini-machine-model v0.1 against the live my-lisp oracle (:9999).
Checks: later-rule-wins conflict resolution, tag application, proof trace."""
import socket, re, sys

src = open("prototype/machine_model_v01.my", encoding="utf-8").read()
code = " ".join(re.sub(r";.*$", "", l) for l in src.split("\n"))
code = re.sub(r"\s+", " ", code).strip()
payload = f'(request (id 7) (op eval) (source "{code}"))'

s = socket.create_connection(("127.0.0.1", 9999), timeout=25)
s.sendall((payload + "\n").encode())
s.settimeout(20); data = b""
try:
    while True:
        b = s.recv(65536)
        if not b: break
        data += b
except socket.timeout:
    pass
s.close()
resp = data.decode(errors="replace")

v = resp.split("(value ", 1)[1] if "(value " in resp else ""
checks = {
    "status ok": "(status ok)" in resp,
    "later-rule-wins (guna over vrddhi)": "guna" in v and "vrddhi" not in v,
    "dhatu applied on action node": "dhatu" in v,
    "proof trace ids present": "R-1-1-2-guna" in v and "R-1-3-1-dhatu" in v,
}
for k, ok in checks.items():
    print(f"  {k}: {'PASS' if ok else 'FAIL'}")
sys.exit(0 if all(checks.values()) else 1)
