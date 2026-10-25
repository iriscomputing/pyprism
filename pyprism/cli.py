#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
from .crystallizer import PyPrismVenvCrystallizer

def main():
    parser = argparse.ArgumentParser(description="PyPrism — Hermetic Python Virtualenv Crystallizer")
    parser.add_argument("output", help="Path to output .pycryst executable artifact")
    parser.add_argument("--venv", default=None, help="Path to source virtual environment (defaults to active venv)")
    parser.add_argument("--entrypoint", default=None, help="Entrypoint function, e.g. 'mypackage.app:main'")
    
    args = parser.parse_args()
    crystallizer = PyPrismVenvCrystallizer(args.venv)
    res = crystallizer.crystallize(
        output_crystal_path=Path(args.output),
        app_entrypoint=args.entrypoint
    )
    print(f"[+] Crystallized {res['files_crystallized']} files from {len(res['packages'])} packages into {res['crystal_bytes']} bytes.")
    print(f"    Artifact: {res['crystal_path']}")
    print(f"    SHA-256:  {res['crystal_sha256']}")

if __name__ == "__main__":
    main()
