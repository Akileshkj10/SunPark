from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

W, H = A4  # 595.28 x 841.89

# ── COLOURS ─────────────────────────────────────────────────────────────────
DARK = colors.HexColor("#0A1628")  # deep navy
MID = colors.HexColor("#1A3A5C")  # mid navy
ACCENT = colors.HexColor("#F5A623")  # warm amber / solar gold
LIGHT = colors.HexColor("#E8F0F8")  # pale blue
WHITE = colors.white
GREY = colors.HexColor("#6B7A8D")
LGREY = colors.HexColor("#BDC8D6")

# ── FONTS (Airtable-style fallback on Windows) ──────────────────────────────
FONT_REG = "Helvetica"
FONT_MED = "Helvetica-Bold"
FONT_BOLD = "Helvetica-Bold"

_segoe_regular = r"C:\Windows\Fonts\segoeui.ttf"
_segoe_semibold = r"C:\Windows\Fonts\seguisb.ttf"
_segoe_bold = r"C:\Windows\Fonts\segoeuib.ttf"

if os.path.exists(_segoe_regular):
    pdfmetrics.registerFont(TTFont("AirtableText", _segoe_regular))
    FONT_REG = "AirtableText"
if os.path.exists(_segoe_semibold):
    pdfmetrics.registerFont(TTFont("AirtableTextMedium", _segoe_semibold))
    FONT_MED = "AirtableTextMedium"
elif os.path.exists(_segoe_bold):
    pdfmetrics.registerFont(TTFont("AirtableTextMedium", _segoe_bold))
    FONT_MED = "AirtableTextMedium"
if os.path.exists(_segoe_bold):
    pdfmetrics.registerFont(TTFont("AirtableTextBold", _segoe_bold))
    FONT_BOLD = "AirtableTextBold"


# ── HELPERS ──────────────────────────────────────────────────────────────────
def para(c_obj, text, x, y, w, style, max_lines=None):
    """Draw a Paragraph and return the height used."""
    p = Paragraph(text, style)
    aw, ah = p.wrap(w, 9999)
    p.drawOn(c_obj, x, y - ah)
    return ah


def rect(c_obj, x, y, w, h, fill, stroke=None, radius=0):
    c_obj.saveState()
    c_obj.setFillColor(fill)
    if stroke:
        c_obj.setStrokeColor(stroke)
        c_obj.setLineWidth(0.5)
    else:
        c_obj.setStrokeColor(fill)
    c_obj.roundRect(x, y, w, h, radius, fill=1, stroke=1 if stroke else 0)
    c_obj.restoreState()


def line(c_obj, x1, y1, x2, y2, color=ACCENT, width=1):
    c_obj.saveState()
    c_obj.setStrokeColor(color)
    c_obj.setLineWidth(width)
    c_obj.line(x1, y1, x2, y2)
    c_obj.restoreState()


def text(c_obj, txt, x, y, font=FONT_REG, size=10, color=WHITE, align="left"):
    c_obj.saveState()
    c_obj.setFont(font, size)
    c_obj.setFillColor(color)
    if align == "center":
        c_obj.drawCentredString(x, y, txt)
    elif align == "right":
        c_obj.drawRightString(x, y, txt)
    else:
        c_obj.drawString(x, y, txt)
    c_obj.restoreState()


# ── STYLES ───────────────────────────────────────────────────────────────────
def make_styles():
    body = ParagraphStyle(
        "body",
        fontName=FONT_REG,
        fontSize=8.3,
        textColor=colors.HexColor("#2D3748"),
        leading=11.1,
        spaceAfter=2,
    )
    body_w = ParagraphStyle(
        "body_w",
        fontName=FONT_REG,
        fontSize=7.5,
        textColor=WHITE,
        leading=9.9,
    )
    body_g = ParagraphStyle(
        "body_g",
        fontName=FONT_REG,
        fontSize=7.4,
        textColor=GREY,
        leading=9.6,
    )
    bullet = ParagraphStyle(
        "bullet",
        fontName=FONT_REG,
        fontSize=8.2,
        textColor=colors.HexColor("#2D3748"),
        leftIndent=9,
        firstLineIndent=-9,
        spaceAfter=3,
        leading=10.9,
    )
    bullet_w = ParagraphStyle(
        "bullet_w",
        fontName=FONT_REG,
        fontSize=7.5,
        leftIndent=9,
        firstLineIndent=-9,
        textColor=WHITE,
        leading=9.8,
    )
    label = ParagraphStyle(
        "label",
        fontName=FONT_MED,
        fontSize=6.4,
        textColor=ACCENT,
        leading=8.0,
        spaceAfter=1,
        tracking=1,
    )
    label_d = ParagraphStyle(
        "label_d",
        fontName=FONT_MED,
        fontSize=6.4,
        textColor=LGREY,
        leading=8.0,
        spaceAfter=1,
    )
    small = ParagraphStyle("small", fontName=FONT_REG, fontSize=6.8, textColor=GREY, leading=8.8)
    return body, body_w, body_g, bullet, bullet_w, label, label_d, small


# ── PAGE 1 ───────────────────────────────────────────────────────────────────
def page1(c):
    body, body_w, body_g, bullet, bullet_w, label, label_d, small = make_styles()
    M = 18 * mm  # margin

    # ── HEADER BAND ──────────────────────────────────────────────────────────
    rect(c, 0, H - 52 * mm, W, 52 * mm, DARK)

    # subtle diagonal accent stripe
    c.saveState()
    c.setFillColor(MID)
    c.setStrokeColor(MID)
    p = c.beginPath()
    p.moveTo(W - 90 * mm, H)
    p.lineTo(W, H)
    p.lineTo(W, H - 52 * mm)
    p.lineTo(W - 130 * mm, H - 52 * mm)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.restoreState()

    # Logo / company name
    text(c, "SunPark", M, H - 18 * mm, FONT_BOLD, 26, WHITE)
    text(c, "Solar Carport as a Service", M, H - 27 * mm, FONT_REG, 11, ACCENT)

    # Tagline
    tagline_style = ParagraphStyle("tag", fontName=FONT_REG, fontSize=8.6, textColor=LGREY, leading=12)
    para(
        c,
        "Turning wasted urban space into clean energy infrastructure across<br/>"
        "Morocco's commercial sector — without asking customers to carry the upfront burden.",
        M,
        H - 33.5 * mm,
        W - 2 * M,
        tagline_style,
    )

    # CONFIDENTIAL badge
    rect(c, W - M - 38 * mm, H - 21 * mm, 38 * mm, 8 * mm, ACCENT, radius=2)
    text(c, "INVESTOR TEASER  |  CONFIDENTIAL", W - M - 19 * mm, H - 16.8 * mm, FONT_MED, 5.5, DARK, "center")

    # ── AMBER ACCENT LINE ─────────────────────────────────────────────────────
    line(c, 0, H - 52 * mm, W, H - 52 * mm, ACCENT, 2)

    # ── TWO-COLUMN BODY ───────────────────────────────────────────────────────
    col1_x = M
    col2_x = W / 2 + 5 * mm
    col_w = W / 2 - M - 5 * mm
    top_y = H - 62 * mm

    # ── LEFT COLUMN ──────────────────────────────────────────────────────────

    # --- THE PROBLEM ---
    problem_h = 48 * mm
    rect(c, col1_x - 2 * mm, top_y - problem_h, col_w + 4 * mm, problem_h, LIGHT, radius=3)
    y = top_y
    para(c, "THE PROBLEM", col1_x, y, col_w, label)
    y -= 7 * mm
    line(c, col1_x, y + 4 * mm, col1_x + col_w, y + 4 * mm, LGREY, 0.4)
    problems = [
        ("<b>Rising grid costs</b> — Commercial tariffs hit £0.086/kWh; VAT climbing to 20% by 2026.",),
        (
            "<b>The CAPEX Wall</b> — A standard 200-space solar carport costs ~£262K upfront. "
            "Operators on leased premises have no appetite to own energy infrastructure.",
        ),
        ("<b>Split incentives</b> — Tenants pay bills; landlords own the roof. Deals die at feasibility.",),
    ]
    for (txt_,) in problems:
        ph = para(c, "&#8226;  " + txt_, col1_x, y, col_w, bullet)
        y -= ph + 1.5 * mm

    y -= 3 * mm

    # --- THE SOLUTION ---
    para(c, "THE SOLUTION", col1_x, y, col_w, label)
    y -= 6 * mm
    line(c, col1_x, y + 4 * mm, col1_x + col_w, y + 4 * mm, LGREY, 0.4)

    sol_txt = (
        "SunPark <b>finances, builds, owns, and operates</b> modular solar canopies over "
        "commercial parking lots. Clients sign a 20-year Power Purchase Agreement at "
        "<b>£0.069/kWh</b> — no upfront cost, no asset liability, no maintenance. "
        "We own the asset, carry all risk, and collect recurring energy revenue for the "
        "life of the contract."
    )
    ph = para(c, sol_txt, col1_x, y, col_w, body)
    y -= ph + 3 * mm

    # --- WHY NOW ---
    para(c, "WHY NOW", col1_x, y, col_w, label)
    y -= 6 * mm
    line(c, col1_x, y + 4 * mm, col1_x + col_w, y + 4 * mm, LGREY, 0.4)

    now_items = [
        "<b>Law 82-21 (2023)</b> — Morocco's first framework for third-party PPAs and commercial self-generation.",
        "<b>SR500 Programme</b> — Morocco–Switzerland initiative targeting 500 MW of commercial solar by 2030.",
        "<b>Green finance aligned</b> — IFC &amp; Crédit du Maroc announced a $100M green lending facility.",
        "<b>18.9% CAGR</b> — Morocco's solar market growth rate (IRENA 2024).",
    ]
    for item in now_items:
        ph = para(c, "&#8226;  " + item, col1_x, y, col_w, bullet)
        y -= ph + 1 * mm

    y -= 4 * mm

    # --- MARKET OPPORTUNITY ---
    para(c, "MARKET OPPORTUNITY", col1_x, y, col_w, label)
    y -= 6 * mm
    line(c, col1_x, y + 4 * mm, col1_x + col_w, y + 4 * mm, LGREY, 0.4)

    mkt_txt = (
        "Bottom-up analysis of Morocco's commercial sector identifies <b>~1,000 viable sites</b> "
        "across retail, logistics, hospitality, and offices — representing a "
        "<b>£260M total addressable market</b> at £260K per installation. "
        "Target segments: retail chains, logistics operators, hotel groups, and office complexes."
    )
    ph = para(c, mkt_txt, col1_x, y, col_w, body)
    y -= ph

    # ── RIGHT COLUMN ─────────────────────────────────────────────────────────
    y = top_y

    # --- BUSINESS MODEL ---
    business_h = 36 * mm
    rect(c, col2_x - 2 * mm, y - business_h, col_w + 4 * mm, business_h, colors.HexColor("#F0F4F8"), radius=3)
    para(c, "BUSINESS MODEL", col2_x, y, col_w, label)
    y -= 6 * mm
    line(c, col2_x, y + 4 * mm, col2_x + col_w, y + 4 * mm, LGREY, 0.4)

    bm_txt = (
        "A single repeatable logic: fund → build → own → sell cheaper electricity → "
        "collect 20-year contracted revenue. Capital structure: <b>70% green-bank project "
        "debt / 30% equity</b> per site. Each SPV is self-financing against its own "
        "contracted PPA cashflows, enabling disciplined portfolio scaling without "
        "repeated equity fundraising."
    )
    ph = para(c, bm_txt, col2_x, y, col_w, body)
    y -= ph + 3 * mm

    # --- UNIT ECONOMICS (mini stat boxes) ---
    para(c, "UNIT ECONOMICS  (per 760 kWp site)", col2_x, y, col_w, label)
    y -= 7.5 * mm

    stats = [
        ("£87K", "Annual Revenue"),
        ("86.5%", "EBITDA Margin"),
        ("4 Yrs", "Payback (unlevered)"),
        ("63.9%", "Levered IRR (20yr)"),
    ]
    box_w = col_w / 4 - 1.5 * mm
    bx = col2_x
    for val, lbl in stats:
        rect(c, bx, y - 14 * mm, box_w, 14 * mm, DARK, radius=2)
        text(c, val, bx + box_w / 2, y - 6 * mm, FONT_MED, 9.5, ACCENT, "center")
        text(c, lbl, bx + box_w / 2, y - 11 * mm, FONT_REG, 5.5, LGREY, "center")
        bx += box_w + 2 * mm

    y -= 18.5 * mm

    # --- 3-YEAR FORECAST ---
    para(c, "THREE-YEAR FORECAST", col2_x, y, col_w, label)
    y -= 6 * mm
    line(c, col2_x, y + 4 * mm, col2_x + col_w, y + 4 * mm, LGREY, 0.4)

    # Table
    col_labels = ["", "Y1 (2026)", "Y2 (2027)", "Y3 (2028)"]
    rows = [
        ["Sites operational", "1", "9", "17"],
        ["Revenue", "£86K", "£777K", "£1.5M"],
        ["EBITDA", "£75K", "£672K", "£1.3M"],
        ["EBITDA margin", "86.5%", "86.5%", "86.5%"],
        ["Net income", "£41K", "£373K", "£722K"],
    ]

    tw = col_w
    cw = [tw * 0.40, tw * 0.20, tw * 0.20, tw * 0.20]
    hdr_h = 6 * mm
    row_h = 5.4 * mm

    # header row
    bx = col2_x
    for i, lbl in enumerate(col_labels):
        rect(c, bx, y - hdr_h, cw[i] - 0.8 * mm, hdr_h, DARK, radius=0)
        text(c, lbl, bx + cw[i] / 2 - 0.4 * mm, y - 4.0 * mm, FONT_MED, 6.1, ACCENT, "center")
        bx += cw[i]
    y -= hdr_h + 0.5 * mm

    for ri, row in enumerate(rows):
        fill = colors.HexColor("#F7FAFC") if ri % 2 == 0 else WHITE
        bx = col2_x
        for ci, cell in enumerate(row):
            rect(c, bx, y - row_h, cw[ci] - 0.8 * mm, row_h, fill, radius=0)
            fc = MID if ci == 0 else colors.HexColor("#1A202C")
            fn = FONT_MED if ci == 0 else FONT_REG
            text(
                c,
                cell,
                bx + 2 * mm if ci == 0 else bx + cw[ci] / 2 - 0.4 * mm,
                y - 3.5 * mm,
                fn,
                6.2,
                fc,
                "left" if ci == 0 else "center",
            )
            bx += cw[ci]
        y -= row_h

    y -= 5 * mm

    # --- PORTFOLIO MILESTONES ---
    para(c, "PORTFOLIO MILESTONES", col2_x, y, col_w, label)
    y -= 6.5 * mm
    line(c, col2_x, y + 4 * mm, col2_x + col_w, y + 4 * mm, LGREY, 0.4)

    milestones = [
        ("Breakeven", "4 sites", "£340K ARR", "Anchor chain LOI signed"),
        ("Series A Ready", "20 sites", "£1.7M ARR", "Reference-led expansion"),
        ("Exit Ready", "50+ sites", "£4.25M+ ARR", "Infrastructure fund acquisition"),
    ]
    for stage, sites, arr, trigger in milestones:
        # dot
        c.saveState()
        c.setFillColor(ACCENT)
        c.circle(col2_x + 2 * mm, y - 2 * mm, 1.5 * mm, fill=1, stroke=0)
        c.restoreState()
        ms_style = ParagraphStyle("ms", fontName=FONT_MED, fontSize=7.5, textColor=MID, leading=10)
        ms_sub = ParagraphStyle("ms_sub", fontName=FONT_REG, fontSize=6.5, textColor=GREY, leading=9)
        text(c, f"{stage}  ·  {sites}  ·  {arr}", col2_x + 5.5 * mm, y - 1 * mm, FONT_MED, 7.1, MID)
        text(c, trigger, col2_x + 5.5 * mm, y - 5 * mm, FONT_REG, 6.1, GREY)
        y -= 9 * mm

    # ── FOOTER ────────────────────────────────────────────────────────────────
    rect(c, 0, 0, W, 10 * mm, DARK)
    text(c, "SunPark  |  Solar Carport as a Service  |  sunpark.ma", W / 2, 3.5 * mm, FONT_REG, 7, LGREY, "center")
    text(c, "1 / 2", W - M, 3.5 * mm, FONT_REG, 7, LGREY, "right")


# ── PAGE 2 ───────────────────────────────────────────────────────────────────
def page2(c):
    body, body_w, body_g, bullet, bullet_w, label, label_d, small = make_styles()
    M = 18 * mm

    # ── HEADER BAND ──────────────────────────────────────────────────────────
    rect(c, 0, H - 20 * mm, W, 20 * mm, DARK)
    text(c, "SunPark", M, H - 7.5 * mm, FONT_MED, 12, WHITE)
    text(c, "INVESTOR TEASER — PAGE 2", M, H - 14 * mm, FONT_REG, 7, LGREY)
    line(c, 0, H - 20 * mm, W, H - 20 * mm, ACCENT, 2)

    M2 = M
    col1_x = M2
    col2_x = W / 2 + 5 * mm
    col_w = W / 2 - M2 - 5 * mm
    top_y = H - 28 * mm

    y1 = top_y
    y2 = top_y

    # ══ LEFT COLUMN ══════════════════════════════════════════════════════════

    # --- COMPETITIVE ADVANTAGE ---
    para(c, "COMPETITIVE ADVANTAGE", col1_x, y1, col_w, label)
    y1 -= 6 * mm
    line(c, col1_x, y1 + 4 * mm, col1_x + col_w, y1 + 4 * mm, LGREY, 0.4)

    comp_text = (
        "SunPark is <b>not a solar company — it is a retail energy contract company.</b> "
        "No structured competitor in Morocco currently combines PPA financing, full asset "
        "ownership, multi-site O&amp;M, and the ability to operate on leased commercial "
        "premises under a single standardised contract."
    )
    ph = para(c, comp_text, col1_x, y1, col_w, body)
    y1 -= ph + 2 * mm

    moat_items = [
        "<b>First-mover under Law 82-21</b> — 12+ months of regulatory engagement; ONEE relationships built.",
        "<b>Standardised PPA template</b> — Dissolves the split-ownership blocker; repeatable, bankable.",
        "<b>Asset ownership model</b> — 20-year contracts create deep switching costs and contracted revenue.",
        "<b>Local market depth</b> — Moroccan founder; French and Arabic fluency; direct retailer access.",
    ]
    for item in moat_items:
        ph = para(c, "&#8226;  " + item, col1_x, y1, col_w, bullet)
        y1 -= ph + 1 * mm

    y1 -= 4 * mm

    # --- COMPARISON TABLE ---
    para(c, "HOW WE COMPARE", col1_x, y1, col_w, label)
    y1 -= 6 * mm
    line(c, col1_x, y1 + 4 * mm, col1_x + col_w, y1 + 4 * mm, LGREY, 0.4)

    col_labels = ["", "SunPark", "EPC Installer", "Grid"]
    rows2 = [
        ["Upfront cost to client", "£0", "£262K", "£0"],
        ["Client owns asset", "No", "Yes", "N/A"],
        ["Client maintains", "No", "Yes", "N/A"],
        ["Cost vs grid", "–20%", "–20%*", "Baseline"],
        ["Contract certainty", "20yr", "None", "Variable"],
    ]

    tw = col_w
    cw2 = [tw * 0.42, tw * 0.19, tw * 0.20, tw * 0.19]
    hdr_h = 5.7 * mm
    row_h = 5.1 * mm

    bx = col1_x
    for i, lbl in enumerate(col_labels):
        rect(c, bx, y1 - hdr_h, cw2[i] - 0.8 * mm, hdr_h, DARK, radius=0)
        text(c, lbl, bx + cw2[i] / 2 - 0.4 * mm, y1 - 3.9 * mm, FONT_MED, 5.8, ACCENT, "center")
        bx += cw2[i]
    y1 -= hdr_h + 0.5 * mm

    for ri, row in enumerate(rows2):
        fill_r = colors.HexColor("#F7FAFC") if ri % 2 == 0 else WHITE
        bx = col1_x
        for ci, cell in enumerate(row):
            rect(c, bx, y1 - row_h, cw2[ci] - 0.8 * mm, row_h, fill_r, radius=0)
            if ci == 1:
                # SunPark col — highlight
                rect(c, bx, y1 - row_h, cw2[ci] - 0.8 * mm, row_h, colors.HexColor("#E8F4E8"), radius=0)
            fc = MID if ci == 0 else (colors.HexColor("#276749") if ci == 1 else colors.HexColor("#1A202C"))
            fn = FONT_MED if ci in (0, 1) else FONT_REG
            text(
                c,
                cell,
                bx + 2 * mm if ci == 0 else bx + cw2[ci] / 2 - 0.4 * mm,
                y1 - 3.5 * mm,
                fn,
                6.1,
                fc,
                "left" if ci == 0 else "center",
            )
            bx += cw2[ci]
        y1 -= row_h

    y1 -= 2 * mm
    text(c, "* After 7-year payback period", col1_x + 1 * mm, y1, FONT_REG, 5.5, GREY)
    y1 -= 6 * mm

    # --- TRACTION ---
    para(c, "TRACTION & VALIDATION", col1_x, y1, col_w, label)
    y1 -= 6 * mm
    line(c, col1_x, y1 + 4 * mm, col1_x + col_w, y1 + 4 * mm, LGREY, 0.4)

    traction = [
        ("<b>12 months</b> of expert-led market discovery across Morocco — zero structured retail EaaS providers found.",),
        ("<b>Pilot site secured</b> — Agadir logistics warehouse; SOLAROC (EPC partner) engaged with quotation-backed cost model.",),
        ("<b>Policy tailwind confirmed</b> — Law 82-21 operational; SR500 active; IFC–Crédit du Maroc $100M facility aligned.",),
        ("<b>Failure modes mapped</b> — Model designed specifically to dissolve the three structural blockers preventing solar adoption.",),
    ]
    for (t,) in traction:
        ph = para(c, "&#8226;  " + t, col1_x, y1, col_w, bullet)
        y1 -= ph + 1 * mm

    y1 -= 4 * mm

    # --- GO-TO-MARKET ---
    para(c, "GO-TO-MARKET", col1_x, y1, col_w, label)
    y1 -= 6 * mm
    line(c, col1_x, y1 + 4 * mm, col1_x + col_w, y1 + 4 * mm, LGREY, 0.4)

    gtm = (
        "Direct B2B enterprise sales targeting facilities directors, CFOs, and procurement heads "
        "at retail chains, logistics operators, and hotel groups. Phase 1: warm-network pilot in Agadir. "
        "Phase 2: reference-led outreach to commercial chains. Phase 3: framework agreements "
        "enabling multi-site rollout from a single negotiation."
    )
    ph = para(c, gtm, col1_x, y1, col_w, body)

    # ══ RIGHT COLUMN ══════════════════════════════════════════════════════════

    # --- TEAM ---
    team_card_h = 66 * mm
    rect(c, col2_x - 2 * mm, y2 - team_card_h, col_w + 4 * mm, team_card_h, DARK, radius=3)
    y2_i = y2
    para(
        c,
        "THE TEAM",
        col2_x,
        y2_i,
        col_w,
        ParagraphStyle("lw", fontName=FONT_MED, fontSize=6.2, textColor=ACCENT, leading=7.6, spaceAfter=1),
    )
    y2_i -= 7 * mm
    line(c, col2_x, y2_i + 4 * mm, col2_x + col_w, y2_i + 4 * mm, colors.HexColor("#1A3A5C"), 0.4)

    team = [
        (
            "Youssef",
            "Commercial & PPA",
            "Moroccan founder; 2 B2B startups; direct retailer relationships in Casablanca &amp; Rabat.",
        ),
        ("Fariha", "Finance & Capital", "Project finance training; PwC Assurance; SPV architecture and infrastructure valuation."),
        ("Akilesh", "Technical & EPC", "Electrical Engineering; 3 yrs commercial PV design &amp; EPC management in India."),
        (
            "Sybil",
            "Ops & Regulatory",
            "Management consulting; PwC Nigeria; regulatory stakeholder management across energy.",
        ),
        ("Ahmad", "Partnerships", "Economics &amp; Politics; Vitol energy markets exposure; regional expansion mapping."),
    ]
    for name, role, bio in team:
        c.saveState()
        c.setFillColor(ACCENT)
        c.circle(col2_x + 2 * mm, y2_i - 1.5 * mm, 1.2 * mm, fill=1, stroke=0)
        c.restoreState()
        text(c, f"{name}  ·  {role}", col2_x + 5.5 * mm, y2_i - 0.5 * mm, FONT_MED, 6.6, WHITE)
        ph = para(c, bio, col2_x + 5.5 * mm, y2_i - 5 * mm, col_w - 5.5 * mm, body_w)
        y2_i -= ph + 4.8 * mm

    y2 = y2_i - 1 * mm

    # --- CAPITAL RAISE ---
    para(c, "CAPITAL RAISE", col2_x, y2, col_w, label)
    y2 -= 6 * mm
    line(c, col2_x, y2 + 4 * mm, col2_x + col_w, y2 + 4 * mm, LGREY, 0.4)

    # big number
    text(c, "£420,000", col2_x, y2 - 1 * mm, FONT_BOLD, 16.5, MID)
    text(c, "Seed  |  Convertible Note", col2_x, y2 - 8 * mm, FONT_REG, 7.4, GREY)
    y2 -= 12 * mm

    terms = [("Instrument", "Convertible Note"), ("Valuation Cap", "£2.6M"), ("Discount", "20%")]
    tw2 = col_w
    for k, v in terms:
        rect(c, col2_x, y2 - 6 * mm, tw2 / 2 - 2 * mm, 6 * mm, LIGHT, radius=2)
        rect(c, col2_x + tw2 / 2 + 0.5 * mm, y2 - 6 * mm, tw2 / 2 - 2 * mm, 6 * mm, colors.HexColor("#E8F4F0"), radius=2)
        text(c, k, col2_x + 2 * mm, y2 - 2.5 * mm, FONT_REG, 6.1, GREY)
        text(c, v, col2_x + tw2 / 2 + 2.5 * mm, y2 - 2.5 * mm, FONT_MED, 6.6, MID)
        y2 -= 7.5 * mm

    y2 -= 2 * mm

    # Use of proceeds
    para(c, "USE OF PROCEEDS", col2_x, y2, col_w, label)
    y2 -= 6 * mm
    line(c, col2_x, y2 + 4 * mm, col2_x + col_w, y2 + 4 * mm, LGREY, 0.4)

    proceeds = [
        ("£341K", "Company capital — legal, regulatory, commercial, feasibility, contingency"),
        ("£79K", "Site SPV equity — triggers £184K green-bank debt; funds Agadir pilot installation"),
    ]
    for amt, desc in proceeds:
        text(c, amt, col2_x, y2 - 2 * mm, FONT_MED, 8.4, ACCENT)
        ph = para(
            c,
            desc,
            col2_x + 15 * mm,
            y2 - 0.5 * mm,
            col_w - 15 * mm,
            ParagraphStyle("pdesc", fontName=FONT_REG, fontSize=7, textColor=colors.HexColor("#2D3748"), leading=9.5),
        )
        y2 -= max(ph + 2 * mm, 8 * mm)

    y2 -= 3 * mm

    # What the round buys
    para(c, "WHAT THIS ROUND DELIVERS", col2_x, y2, col_w, label)
    y2 -= 6 * mm
    line(c, col2_x, y2 + 4 * mm, col2_x + col_w, y2 + 4 * mm, LGREY, 0.4)

    delivers = [
        "Agadir pilot site live (Month 12)",
        "Two independent follow-on customer LOIs signed",
        "Standardised PPA template &amp; ONEE approvals in place",
        "Series A readiness within 18 months",
    ]
    for d in delivers:
        c.saveState()
        c.setFillColor(colors.HexColor("#276749"))
        c.circle(col2_x + 2 * mm, y2 - 2 * mm, 1.3 * mm, fill=1, stroke=0)
        c.restoreState()
        ph = para(
            c,
            d,
            col2_x + 5.5 * mm,
            y2 - 0.5 * mm,
            col_w - 5.5 * mm,
            ParagraphStyle("dl", fontName=FONT_REG, fontSize=7.5, textColor=colors.HexColor("#1A202C"), leading=10),
        )
        y2 -= ph + 2 * mm

    # ── CTA BOX ───────────────────────────────────────────────────────────────
    rect(c, M, 15 * mm, W - 2 * M, 18 * mm, DARK, radius=4)
    line(c, M, 15 * mm + 18 * mm, W - 2 * M + M, 15 * mm + 18 * mm, ACCENT, 1.5)

    text(c, "To arrange a meeting or request the full business plan, please contact:", W / 2, 29 * mm, FONT_REG, 8, LGREY, "center")
    text(c, "team@sunpark.ma", W / 2, 22 * mm, FONT_MED, 11, ACCENT, "center")
    text(c, "sunpark.ma", W / 2, 18 * mm, FONT_REG, 8, LGREY, "center")

    # ── FOOTER ────────────────────────────────────────────────────────────────
    rect(c, 0, 0, W, 10 * mm, DARK)
    text(c, "SunPark  |  Solar Carport as a Service  |  sunpark.ma", W / 2, 3.5 * mm, FONT_REG, 7, LGREY, "center")
    text(c, "2 / 2", W - M, 3.5 * mm, FONT_REG, 7, LGREY, "right")
    text(c, "This document is confidential and intended solely for the named recipient.", M, 3.5 * mm, FONT_REG, 5.5, colors.HexColor("#4A5568"))


# ── MAIN ─────────────────────────────────────────────────────────────────────
out = r"c:\Users\akile\projects\Sunpark\deliverables\SunPark_Investment_Teaser.pdf"
os.makedirs(os.path.dirname(out), exist_ok=True)
c = canvas.Canvas(out, pagesize=A4)
c.setTitle("SunPark — Investor Teaser")
c.setAuthor("SunPark")

page1(c)
c.showPage()
page2(c)
c.save()
print("Done:", out)
