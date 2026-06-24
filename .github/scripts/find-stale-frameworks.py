#!/usr/bin/env python3
"""Find framework wiki directories that have not been updated recently."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DISPLAY_NAME_OVERRIDES = {
    "beanie": "Beanie",
    "fastapi": "FastAPI",
    "jest": "Jest",
    "mongodb": "MongoDB",
    "nextjs": "Next.js",
    "postgres": "PostgreSQL",
    "pydantic": "Pydantic",
    "pymongo": "PyMongo",
    "pytest": "pytest",
    "react": "React",
    "redis": "Redis",
    "shadcnui": "shadcn/ui",
    "sqlalchemy": "SQLAlchemy",
    "sqlalchemy/alembic": "Alembic",
    "tanstack": "TanStack",
    "zod": "Zod",
}


def run_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return result.stdout.strip()


def parse_datetime(value: str) -> datetime:
    if value.endswith("Z"):
        value = f"{value[:-1]}+00:00"
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def load_metadata(path: str) -> dict[str, Any]:
    with Path(path).open(encoding="utf-8") as metadata_file:
        return json.load(metadata_file)


def display_name_for(framework_path: str, metadata: dict[str, Any]) -> str:
    framework_name = str(metadata.get("framework") or Path(framework_path).name)
    display_name = metadata.get("display_name")
    if display_name:
        display_name = str(display_name)
        return DISPLAY_NAME_OVERRIDES.get(framework_name) or DISPLAY_NAME_OVERRIDES.get(display_name, display_name)

    return DISPLAY_NAME_OVERRIDES.get(framework_name, framework_name.replace("-", " ").title())


def discover_frameworks() -> list[dict[str, str]]:
    metadata_paths = run_git(["ls-files", "frameworks/**/metadata.json"]).splitlines()
    frameworks: list[dict[str, str]] = []

    for metadata_path in metadata_paths:
        framework_path = str(Path(metadata_path).parent)
        metadata = load_metadata(metadata_path)
        frameworks.append(
            {
                "path": framework_path,
                "display_name": display_name_for(framework_path, metadata),
            }
        )

    return sorted(frameworks, key=lambda framework: framework["path"])


def nested_framework_paths(framework_path: str, all_framework_paths: list[str]) -> list[str]:
    prefix = f"{framework_path}/"
    return [
        candidate
        for candidate in all_framework_paths
        if candidate != framework_path and candidate.startswith(prefix)
    ]


def last_repo_update(framework_path: str, all_framework_paths: list[str]) -> datetime | None:
    pathspecs = [framework_path]
    for nested_path in nested_framework_paths(framework_path, all_framework_paths):
        pathspecs.append(f":(exclude){nested_path}")

    output = run_git(["log", "-1", "--format=%cI", "--", *pathspecs])
    if not output:
        return None
    return parse_datetime(output)


def find_stale_frameworks(now: datetime, threshold_days: int) -> list[dict[str, Any]]:
    frameworks = discover_frameworks()
    framework_paths = [framework["path"] for framework in frameworks]
    stale_frameworks: list[dict[str, Any]] = []

    for framework in frameworks:
        last_updated_at = last_repo_update(framework["path"], framework_paths)
        if last_updated_at is None:
            continue

        age_days = (now - last_updated_at).days
        if age_days > threshold_days:
            stale_frameworks.append(
                {
                    "path": framework["path"],
                    "display_name": framework["display_name"],
                    "last_updated_at": last_updated_at.isoformat().replace("+00:00", "Z"),
                    "age_days": age_days,
                    "threshold_days": threshold_days,
                    "marker": f"framework-freshness:{framework['path']}",
                }
            )

    return stale_frameworks


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--threshold-days", type=int, default=30)
    parser.add_argument("--now", help="ISO-8601 timestamp used for deterministic tests")
    parser.add_argument("--output", default="framework-freshness-report.json")
    args = parser.parse_args()

    if args.threshold_days < 0:
        parser.error("--threshold-days must be zero or greater")

    now = parse_datetime(args.now) if args.now else datetime.now(timezone.utc)
    stale_frameworks = find_stale_frameworks(now=now, threshold_days=args.threshold_days)

    report = {
        "generated_at": now.isoformat().replace("+00:00", "Z"),
        "threshold_days": args.threshold_days,
        "stale_frameworks": stale_frameworks,
    }
    Path(args.output).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
