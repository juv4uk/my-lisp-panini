#!/usr/bin/env python3
"""Verify symbolic-inference anuvrtti chain against live oracle :9999."""
import socket, re, sys
src=open("prototype/symbolic_inference.my",encoding="utf-8").read()
code=" ".join(re.sub(r";.*$","",l) for l in src.split("\n"))
code=re.sub(r"\s+"," ",code).strip()
s=socket.create_connection(("127.0.0.1",9999),timeout=25)
payload=f'(request (id 11) (op eval) (source "{code}"))'
s.sendall((payload+"\n").encode()); s.settimeout(20); d=b""
try:
    while True:
        b=s.recv(65536)
        if not b: break
        d+=b
except socket.timeout: pass
s.close()
resp=d.decode(errors="replace")
v=resp.split("(value ",1)[1] if "(value " in resp else ""
checks={
 "status ok": "(status ok)" in resp,
 "ctx pratyayah": "pratyayah" in v,
 "ctx paras-ca": "paras-ca" in v,
 "sap-target applied": "sap-target" in v,
 "trace 3 rules": all(x in v for x in ["R-3-1-1-pratyayah","R-3-1-2-paras-ca","R-3-1-68-kartari-sap"]),
}
for k,ok in checks.items(): print(f"  {k}: {'PASS' if ok else 'FAIL'}")
sys.exit(0 if all(checks.values()) else 1)
