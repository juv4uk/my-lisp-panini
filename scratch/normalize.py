import os
import glob

replacements = {
    "bhvAdi": "BvAdi",
    "rudhAdi": "ruDAdi",
    "svataMtraH": "svatantraH",
    "saMpradAnam": "sampradAnam",
    "BIitrARAM Bayahetuh": "BItrArTAnAM BayahetuH",
    "taTAyuktaM": "taTAyuktam" # sometimes ending M is m, but taTAyuktaM is fine in sandhi. I'll leave taTAyuktaM.
}

def normalize_slp1():
    files = glob.glob('panini/registry/**/*.yaml', recursive=True)
    count = 0
    for f in files:
        with open(f, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            
        new_content = content
        for old, new in replacements.items():
            new_content = new_content.replace(old, new)
            
        if content != new_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            count += 1
            print(f"Updated: {f}")
            
    print(f"Normalization complete. {count} files updated.")

if __name__ == "__main__":
    normalize_slp1()
