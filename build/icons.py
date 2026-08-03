"""Inline SVG icons for orientation strips (print-safe, greyscale-safe).

Paths use currentColor so CSS can set ink/muted. No external sprite fetch —
Playwright PDF and GitHub Pages both get the same inline markup.
"""

from __future__ import annotations

# Minimal 24×24 line icons. ViewBox shared; stroke inherits currentColor.
_ICONS: dict[str, str] = {
    # Compass / orientation
    "compass": (
        '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.5"/>'
        '<path d="M12 3v2M12 19v2M3 12h2M19 12h2" fill="none" stroke="currentColor" stroke-width="1.5"/>'
        '<path d="M12 8l2.5 6H9.5L12 8z" fill="currentColor"/>'
    ),
    # Book / Part I
    "book": (
        '<path d="M5 4.5h9.5A2.5 2.5 0 0 1 17 7v12.5H7.5A2.5 2.5 0 0 0 5 22V4.5z" '
        'fill="none" stroke="currentColor" stroke-width="1.5"/>'
        '<path d="M5 4.5A2.5 2.5 0 0 1 7.5 2H17" fill="none" stroke="currentColor" stroke-width="1.5"/>'
        '<path d="M9 8h5M9 11.5h5" fill="none" stroke="currentColor" stroke-width="1.4"/>'
    ),
    # Wrench / Part II
    "wrench": (
        '<path d="M14.5 6.5a3.5 3.5 0 0 0-4.7 4.7L4 17v3h3l5.8-5.8a3.5 3.5 0 0 0 4.7-4.7l-2.2 1.2-2.8-2.8 1-2.4z" '
        'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/>'
    ),
    # Stop / Part III (octagon)
    "stop": (
        '<path d="M8 3h8l5 5v8l-5 5H8l-5-5V8l5-5z" fill="none" stroke="currentColor" stroke-width="1.5"/>'
        '<path d="M8.5 12h7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>'
    ),
    # Edge / Part IV (broken corner)
    "edge": (
        '<path d="M4 8V4h4M20 8V4h-4M4 16v4h4M20 16v4h-4" fill="none" stroke="currentColor" stroke-width="1.5"/>'
        '<path d="M9 12h2.5L14 9.5 16.5 12H19" fill="none" stroke="currentColor" stroke-width="1.5" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
    ),
    # Link / appendix exit
    "link": (
        '<path d="M9.5 14.5l5-5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>'
        '<path d="M11 16.5l-1.2 1.2a3.2 3.2 0 0 1-4.5-4.5L6.5 12" fill="none" stroke="currentColor" '
        'stroke-width="1.5" stroke-linecap="round"/>'
        '<path d="M13 7.5l1.2-1.2a3.2 3.2 0 0 1 4.5 4.5L17.5 12" fill="none" stroke="currentColor" '
        'stroke-width="1.5" stroke-linecap="round"/>'
    ),
    # Path / reading path
    "path": (
        '<circle cx="6" cy="18" r="2" fill="none" stroke="currentColor" stroke-width="1.5"/>'
        '<circle cx="18" cy="6" r="2" fill="none" stroke="currentColor" stroke-width="1.5"/>'
        '<path d="M7.5 16.5C10 14 10 10 12 9s4-1 5.5-2.5" fill="none" stroke="currentColor" '
        'stroke-width="1.5" stroke-linecap="round"/>'
    ),
}


def svg_icon(name: str, *, css_class: str = "nav-icon-svg") -> str:
    paths = _ICONS.get(name) or _ICONS["compass"]
    # role=img + aria-hidden: decorative; surrounding text carries meaning.
    return (
        f'<svg class="{css_class}" width="16" height="16" viewBox="0 0 24 24" '
        f'xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false">'
        f"{paths}</svg>"
    )


def icon_label(name: str, label: str) -> str:
    return (
        f'<span class="nav-icon-label">'
        f'{svg_icon(name)}'
        f'<span class="nav-icon-text">{label}</span>'
        f"</span>"
    )
