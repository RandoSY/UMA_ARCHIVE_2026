#!/usr/bin/env python3
"""
Create or repair the UMA Archive 2026 repository structure.

Usage:
    python tools/create_archive_structure.py --dry-run
    python tools/create_archive_structure.py
    python tools/create_archive_structure.py --overwrite
"""

from __future__ import annotations

import argparse
from pathlib import Path

STRUCTURE = {
    "00_Master_Architecture": [
        "UMA_Platform_Overview",
        "Measured_World_Machine_Self",
        "Publication_Pathway",
        "Glossary_and_Named_Phrases",
    ],
    "01_Nugget": [
        "PIC_Black_Box",
        "GCBASIC_and_SNAP",
        "Nugget_FWLIB",
        "Source_to_Assembly_to_Simulator",
        "Programmable_555",
    ],
    "02_REDBoard_Revival": [
        "AVR_Spirit",
        "Arduino_Nano_Bridge",
        "Nugget_2Wire_Sensor_Shield",
        "KiCad_PCB_Work",
        "Pin_Assignment_Documentation",
    ],
    "03_One_Bit_Labs": [
        "555_7400_Monte_Carlo_Duty_Cycle",
        "Catch_the_Clock",
        "One_Bit_Reaction_Timer",
        "Binomial_Distribution_Tutorial",
        "Statistics_Dashboard",
    ],
    "04_Measured_World_Instruments": [
        "Kitech_Kitchen_Lab",
        "Singing_Ruler",
        "Smart_eScale",
        "Tapeless_Ruler",
        "KitchenLab_Dynametrics",
        "Newton_Cooling_Tea_Calorimetry",
    ],
    "05_Measured_Machine_Robot_EDU": [
        "Green_Robot_EDU",
        "Prospector_Robot",
        "ECHONAV",
        "Undersea_Mining_Origin",
        "Nonviolent_Exploration_Framework",
    ],
    "06_Measured_Self": [
        "QMeter",
        "WalkWise",
        "SQM_Plus",
        "Naggler",
        "Tone_Trainer",
        "Tai_Chi_Timer",
    ],
    "07_Dashboards_and_Virtual_Instruments": [
        "WebBLE_NUS",
        "WebSerial",
        "UMA_Text_Protocol",
        "Virtual_DMM",
        "Picowscope",
        "Frequency_Meter",
        "eScale_Dashboard",
        "Reaction_Timer_Dashboard",
    ],
    "08_Comics_and_Visual_Storytelling": [
        "UMA_12_Panel_Comics",
        "Sixty_Panel_Environs_Comic",
        "One_Hundred_Twenty_Panel_Archive_Comic",
        "REDBoard_Comics",
        "AVR_Spirit_Logo",
        "Brittle_System_Yellow_Pad_Comic",
    ],
    "09_Executive_Summaries_and_PDFs": [
        "UMA_Project_Inventory",
        "Nugget_Executive_Summaries",
        "Teacher_Guides",
        "Programmer_Guides",
        "Publication_Drafts",
    ],
    "10_Code_and_Firmware": [
        "PIC_GCBASIC",
        "AVR_Arduino_Nano",
        "RP2040_Pico",
        "ESP32",
        "Microbit",
        "Shared_Protocols",
    ],
    "11_Hardware_and_PCB": [
        "KiCad",
        "Schematics",
        "BOMs",
        "Pin_Maps",
        "Wiring_Diagrams",
        "Fabrication_Notes",
    ],
    "12_Data_and_Analysis": [
        "Sample_CSV",
        "Jupyter_Notebooks",
        "Statistics_Tutorials",
        "Calibration_Data",
        "Experiment_Results",
    ],
    "templates": [],
    "tools": [],
}

TEMPLATE_FILES = [
    "PROJECT_ONE_PAGER_TEMPLATE.md",
    "EXPERIMENT_RECORD_TEMPLATE.md",
    "HARDWARE_PROJECT_TEMPLATE.md",
    "FIRMWARE_PROJECT_TEMPLATE.md",
    "TEACHER_GUIDE_TEMPLATE.md",
    "PROGRAMMER_GUIDE_TEMPLATE.md",
    "COMIC_STORYBOARD_TEMPLATE.md",
    "PUBLICATION_CANDIDATE_TEMPLATE.md",
    "DECISION_LOG_TEMPLATE.md",
]

ROOT_FILES = {
    "README.md": "# UMA Archive 2026\n\nMeasured World · Measured Machine · Measured Self\n",
    "LICENSE.md": "# License Placeholder\n\nChoose a license before public reuse.\n",
    "CHANGELOG.md": "# Changelog\n\n## [0.1.0] - Initial archive skeleton\n",
    "CONTRIBUTING.md": "# Contributing\n\nUse templates and preserve the archive structure.\n",
    "ARCHIVE_INDEX.md": "# Archive Index\n",
    "GLOSSARY.md": "# Glossary\n",
    "PROJECT_STATUS.md": "# Project Status\n",
    "PUBLICATION_PATHWAY.md": "# Publication Pathway\n",
    ".gitignore": "# Add project-specific ignores here.\n",
}

def safe_write(path: Path, content: str, overwrite: bool, dry_run: bool, created_files: list[str]) -> None:
    if path.exists() and not overwrite:
        return
    if dry_run:
        print(f"Would write file: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    created_files.append(str(path))

def ensure_dir(path: Path, dry_run: bool, created_dirs: list[str]) -> None:
    if path.exists():
        return
    if dry_run:
        print(f"Would create dir:  {path}")
        return
    path.mkdir(parents=True, exist_ok=True)
    created_dirs.append(str(path))

def print_tree(base: Path) -> None:
    for path in sorted(base.rglob("*")):
        rel = path.relative_to(base)
        depth = len(rel.parts) - 1
        print("  " * depth + ("└── " if depth else "") + rel.name)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Show what would be created without writing files.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing starter files.")
    args = parser.parse_args()

    base = Path.cwd()
    created_dirs: list[str] = []
    created_files: list[str] = []

    for dirname, subdirs in STRUCTURE.items():
        ensure_dir(base / dirname, args.dry_run, created_dirs)
        for subdir in subdirs:
            ensure_dir(base / dirname / subdir, args.dry_run, created_dirs)
            safe_write(base / dirname / subdir / ".gitkeep", "", args.overwrite, args.dry_run, created_files)

    for filename, content in ROOT_FILES.items():
        safe_write(base / filename, content, args.overwrite, args.dry_run, created_files)

    for dirname in [d for d in STRUCTURE if d[:2].isdigit()]:
        safe_write(
            base / dirname / "README.md",
            f"# {dirname}\n\nPurpose, contents, status, and next actions for this archive area.\n",
            args.overwrite,
            args.dry_run,
            created_files,
        )

    for template in TEMPLATE_FILES:
        safe_write(base / "templates" / template, f"# {template.replace('_', ' ').replace('.md', '')}\n\nFill in this template.\n", args.overwrite, args.dry_run, created_files)

    safe_write(
        base / "tools" / "README.md",
        "# Tools\n\nRun `python tools/create_archive_structure.py --dry-run` before creating or repairing the structure.\n",
        args.overwrite,
        args.dry_run,
        created_files,
    )

    print("\nSummary")
    print("-------")
    print(f"Created folders: {len(created_dirs)}")
    print(f"Created files:   {len(created_files)}")

    if not args.dry_run:
        missing_readmes = [d for d in STRUCTURE if d[:2].isdigit() and not (base / d / "README.md").exists()]
        missing_templates = [t for t in TEMPLATE_FILES if not (base / "templates" / t).exists()]
        if missing_readmes:
            print("Missing numbered-folder README files:", missing_readmes)
        if missing_templates:
            print("Missing template files:", missing_templates)
        if not missing_readmes and not missing_templates:
            print("Checks passed: numbered folders have README files and all templates exist.")

        print("\nRepository tree:")
        print_tree(base)

    print("\nNext steps:")
    print("1. Review README.md, PROJECT_STATUS.md, and GLOSSARY.md.")
    print("2. Choose a license before making public reuse claims.")
    print("3. Run: git init && git add . && git commit -m \"Create initial UMA archive structure\"")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
