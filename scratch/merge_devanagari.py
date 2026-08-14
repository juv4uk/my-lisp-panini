
import sys
import os

tsv_path = r'C:\Users\user\.gemini\antigravity-ide\brain\1e722a21-e0d7-4766-9d2f-5983d99a9234\.system_generated\steps\800\content.md'
yaml_path = r'c:\GitHub\my-lisp-panini\panini\registry\sutras\index.yaml'

with open(tsv_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

sutra_map = {}
for line in lines:
    parts = line.strip().split('\t')
    if len(parts) == 2 and parts[0][0].isdigit():
        sutra_map[parts[0]] = parts[1]

# Re-generate index.yaml manually without yaml module, because it's not installed
with open(yaml_path, 'r', encoding='utf-8') as f:
    yaml_lines = f.readlines()

out_lines = []
for line in yaml_lines:
    out_lines.append(line.rstrip())
    if line.startswith('  "'):
        # Extract ID
        sid = line.split('"')[1]
        if sid in sutra_map:
            out_lines.append(f'    devanagari: "{sutra_map[sid]}"')

with open(yaml_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(out_lines))
