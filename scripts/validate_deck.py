#!/usr/bin/env python3

"""Validate one ECE6210 RISE notebook."""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path


ALLOWED_SLIDE_TYPES = {"slide", "subslide", "fragment", "skip", "notes", "-"}
IMAGE_PATTERN = re.compile(r"src=[\"']([^\"']+)[\"']", re.IGNORECASE)


def source_text(cell: dict) -> str:
    source = cell.get("source", [])
    if isinstance(source, str):
        return source
    return "".join(source)


def python_source_for_parse(source: str) -> str | None:
    lines = source.splitlines()
    first = next((line.strip() for line in lines if line.strip()), "")
    if first.startswith("%%"):
        return None

    cleaned = []
    for line in lines:
        if line.startswith("%") or line.startswith("!"):
            cleaned.append("pass")
        else:
            cleaned.append(line)
    return "\n".join(cleaned)


def validate(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"Notebook cannot be read: {exc}"], warnings

    if notebook.get("nbformat") != 4:
        errors.append("Notebook must use nbformat 4.")

    rise = notebook.get("metadata", {}).get("rise")
    if not isinstance(rise, dict):
        errors.append("Notebook metadata.rise is missing.")

    cells = notebook.get("cells")
    if not isinstance(cells, list) or not cells:
        errors.append("Notebook has no cells.")
        return errors, warnings

    first_type = cells[0].get("metadata", {}).get("slideshow", {}).get("slide_type")
    if first_type != "slide":
        errors.append("Cell 0 must start a new slide.")

    presented_cells = 0
    for index, cell in enumerate(cells):
        text = source_text(cell)
        slide_type = cell.get("metadata", {}).get("slideshow", {}).get("slide_type")

        if slide_type not in ALLOWED_SLIDE_TYPES:
            errors.append(f"Cell {index}: invalid or missing RISE slide_type.")
        elif slide_type != "skip":
            presented_cells += 1

        if "\u2014" in text:
            errors.append(f"Cell {index}: em dash is not permitted.")

        for image_reference in IMAGE_PATTERN.findall(text):
            if image_reference.startswith(("http://", "https://", "data:")):
                continue
            image_path = path.parent / image_reference
            if not image_path.exists():
                errors.append(f"Cell {index}: missing image {image_reference}.")

        if cell.get("cell_type") == "code":
            python_source = python_source_for_parse(text)
            if python_source is not None:
                try:
                    ast.parse(python_source)
                except SyntaxError as exc:
                    errors.append(
                        f"Cell {index}: Python syntax error on line {exc.lineno}: {exc.msg}."
                    )

            for output in cell.get("outputs", []):
                if output.get("output_type") == "error":
                    name = output.get("ename", "Error")
                    value = output.get("evalue", "")
                    errors.append(f"Cell {index}: stored execution error {name}: {value}.")

    if presented_cells > 70:
        warnings.append(
            f"Deck has {presented_cells} presented cells. Review the pacing above 70."
        )

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebook", type=Path)
    args = parser.parse_args()

    errors, warnings = validate(args.notebook)

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"PASSED: {args.notebook} with {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
