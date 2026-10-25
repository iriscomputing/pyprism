# PyPrism

> **Hermetic single-file virtualenv crystallizer and zero-drift executable packager for Python.**

[![PyPI version](https://img.shields.io/badge/pypi-v1.0.0-blue.svg)](#)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-00f0ff.svg)](#)
[![License: Proprietary / Commercial](https://img.shields.io/badge/license-Commercial-b829ff.svg)](#)

`pyprism` captures an entire Python virtual environment—including all dependencies, native libraries, and entrypoints—and transmutes it into an immutable, single-file executable crystal (`.pycryst`). Run your application anywhere Python 3 is installed with zero `pip install`, zero dependency drift, and guaranteed reproducible execution.

---

## Key Features

- **Single-File Hermetic Packaging**: Bundles `site-packages` into a standalone, executable zipimport archive.
- **Zero Dependency Drift**: Freezes exact dependency trees so code never breaks due to upstream package updates or ambient environments.
- **Zero Installation Overhead**: Runs natively on any POSIX system without needing virtualenv creation or external package managers.
- **Sub-Second Compilation**: Fast bytecode deduplication and optical compression.

---

## Installation

```bash
pip install pyprism
```

---

## Quickstart

### 1. Crystallize Active Virtualenv into a Single Executable
```bash
# Point to your entrypoint (module:function)
pyprism dist/my_app.pycryst --entrypoint mypackage.server:start
```

### 2. Run the Resulting Executable
The output `.pycryst` is directly executable:
```bash
chmod +x dist/my_app.pycryst
./dist/my_app.pycryst
```
Or execute with any Python 3 runtime:
```bash
python3 dist/my_app.pycryst
```

---

## Python API

```python
from pyprism import PyPrismVenvCrystallizer

crystallizer = PyPrismVenvCrystallizer()
result = crystallizer.crystallize(
    output_crystal_path="dist/production_service.pycryst",
    app_entrypoint="mypackage.server:main"
)

print(f"Crystallized {result['files_crystallized']} files in {result['compilation_time_ms']} ms")
```

---

## Corporate & Legal Notice

Copyright &copy; 2026 **Campfire Creative LLC DBA Iris Computing**. All rights reserved.
