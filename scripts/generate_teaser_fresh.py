from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUT_PATH = Path("deliverables/SunPark_Investment_Teaser.pdf")


PALETTE = {
    "dark": colors.HexColor("#0A1628"),
    "mid": colors.HexColor("#1A3A5C"),
    "accent": colors.HexColor("#F5A623"),
    "light": colors.HexColor("#E8F0F8"),
    "soft": colors.HexColor("#F3F6FA"),
    "ink": colors.HexColor("#1F2937"),
    "body": colors.HexColor("#2D3748"),
    "muted": colors.HexColor("#6B7A8D"),
    "line": colors.HexColor("#D4DCE7"),
    "white": colors.white,
}


def register_fonts() -> tuple[str, str, str]:
    regular = Path(r"C:\Windows\Fonts\segoeui.ttf")
    semibold = Path(r"C:\Windows\Fonts\seguisb.ttf")
    bold = Path(r"C:\Windows\Fonts\segoeuib.ttf")

    font_regular = "Helvetica"
    font_medium = "Helvetica-Bold"
    font_bold = "Helvetica-Bold"

    if regular.exists():
        pdfmetrics.registerFont(TTFont("TeaserRegular", str(regular)))
        font_regular = "TeaserRegular"
    if semibold.exists():
        pdfmetrics.registerFont(TTFont("TeaserMedium", str(semibold)))
        font_medium = "TeaserMedium"
    elif bold.exists():
        pdfmetrics.registerFont(TTFont("TeaserMedium", str(bold)))
        font_medium = "TeaserMedium"
    if bold.exists():
        pdfmetrics.registerFont(TTFont("TeaserBold", str(bold)))
        font_bold = "TeaserBold"

    return font_regular, font_medium, font_bold


FONT_REG, FONT_MED, FONT_BOLD = register_fonts()


def s() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "kicker": ParagraphStyle(
            "kicker",
            parent=base["Normal"],
            fontName=FONT_MED,
            fontSize=7.8,
            leading=9.8,
            textColor=PALETTE["accent"],
        ),
        "h1": ParagraphStyle(
            "h1",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=31,
            leading=35,
            textColor=PALETTE["white"],
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=16.8,
            leading=20.5,
            textColor=PALETTE["ink"],
        ),
        "subhead": ParagraphStyle(
            "subhead",
            parent=base["Normal"],
            fontName=FONT_REG,
            fontSize=10.6,
            leading=14.2,
            textColor=PALETTE["line"],
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["Normal"],
            fontName=FONT_REG,
            fontSize=10.0,
            leading=13.8,
            textColor=PALETTE["body"],
        ),
        "body_dark": ParagraphStyle(
            "body_dark",
            parent=base["Normal"],
            fontName=FONT_REG,
            fontSize=9.2,
            leading=12.6,
            textColor=PALETTE["white"],
        ),
        "meta": ParagraphStyle(
            "meta",
            parent=base["Normal"],
            fontName=FONT_REG,
            fontSize=8.0,
            leading=10.5,
            textColor=PALETTE["muted"],
        ),
        "value": ParagraphStyle(
            "value",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=14.5,
            leading=16.5,
            textColor=PALETTE["accent"],
            alignment=1,
        ),
        "label_small": ParagraphStyle(
            "label_small",
            parent=base["Normal"],
            fontName=FONT_REG,
            fontSize=7.1,
            leading=9.1,
            textColor=PALETTE["line"],
            alignment=1,
        ),
        "header_badge": ParagraphStyle(
            "header_badge",
            parent=base["Normal"],
            fontName=FONT_MED,
            fontSize=6.8,
            leading=8.8,
            textColor=PALETTE["dark"],
            alignment=1,
        ),
    }


STYLES = s()


def bullets(lines: list[str]) -> str:
    return "<br/>".join([f"- {line}" for line in lines])


def section_block(title: str, content: str) -> list:
    return [
        Paragraph(title.upper(), STYLES["kicker"]),
        Spacer(1, 1.8 * mm),
        Table(
            [[""]],
            colWidths=[84 * mm],
            rowHeights=[0.5 * mm],
            style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), PALETTE["line"])]),
        ),
        Spacer(1, 2.4 * mm),
        Paragraph(content, STYLES["body"]),
        Spacer(1, 3.2 * mm),
    ]


def stat_card(value: str, label: str) -> Table:
    t = Table([[Paragraph(value, STYLES["value"])], [Paragraph(label, STYLES["label_small"])]], colWidths=[19.5 * mm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALETTE["dark"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 3.0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3.0),
                ("TOPPADDING", (0, 0), (-1, -1), 5.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5.5),
            ]
        )
    )
    return t


def top_header() -> Table:
    left = [
        Paragraph("SunPark", STYLES["h1"]),
        Paragraph("Solar Carport as a Service", ParagraphStyle("subtitle", fontName=FONT_REG, fontSize=11, leading=13.5, textColor=PALETTE["accent"])),
        Spacer(1, 1.8 * mm),
        Paragraph(
            "Turning urban parking space into clean energy infrastructure in Morocco, with no upfront client capex.",
            STYLES["subhead"],
        ),
    ]

    badge = Table([[Paragraph("INVESTOR TEASER  |  CONFIDENTIAL", STYLES["header_badge"])]], colWidths=[52 * mm])
    badge.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALETTE["accent"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 4.0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4.0),
                ("TOPPADDING", (0, 0), (-1, -1), 4.2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4.2),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )

    wrapper = Table([[left, badge]], colWidths=[120 * mm, 55 * mm])
    wrapper.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALETTE["dark"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 11.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 11.5),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (1, 0), (1, 0), "RIGHT"),
            ]
        )
    )
    return wrapper


def page_one_content() -> list:
    left_story = []
    right_story = []

    problem_card = Table(
        [[Paragraph("THE PROBLEM", STYLES["kicker"])], [Paragraph(bullets([
            "Rising grid costs: commercial benchmark is GBP 0.086 per kWh in source material.",
            "Upfront capex barriers still block adoption for many operators.",
            "Split ownership between tenants and landlords slows commercial decisions.",
        ]), STYLES["body"])]],
        colWidths=[84 * mm],
    )
    problem_card.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALETTE["light"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ]
        )
    )
    left_story.extend([problem_card, Spacer(1, 3.8 * mm)])

    left_story.extend(
        section_block(
            "The solution",
            "SunPark finances, builds, owns, and operates modular solar canopies over commercial parking. Clients buy power under a long term PPA at GBP 0.069 per kWh in source material.",
        )
    )
    left_story.extend(
        section_block(
            "Why now",
            bullets(
                [
                    "Law 82-21 created a framework for third party PPAs and distributed self generation.",
                    "Installations below 5 MW benefit from simpler licensing pathways.",
                    "National programs include a 52 percent renewable capacity target and SR500 with 500 MW C and I target by 2030.",
                ]
            ),
        )
    )
    left_story.extend(
        section_block(
            "Market opportunity",
            "Bottom up source analysis references about 1,000 viable commercial sites across retail, logistics, hospitality, and office segments.",
        )
    )

    business_model_card = Table(
        [[Paragraph("BUSINESS MODEL", STYLES["kicker"])], [Paragraph(
            "Repeatable model: fund, build, own, operate, and sell electricity under long term contracted PPAs. Source model references 70 percent debt and 30 percent equity per site.",
            STYLES["body"],
        )]],
        colWidths=[84 * mm],
    )
    business_model_card.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALETTE["soft"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
            ]
        )
    )
    right_story.extend([business_model_card, Spacer(1, 3.8 * mm)])

    right_story.append(Paragraph("UNIT ECONOMICS", STYLES["kicker"]))
    right_story.append(Spacer(1, 2.0 * mm))
    stats_row = Table(
        [[
            stat_card("GBP 87K", "Annual revenue"),
            stat_card("86.5%", "EBITDA margin"),
            stat_card("4 years", "Payback"),
            stat_card("63.9%", "Levered IRR"),
        ]],
        colWidths=[84 * mm],
    )
    stats_row.setStyle(
        TableStyle(
            [
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    right_story.extend([stats_row, Spacer(1, 3.8 * mm)])

    right_story.append(Paragraph("THREE YEAR FORECAST", STYLES["kicker"]))
    right_story.append(Spacer(1, 1.8 * mm))
    forecast = Table(
        [
            ["", "Y1", "Y2", "Y3"],
            ["Sites operational", "1", "9", "17"],
            ["Revenue", "GBP 86K", "GBP 777K", "GBP 1.5M"],
            ["EBITDA", "GBP 75K", "GBP 672K", "GBP 1.3M"],
            ["EBITDA margin", "86.5%", "86.5%", "86.5%"],
            ["Net income", "GBP 41K", "GBP 373K", "GBP 722K"],
        ],
        colWidths=[34 * mm, 16.5 * mm, 16.5 * mm, 17 * mm],
    )
    forecast.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), PALETTE["dark"]),
                ("TEXTCOLOR", (0, 0), (-1, 0), PALETTE["accent"]),
                ("FONTNAME", (0, 0), (-1, 0), FONT_MED),
                ("FONTSIZE", (0, 0), (-1, -1), 8.0),
                ("FONTNAME", (0, 1), (0, -1), FONT_MED),
                ("TEXTCOLOR", (0, 1), (-1, -1), PALETTE["ink"]),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [PALETTE["white"], PALETTE["soft"]]),
                ("GRID", (0, 0), (-1, -1), 0.35, PALETTE["line"]),
                ("ALIGN", (1, 1), (-1, -1), "CENTER"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4.8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4.8),
            ]
        )
    )
    right_story.extend([forecast, Spacer(1, 3.8 * mm)])

    right_story.append(Paragraph("PORTFOLIO MILESTONES", STYLES["kicker"]))
    right_story.append(Spacer(1, 1.6 * mm))
    right_story.append(
        Paragraph(
            bullets(
                [
                    "Breakeven: 4 sites and GBP 340K ARR.",
                    "Series A readiness: 20 sites and GBP 1.7M ARR.",
                    "Scale readiness: 50 plus sites and GBP 4.25M plus ARR.",
                ]
            ),
            STYLES["body"],
        )
    )
    right_story.extend(
        section_block(
            "Execution readiness",
            "Operational architecture in source material includes monitoring, O and M coordination, billing relationship management, and annual sustainability reporting.",
        )
    )

    page_grid = Table([[left_story, right_story]], colWidths=[84 * mm, 84 * mm])
    page_grid.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return [page_grid]


def page_two_content() -> list:
    left_story = []
    right_story = []

    left_story.extend(
        section_block(
            "Competitive advantage",
            "SunPark combines financing, ownership, operations, and long term PPA structure under one framework adapted for commercial parking in Morocco.",
        )
    )
    left_story.extend(
        section_block(
            "How we compare",
            "Client capex: SunPark GBP 0. Client ownership and maintenance: no. Cost position in source model: below benchmark.",
        )
    )
    left_story.extend(
        section_block(
            "Traction and validation",
            bullets(
                [
                    "Twelve months of market discovery work is documented in source material.",
                    "Agadir logistics warehouse is identified as a pilot candidate.",
                    "Execution model focuses on removing capex, ownership, and contract barriers.",
                ]
            ),
        )
    )
    left_story.extend(
        section_block(
            "Go to market",
            "Direct B2B outreach to facilities, procurement, and finance decision makers. Model is designed for repeat rollout across multi site operators.",
        )
    )

    team_card = Table(
        [[Paragraph("THE TEAM", STYLES["kicker"])], [Paragraph(
            bullets(
                [
                    "Youssef: Commercial access and PPA negotiations.",
                    "Fariha: Financial model, capital structure, and SPV architecture.",
                    "Akilesh: Technical feasibility, system sizing, and EPC oversight.",
                    "Sybil: Operations, regulation, and stakeholder coordination.",
                    "Ahmad: Partnerships, investor access, and regional mapping.",
                ]
            ),
            STYLES["body_dark"],
        )]],
        colWidths=[84 * mm],
    )
    team_card.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALETTE["dark"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )
    right_story.extend([team_card, Spacer(1, 3.6 * mm)])

    right_story.append(Paragraph("CAPITAL RAISE", STYLES["kicker"]))
    right_story.append(Paragraph("GBP 420,000", ParagraphStyle("raise", fontName=FONT_BOLD, fontSize=20, leading=23, textColor=PALETTE["mid"])))
    right_story.append(Paragraph("Seed convertible note", STYLES["meta"]))
    right_story.append(Spacer(1, 2.2 * mm))

    terms = Table(
        [
            ["Instrument", "Convertible note"],
            ["Valuation cap", "GBP 2.6M"],
            ["Discount", "20%"],
        ],
        colWidths=[42 * mm, 42 * mm],
    )
    terms.setStyle(
        TableStyle(
            [
                ("ROWBACKGROUNDS", (0, 0), (-1, -1), [PALETTE["light"], colors.HexColor("#E8F4F0")]),
                ("TEXTCOLOR", (0, 0), (-1, -1), PALETTE["mid"]),
                ("FONTNAME", (0, 0), (0, -1), FONT_REG),
                ("FONTNAME", (1, 0), (1, -1), FONT_MED),
                ("FONTSIZE", (0, 0), (-1, -1), 8.2),
                ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#DCE4EC")),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5.0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5.0),
            ]
        )
    )
    right_story.extend([terms, Spacer(1, 3.2 * mm)])

    right_story.extend(
        section_block(
            "Use of proceeds",
            bullets(
                [
                    "GBP 341K for company execution scope, legal work, regulatory work, and feasibility.",
                    "GBP 79K for site SPV equity to unlock project debt and pilot delivery.",
                ]
            ),
        )
    )
    right_story.extend(
        section_block(
            "What this round delivers",
            bullets(
                [
                    "Agadir pilot live target in month 12.",
                    "Two follow on LOIs as commercial validation objective.",
                    "Standardized PPA template and approval readiness package.",
                    "Series A readiness target within 18 months.",
                ]
            ),
        )
    )
    right_story.extend(
        section_block(
            "Discussion request",
            "Follow up discussion can include detailed legal pack, regulatory path assumptions, and full financial model with scenario analysis.",
        )
    )

    page_grid = Table([[left_story, right_story]], colWidths=[84 * mm, 84 * mm])
    page_grid.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return [page_grid]


def footer_bar(page_num: int) -> Table:
    t = Table(
        [[
            Paragraph("SunPark  |  Solar Carport as a Service  |  sunpark.ma", ParagraphStyle("f1", fontName=FONT_REG, fontSize=7.8, leading=9.2, textColor=PALETTE["line"])),
            Paragraph(f"{page_num} / 2", ParagraphStyle("f2", fontName=FONT_REG, fontSize=7.8, leading=9.2, textColor=PALETTE["line"], alignment=2)),
        ]],
        colWidths=[150 * mm, 25 * mm],
    )
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALETTE["dark"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 4.8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4.8),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    return t


def build_story() -> list:
    story = []

    story.append(top_header())
    story.append(Spacer(1, 0.9 * mm))
    accent_rule = Table([[""]], colWidths=[175 * mm], rowHeights=[0.8 * mm])
    accent_rule.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), PALETTE["accent"])]))
    story.extend([accent_rule, Spacer(1, 4.4 * mm)])
    story.extend(page_one_content())
    story.append(Spacer(1, 4.4 * mm))
    story.append(footer_bar(1))

    story.append(PageBreak())

    page2_head = Table(
        [[
            Paragraph("SunPark", ParagraphStyle("p2h1", fontName=FONT_MED, fontSize=13, leading=15.5, textColor=PALETTE["white"])),
            Paragraph("INVESTOR TEASER  |  PAGE 2", ParagraphStyle("p2h2", fontName=FONT_REG, fontSize=8, leading=10.2, textColor=PALETTE["line"], alignment=2)),
        ]],
        colWidths=[120 * mm, 55 * mm],
    )
    page2_head.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALETTE["dark"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 7.2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7.2),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    story.extend([page2_head, Spacer(1, 0.9 * mm), accent_rule, Spacer(1, 4.4 * mm)])
    story.extend(page_two_content())
    story.append(Spacer(1, 4.4 * mm))
    story.append(footer_bar(2))
    return story


def build_pdf() -> Path:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUT_PATH),
        pagesize=A4,
        leftMargin=17 * mm,
        rightMargin=17 * mm,
        topMargin=14 * mm,
        bottomMargin=10 * mm,
        title="SunPark - Investment Teaser",
        author="SunPark",
    )
    doc.build(build_story())
    return OUT_PATH


if __name__ == "__main__":
    output = build_pdf()
    print(f"Generated: {output}")
