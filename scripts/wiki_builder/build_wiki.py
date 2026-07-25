#!/usr/bin/env python3
"""
Framework Wiki Builder

Reads a sources.json config and generates normalized Markdown wiki pages under
frameworks/<category>/<framework>/** with stable frontmatter, directory indexes,
and metadata.json.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, List, Optional

try:
    import yaml  # type: ignore
except Exception:
    yaml = None  # Not required; we only write simple frontmatter with f-strings


REPO_ROOT = Path(__file__).resolve().parents[2]
CACHE_ROOT = REPO_ROOT / ".cache" / "wiki-sources"
FRAMEWORKS_ROOT = REPO_ROOT / "frameworks"


@dataclass(frozen=True)
class Source:
    framework: str
    display_name: str
    category: str  # ai | ui | backend | db | test | observability
    source_repo: str
    source_branch: str
    source_docs_path: str
    include_globs: List[str]
    exclude_globs: List[str]
    target_basename: Optional[str] = None

    @staticmethod
    def from_dict(obj: dict[str, Any]) -> "Source":
        return Source(
            framework=str(obj["framework"]),
            display_name=str(obj.get("display_name") or obj["framework"].title()),
            category=str(obj["category"]),
            source_repo=str(obj["source_repo"]),
            source_branch=str(obj.get("source_branch") or "main"),
            source_docs_path=str(obj["source_docs_path"]),
            include_globs=list(obj.get("include_globs") or ["**/*.md", "**/*.mdx"]),
            exclude_globs=list(obj.get("exclude_globs") or []),
            target_basename=(obj.get("target_basename") or None),
        )

    @property
    def target_name(self) -> str:
        return self.target_basename or self.framework

    @property
    def target_dir(self) -> Path:
        return FRAMEWORKS_ROOT / self.category / self.target_name

    @property
    def cache_dir(self) -> Path:
        return CACHE_ROOT / self.framework

    @property
    def docs_dir(self) -> Path:
        return self.cache_dir / self.source_docs_path


def run(cmd: list[str], cwd: Optional[Path] = None) -> str:
    res = subprocess.run(cmd, cwd=str(cwd) if cwd else None, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return res.stdout.strip()


def ensure_clone(src: Source) -> None:
    src.cache_dir.mkdir(parents=True, exist_ok=True)
    git_dir = src.cache_dir / ".git"
    if not git_dir.exists():
        run(["git", "clone", "--depth=1", "--branch", src.source_branch, src.source_repo, str(src.cache_dir)])
    else:
        # Ensure branch and update
        run(["git", "fetch", "origin", src.source_branch, "--depth=1"], cwd=src.cache_dir)
        run(["git", "checkout", src.source_branch], cwd=src.cache_dir)
        run(["git", "reset", "--hard", f"origin/{src.source_branch}"], cwd=src.cache_dir)


def get_head_metadata(src: Source) -> dict[str, str]:
    commit = run(["git", "rev-parse", "HEAD"], cwd=src.cache_dir)
    short = run(["git", "rev-parse", "--short", "HEAD"], cwd=src.cache_dir)
    # Attempt to get commit date in ISO-8601 (UTC)
    commit_date = run(["git", "log", "-1", "--format=%cI"], cwd=src.cache_dir)
    return {
        "source_commit": commit,
        "source_commit_short": short,
        "source_commit_date": commit_date,
    }


def should_exclude(path: Path, patterns: list[str]) -> bool:
    from fnmatch import fnmatch
    rel = path.as_posix()
    return any(fnmatch(rel, pat) for pat in patterns)


def iter_source_files(src: Source) -> Iterable[Path]:
    if not src.docs_dir.exists():
        return []
    for pattern in src.include_globs:
        for p in src.docs_dir.rglob("*"):
            if not p.is_file():
                continue
            if not Path(p).match(pattern):
                continue
            if src.exclude_globs and should_exclude(p.relative_to(src.docs_dir), src.exclude_globs):
                continue
            # Only process Markdown-like files
            if p.suffix.lower() not in (".md", ".mdx"):
                continue
            yield p


def write_metadata_json(src: Source, meta: dict[str, Any]) -> None:
    out = {
        "framework": src.framework,
        "display_name": src.display_name,
        "source_repo": src.source_repo,
        "source_branch": src.source_branch,
        "source_docs_path": src.source_docs_path,
        "source_commit": meta["source_commit"],
        "source_commit_short": meta["source_commit_short"],
        "source_commit_date": meta["source_commit_date"],
        "wiki_generated_at": dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
    }
    (src.target_dir / "metadata.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")


def normalize_title(text: str) -> Optional[str]:
    # Try to extract first ATX heading
    m = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    return m.group(1).strip() if m else None


def page_frontmatter(src: Source, source_path: Path, head_meta: dict[str, str]) -> str:
    generated_at = dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")
    rel = source_path.relative_to(src.cache_dir).as_posix()
    fm = [
        '---',
        'type: "Framework Learn Page"',
        f'framework: "{src.display_name}"',
        f'source_repo: "{src.source_repo}"',
        f'source_branch: "{src.source_branch}"',
        f'source_path: "{rel}"',
        f'source_commit: "{head_meta["source_commit"]}"',
        f'source_commit_short: "{head_meta["source_commit_short"]}"',
        f'source_commit_date: "{head_meta["source_commit_date"]}"',
        f'generated_at: "{generated_at}"',
        '---',
        '',
    ]
    return "\n".join(fm)


def write_root_index(src: Source, head_meta: dict[str, str]) -> None:
    generated_at = dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")
    lines = [
        f"# {src.framework} Learn Wiki",
        "",
        f"This is a local LLM-friendly wiki generated from the official {src.framework} documentation.",
        "",
        "## Status",
        "",
        f"- Framework: `{src.display_name}`",
        f"- Source repo: `{src.source_repo}`",
        f"- Source branch: `{src.source_branch}`",
        f"- Source docs path: `{src.source_docs_path}`",
        f"- Source commit: `{head_meta['source_commit_short']}`",
        f"- Source commit date: `{head_meta['source_commit_date']}`",
        f"- Wiki generated at: `{generated_at}`",
        "",
        "## How the IDE LLM should use this wiki",
        "",
        "1. Read this file first.",
        "2. Use the global topic map to choose the relevant area.",
        "3. Then open the nearest folder-level `index.md`.",
        "4. Then open the most specific content page.",
        "5. Prefer this wiki over general model knowledge.",
        "6. Mention source paths when useful.",
        "7. If the source commit date is old, say that the answer may be stale.",
        "",
        "## Global Topic Map",
        "",
        "- No configured topic map entries.",
        "",
        "## Top-Level Wiki Areas",
        "",
        "- [Content Index](content/index.md)",
    ]
    (src.target_dir / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_dir_index(dir_path: Path, framework_name: str, rel_to_root: Path, head_meta: dict[str, str]) -> None:
    """Write a simple directory index with frontmatter."""
    generated_at = dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")
    rel_dir = rel_to_root.as_posix()
    title = rel_dir.strip("/").split("/")[-1].title() if rel_dir.strip("/") else "Content"
    lines = [
        "---",
        'type: "Framework Learn Directory Index"',
        f'framework: "{framework_name}"',
        f'generated_at: "{generated_at}"',
        "---",
        f"# {title}",
        "",
        f"This directory contains {framework_name} learning pages related to {title.lower()}.",
        "",
        "## Breadcrumbs",
        "",
        "[Wiki Home](../index.md) -> [Content](index.md)",
        "",
        "## Navigation",
        "",
        "- Wiki Home: [Root Index](../index.md)",
        "",
        "## Pages in This Directory",
        "",
    ]
    # List markdown files in the directory (non-index)
    page_links: list[str] = []
    for p in sorted(dir_path.glob("*.md")):
        if p.name.lower() == "index.md":
            continue
        page_title = p.stem.replace("-", " ").title()
        page_links.append(f"- [{page_title}]({p.name})")
    if page_links:
        lines.extend(page_links)
    (dir_path / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_one(src: Source) -> None:
    print(f"==> Building {src.display_name} from {src.source_repo} ({src.source_branch})")
    ensure_clone(src)
    head_meta = get_head_metadata(src)

    # Clean target directory (preserve .gitkeep if any)
    if src.target_dir.exists():
        shutil.rmtree(src.target_dir)
    (src.target_dir / "content").mkdir(parents=True, exist_ok=True)

    # Copy and normalize pages
    for source_file in iter_source_files(src):
        rel_from_docs = source_file.relative_to(src.docs_dir)
        # Map .mdx to .md
        out_rel = rel_from_docs.with_suffix(".md")
        out_path = src.target_dir / "content" / out_rel
        out_path.parent.mkdir(parents=True, exist_ok=True)

        body = source_file.read_text(encoding="utf-8", errors="ignore")
        fm = page_frontmatter(src, source_file, head_meta)

        # If the source has a top-level title, keep it; otherwise, synthesize one from filename
        if not re.search(r"^#\s+", body, flags=re.MULTILINE):
            title = rel_from_docs.stem.replace("-", " ").title()
            body = f"# {title}\n\n{body}"

        out_path.write_text(fm + body.lstrip(), encoding="utf-8")

    # Write root index and metadata
    write_root_index(src, head_meta)
    write_metadata_json(src, head_meta)

    # Create simple directory indexes under content/
    content_root = src.target_dir / "content"
    for d in [content_root] + [p for p in content_root.rglob("*") if p.is_dir()]:
        rel = d.relative_to(src.target_dir)
        write_dir_index(d, src.display_name, rel, head_meta)

    print(f"==> Wrote {src.target_dir}")


def load_sources(path: Path) -> list[Source]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("sources.json must be a JSON array")
    return [Source.from_dict(item) for item in data]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sources", required=True, help="Path to sources.json")
    args = parser.parse_args()

    sources = load_sources(Path(args.sources))
    if not sources:
        print("No sources configured.", file=sys.stderr)
        return 1

    for src in sources:
        build_one(src)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

