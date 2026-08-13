import yaml
import os

yaml_path = r'c:\GitHub\my-lisp-panini\panini\registry\sutras\index.yaml'
lisp_path = r'c:\GitHub\my-lisp-panini\panini\registry\sutras.my'

def escape_lisp_string(s):
    if not s: return ""
    return s.replace('\\', '\\\\').replace('"', '\\"')

with open(yaml_path, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

sutras = data.get('sutras', {})

lisp_lines = []
lisp_lines.append(";; Auto-generated Ashtadhyayi Sutra Registry")
lisp_lines.append(";; Contains ~4000 sutras with SLP1 and Devanagari text")
lisp_lines.append("")
lisp_lines.append("(def *ashtadhyayi*")
lisp_lines.append("  (hash")

for sid, info in sutras.items():
    if not info: continue
    dev = escape_lisp_string(info.get('devanagari', ''))
    slp1 = escape_lisp_string(info.get('slp1', ''))
    type = escape_lisp_string(info.get('type', 'vidhi'))
    mean = escape_lisp_string(info.get('meaning_en', ''))
    
    lisp_lines.append(f'    "{sid}" (hash :devanagari "{dev}" :slp1 "{slp1}" :type "{type}" :meaning "{mean}")')

lisp_lines.append("  ))")
lisp_lines.append("")
lisp_lines.append("(defn get-sutra-text [id]")
lisp_lines.append("  (let ((s (get *ashtadhyayi* id)))")
lisp_lines.append("    (if s (get s :slp1) nil)))")
lisp_lines.append("")

with open(lisp_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(lisp_lines))

print(f"Generated {lisp_path} with {len(sutras)} sutras.")
