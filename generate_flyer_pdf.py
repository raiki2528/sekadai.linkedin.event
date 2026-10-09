#!/usr/bin/env python3
"""Generate 2-page flyer PDF from flyer.html (1080×1920 per page)."""

from pathlib import Path

DIR = Path(__file__).resolve().parent
HTML = DIR / "flyer.html"
PDF = DIR / "世界一周大学×LinkedIn チラシ 2026-10-15.pdf"
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")


def main() -> None:
    from playwright.sync_api import sync_playwright

    url = HTML.as_uri()
    with sync_playwright() as p:
        launch_options = {"executable_path": str(CHROME)} if CHROME.exists() else {}
        browser = p.chromium.launch(**launch_options)
        page = browser.new_page(viewport={"width": 1080, "height": 800})
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(800)
        page.pdf(
            path=str(PDF),
            width="1080px",
            height="1920px",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        browser.close()
    print(f"Wrote {PDF}")


if __name__ == "__main__":
    main()
