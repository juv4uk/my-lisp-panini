import os
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

yaml_path = r'c:\GitHub\my-lisp-panini\panini\registry\sutras\index.yaml'

with open(yaml_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

out_lines = []
current_devanagari = None

for line in lines:
    stripped = line.strip()
    if stripped.startswith('devanagari: "'):
        # Extract devanagari text
        devanagari_text = stripped.split('"')[1]
        out_lines.append(line.rstrip())
        
        # Add SLP1 transliteration right after
        slp1_text = transliterate(devanagari_text, sanscript.DEVANAGARI, sanscript.SLP1)
        # Indentation should match "devanagari: " line
        indent = line[:len(line) - len(line.lstrip())]
        out_lines.append(f'{indent}slp1: "{slp1_text}"')
    elif stripped.startswith('slp1: "'):
        # If it already had a manual SLP1 entry, we might want to keep it or let the loop above add it.
        # But wait, our manual slp1 in index.yaml was mostly removed when we re-wrote it?
        # Let's check if the line exists. If it exists, we skip it because we just inserted it or it was manual.
        # Actually, in the previous run, I added devanagari to all, but didn't touch slp1, except for the key sutras which already had slp1.
        # If a line already has slp1, we just overwrite it by ignoring it here (since we add it after devanagari).
        # Actually, it's safer to just let the script output the existing line if we haven't seen devanagari, 
        # but if we saw devanagari, we already output a new slp1 line.
        # So we can just drop existing slp1 lines to avoid duplicates.
        pass
    else:
        out_lines.append(line.rstrip())

with open(yaml_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(out_lines))

print("Successfully added SLP1 transliteration for all sutras in index.yaml.")
