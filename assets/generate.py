#!/usr/bin/env python3
"""Sinh các SVG động (lấp lánh) cho README. Chạy: python3 assets/generate.py"""
import json
import math
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


ICONS = json.loads((OUT / "icons.json").read_text())  # simple-icons 11.15.0 (CC0)

# (slug icon, nhãn, màu ghi đè nếu màu gốc quá tối trên nền đêm)
SKILLS = [
    ("nextdotjs", "Next.js", "#ffffff"), ("react", "React", None), ("typescript", "TypeScript", None),
    ("javascript", "JavaScript", None), ("nodedotjs", "Node.js", None), ("dotnet", "ASP.NET Core", None),
    ("csharp", "C#", None), ("angular", "Angular", "#dd0031"), ("tailwindcss", "Tailwind", None),
    ("mongodb", "MongoDB", None), ("microsoftsqlserver", "SQL Server", None), ("postgresql", "PostgreSQL", None),
    ("python", "Python", None), ("unity", "Unity", None), ("blender", "Blender", None),
    ("docker", "Docker", None), ("git", "Git", None), ("vercel", "Vercel", "#ffffff"),
    ("cloudinary", "Cloudinary", None), ("pwa", "PWA", None),
]


def brighten(hexcol, min_lum=0.42):
    """Pha trắng vào màu thương hiệu quá tối để đọc được trên nền tối."""
    r, g, b = (int(hexcol[i:i + 2], 16) / 255 for i in (1, 3, 5))
    lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
    if lum >= min_lum:
        return hexcol
    t = min(1, (min_lum - lum) / (1 - lum) + 0.15)
    r, g, b = (c + (1 - c) * t for c in (r, g, b))
    return "#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255))


CHIP_R = 29  # bán kính chip tròn chỉ có icon


def flying_chip(rng, slug, label, color, fx, fy, vx, vy, begin, period=14.0, fly=2.4):
    """Chip icon xuất phát nhỏ xíu ở điểm xa (vx,vy), bay theo đường cong nhỏ, to dần rồi đậu ở (fx,fy).
    Cuối chu kỳ phóng to lướt qua 'camera' và mờ đi, rồi lặp lại."""
    col = brighten(color or "#" + ICONS[slug]["hex"])
    R = CHIP_R
    # đường cong bậc 2 từ điểm xa tới (0,0) trong toạ độ đích
    sx, sy = vx - fx, vy - fy
    length = math.hypot(sx, sy) or 1
    bend = rng.choice((-1, 1)) * rng.uniform(0.16, 0.3) * length
    cx, cy = sx / 2 + (-sy / length) * bend, sy / 2 + (sx / length) * bend
    path = f"M{sx:.1f},{sy:.1f} Q{cx:.1f},{cy:.1f} 0,0"

    k1, k2, k3 = fly / period, (period - 2.6) / period, (period - 1.5) / period
    kt = f"0;{k1:.4f};{k2:.4f};{k3:.4f};1"
    ease = "0.45 0 0.2 1;0 0 1 1;0.5 0 1 1;0 0 1 1"
    timing = f'dur="{period}s" begin="{begin:.2f}s" repeatCount="indefinite"'
    bob = rng.uniform(2.8, 4.6)

    halo = rng.uniform(2.2, 3.8)
    body = (f'<title>{label}</title>'
            f'<circle r="{R + 8}" fill="{col}" opacity="0.1"><animate attributeName="opacity" values="0.05;0.22;0.05" '
            f'dur="{halo:.1f}s" repeatCount="indefinite"/></circle>'
            f'<circle r="{R}" fill="#0b0f19" fill-opacity="0.9" stroke="{col}" stroke-opacity="0.8" stroke-width="1.6"/>'
            f'<path d="{ICONS[slug]["d"]}" fill="{col}" transform="translate(-15,-15) scale(1.25)"/>'
            + sparkle(R * 0.72, -R * 0.72, 7, "#ffffff", rng.uniform(1.8, 3.2), rng.uniform(0, 4)))
    return f'''<g transform="translate({fx:.1f},{fy:.1f})">
<path d="{path}" pathLength="1" fill="none" stroke="{col}" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="1 1" stroke-dashoffset="1" opacity="0">
<animate attributeName="stroke-dashoffset" values="1;0;0;0;0" keyTimes="{kt}" calcMode="spline" keySplines="{ease}" {timing}/>
<animate attributeName="opacity" values="0;0.55;0;0;0" keyTimes="0;{k1 * 0.75:.4f};{k1 * 1.25:.4f};{k3:.4f};1" {timing}/>
</path>
<g opacity="0">
<animateMotion path="{path}" keyPoints="0;1;1;1;1" keyTimes="{kt}" calcMode="spline" keySplines="{ease}" {timing}/>
<animateTransform attributeName="transform" type="scale" values="0.03;1;1;1.7;1.7" keyTimes="{kt}" calcMode="spline" keySplines="{ease}" {timing}/>
<animate attributeName="opacity" values="0;1;1;0;0" keyTimes="{kt}" calcMode="spline" keySplines="0 0.7 0.4 1;0 0 1 1;0.4 0 1 1;0 0 1 1" {timing}/>
<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -5;0 0" dur="{bob:.1f}s" repeatCount="indefinite"/>
{body}
</g></g></g>'''


# ───────────────────────── pixel art (tự vẽ) ─────────────────────────
PX = 4  # 1 điểm ảnh pixel = 4 đơn vị SVG

PAL = {
    "k": "#1a1c2c", "h": "#3b2a4a", "s": "#f6c7a1", "d": "#d9926a", "r": "#f28b8b", "w": "#ffffff",
    # lập trình viên
    "b": "#3b6fd8", "g": "#c9d1d9", "c": "#58a6ff", "C": "#a5d6ff", "G": "#6e7681", "n": "#2d3047",
    # lửa
    "F": "#e8451e", "f": "#ff8c1a", "y": "#ffd23f", "o": "#8a4b2a", "O": "#5c2e17",
    # tu sĩ
    "W": "#e8f0ff", "V": "#9fb4d9", "t": "#2ec4b6", "L": "#bcd9ff",
    # gym
    "a": "#e84a5f", "P": "#3d4250", "S": "#9aa4b2",
    # slime
    "m": "#5ad16b", "M": "#2f9e44",
    # mèo
    "e": "#f4a259", "E": "#c46a2a",
}

CODER_HEAD = [
    "......kkkkkk......",
    ".....khhhhhhk.....",
    "....khhhhhhhhk....",
    "....khhhhhhhhk....",
    "....khsshhsshk....",
    "....kssssssssk....",
    "....kskssssksk....",
    "....krssssssrk....",
    ".....kssddssk.....",
    "...kkkkkkkkkkkk...",
    "..kbbkkkkkkkkbbk..",
    "..kbkggggggggkbk..",
    "..kbkgggccgggkbk..",
    "..kbkggggggggkbk..",
]
CODER_LEGS = [
    ".kknGGGGGGGGGGnkk.",
    ".knnnnkkkkkknnnnk.",
    "..kkkk......kkkk..",
]
CODER = [
    CODER_HEAD + ["..kskkkkkkkkkkbk.."] + CODER_LEGS,
    CODER_HEAD[:12] + ["..kbkgggCCgggkbk..", "..kbkggggggggksk..", "..kbkkkkkkkkkkbk.."] + CODER_LEGS,
    CODER_HEAD[:13] + ["..kskggggggggkbk..", "..kbkkkkkkkkkksk.."] + CODER_LEGS,
    CODER_HEAD[:6] + ["....ksddssddsk...."] + CODER_HEAD[7:12] + ["..kbkgggCCgggkbk..", "..kbkggggggggkbk..", "..kbkkkkkkkkkksk.."] + CODER_LEGS,
]

FIRE_LOGS = [".kOoooooOOk.", "kOoOOOOooOOk"]
FIRE = [
    ["......F.....", ".....FfF....", "....FffyF...", "...FffyyfF..", "...FfywyyfF.", "..FfyywwyfF.", "..FfyywwyfF.", "...FfyyyfF.."] + FIRE_LOGS,
    [".....F......", "....FfF.....", "....FfyfF...", "...FfyyffF..", "..FfyywyfF..", "..FfywwyyfF.", "..FfyywwyfF.", "...FfyyyfF.."] + FIRE_LOGS,
    [".......F....", "......FfF...", "....FFfyF...", "...FfyyyfF..", "...FfyywyfF.", "..FfyywwyfF.", "..FfywwyyfF.", "...FfyyyfF.."] + FIRE_LOGS,
]

MONK = [[
    ".......kkkk.......",
    "......khhhhky.....",
    "......kkhhkk......",
    ".....khhhhhhk.....",
    "....khhhhhhhhk....",
    "....khhsssshhk....",
    "....khsssssshk....",
    "....ksddssddsk....",
    "....krssssssrk....",
    ".....kssssssk.....",
    "......kkkkkk......",
    ".....kWWttWWk.....",
    "....kWWWttWWWk....",
    "...kWWVWttWVWWk...",
    "..kWWVksssskVWWk..",
    ".kWWWVVkkkkVVWWWk.",
    "kWWWWVVVVVVVVWWWWk",
    ".kkkkkkkkkkkkkkkk.",
]]

SWORD = [[
    "..w..", ".wLw.", ".wLw.", ".wLw.", ".wLw.", ".wLw.", ".wLw.", ".wLw.", ".wLw.",
    "yyyyy", "..t..", "..t..", ".kyk.",
]]

GYM_BODY = [
    "........kkkk........",
    ".......khhhhk.......",
    "......khaaaahk......",
    "......kssssssk......",
    "......kskssksk......",
    "......krssssrk......",
    ".......kssssk.......",
    "........kkkk........",
    "....kaaaaaaaaaak....",
    "...ksaaaaaaaaaask...",
    "...ksaaaaaaaaaask...",
    "....kaaaaaaaaaak....",
    ".....knnnnnnnnk.....",
    ".....knnnkknnnk.....",
    "......kssk..kssk....",
    "......kssk..kssk....",
    ".....kkkkk..kkkkk...",
]


def _gym_up():
    rows = ["PP................PP", "PPSksSSSSSSSSSSskSPP", "PP.ks..........sk.PP"] + [r for r in GYM_BODY]
    for i in range(3, 12):  # cánh tay thẳng lên
        r = list(rows[i])
        r[3], r[4], r[15], r[16] = "k", "s", "s", "k"
        rows[i] = "".join(r)
    return rows


def _gym_down():
    rows = ["." * 20] * 3 + [r for r in GYM_BODY]
    rows[9] = "PP" + rows[9][2:18] + "PP"
    rows[10] = "PPSksSSSSSSSSSSskSPP"
    rows[11] = "PP" + rows[11][2:18] + "PP"
    return rows


GYM = [_gym_down(), _gym_up()]

SLIME = [[
    ".....kkkk.....",
    "...kkmmmmkk...",
    "..kmmwwmmmmk..",
    ".kmmwmmmmmmMk.",
    ".kmmmkmmkmmMk.",
    "kmmmmkmmkmmmMk",
    "kmmmmmmmmmmmMk",
    "kMmmmmmmmmMMMk",
    ".kkkkkkkkkkkk.",
]]

CAT_TOP = [
    "...........k..k.",
    "..........kekkek",
    "k.........keeeek",
    "ek........keekek",
    ".ek.......keeeek",
    "..ekkkkkkkkeeek.",
    "..keeeeeeeeeeek.",
    "..kEeEeeeeEeeek.",
    "..keeewwwwweek..",
]
CAT = [CAT_TOP + ["..kk.kk...kk.kk."], CAT_TOP + ["...kk.kk.kk.kk.."]]


def pixels(rows, x=0, y=0):
    """Gộp các điểm cùng màu liền nhau thành path để file nhẹ."""
    paths = {}
    for j, row in enumerate(rows):
        i = 0
        while i < len(row):
            ch = row[i]
            n = 1
            while i + n < len(row) and row[i + n] == ch:
                n += 1
            if ch != ".":
                paths.setdefault(ch, []).append(f"M{x + i * PX},{y + j * PX}h{n * PX}v{PX}h{-n * PX}z")
            i += n
    return "".join(f'<path fill="{PAL[c]}" d="{"".join(d)}"/>' for c, d in paths.items())


def sprite(frames, x, ground, weights=None, dur=0.8):
    """Đặt sprite sao cho chân chạm mặt đất; nhiều khung thì luân phiên hiện từng khung."""
    hgt, wid = len(frames[0]) * PX, len(frames[0][0]) * PX
    x0, y0 = x - wid / 2, ground - hgt
    if len(frames) == 1:
        return f'<g transform="translate({x0:.0f},{y0:.0f})">{pixels(frames[0])}</g>'
    weights = weights or [1] * len(frames)
    total = sum(weights)
    kt = ";".join(f"{sum(weights[:i]) / total:.4f}" for i in range(len(frames)))
    out = []
    for i, f in enumerate(frames):
        vals = ";".join("visible" if j == i else "hidden" for j in range(len(frames)))
        out.append(f'<g visibility="{"visible" if i == 0 else "hidden"}"><animate attributeName="visibility" values="{vals}" '
                   f'keyTimes="{kt}" calcMode="discrete" dur="{dur}s" repeatCount="indefinite"/>{pixels(f)}</g>')
    return f'<g transform="translate({x0:.0f},{y0:.0f})">{"".join(out)}</g>'


def rising(rng, x, y, color, n, spread=30, height=60, size=PX):
    """Hạt sáng bay lên rồi tắt (tia lửa, linh khí, ký tự code)."""
    out = []
    for _ in range(n):
        dx, dur, delay = rng.uniform(-spread, spread), rng.uniform(1.6, 3.2), rng.uniform(0, 3)
        out.append(f'<rect x="{x + dx:.0f}" y="{y:.0f}" width="{size}" height="{size}" fill="{color}" opacity="0">'
                   f'<animate attributeName="y" values="{y:.0f};{y - height:.0f}" dur="{dur:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite"/>'
                   f'<animate attributeName="opacity" values="0;1;0" dur="{dur:.1f}s" begin="{delay:.1f}s" repeatCount="indefinite"/></rect>')
    return "".join(out)


def pixel_scene(rng, w, ground):
    """Dải cỏ pixel và các nhân vật đứng trên mép dưới banner."""
    # mặt đất: một hàng cỏ, hai hàng đất, vài ngọn cỏ nhô lên
    turf = [f'<rect x="0" y="{ground}" width="{w}" height="{PX}" fill="#3fa36b"/>',
            f'<rect x="0" y="{ground + PX}" width="{w}" height="{PX * 3}" fill="#2a1d2e"/>']
    for x in range(0, w, PX * 3):
        if rng.random() < 0.35:
            tall = rng.choice((1, 1, 2))
            turf.append(f'<rect x="{x}" y="{ground - tall * PX}" width="{PX}" height="{tall * PX}" fill="#3fa36b"/>')
        if rng.random() < 0.25:
            turf.append(f'<rect x="{x + PX}" y="{ground + PX * 2}" width="{PX}" height="{PX}" fill="#3a2a40"/>')
    for x in (232, 470, 712, 1010):  # hoa nhỏ nhấp nháy
        col = rng.choice(("#ffd6f5", "#ffe9a8", "#bcd9ff"))
        turf.append(f'<rect x="{x}" y="{ground - PX}" width="{PX}" height="{PX}" fill="#3fa36b"/>'
                    f'<rect x="{x}" y="{ground - 2 * PX}" width="{PX}" height="{PX}" fill="{col}">'
                    f'<animate attributeName="opacity" values="1;0.35;1" dur="{rng.uniform(1.8, 3):.1f}s" repeatCount="indefinite"/></rect>')

    parts = ["".join(turf)]
    # lập trình viên + lửa trại
    parts.append(sprite(CODER, 92, ground, [3, 2, 3, 2], 1.0))
    parts.append(rising(rng, 92, ground - 50, "#58a6ff", 5, 18, 50))
    parts.append(f'<ellipse cx="168" cy="{ground - 18}" rx="34" ry="22" fill="#ff8c1a" opacity="0.18">'
                 f'<animate attributeName="opacity" values="0.12;0.26;0.15;0.22;0.12" dur="1.2s" repeatCount="indefinite"/></ellipse>')
    parts.append(sprite(FIRE, 168, ground, dur=0.45))
    parts.append(rising(rng, 168, ground - 34, "#ffd23f", 6, 10, 46))
    # slime nảy
    sw = len(SLIME[0][0]) * PX
    parts.append(f'<g transform="translate(330,{ground})"><g>'
                 f'<animateTransform attributeName="transform" type="translate" values="0 0;0 0;0 -26;0 0;0 0" keyTimes="0;0.35;0.6;0.85;1" '
                 f'calcMode="spline" keySplines="0 0 1 1;0.2 0.6 0.4 1;0.6 0 0.8 0.4;0 0 1 1" dur="1.4s" repeatCount="indefinite"/>'
                 f'<g><animateTransform attributeName="transform" type="scale" values="1 1;1.18 0.8;0.9 1.14;1.18 0.8;1 1" keyTimes="0;0.3;0.6;0.88;1" dur="1.4s" repeatCount="indefinite"/>'
                 f'{sprite(SLIME, 0, 0)}</g></g></g>')
    # tu sĩ ngồi thiền lơ lửng + phi kiếm
    mx = w / 2
    parts.append(f'<ellipse cx="{mx}" cy="{ground - 2}" rx="34" ry="6" fill="#2ec4b6" opacity="0.35">'
                 f'<animate attributeName="rx" values="34;26;34" dur="3s" repeatCount="indefinite"/></ellipse>')
    parts.append(f'<ellipse cx="{mx}" cy="{ground - 40}" rx="56" ry="46" fill="#2ec4b6" opacity="0.1">'
                 f'<animate attributeName="opacity" values="0.06;0.18;0.06" dur="3s" repeatCount="indefinite"/></ellipse>')
    parts.append(f'<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -8;0 0" dur="3s" repeatCount="indefinite"/>'
                 f'{sprite(MONK, mx, ground - 14)}</g>')
    parts.append(f'<g><animateTransform attributeName="transform" type="translate" values="0 -8;0 0;0 -8" dur="3s" repeatCount="indefinite"/>'
                 f'{sprite(SWORD, mx + 62, ground - 20)}</g>')
    parts.append(rising(rng, mx, ground - 20, "#7ee8de", 7, 46, 70))
    # người tập gym
    parts.append(sprite(GYM, 840, ground, [1, 1], 1.4))
    # mèo đi qua lại
    cw = len(CAT[0][0]) * PX
    parts.append(f'<g><animateTransform attributeName="transform" type="translate" values="930 0;1130 0;1130 0;930 0;930 0" '
                 f'keyTimes="0;0.45;0.5;0.95;1" dur="12s" repeatCount="indefinite"/>'
                 f'<g><animateTransform attributeName="transform" type="scale" values="1 1;-1 1" keyTimes="0;0.5" calcMode="discrete" dur="12s" repeatCount="indefinite"/>'
                 f'{sprite(CAT, 0, ground, dur=0.4)}</g></g>')
    return "\n".join(parts)


def hero(lang):
    w, h = 1200, 660
    ground = h - 4 * PX
    rng = random.Random(7)
    t = {
        "en": dict(sub="fullstack developer  ·  ai/ml  ·  game dev", tags=["erp / crm", "university systems", "ai · xai research", "unity games", "community apps"], loc="ho chi minh city, vietnam"),
        "vi": dict(sub="lập trình viên fullstack  ·  ai/ml  ·  làm game", tags=["erp / crm", "hệ thống đại học", "nghiên cứu ai · xai", "game unity", "ứng dụng cộng đồng"], loc="tp. hồ chí minh, việt nam"),
    }[lang]
    # hàng pill lĩnh vực
    pills, x = [], 0
    for i, tag in enumerate(t["tags"]):
        pw = len(tag) * 9.4 + 34
        pills.append(f'<g transform="translate({x:.0f},0)"><rect width="{pw:.0f}" height="36" rx="18" fill="#161b22" fill-opacity="0.8" stroke="url(#shine)" stroke-width="1.3"/>'
                     f'<text x="{pw / 2:.0f}" y="24" text-anchor="middle" fill="#e6edf3" font-family="{FONT}" font-size="16">{tag}</text></g>')
        x += pw + 14
    px = (w - (x - 14)) / 2

    # vị trí đậu của các chip: hàng trên, hai bên, hàng dưới
    rows = [(SKILLS[0:7], 70, 30, w - 30), (SKILLS[13:20], 496, 190, w - 190)]
    slots = []
    for items, y, left, right in rows:
        gap = (right - left) / len(items)
        for i, s in enumerate(items):
            slots.append((s, left + gap * (i + 0.5), y + (14 if i % 2 else -10)))
    for i, s in enumerate(SKILLS[7:13]):
        side = i % 2
        slots.append((s, 100 if side == 0 else w - 100, (180, 296, 412)[i // 2] + (8 if side else 0)))
    order = list(range(len(slots)))
    rng.shuffle(order)
    chips = "\n".join(
        flying_chip(rng, s[0], s[1], s[2], fx, fy, w / 2 + rng.uniform(-70, 70), 290 + rng.uniform(-40, 40), 0.3 + order[i] * 0.2)
        for i, (s, fx, fy) in enumerate(slots))

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
{field(rng, w, h, 170, 40, 5, 14)}
{shooting(1150, -20, 110, 7, 1)}
{shooting(820, -30, 90, 9, 4.5)}
{shooting(1300, 120, 130, 11, 7)}
<text x="{w / 2}" y="188" text-anchor="middle" fill="#8b949e" font-family="{MONO}" font-size="17" letter-spacing="3">~/tandzp0o</text>
<text x="{w / 2}" y="268" text-anchor="middle" fill="url(#shine)" font-family="{FONT}" font-size="76" font-weight="800" filter="url(#soft)" opacity="0.55">Lê Trương Trọng Tấn</text>
<text x="{w / 2}" y="268" text-anchor="middle" fill="url(#shine)" font-family="{FONT}" font-size="76" font-weight="800">Lê Trương Trọng Tấn</text>
<text x="{w / 2}" y="318" text-anchor="middle" fill="#c9d1d9" font-family="{FONT}" font-size="25" letter-spacing="1">{t["sub"]}</text>
<g transform="translate({px:.0f},346)">{"".join(pills)}</g>
<text x="{w / 2}" y="424" text-anchor="middle" fill="#8b949e" font-family="{FONT}" font-size="16" letter-spacing="2">{t["loc"]}</text>
<g shape-rendering="crispEdges">{pixel_scene(rng, w, ground)}</g>
{chips}
</g>
<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="21" fill="none" stroke="url(#shine)" stroke-width="1.5" opacity="0.7"/>
</svg>'''


# ─────────────── nhân vật pixel cho tiêu đề từng mục ───────────────
def overlay(base, sub, ox, oy):
    """Dán lưới con lên lưới gốc ('.' là trong suốt), tự nới rộng nếu cần."""
    rows = [list(r) for r in base]
    for j, line in enumerate(sub):
        for i, ch in enumerate(line):
            if ch == ".":
                continue
            row = rows[oy + j]
            while len(row) <= ox + i:
                row.append(".")
            row[ox + i] = ch
    width = max(len(r) for r in rows)
    return ["".join(r).ljust(width, ".") for r in rows]


def same_width(frames):
    width = max(len(r) for f in frames for r in f)
    return [[r.ljust(width, ".") for r in f] for f in frames]


AV_HEAD = CODER_HEAD[:9]
AV_TORSO = [
    "....kkbbbbbbkk....",
    "...kbbbbbbbbbbk...",
    "..kbkbbbbbbbbkbk..",
    "..kbkbbbccbbbkbk..",
    "..kskbbbbbbbbksk..",
]
AV_LEGS = ["....knnnnnnnnk....", "....knnnkknnnk....", "....knnk..knnk....", "...kkkkk..kkkkk..."]
AV_WALK = [
    ["....knnnnnnnnk....", "....knnnkknnnk....", "...knnk....knnk...", "..kkkkk....kkkkk.."],
    ["....knnnnnnnnk....", "....knnnkknnnk....", ".....knnkknnk.....", ".....kkkkkkkk....."],
]
AV_NO_RIGHT_ARM = overlay(AV_HEAD + AV_TORSO + AV_LEGS, ["k..", "k..", "k.."], 13, 11)
for _r in (11, 12, 13):  # xoá hẳn tay phải buông xuống
    AV_NO_RIGHT_ARM[_r] = AV_NO_RIGHT_ARM[_r][:14] + ".." + AV_NO_RIGHT_ARM[_r][16:]
WAVE = same_width([
    overlay(AV_NO_RIGHT_ARM, [".kk.", "kssk", "kssk", ".kbk", "kbk.", "kbk.", "bk.."], 14, 4),
    overlay(AV_NO_RIGHT_ARM, [".kk", "kssk", "kssk", "kbk", "kbk", ".bk", ".bk"], 13, 4),
])
BRIEFCASE = [".kkk.", "kooOk", "koyOk", "kkkkk"]
WALK = same_width([overlay(AV_HEAD + AV_TORSO + legs, BRIEFCASE, 14, 14) for legs in AV_WALK])

CHEST_BODY = [
    ".kyoooykkyoooyk.",
    ".kyoooyyyyoooyk.",
    ".kyooooooooooyk.",
    ".kyOOOOOOOOOOyk.",
    ".kkkkkkkkkkkkkk.",
]
CHEST = [
    ["................", "................", "................",
     "..kkkkkkkkkkkk..", ".koooooooooooOk.", ".kyoooooooooOyk.", ".kkkkkkyykkkkkk."] + CHEST_BODY,
    ["................", "..kkkkkkkkkkkk..", ".kOOOOOOOOOOOOk.",
     ".kkkkkkkkkkkkkk.", ".kywwyyyywwyyyk.", ".kyyyywwyyyyyyk.", ".kkkkkkkkkkkkkk."] + CHEST_BODY,
]

POTION_TOP = ["....kkkk....", "....kook....", "....kOOk....", "....kLLk....", "....kLLk....",
              "...kLLLLk...", "..kLLLLLLk..", ".kLLLLLLLLk."]
POTION_BOTTOM = ["kppppppqqqpk", ".kqpppqqqqk.", "..kkkkkkkk.."]
POTION = [
    POTION_TOP + [".kppwppppqk.","kpppwppppppk", "kppwpppppqpk", "kpppppppqqpk"] + POTION_BOTTOM,
    POTION_TOP + [".kpppppwpqk.", "kppppppwpppk", "kpwppppppqpk", "kppppwppqqpk"] + POTION_BOTTOM,
]

CAP = [
    ["........kk........", "......kkNNkk......", "....kkNNNNNNkk....", "..kkNNNNyyNNNNkk..",
     "kkNNNNNNNNyyNNNNkk", "..kkNNNNNNNNyykk..", "....kkNNNNNNkkyy..", ".....knnnnnnk.yy..",
     ".....knnnnnnk.yy..", ".....kkkkkkkkyyyy."],
    ["........kk........", "......kkNNkk......", "....kkNNNNNNkk....", "..kkNNNNyyNNNNkk..",
     "kkNNNNNNNNyyNNNNkk", "..kkNNNNNNNNyykk..", "....kkNNNNNNkkyy..", ".....knnnnnnk..yy.",
     ".....knnnnnnk..yy.", ".....kkkkkkkk.yyyy"],
]
BOOKS = [
    "..kkkkkkkkkkkkkk..",
    "..kaaaaaaaaaawwk..",
    "..kaaayaaaaaawwk..",
    ".kkkkkkkkkkkkkkkk.",
    ".kwwbbbbbbbbbbbbk.",
    ".kwwbbbbbbbybbbbk.",
    ".kkkkkkkkkkkkkkkk.",
]
PAL.update({"p": "#c45ce6", "q": "#8f3fbf", "N": "#5b6194"})


def bubble(x, y, text, dur, show=(0.08, 0.55)):
    """Bóng thoại pixel hiện lên một lúc rồi tắt."""
    bw = len(text) * 11 + 18
    a, b = show
    return (f'<g opacity="0"><animate attributeName="opacity" values="0;1;1;0;0" keyTimes="0;{a};{b};{b + 0.05};1" dur="{dur}s" repeatCount="indefinite"/>'
            f'<rect x="{x - bw:.0f}" y="{y}" width="{bw}" height="28" fill="#ffffff" stroke="#1a1c2c" stroke-width="4"/>'
            f'<rect x="{x - 8:.0f}" y="{y + 26}" width="8" height="8" fill="#ffffff"/><rect x="{x:.0f}" y="{y + 26}" width="4" height="12" fill="#1a1c2c"/>'
            f'<rect x="{x - 12:.0f}" y="{y + 30}" width="4" height="4" fill="#1a1c2c"/>'
            f'<text x="{x - bw / 2:.0f}" y="{y + 20}" text-anchor="middle" fill="#1a1c2c" font-family="{MONO}" font-size="16" font-weight="700">{text}</text></g>')


def section_sprite(key, lang, rng, cx, ground):
    if key == "about":
        hi = {"en": "hi!", "vi": "chào!"}[lang]
        return (sprite(WAVE, cx, ground, dur=0.7)
                + bubble(cx - 40, 4, hi, 4.0))
    if key == "experience":
        xp = (f'<text x="{cx - 42}" y="40" text-anchor="end" fill="#f59e0b" stroke="#1a1c2c" stroke-width="3" paint-order="stroke" '
              f'font-family="{MONO}" font-size="18" font-weight="800" opacity="0">+XP'
              f'<animate attributeName="y" values="46;14" dur="2s" repeatCount="indefinite"/>'
              f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.15;0.7;1" dur="2s" repeatCount="indefinite"/></text>')
        return (f'<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -4;0 0;0 -4;0 0" '
                f'keyTimes="0;0.25;0.5;0.75;1" calcMode="discrete" dur="1s" repeatCount="indefinite"/>'
                f'{sprite(WALK, cx, ground, dur=0.5)}</g>' + xp)
    if key == "projects":
        dur, k = 3.0, 0.42  # rương đóng 42% thời gian, rồi mở
        glow = (f'<g visibility="hidden"><animate attributeName="visibility" values="hidden;visible" keyTimes="0;{k}" '
                f'calcMode="discrete" dur="{dur}s" repeatCount="indefinite"/>'
                f'<ellipse cx="{cx}" cy="{ground - 34}" rx="46" ry="30" fill="#ffd23f" opacity="0.28"/>'
                + rising(rng, cx, ground - 30, "#ffd23f", 6, 24, 34)
                + sparkle(cx - 34, ground - 50, 7, "#ffe9a8", 1.2, 0) + sparkle(cx + 36, ground - 44, 6, "#ffffff", 1.4, 0.4) + '</g>')
        return glow + sprite(CHEST, cx, ground, [k, 1 - k], dur)
    if key == "skills":
        return (f'<ellipse cx="{cx}" cy="{ground - 22}" rx="34" ry="26" fill="#c45ce6" opacity="0.2">'
                f'<animate attributeName="opacity" values="0.1;0.32;0.1" dur="2s" repeatCount="indefinite"/></ellipse>'
                + sprite(POTION, cx, ground, dur=0.6)
                + rising(rng, cx, ground - 60, "#e9a6ff", 5, 8, 40)
                + sparkle(cx + 30, ground - 52, 7, "#ffffff", 1.8, 0.3) + sparkle(cx - 32, ground - 30, 5, "#e9a6ff", 2.2, 1))
    if key == "education":
        cap = sprite(CAP, cx + 2, ground - len(BOOKS) * PX + 6, dur=0.5)
        return (sprite([BOOKS], cx, ground)
                + f'<g><animateTransform attributeName="transform" type="translate" values="0 0;0 0;0 -12;0 0" keyTimes="0;0.4;0.7;1" '
                  f'calcMode="spline" keySplines="0 0 1 1;0.2 0.6 0.4 1;0.6 0 0.8 0.4" dur="1.8s" repeatCount="indefinite"/>{cap}</g>'
                + sparkle(cx - 40, 18, 7, "#ffe9a8", 1.8, 0) + sparkle(cx + 40, 26, 6, "#bcd9ff", 2.2, 0.8))
    return ""


def section(key, title, lang, seed):
    """Tiêu đề mục: nền trong suốt, đọc được ở cả giao diện sáng và tối; nhân vật pixel ở bên phải."""
    w, h = 1200, 84
    mid = 44
    rng = random.Random(seed)
    cols = ("#3b82f6", "#a855f7", "#ec4899", "#f59e0b", "#3b82f6")
    tw = len(title) * 14 + 6
    line_end = w - 220
    stars = "".join(sparkle(rng.uniform(tw + 70, line_end), rng.uniform(16, h - 16), rng.uniform(4, 10),
                            rng.choice(cols), rng.uniform(1.6, 3.6), rng.uniform(0, 4), rng.random() < 0.4) for _ in range(14))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{title}">
<defs>{shimmer("g", w, cols, 5)}</defs>
{sparkle(22, mid - 2, 15, "#a855f7", 2.4, 0, True)}
{sparkle(40, mid - 18, 6, "#f59e0b", 1.8, 0.6)}
<text x="58" y="{mid + 10}" fill="url(#g)" font-family="{FONT}" font-size="28" font-weight="800" letter-spacing="1">{title}</text>
<rect x="{tw + 60}" y="{mid - 1}" width="{line_end - tw - 60}" height="2" rx="1" fill="url(#g)" opacity="0.45"/>
<circle r="3.5" cy="{mid}" fill="#f59e0b"><animate attributeName="cx" values="{tw + 60};{line_end}" dur="4s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;1;0" dur="4s" repeatCount="indefinite"/></circle>
{stars}
<g shape-rendering="crispEdges">{section_sprite(key, lang, rng, w - 80, h - 4)}</g>
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
            files[f"sec-{key}-{lang}.svg"] = section(key, titles[i], lang, 20 + j)
    for name, svg in files.items():
        (OUT / name).write_text(svg, encoding="utf-8")
        print(f"{name}: {len(svg) / 1024:.1f} KB")
