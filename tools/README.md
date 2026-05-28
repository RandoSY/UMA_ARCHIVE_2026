# Tools

## Create or repair archive structure

Dry run:

```bash
python tools/create_archive_structure.py --dry-run
```

Create missing folders and files:

```bash
python tools/create_archive_structure.py
```

Overwrite starter files:

```bash
python tools/create_archive_structure.py --overwrite
```

The script uses only the Python standard library and should work on Windows 11 and Linux.
