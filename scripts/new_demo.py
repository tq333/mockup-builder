#!/usr/bin/env python3
"""
Initialize a new demo file by copying the base template.

Usage:
    python3 new_demo.py [output.html] [--theme {default,yellow,green,purple,pink}]
                       [--title "Page Title"] [--multi] [--no-open]

Defaults:
    output.html = ./demo.html
    theme       = default
    title       = "Mockup Demo"
    auto-open   = on (pass --no-open to skip)

The generated file has the body pre-filled with a tiny placeholder so the
agent can run the lint script and open it in the browser immediately, then
incrementally replace the body content with actual page structure.
"""

import argparse
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
TEMPLATE_BASE = SCRIPT_DIR.parent / "assets" / "template-base.html"
TEMPLATE_MULTI = SCRIPT_DIR.parent / "assets" / "template-multi.html"

PLACEHOLDER_BODY = """
<nav class="navbar">
  <a href="#" class="navbar-brand"><i class="iconoir-sparks"></i> Demo</a>
  <div class="navbar-spacer" style="flex:1"></div>
</nav>
<main style="max-width:1200px;margin:0 auto;padding:var(--sp8) var(--sp6)">
  <h1 style="font-size:var(--fs-2xl);font-weight:700;margin-bottom:var(--sp4)">Demo placeholder</h1>
  <p style="color:var(--color-muted);font-size:var(--fs-sm);max-width:560px;line-height:1.7">
    The agent will replace this body with the actual page structure.
    If you can read this in a browser, the template is wired correctly.
  </p>
</main>
""".strip()


def open_in_browser(path: Path) -> bool:
    """Open the file in the default browser. Return True on success."""
    try:
        system = platform.system()
        if system == "Darwin":
            subprocess.run(["open", str(path)], check=False)
        elif system == "Windows":
            os.startfile(str(path))  # type: ignore[attr-defined]
        else:  # Linux / others
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
    parser.add_argument("output", nargs="?", default="demo.html")
    parser.add_argument("--theme", default="default",
                        choices=["default", "yellow", "green", "purple", "pink"])
    parser.add_argument("--title", default="Mockup Demo")
    parser.add_argument("--multi", action="store_true",
                        help="Use multi-variant template (sidebar + scroll-spy)")
    parser.add_argument("--no-open", action="store_true",
                        help="Skip auto-opening the file in the default browser")
    args = parser.parse_args()

    template = TEMPLATE_MULTI if args.multi else TEMPLATE_BASE
    if not template.exists():
        print(f"Template not found: {template}", file=sys.stderr)
        sys.exit(1)

    html = template.read_text(encoding="utf-8")
    body_attrs = "" if args.theme == "default" else f' data-theme="{args.theme}"'
    html = html.replace("<!-- SLOT:title -->Mockup Demo", args.title)
    html = html.replace("<!-- SLOT:body-attrs -->", body_attrs)
    if not args.multi:
        html = html.replace("<!-- SLOT:body -->", PLACEHOLDER_BODY)
    html = html.replace("<!-- SLOT:page-styles -->", "")

    out = Path(args.output).resolve()
    out.write_text(html, encoding="utf-8")
    print(f"✅ Created: {out}")
    print(f"   Open with: file://{out}")

    if not args.no_open:
        if open_in_browser(out):
            print("🌐 Opened in default browser")


if __name__ == "__main__":
    main()
