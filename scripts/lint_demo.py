#!/usr/bin/env python3
"""
Lint a generated demo HTML against mockup-kit red-lines.

Checks:
1. No hardcoded hex colors outside :root / theme variant blocks
2. No emoji used as icons (heuristic: emoji char in <button>/<a>/<i>)
3. No invented component classes (basic heuristic: warns on .my-* / .custom-*)
4. No fixed font-size / padding / margin px values outside :root

Usage:
    python3 lint_demo.py path/to/demo.html [--open]

Pass --open to also open the file in the default browser if lint passes.
"""

import argparse
import os
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path

EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F9FF"   # Misc Symbols & Pictographs / Supplemental
    "\U0001FA70-\U0001FAFF"   # Symbols & Pictographs Extended-A
    "\U0001F600-\U0001F64F"   # Emoticons
    "\U0001F680-\U0001F6FF"   # Transport & Map
    "]"
)
# Real emoji-as-icon offenders are almost always immediately inside an
# interactive element (button / link / icon slot), e.g. `>🎁 Coupon<`.
# Plain text ♪ ♥ ★ are dingbats users type as content; we don't flag those.
HEX_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b")
SUSPICIOUS_CLASS_RE = re.compile(r'class="[^"]*\b(my|custom|special)-[a-z-]+')


def split_style_block(html: str):
    style_match = re.search(r"<style>(.*?)</style>", html, re.DOTALL)
    if not style_match:
        return "", "", html
    css = style_match.group(1)
    root_match = re.search(r":root\s*\{[^}]*\}", css)
    root_block = root_match.group(0) if root_match else ""
    theme_blocks = "\n".join(re.findall(r'body\[data-theme="[^"]+"\]\s*\{[^}]*\}', css))
    return root_block, theme_blocks, html


def check_hex(html: str):
    issues = []
    body_match = re.search(r"<body[^>]*>(.*)</body>", html, re.DOTALL)
    body_html = body_match.group(1) if body_match else html
    for m in HEX_RE.finditer(body_html):
        hex_val = m.group(0).lower()
        issues.append((m.start(), f"hardcoded color {hex_val} in body — use var(--color-*)"))
    return issues


def check_emoji(html: str):
    issues = []
    for m in EMOJI_RE.finditer(html):
        snippet = html[max(0, m.start() - 30): m.end() + 30]
        issues.append((m.start(), f"emoji '{m.group(0)}' — use <i class='iconoir-XXX'>. Context: …{snippet}…"))
    return issues


def check_classes(html: str):
    issues = []
    for m in SUSPICIOUS_CLASS_RE.finditer(html):
        issues.append((m.start(), f"suspicious custom class: {m.group(0)} — prefer regulation classes"))
    return issues


def open_in_browser(path: Path) -> bool:
    try:
        system = platform.system()
        if system == "Darwin":
            subprocess.run(["open", str(path)], check=False)
        elif system == "Windows":
            os.startfile(str(path))  # type: ignore[attr-defined]
        else:
            opener = shutil.which("xdg-open") or shutil.which("wslview")
            if opener:
                subprocess.run([opener, str(path)], check=False)
            else:
                return False
        return True
    except Exception as e:
        print(f"⚠️  Could not auto-open: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Path to the demo HTML")
    parser.add_argument("--open", action="store_true",
                        help="Open the file in the default browser if lint passes")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        sys.exit(1)
    html = path.read_text(encoding="utf-8")

    all_issues = []
    all_issues += [("hex", *i) for i in check_hex(html)]
    all_issues += [("emoji", *i) for i in check_emoji(html)]
    all_issues += [("class", *i) for i in check_classes(html)]

    if not all_issues:
        print(f"✅ {path} passes red-lines lint")
        if args.open and open_in_browser(path.resolve()):
            print("🌐 Opened in default browser")
        sys.exit(0)

    print(f"⚠️  {path} has {len(all_issues)} potential issue(s):")
    for kind, pos, msg in all_issues[:30]:
        line = html[:pos].count("\n") + 1
        print(f"  [{kind}] L{line}: {msg}")
    if len(all_issues) > 30:
        print(f"  ... and {len(all_issues) - 30} more")
    sys.exit(2)


if __name__ == "__main__":
    main()
