#!/usr/bin/env python3
"""Light read-only validator for coordination/dependencies.yaml.
Checks: pinned revisions exist; claims match ecosystem/imports file;
upstream HEAD drift is REPORTED (warn), not failed."""
import re, subprocess, sys
try:
    import yaml
except ImportError:
    sys.exit("PyYAML required")

doc = yaml.safe_load(open("coordination/dependencies.yaml", encoding="utf-8"))
fails, warns = [], []

for up in doc.get("upstream", []):
    lp = up["local_path"]; pin = up["pinned_revision"]
    def git(*a):
        return subprocess.run(["git", "-C", lp, *a], capture_output=True, text=True)
    if git("cat-file", "-e", f"{pin}^{{commit}}").returncode != 0:
        fails.append(f"{up['id']}: pinned revision {pin} NOT FOUND")
        continue
    head = git("rev-parse", "--short=7", "HEAD").stdout.strip()
    if head != pin[:7]:
        warns.append(f"{up['id']}: HEAD {head} ahead of pin {pin[:7]} (drift report)")

    imp = open(up["imports_file"], encoding="utf-8").read()
    file_claims = set(re.findall(r"\(claim (\S+) \(revision \"([^\"]+)\"\)", imp))
    yaml_claims = {(c["id"], c.get("status")) for c in up.get("claims", [])}
    for cid, _rev in file_claims:
        if not any(cid == yid for yid, _ in yaml_claims):
            fails.append(f"claim {cid} в imports файлі відсутній у реєстрі")
    for yid, _st in yaml_claims:
        if not any(cid == yid for cid, _r in file_claims):
            fails.append(f"claim {yid} є в реєстрі, але нема в imports файлі")

print("== validation report ==")
for w in warns: print("WARN:", w)
for f in fails: print("FAIL:", f)
print(f"fails={len(fails)} warns={len(warns)}")
sys.exit(1 if fails else 0)
