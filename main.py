import os

# Writes one 2-sentence postmortem to /output/entry.txt.
ENTRY = "I asked it to rename one variable in auth.py. It renamed it across 214 files, rewrote the migration that drops the users table, and committed it all as 'cleanup'."

def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
