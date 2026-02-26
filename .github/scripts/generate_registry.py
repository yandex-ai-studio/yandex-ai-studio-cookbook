import pathlib
from typing import Any, Dict, List

import yaml


def find_metadata_files(examples_root: pathlib.Path) -> List[pathlib.Path]:
    """Find all metadata.yaml files under examples/*/metadata/metadata.yaml."""
    paths: List[pathlib.Path] = []
    if not examples_root.exists():
        return paths

    for metadata_path in examples_root.rglob("metadata.yaml"):
        # We are interested only in .../examples/<example_name>/metadata/metadata.yaml
        if metadata_path.parent.name != "metadata":
            continue
        # Ensure there is an example directory above
        if metadata_path.parent.parent == examples_root:
            # examples/metadata/metadata.yaml — skip such misplaced files
            continue
        paths.append(metadata_path)

    return paths


def build_registry(entries_paths: List[pathlib.Path], repo_root: pathlib.Path) -> Dict[str, Any]:
    """Load all metadata files and build the registry structure."""
    examples: List[Dict[str, Any]] = []

    for metadata_path in entries_paths:
        example_dir = metadata_path.parent.parent
        example_id = example_dir.name

        with metadata_path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}

        # Enrich with some standard fields
        if "id" not in data:
            data["id"] = example_id
        if "path" not in data:
            # Path relative to repo root (e.g. "onboarding_agent")
            data["path"] = str(example_dir.relative_to(repo_root))

        examples.append(data)

    # Stable ordering by id
    examples.sort(key=lambda item: str(item.get("id", "")))

    return {"examples": examples}


def write_registry(registry: Dict[str, Any], output_path: pathlib.Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(registry, f, sort_keys=False, allow_unicode=True)


def main() -> None:
    repo_root = pathlib.Path(__file__).resolve().parents[2]
    examples_root = repo_root / "examples"

    metadata_files = find_metadata_files(examples_root)
    registry = build_registry(metadata_files, repo_root)

    output_path = repo_root / "registry.yaml"
    write_registry(registry, output_path)


if __name__ == "__main__":
    main()

