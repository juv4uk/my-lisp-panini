import yaml
import re

yaml_path = r'c:\GitHub\my-lisp-panini\panini\registry\sutras\index.yaml'

with open(yaml_path, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

sutras = data.get('sutras', {})

for sid, info in sutras.items():
    if not info: continue
    meaning = info.get('meaning_en', '')
    
    # Heuristics
    sutra_type = 'vidhi'
    if 'are called' in meaning or 'is called' in meaning:
        sutra_type = 'samjna'
    elif 'From here onwards' in meaning or 'Till ' in meaning:
        sutra_type = 'adhikara'
    elif 'If two sutras' in meaning or 'precedence' in meaning:
        sutra_type = 'paribhasha'
    
    info['type'] = sutra_type

# We'll save it back to index.yaml
with open(yaml_path, 'w', encoding='utf-8') as f:
    yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

print("Sutras tagged and saved.")
