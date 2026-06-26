"""
SunPark Investment Teaser - clean canvas-based PDF
Every element is measured before drawing. No flowable nesting.
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

OUT = Path("deliverables/SunPark_Investment_Teaser.pdf")

W, H = A4   # 595.28 x 841.89 pt

# ─── PALETTE ─────────────────────────────────────────────────────────────────
P = {
    "dark":   colors.HexColor("#0A1628"),
    "mid":    colors.HexColor("#1A3A5C"),
    "accent": colors.HexColor("#F5A623"),
    "light":  colors.HexColor("#E8F0F8"),
    "soft":   colors.HexColor("#F3F6FA"),
    "ink":    colors.HexColor("#1F2937"),
    "body":   colors.HexColor("#374151"),
    "muted":  colors.HexColor("#6B7A8D"),
    "line":   colors.HexColor("#CBD5E0"),
    "green":  colors.HexColor("#276749"),
    "white":  colors.white,
    "cream":  colors.HexColor("#E8F4E8"),
}

# ─── FONTS (Inter — Airtable design system substitute) ───────────────────────
def _reg(name: str, path: str) -> bool:
    p = Path(path)
    if p.exists():
        pdfmetrics.registerFont(TTFont(name, str(p)))
        return True
    return False

# Prefer converted Inter TTFs (extracted from @fontsource/inter)
_base = Path("deliverables/fonts")
if _reg("Inter_400", str(_base / "inter-400.ttf")) and \
   _reg("Inter_500", str(_base / "inter-500.ttf")) and \
   _reg("Inter_600", str(_base / "inter-600.ttf")):
    FR, FM, FB = "Inter_400", "Inter_500", "Inter_600"
else:
    # Fallback to Segoe UI (closest on Windows) then Helvetica
    FR = "SF_Reg"  if _reg("SF_Reg",  r"C:\Windows\Fonts\segoeui.ttf")  else "Helvetica"
    FM = "SF_Med"  if _reg("SF_Med",  r"C:\Windows\Fonts\seguisb.ttf")  else "Helvetica-Bold"
    FB = "SF_Bold" if _reg("SF_Bold", r"C:\Windows\Fonts\segoeuib.ttf") else "Helvetica-Bold"
    if FM == "Helvetica-Bold":
        FM = FB

# ─── LAYOUT CONSTANTS ────────────────────────────────────────────────────────
LM   = 16 * mm          # left margin
RM   = 16 * mm          # right margin
CW   = W - LM - RM      # ~504 pt full content width
GAP  = 9 * mm           # column gap
COL  = (CW - GAP) / 2  # ~238 pt per column (~84 mm)

# ─── STYLE FACTORY ───────────────────────────────────────────────────────────
def sty(name, fn, fs, ld, col, align=TA_LEFT, li=0, fi=0) -> ParagraphStyle:
    return ParagraphStyle(name, fontName=fn, fontSize=fs, leading=ld,
                          textColor=col, alignment=align,
                          leftIndent=li, firstLineIndent=fi)

# Airtable design system type scale (Inter substituting Haas Grotesk)
# display-xl 48/500, display-lg 40/400, display-md 32/400
# title-lg 24/400, title-sm 18/500, label-md 16/500
# body-md 14/400, caption 14/500, legal 13/600
S = {
    # Section kicker — caption style: 500 weight, tracked uppercase
    "kicker":   sty("kicker",  FM, 7.8,   9.8,  P["accent"]),
    # Hero h1 — display-xl equivalent in print (~34pt maps to 48px screen)
    "h1":       sty("h1",      FM, 34,    38,   P["white"]),
    # Sub-brand line — title-lg weight 400
    "h1sub":    sty("h1sub",   FR, 12,    15.2, P["accent"]),
    # Tagline — body-md weight 400
    "tagline":  sty("tagline", FR, 10.0,  14.0, P["line"]),
    # Running body copy — body-md: 14/400/1.25 → in print ~9.5pt
    "body":     sty("body",    FR, 9.6,   13.6, P["body"]),
    # Body on dark — same scale, white
    "body_w":   sty("body_w",  FR, 9.2,   13.0, P["white"]),
    # Meta / legal — legal: 13px/600 → ~7pt in print
    "meta":     sty("meta",    FR, 7.8,   10.4, P["muted"]),
    # Badge label — legal weight 600
    "badge":    sty("badge",   FB, 6.6,    8.2, P["dark"],   TA_CENTER),
    # Stat value — display-md weight 400
    "sv":       sty("sv",      FM, 14.5,  17,   P["accent"], TA_CENTER),
    # Stat label — caption 500
    "sl":       sty("sl",      FM, 6.8,    8.8, P["line"],   TA_CENTER),
    # Table header — label-md 500
    "th":       sty("th",      FM, 7.8,   10.2, P["accent"]),
    "th_c":     sty("th_c",    FM, 7.8,   10.2, P["accent"], TA_CENTER),
    # Table data row — body-md 400
    "td":       sty("td",      FM, 8.2,   11.0, P["mid"]),
    "td_c":     sty("td_c",    FR, 8.2,   11.0, P["ink"],    TA_CENTER),
    "td_grn":   sty("td_grn",  FM, 8.2,   11.0, P["green"],  TA_CENTER),
    # Capital raise number — display-md
    "raise":    sty("raise",   FM, 26,    29,   P["mid"]),
    # Page 2 header brand — title-sm 500
    "p2brand":  sty("p2brand", FM, 13.5,  16,   P["white"]),
    "p2sub":    sty("p2sub",   FR, 7.8,   10.2, P["line"],   TA_RIGHT),
    # Footer — body-md 400
    "foot":     sty("foot",    FR, 7.6,    9.6, P["line"]),
    "foot_r":   sty("foot_r",  FR, 7.6,    9.6, P["line"],   TA_RIGHT),
    # Proceeds amount — title-sm 500
    "amtlbl":   sty("amtlbl",  FM, 10.0,  13.0, P["accent"]),
    # Milestone stage title — title-sm 500
    "ms_title": sty("ms_title",FM, 9.5,   12.0, P["mid"]),
    # Disclaimer — legal 600
    "disc":     sty("disc",    FB, 6.6,    8.4, P["muted"]),
}

# ─── PRIMITIVES ──────────────────────────────────────────────────────────────
def measure(text: str, style: ParagraphStyle, width: float) -> float:
    _, h = Paragraph(text, style).wrap(width, 9999)
    return h

def draw_text(cv, text: str, x: float, y: float, width: float, style: ParagraphStyle) -> float:
    """Draw paragraph with TOP at y. Returns height used."""
    p = Paragraph(text, style)
    _, h = p.wrap(width, 9999)
    p.drawOn(cv, x, y - h)
    return h

def fill_rect(cv, x: float, y: float, w: float, h: float,
              fill, radius: float = 0):
    """Draw filled rect. y = TOP of rect."""
    cv.saveState()
    cv.setFillColor(fill)
    cv.setStrokeColor(fill)
    if radius:
        cv.roundRect(x, y - h, w, h, radius, fill=1, stroke=0)
    else:
        cv.rect(x, y - h, w, h, fill=1, stroke=0)
    cv.restoreState()

def rule(cv, x: float, y: float, w: float, col, thickness: float = 0.5):
    cv.saveState()
    cv.setStrokeColor(col)
    cv.setLineWidth(thickness)
    cv.line(x, y, x + w, y)
    cv.restoreState()

def dot(cv, x: float, y: float, r: float, col):
    cv.saveState()
    cv.setFillColor(col)
    cv.circle(x, y, r, fill=1, stroke=0)
    cv.restoreState()

def section_head(cv, x: float, y: float, w: float, title: str) -> float:
    """Draw kicker + rule. Returns total height consumed."""
    h = draw_text(cv, title.upper(), x, y, w, S["kicker"])
    y -= h + 2.0 * mm
    rule(cv, x, y, w, P["line"], 0.6)
    return h + 2.0 * mm + 3.2 * mm   # gap after rule included

def bullet_list(cv, x: float, y: float, w: float, items: list, style_key: str,
                dot_col=None, gap: float = 3.4) -> float:
    """Draw bulleted list. Returns total height consumed."""
    sc = dot_col or P["accent"]
    total = 0.0
    for item in items:
        h = draw_text(cv, item, x + 5.5 * mm, y, w - 5.5 * mm, S[style_key])
        dot(cv, x + 1.8 * mm, y - h / 2, 1.8, sc)
        drop = h + gap
        y     -= drop
        total += drop
    return total

def filled_card(cv, x: float, y: float, w: float, fill,
                inner: list, pad: float = 9.0, radius: float = 4) -> float:
    """
    inner = list of (text, style_key) tuples.
    Measures height first, draws rect, then text.
    Returns total height of card.
    """
    iw = w - 2 * pad
    total_h = 2 * pad
    heights = []
    for text, sk in inner:
        h = measure(text, S[sk], iw)
        heights.append(h)
        total_h += h + 3.2 * mm
    total_h -= 3.2 * mm   # remove trailing gap

    fill_rect(cv, x, y, w, total_h, fill, radius)

    cy = y - pad
    for (text, sk), h in zip(inner, heights):
        draw_text(cv, text, x + pad, cy, iw, S[sk])
        cy -= h + 3.2 * mm

    return total_h

def footer(cv, page_num: int):
    fy   = 10.5 * mm
    fh   = 9.5 * mm
    fill_rect(cv, 0, fy, W, fh, P["dark"])
    draw_text(cv, "SunPark  |  Solar Carport as a Service  |  sunpark.ma",
              LM, fy - 1.5 * mm, CW * 0.78, S["foot"])
    draw_text(cv, f"{page_num} / 2",
              LM + CW * 0.78, fy - 1.5 * mm, CW * 0.22, S["foot_r"])

# ─── PAGE 1 ──────────────────────────────────────────────────────────────────
def page1(cv):
    HDR_H = 56 * mm

    # Dark header band
    fill_rect(cv, 0, H, W, HDR_H, P["dark"])

    # Mid-navy diagonal stripe
    cv.saveState()
    cv.setFillColor(P["mid"])
    pth = cv.beginPath()
    pth.moveTo(W - 85 * mm, H)
    pth.lineTo(W, H)
    pth.lineTo(W, H - HDR_H)
    pth.lineTo(W - 130 * mm, H - HDR_H)
    pth.close()
    cv.drawPath(pth, fill=1, stroke=0)
    cv.restoreState()

    # Branding
    ty = H - 12 * mm
    h  = draw_text(cv, "SunPark", LM, ty, 110 * mm, S["h1"])
    ty -= h + 1.5 * mm
    h  = draw_text(cv, "Solar Carport as a Service", LM, ty, 120 * mm, S["h1sub"])
    ty -= h + 2.5 * mm
    draw_text(cv, "Turning commercial parking into clean energy infrastructure"
              " across Morocco, with no upfront client capex.",
              LM, ty, CW * 0.58, S["tagline"])

    # Badge — investor teaser only (no confidential)
    BW, BH = 42 * mm, 8.5 * mm
    bx = W - RM - BW
    by = H - 11 * mm
    fill_rect(cv, bx, by, BW, BH, P["accent"], radius=2)
    draw_text(cv, "INVESTOR TEASER",
              bx, by - (BH - 8.0) / 2, BW, S["badge"])

    # Accent separator
    sep_y = H - HDR_H
    rule(cv, 0, sep_y, W, P["accent"], 2.2)

    # ── TWO COLUMNS ──────────────────────────────────────────────────────────
    lx = LM
    rx = LM + COL + GAP
    ly = sep_y - 6 * mm
    ry = ly

    # ── LEFT ─────────────────────────────────────────────────────────────────

    # Problem card
    card_h = filled_card(cv, lx, ly, COL, P["light"], [
        ("THE PROBLEM", "kicker"),
        ("Rising grid costs: commercial tariff benchmark is GBP 0.086 per kWh and rising.", "body"),
        ("The capex barrier: a standard carport costs around GBP 260K upfront for operators.", "body"),
        ("Split ownership between tenants and landlords blocks commercial solar decisions.", "body"),
    ])
    ly -= card_h + 5.5 * mm

    # Solution
    ly -= section_head(cv, lx, ly, COL, "The Solution")
    sol = ("SunPark finances, builds, owns, and operates modular solar canopies"
           " over commercial parking. Clients sign a 20-year Power Purchase Agreement"
           " at GBP 0.069 per kWh in the source model. Zero upfront cost, no asset"
           " liability, and no maintenance responsibility.")
    ly -= draw_text(cv, sol, lx, ly, COL, S["body"]) + 5.5 * mm

    # Why now
    ly -= section_head(cv, lx, ly, COL, "Why Now")
    items = [
        "Law 82-21 created Morocco's first framework for third-party PPAs and distributed self-generation.",
        "Installations below 5 MW use a simplified licensing pathway.",
        "SR500 programme targets 500 MW of commercial and industrial solar by 2030.",
        "Commercial grid tariff VAT rises to 20 percent in 2026 under the Finance Act.",
        "Morocco solar sector growing at 18.9 percent CAGR (Grand View Research, 2025).",
    ]
    ly -= bullet_list(cv, lx, ly, COL, items, "body") + 4.0 * mm

    # Market opportunity
    ly -= section_head(cv, lx, ly, COL, "Market Opportunity")
    ly -= draw_text(cv,
        "Source analysis references around 1,000 viable commercial sites across"
        " retail, logistics, hospitality, and office sectors in Morocco,"
        " representing a total addressable market of GBP 260M at GBP 260K per installation.",
        lx, ly, COL, S["body"])

    # ── RIGHT ─────────────────────────────────────────────────────────────────

    # Business model card
    bm_h = filled_card(cv, rx, ry, COL, P["soft"], [
        ("BUSINESS MODEL", "kicker"),
        ("Repeatable capital model: fund, build, own, operate, and collect"
         " contracted revenue. Source model references 70 percent project debt"
         " and 30 percent equity per site. Each site SPV is self-financing.", "body"),
    ])
    ry -= bm_h + 5.5 * mm

    # Unit economics — uniform stat boxes with centred value + label
    ry -= section_head(cv, rx, ry, COL, "Unit Economics  (per site, base case)")
    stats = [
        ("GBP 87K",  "Annual Revenue"),
        ("~86%",     "Gross Margin"),
        ("~2 Years", "Equity Payback"),
        ("GBP 2.2M", "20yr Revenue"),
    ]
    n_gaps = len(stats) - 1
    box_gap = 2.5       # pt gap between boxes
    sw  = (COL - n_gaps * box_gap) / len(stats)
    bh  = 18 * mm       # fixed card height so all boxes are identical

    bx2 = rx
    for val, lbl in stats:
        # measure this box's own content for precise vertical centering
        this_tv_h = measure(val, S["sv"], sw)
        this_tl_h = measure(lbl, S["sl"], sw - 4)
        inner_h   = this_tv_h + 2 * mm + this_tl_h
        top_pad   = (bh - inner_h) / 2
        fill_rect(cv, bx2, ry, sw, bh, P["dark"], radius=3)
        draw_text(cv, val, bx2,     ry - top_pad,                   sw,     S["sv"])
        draw_text(cv, lbl, bx2 + 2, ry - top_pad - this_tv_h - 2 * mm, sw - 4, S["sl"])
        bx2 += sw + box_gap
    ry -= bh + 5.5 * mm

    # Forecast table
    ry -= section_head(cv, rx, ry, COL, "Three-Year Forecast")
    cws  = [COL * 0.36, COL * 0.21, COL * 0.22, COL * 0.21]
    hdrs = ["Metric", "Y1 2026", "Y2 2027", "Y3 2028"]
    rows = [
        ["Sites operational", "1",       "9",       "17"],
        ["Revenue",           "GBP 86K", "GBP 777K","GBP 1.5M"],
        ["EBITDA",            "GBP 75K", "GBP 672K","GBP 1.3M"],
        ["Gross margin",       "~86%",    "~86%",    "~86%"],
        ["Net income",        "GBP 41K", "GBP 373K","GBP 722K"],
    ]
    rh = 6.8 * mm

    fill_rect(cv, rx, ry, COL, rh, P["dark"])
    xo = rx
    for hdr, cw in zip(hdrs, cws):
        sk = "th" if hdr == "Metric" else "th_c"
        draw_text(cv, hdr, xo + 3, ry - (rh - 10) / 2, cw - 6, S[sk])
        xo += cw
    ry -= rh

    row_fills = [P["soft"], P["white"]]
    for ri, row in enumerate(rows):
        fill_rect(cv, rx, ry, COL, rh, row_fills[ri % 2])
        rule(cv, rx, ry, COL, P["line"], 0.3)
        xo = rx
        for ci, (cell, cw) in enumerate(zip(row, cws)):
            sk = "td" if ci == 0 else "td_c"
            draw_text(cv, cell, xo + 3, ry - (rh - 10.8) / 2, cw - 6, S[sk])
            xo += cw
        ry -= rh
    ry -= 5.5 * mm

    # Portfolio milestones
    ry -= section_head(cv, rx, ry, COL, "Portfolio Milestones")
    milestones = [
        ("Breakeven",      "4 sites, GBP 340K ARR. Anchor chain LOI signed."),
        ("Series A Ready", "20 sites, GBP 1.7M ARR. Reference-led expansion underway."),
        ("Scale Ready",    "50 plus sites, GBP 4.25M plus ARR. Infrastructure fund opportunity."),
    ]
    for stage, detail in milestones:
        h1 = draw_text(cv, stage,  rx + 5.5 * mm, ry,       COL - 5.5 * mm, S["ms_title"])
        h2 = draw_text(cv, detail, rx + 5.5 * mm, ry - h1,  COL - 5.5 * mm, S["meta"])
        dot(cv, rx + 1.8 * mm, ry - h1 / 2, 2.2, P["accent"])
        ry -= h1 + h2 + 4 * mm

    footer(cv, 1)


# ─── PAGE 2 ──────────────────────────────────────────────────────────────────
def page2(cv):
    HDR_H = 20 * mm

    fill_rect(cv, 0, H, W, HDR_H, P["dark"])
    # Brand name centred vertically in header band
    brand_h = measure("SunPark", S["p2brand"], 100 * mm)
    draw_text(cv, "SunPark", LM, H - (HDR_H - brand_h) / 2, 100 * mm, S["p2brand"])
    # Sub label aligned to same vertical centre, right-aligned
    sub_h = measure("INVESTOR TEASER  |  PAGE 2", S["p2sub"], CW)
    draw_text(cv, "INVESTOR TEASER  |  PAGE 2",
              LM, H - (HDR_H - sub_h) / 2, CW, S["p2sub"])
    rule(cv, 0, H - HDR_H, W, P["accent"], 2.2)

    lx = LM
    rx = LM + COL + GAP
    ly = H - HDR_H - 6 * mm
    ry = ly

    # ── LEFT ─────────────────────────────────────────────────────────────────

    # Competitive advantage
    ly -= section_head(cv, lx, ly, COL, "Competitive Advantage")
    ly -= draw_text(cv,
        "SunPark is not a solar company. It is a commercial energy contract company."
        " No structured competitor currently combines PPA financing, full asset ownership,"
        " multi-site operations, and the ability to operate on leased commercial premises"
        " under one standardised contract in Morocco.",
        lx, ly, COL, S["body"]) + 3.0 * mm
    moat = [
        "First-mover under Law 82-21 with 12 plus months of regulatory engagement.",
        "Standardised PPA template dissolves the split-ownership blocker.",
        "Asset ownership creates 20-year contracted revenue and high switching costs.",
        "Moroccan founder with direct retailer access and French and Arabic fluency.",
    ]
    ly -= bullet_list(cv, lx, ly, COL, moat, "body") + 4.5 * mm

    # Comparison table — source: PPTX slide 10 (exact competitors and dimensions)
    ly -= section_head(cv, lx, ly, COL, "How We Compare")
    # 5 columns: dimension label + 4 competitor types from slide 10
    cws2  = [COL * 0.35, COL * 0.165, COL * 0.165, COL * 0.165, COL * 0.155]
    hdrs2 = ["Dimension", "SunPark", "Local Inst.", "Ind. PPA", "In-house"]
    rows2 = [
        ["PPA financing",       "Yes", "No",     "Bespoke", "No"],
        ["Retail contracts",    "Yes", "No",     "No",      "No"],
        ["Multi-site rollout",  "Yes", "No",     "No",      "No"],
        ["Full O&M included",   "Yes", "No",     "No",      "Yes"],
        ["Works on leased site","Yes", "Rarely", "No",      "No"],
    ]
    rh2     = 6.5 * mm
    hdr_rh  = 8.5 * mm

    fill_rect(cv, lx, ly, COL, hdr_rh, P["dark"])
    xo = lx
    for hdr, cw in zip(hdrs2, cws2):
        sk = "th" if hdr == "Dimension" else "th_c"
        th = measure(hdr, S[sk], cw - 6)
        draw_text(cv, hdr, xo + 3, ly - (hdr_rh - th) / 2, cw - 6, S[sk])
        xo += cw
    ly -= hdr_rh

    for ri, row in enumerate(rows2):
        fill_rect(cv, lx, ly, COL, rh2, P["soft"] if ri % 2 == 0 else P["white"])
        fill_rect(cv, lx + cws2[0], ly, cws2[1], rh2, P["cream"])
        rule(cv, lx, ly, COL, P["line"], 0.3)
        xo = lx
        for ci, (cell, cw) in enumerate(zip(row, cws2)):
            if   ci == 0: sk = "td"
            elif ci == 1: sk = "td_grn"
            else:         sk = "td_c"
            ch = measure(cell, S[sk], cw - 6)
            draw_text(cv, cell, xo + 3, ly - (rh2 - ch) / 2, cw - 6, S[sk])
            xo += cw
        ly -= rh2
    ly -= 7 * mm

    # Traction
    ly -= section_head(cv, lx, ly, COL, "Traction and Validation")
    traction = [
        "Twelve months of structured market discovery is documented in source material.",
        "Agadir logistics warehouse identified as pilot candidate; SOLAROC engaged as EPC partner.",
        "Law 82-21 operational and SR500 active; green bank debt pathway identified for site-level SPVs.",
        "Model designed to resolve three structural adoption blockers identified in discovery work.",
    ]
    ly -= bullet_list(cv, lx, ly, COL, traction, "body") + 4.5 * mm

    # Go to market
    ly -= section_head(cv, lx, ly, COL, "Go to Market")
    draw_text(cv,
        "Direct B2B outreach to facilities directors, CFOs, and procurement heads."
        " Phase 1 is a pilot in Agadir. Phase 2 is reference-led outreach to commercial"
        " chains. Phase 3 enables multi-site rollout from a single framework negotiation.",
        lx, ly, COL, S["body"])

    # ── RIGHT ─────────────────────────────────────────────────────────────────

    # Team card (dark)
    team = [
        "Youssef  Commercial access and PPA negotiations. Moroccan founder with direct retailer relationships.",
        "Fariha   Financial model, capital structure, and SPV architecture. PwC Assurance background.",
        "Akilesh  Technical feasibility, system sizing, and EPC oversight. Commercial PV design background.",
        "Sybil    Operations, regulation, and stakeholder coordination. Management consulting background.",
        "Ahmad    Partnerships, investor access, and regional expansion mapping.",
    ]
    iw = COL - 18
    kh = measure("THE TEAM", S["kicker"], iw)
    t_h = 10 + kh + 3 + 1   # top pad + kicker + gap + rule
    for member in team:
        t_h += measure(member, S["body_w"], iw - 6 * mm) + 3.5 * mm
    t_h += 10   # bottom pad

    fill_rect(cv, rx, ry, COL, t_h, P["dark"], radius=4)
    cy = ry - 10
    draw_text(cv, "THE TEAM", rx + 9, cy, iw, S["kicker"])
    cy -= kh + 2
    rule(cv, rx + 9, cy, iw, colors.HexColor("#1A3A5C"), 0.5)
    cy -= 4
    for member in team:
        h = draw_text(cv, member, rx + 9 + 5.5 * mm, cy, iw - 5.5 * mm, S["body_w"])
        dot(cv, rx + 9 + 1.8 * mm, cy - h / 2, 1.7, P["accent"])
        cy -= h + 3.5 * mm
    ry -= t_h + 5.5 * mm

    # Capital raise
    ry -= section_head(cv, rx, ry, COL, "Capital Raise")
    ry -= draw_text(cv, "GBP 420,000", rx, ry, COL, S["raise"]) + 1.0 * mm
    ry -= draw_text(cv, "Seed convertible note", rx, ry, COL, S["meta"]) + 3.5 * mm

    terms = [
        ("Instrument",    "Convertible note"),
        ("Valuation cap", "GBP 2.6M"),
        ("Milestone",     "First pilot live, two follow-on sites secured, rollout capital ready."),
    ]
    trh_base = 7.2 * mm
    tc1   = COL * 0.44
    tc2   = COL - tc1
    tfill = [P["light"], colors.HexColor("#E8F4F0"), P["light"]]
    tv_style = ParagraphStyle("tv", fontName=FM, fontSize=8.4, leading=11.0,
                              textColor=P["mid"])
    for i, (k, v) in enumerate(terms):
        # make row tall enough to fit value text with 4pt top+bottom padding
        val_h = measure(v, tv_style, tc2 - 8)
        trh   = max(trh_base, val_h + 8)
        fill_rect(cv, rx,        ry, tc1, trh, tfill[i])
        fill_rect(cv, rx + tc1,  ry, tc2, trh, tfill[i])
        rule(cv, rx, ry, COL, P["line"], 0.3)
        draw_text(cv, k, rx + 4, ry - (trh - 10) / 2, tc1 - 8, S["meta"])
        draw_text(cv, v, rx + tc1 + 4, ry - (trh - val_h) / 2, tc2 - 8, tv_style)
        ry -= trh
    ry -= 4.5 * mm

    # Use of proceeds
    ry -= section_head(cv, rx, ry, COL, "Use of Proceeds")
    proceeds = [
        ("GBP 341K",
         "Company operations covering legal, regulatory, commercial development,"
         " feasibility, and contingency reserve."),
        ("GBP 79K",
         "Site SPV equity unlocks GBP 184K of project debt to fund the Agadir pilot installation."),
    ]
    for amt, desc in proceeds:
        ah = draw_text(cv, amt,  rx,             ry,       18 * mm, S["amtlbl"])
        dh = draw_text(cv, desc, rx + 19 * mm,   ry,       COL - 19 * mm, S["body"])
        ry -= max(ah, dh) + 3.5 * mm
    ry -= 2 * mm

    # What this round delivers
    ry -= section_head(cv, rx, ry, COL, "What This Round Delivers")
    delivers = [
        "Agadir pilot site live by month 12.",
        "Standardised PPA template and ONEE approval package finalised.",
        "Series A readiness positioned within 18 months.",
    ]
    bullet_list(cv, rx, ry, COL, delivers, "body", dot_col=P["green"])

    # Disclaimer
    draw_text(cv,
        "This document is confidential and prepared for early-stage investor and advisor discussions."
        " Not an offer document.",
        LM, 14 * mm, CW, S["disc"])

    footer(cv, 2)


# ─── MAIN ────────────────────────────────────────────────────────────────────
def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    cv = canvas.Canvas(str(OUT), pagesize=A4)
    cv.setTitle("SunPark - Investment Teaser")
    cv.setAuthor("SunPark")

    page1(cv)
    cv.showPage()
    page2(cv)
    cv.save()
    print(f"Generated: {OUT}")


if __name__ == "__main__":
    build()
