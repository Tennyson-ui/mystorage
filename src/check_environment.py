"""Verificacao simples do ambiente da Atividade 3 SWOT."""

from __future__ import annotations

import importlib
import os
import platform
from pathlib import Path


PACKAGES = [
    "earthaccess",
    "xarray",
    "netCDF4",
    "h5netcdf",
    "pandas",
    "geopandas",
    "shapely",
    "pyproj",
    "matplotlib",
    "ipyleaflet",
    "ipywidgets",
    "fiona",
    "pyogrio",
    "numpy",
    "requests",
    "pyarrow",
]


def check_import(package: str) -> bool:
    try:
        importlib.import_module(package)
    except Exception as exc:  # pragma: no cover - diagnostic script
        print(f"FALHA import {package}: {exc}")
        return False
    print(f"OK import {package}")
    return True


def check_write() -> bool:
    output_dir = Path("outputs") / "logs"
    output_dir.mkdir(parents=True, exist_ok=True)
    test_file = output_dir / "check_environment.tmp"
    try:
        test_file.write_text("ok\n", encoding="utf-8")
        test_file.unlink(missing_ok=True)
    except Exception as exc:  # pragma: no cover - diagnostic script
        print(f"FALHA escrita em {output_dir}: {exc}")
        return False
    print(f"OK escrita em {output_dir}")
    return True


def main() -> int:
    print("Verificacao do ambiente - Atividade 3 SWOT")
    print(f"Python: {platform.python_version()}")
    print(f"Sistema: {platform.platform()}")
    print(f"Diretorio atual: {Path.cwd()}")
    print(f"HOME: {os.environ.get('HOME', '(nao definido)')}")
    print()

    results = [check_import(package) for package in PACKAGES]
    results.append(check_write())

    print()
    if all(results):
        print("OK ambiente basico verificado.")
        return 0

    print("FALHA ambiente com pendencias. Instale os pacotes ausentes e rode novamente.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
