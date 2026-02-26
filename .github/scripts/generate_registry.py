import pathlib
from typing import Any, Dict, List

import yaml


def find_metadata_files(search_root: pathlib.Path) -> List[pathlib.Path]:
    """Find all metadata.yaml files under <repo_root>/*/metadata/metadata.yaml."""
    paths: List[pathlib.Path] = []
    if not search_root.exists():
        return paths

    for metadata_path in search_root.rglob("metadata.yaml"):
        # We are interested only in <repo_root>/<example_name>/metadata/metadata.yaml
        if metadata_path.parent.name != "metadata":
            continue
        paths.append(metadata_path)

    return paths


def build_registry(entries_paths: List[pathlib.Path], repo_root: pathlib.Path) -> Dict[str, Any]:
    """Load all metadata files and build the registry structure."""
    examples: List[Dict[str, Any]] = []

    for metadata_path in entries_paths:
        example_dir = metadata_path.parent.parent

        with metadata_path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}

        examples.append(data)

    # Stable ordering by id
    examples.sort(key=lambda item: str(item.get("id", "")))

    return {"examples": examples}


def write_registry(registry: Dict[str, Any], output_path: pathlib.Path) -> None:
    """Write registry.yaml with a blank line between examples for readability."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    raw = yaml.safe_dump(registry, sort_keys=False, allow_unicode=True)
    lines = raw.splitlines()

    pretty_lines: List[str] = []
    seen_item = False

    for line in lines:
        # Top-level list item (our examples entries)
        if line.startswith("- "):
            if seen_item:
                # Blank line before every item except the first
                pretty_lines.append("")
            seen_item = True

        pretty_lines.append(line)

    text = "\n".join(pretty_lines) + "\n"

    with output_path.open("w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    # This script lives in <repo_root>/.github/scripts/generate_registry.py,
    # so the repository root is two levels above this file.
    repo_root = pathlib.Path(__file__).resolve().parents[2]

    metadata_files = find_metadata_files(repo_root)
    registry = build_registry(metadata_files, repo_root)

    output_path = repo_root / "registry.yaml"
    write_registry(registry, output_path)


if __name__ == "__main__":
    main()

