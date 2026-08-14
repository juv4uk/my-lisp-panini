"""
Download and convert the Ashtadhyayi sutra data from ashtadhyayi-com/data
into our SLP1-keyed registry format.

Source: sutrartha_english.txt (JSON, Devanagari + English meanings)
Output: panini/registry/sutras/sutras.yaml (key index) +
        panini/registry/sutras/{adhyaya}-{pada}.yaml (per-pada files)

Format of source key: "AAPPSS" where AA=adhyaya, PP=pada, SS=sutra
Example: "11001" = 1.1.1, "73084" = 7.3.84
"""

import json
import os
import urllib.request

SRC_URL = "https://raw.githubusercontent.com/ashtadhyayi-com/data/master/sutraani/sutrartha_english.txt"
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "panini", "registry", "sutras")

# Our key sutras of interest (used in derivations so far)
KEY_SUTRAS = {
    "1.1.1":  "vRdDirAdEc",      # vṛddhi definition
    "1.1.2":  "adenguRaH",       # guṇa definition
    "1.3.2":  "upadeSe'janunAsika it", # it definition
    "1.3.3":  "halantyam",       # final consonant is it
    "1.3.7":  "cutuS ca",        # cu/tu at start are it
    "1.3.9":  "tasya lopaH",     # tasya lopaH — it removal
    "1.4.2":  "vipratiSeDe paraM kAryam",  # conflict resolution
    "1.4.24": "Druvam apAye 'pAdAnam",     # apādāna kāraka
    "1.4.32": "karmaRA yam aBipraiti sampradAnam", # sampradāna
    "1.4.42": "sADakatamaM karaRam",       # karaṇa kāraka
    "1.4.45": "ADAro 'DikaraRam",          # adhikaraṇa
    "1.4.49": "kartur IpsitatamaM karma",  # karman kāraka
    "1.4.54": "svatantraH kartA",          # kartṛ kāraka
    "3.1.68": "kartari Sap",               # śap vikarana for class 1
    "3.2.123": "vartamAne laT",            # present tense laṭ
    "3.4.78": "tiptasjhi...",              # tiṅ endings
    "6.1.78": "eco 'yavAyAvaH",           # eco sandhi
    "7.3.84": "sArvaDAtukarDADAtukayoH",  # guṇa before sārvadhātuka
}


def parse_key(k):
    """Convert "73084" → (7, 3, 84) → "7.3.84" """
    k = k.strip()
    if len(k) == 5:
        a, p, s = int(k[0]), int(k[1]), int(k[2:])
    elif len(k) == 6:
        a, p, s = int(k[0]), int(k[1:3]), int(k[3:])
    else:
        return None
    return (a, p, s)


def format_id(a, p, s):
    return f"{a}.{p}.{s}"


def main():
    print("Downloading sutrartha_english.txt ...")
    with urllib.request.urlopen(SRC_URL) as resp:
        raw = resp.read().decode("utf-8")
    data = json.loads(raw)
    print(f"Loaded {len(data)} sutras.")

    os.makedirs(OUT_DIR, exist_ok=True)

    # Write index file with all sutra IDs + English meanings
    index_lines = [
        "# Ashtadhyayi Sutra Index",
        "# Source: ashtadhyayi-com/data (CC BY-SA 4.0)",
        "# Format: id: sutra-number (SLP1 notation), meaning: English translation",
        "# Note: Original text in Devanagari — SLP1 text added manually for key sutras",
        "---",
        "sutras:",
    ]

    count = 0
    for raw_key, meaning in sorted(data.items()):
        parsed = parse_key(raw_key)
        if not parsed:
            continue
        a, p, s = parsed
        sutra_id = format_id(a, p, s)
        slp1_text = KEY_SUTRAS.get(sutra_id, "")

        line = f'  "{sutra_id}":'
        if slp1_text:
            line += f'\n    slp1: "{slp1_text}"'
        line += f'\n    meaning_en: "{meaning[:120].strip()}"'
        index_lines.append(line)
        count += 1

    out_path = os.path.join(OUT_DIR, "index.yaml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines))
    print(f"Written {count} sutras to {out_path}")

    # Write a focused file with just our key sutras
    key_lines = [
        "# Key Sutras for panini-foundation-v0.1",
        "# These are the sutras directly referenced in our derivations.",
        "# slp1: SLP1 transliteration of sutra text",
        "# meaning_en: English translation",
        "---",
        "key_sutras:",
    ]
    for sutra_id, slp1_text in KEY_SUTRAS.items():
        a, p, s = [int(x) for x in sutra_id.split(".")]
        # Source key format: A + P + SSS (3-digit sutra, zero-padded)
        raw = f"{a}{p}{s:03d}"  # e.g. 1.3.9 → "13009", 7.3.84 → "73084"
        meaning = data.get(raw, "").strip()[:200]
        key_lines.append(f'  "{sutra_id}":')
        key_lines.append(f'    slp1: "{slp1_text}"')
        key_lines.append(f'    meaning_en: "{meaning}"')



    key_out = os.path.join(OUT_DIR, "key-sutras.yaml")
    with open(key_out, "w", encoding="utf-8") as f:
        f.write("\n".join(key_lines))
    print(f"Written key sutras to {key_out}")


if __name__ == "__main__":
    main()
