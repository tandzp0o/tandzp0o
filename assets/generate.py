#!/usr/bin/env python3
"""Sinh các SVG động (lấp lánh) cho README. Chạy: python3 assets/generate.py"""
import random
from pathlib import Path

OUT = Path(__file__).parent
FONT = "system-ui,-apple-system,'Segoe UI',Roboto,'Noto Sans',sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
PALETTE = ["#ffffff", "#bcd9ff", "#58a6ff", "#d2a8ff", "#ffd6f5", "#ffe9a8"]


def sparkle(x, y, r, color, dur, delay, spin=False):
    """Ngôi sao 4 cánh, nhấp nháy theo opacity + scale."""
    k = r * 0.22
    d = (f"M0,{-r} C{k},{-k} {k},{-k} {r},0 C{k},{k} {k},{k} 0,{r} "
         f"C{-k},{k} {-k},{k} {-r},0 C{-k},{-k} {-k},{-k} 0,{-r}Z")
    rot = (f'<animateTransform attributeName="transform" type="rotate" from="0" to="90" '
           f'dur="{dur * 2:.1f}s" repeatCount="indefinite" additive="sum"/>') if spin else ""
    return (f'<g transform="translate({x:.1f},{y:.1f})"><path d="{d}" fill="{color}" opacity="0">'
            f'<animate attributeName="opacity" values="0;1;0" dur="{dur:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite"/>'
            f'<animateTransform attributeName="transform" type="scale" values="0.3;1;0.3" dur="{dur:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite"/>'
            f'{rot}</path></g>')


def dot(x, y, r, color, dur, delay):
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{color}" opacity="0.15">'
            f'<animate attributeName="opacity" values="0.15;1;0.15" dur="{dur:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite"/></circle>')


def field(rng, w, h, n_dots, n_sparkles, rmin=4, rmax=11):
    out = []
    for _ in range(n_dots):
        out.append(dot(rng.uniform(0, w), rng.uniform(0, h), rng.uniform(0.5, 1.6),
                       rng.choice(PALETTE), rng.uniform(1.6, 4.5), rng.uniform(0, 4)))
    for _ in range(n_sparkles):
        out.append(sparkle(rng.uniform(12, w - 12), rng.uniform(12, h - 12), rng.uniform(rmin, rmax),
                           rng.choice(PALETTE), rng.uniform(1.8, 4.2), rng.uniform(0, 5), rng.random() < 0.4))
    return "\n".join(out)


def shimmer(gid, w, colors=("#58a6ff", "#d2a8ff", "#ffffff", "#ffd6f5", "#58a6ff"), dur=4):
    """Gradient chạy ngang để chữ ánh lên."""
    stops = "".join(f'<stop offset="{i / (len(colors) - 1):.2f}" stop-color="{c}"/>' for i, c in enumerate(colors))
    return (f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{w}" y2="0" spreadMethod="reflect">'
            f'{stops}<animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="{w * 2} 0" '
            f'dur="{dur}s" repeatCount="indefinite"/></linearGradient>')


def shooting(x, y, length, dur, delay):
    return (f'<g opacity="0"><line x1="0" y1="0" x2="{length}" y2="0" stroke="url(#tail)" stroke-width="2" stroke-linecap="round" '
            f'transform="rotate(155)"/><circle r="2" fill="#fff"/>'
            f'<animateTransform attributeName="transform" type="translate" values="{x},{y};{x - 520},{y + 240}" '
            f'keyTimes="0;1" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>'
            f'<animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;0.03;0.14;0.2;1" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/></g>')


def hero(lang):
    w, h = 1200, 330
    rng = random.Random(7)
    t = {
        "en": dict(sub="fullstack developer  ·  ai/ml  ·  game dev", tags=["erp / crm", "university systems", "ai · xai research", "unity games", "community apps"], loc="ho chi minh city, vietnam"),
        "vi": dict(sub="lập trình viên fullstack  ·  ai/ml  ·  làm game", tags=["erp / crm", "hệ thống đại học", "nghiên cứu ai · xai", "game unity", "ứng dụng cộng đồng"], loc="tp. hồ chí minh, việt nam"),
    }[lang]
    # hàng pill
    pills, x = [], 0
    for i, tag in enumerate(t["tags"]):
        pw = len(tag) * 8.4 + 30
        pills.append(f'<g transform="translate({x:.0f},0)"><rect width="{pw:.0f}" height="30" rx="15" fill="#161b22" fill-opacity="0.75" stroke="url(#shine)" stroke-width="1.2"/>'
                     f'<text x="{pw / 2:.0f}" y="20" text-anchor="middle" fill="#e6edf3" font-family="{FONT}" font-size="14">{tag}</text></g>')
        x += pw + 12
    px = (w - (x - 12)) / 2
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Lê Trương Trọng Tấn">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d1117"/><stop offset="0.55" stop-color="#130f2a"/><stop offset="1" stop-color="#020409"/></linearGradient>
<radialGradient id="glowA" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#7c5cff" stop-opacity="0.55"/><stop offset="1" stop-color="#7c5cff" stop-opacity="0"/></radialGradient>
<radialGradient id="glowB" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#58a6ff" stop-opacity="0.45"/><stop offset="1" stop-color="#58a6ff" stop-opacity="0"/></radialGradient>
<linearGradient id="tail" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
{shimmer("shine", w)}
<clipPath id="clip"><rect width="{w}" height="{h}" rx="22"/></clipPath>
<filter id="soft" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="9"/></filter>
</defs>
<g clip-path="url(#clip)">
<rect width="{w}" height="{h}" fill="url(#bg)"/>
<ellipse cx="260" cy="60" rx="420" ry="230" fill="url(#glowA)"><animate attributeName="cx" values="260;420;260" dur="14s" repeatCount="indefinite"/></ellipse>
<ellipse cx="980" cy="300" rx="440" ry="240" fill="url(#glowB)"><animate attributeName="cx" values="980;800;980" dur="17s" repeatCount="indefinite"/></ellipse>
{field(rng, w, h, 130, 36, 5, 14)}
{shooting(1150, -20, 110, 7, 1)}
{shooting(820, -30, 90, 9, 4.5)}
{shooting(1300, 40, 130, 11, 7)}
<text x="{w / 2}" y="92" text-anchor="middle" fill="#8b949e" font-family="{MONO}" font-size="15" letter-spacing="3">~/tandzp0o</text>
<text x="{w / 2}" y="158" text-anchor="middle" fill="url(#shine)" font-family="{FONT}" font-size="60" font-weight="800" filter="url(#soft)" opacity="0.55">Lê Trương Trọng Tấn</text>
<text x="{w / 2}" y="158" text-anchor="middle" fill="url(#shine)" font-family="{FONT}" font-size="60" font-weight="800">Lê Trương Trọng Tấn</text>
<text x="{w / 2}" y="198" text-anchor="middle" fill="#c9d1d9" font-family="{FONT}" font-size="20" letter-spacing="1">{t["sub"]}</text>
<g transform="translate({px:.0f},226)">{"".join(pills)}</g>
<text x="{w / 2}" y="296" text-anchor="middle" fill="#6e7681" font-family="{MONO}" font-size="13" letter-spacing="2">{t["loc"]}</text>
</g>
<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="21" fill="none" stroke="url(#shine)" stroke-width="1.5" opacity="0.7"/>
</svg>'''


def section(title, seed):
    """Tiêu đề mục: nền trong suốt, đọc được ở cả giao diện sáng và tối."""
    w, h = 1200, 64
    rng = random.Random(seed)
    cols = ("#3b82f6", "#a855f7", "#ec4899", "#f59e0b", "#3b82f6")
    tw = len(title) * 14 + 6
    stars = "".join(sparkle(rng.uniform(tw + 70, w - 20), rng.uniform(12, h - 12), rng.uniform(4, 10),
                            rng.choice(cols), rng.uniform(1.6, 3.6), rng.uniform(0, 4), rng.random() < 0.4) for _ in range(16))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{title}">
<defs>{shimmer("g", w, cols, 5)}</defs>
{sparkle(22, 30, 15, "#a855f7", 2.4, 0, True)}
{sparkle(40, 14, 6, "#f59e0b", 1.8, 0.6)}
<text x="58" y="41" fill="url(#g)" font-family="{FONT}" font-size="28" font-weight="800" letter-spacing="1">{title}</text>
<rect x="{tw + 60}" y="31" width="{w - tw - 70}" height="2" rx="1" fill="url(#g)" opacity="0.45"/>
<circle r="3.5" cy="32" fill="#f59e0b"><animate attributeName="cx" values="{tw + 60};{w - 10}" dur="4s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;1;0" dur="4s" repeatCount="indefinite"/></circle>
{stars}
</svg>'''


def divider():
    w, h = 1200, 28
    rng = random.Random(3)
    cols = ("#3b82f6", "#a855f7", "#ec4899", "#f59e0b", "#3b82f6")
    stars = "".join(sparkle(rng.uniform(10, w - 10), rng.uniform(6, h - 6), rng.uniform(3, 7), rng.choice(cols),
                            rng.uniform(1.5, 3.5), rng.uniform(0, 4)) for _ in range(28))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="presentation">
<defs>{shimmer("g", w, cols, 5)}</defs>
<rect x="0" y="13" width="{w}" height="2" rx="1" fill="url(#g)" opacity="0.5"/>
{stars}
</svg>'''


def footer(lang):
    w, h = 1200, 130
    rng = random.Random(11)
    text = {"en": "thanks for visiting", "vi": "cảm ơn bạn đã ghé thăm"}[lang]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{text}">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d1117"/><stop offset="0.55" stop-color="#130f2a"/><stop offset="1" stop-color="#020409"/></linearGradient>
{shimmer("shine", w)}
<clipPath id="clip"><rect width="{w}" height="{h}" rx="22"/></clipPath>
</defs>
<g clip-path="url(#clip)"><rect width="{w}" height="{h}" fill="url(#bg)"/>
{field(rng, w, h, 70, 18, 3, 9)}
<text x="{w / 2}" y="74" text-anchor="middle" fill="url(#shine)" font-family="{FONT}" font-size="30" font-weight="700" letter-spacing="2">✦ {text} ✦</text>
</g>
<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="21" fill="none" stroke="url(#shine)" stroke-width="1.5" opacity="0.7"/>
</svg>'''


SECTIONS = {
    "about": ("about", "giới thiệu"),
    "experience": ("experience", "kinh nghiệm"),
    "projects": ("projects", "dự án"),
    "skills": ("skills", "kỹ năng"),
    "education": ("education", "học vấn"),
}

if __name__ == "__main__":
    files = {"divider.svg": divider()}
    for i, lang in enumerate(("en", "vi")):
        files[f"hero-{lang}.svg"] = hero(lang)
        files[f"footer-{lang}.svg"] = footer(lang)
        for j, (key, titles) in enumerate(SECTIONS.items()):
            files[f"sec-{key}-{lang}.svg"] = section(titles[i], 20 + j)
    for name, svg in files.items():
        (OUT / name).write_text(svg, encoding="utf-8")
        print(f"{name}: {len(svg) / 1024:.1f} KB")
