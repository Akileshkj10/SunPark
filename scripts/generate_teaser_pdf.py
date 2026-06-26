from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OUT_PATH = Path("deliverables/SunPark_Investment_Teaser.pdf")

PALETTE = {
    "primary": colors.HexColor("#181d26"),
    "primary_active": colors.HexColor("#0d1218"),
    "body": colors.HexColor("#333840"),
    "muted": colors.HexColor("#41454d"),
    "canvas": colors.HexColor("#ffffff"),
    "surface_soft": colors.HexColor("#f8fafc"),
    "surface_strong": colors.HexColor("#e0e2e6"),
    "signature_coral": colors.HexColor("#aa2d00"),
    "signature_forest": colors.HexColor("#0a2e0e"),
    "signature_cream": colors.HexColor("#f5e9d4"),
    "hairline": colors.HexColor("#dddddd"),
}


def register_fonts() -> tuple[str, str]:
    regular = Path("C:/Windows/Fonts/segoeui.ttf")
    bold = Path("C:/Windows/Fonts/segoeuib.ttf")
    if regular.exists() and bold.exists():
        pdfmetrics.registerFont(TTFont("SunparkText", str(regular)))
        pdfmetrics.registerFont(TTFont("SunparkTextBold", str(bold)))
        return "SunparkText", "SunparkTextBold"
    return "Helvetica", "Helvetica-Bold"


FONT_REGULAR, FONT_BOLD = register_fonts()


def bullet_lines(items: list[str]) -> str:
    return "<br/>".join(f"&bull;&nbsp;{item}" for item in items)


def styles():
    base = getSampleStyleSheet()
    return {
        "meta": ParagraphStyle(
            "meta",
            parent=base["Normal"],
            fontName=FONT_REGULAR,
            fontSize=8.8,
            leading=11,
            textColor=PALETTE["muted"],
        ),
        "brand": ParagraphStyle(
            "brand",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=12,
            leading=14,
            textColor=PALETTE["primary"],
        ),
        "h1": ParagraphStyle(
            "h1",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=24,
            leading=28,
            textColor=PALETTE["primary"],
            spaceAfter=5,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=base["Normal"],
            fontName=FONT_REGULAR,
            fontSize=11.6,
            leading=16.8,
            textColor=PALETTE["body"],
        ),
        "kicker": ParagraphStyle(
            "kicker",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=8.8,
            leading=10.5,
            textColor=PALETTE["muted"],
            textTransform="uppercase",
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=14,
            leading=18,
            textColor=PALETTE["primary"],
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["Normal"],
            fontName=FONT_REGULAR,
            fontSize=10.1,
            leading=15.2,
            textColor=PALETTE["body"],
        ),
        "bullets": ParagraphStyle(
            "bullets",
            parent=base["Normal"],
            fontName=FONT_REGULAR,
            fontSize=9.9,
            leading=14.4,
            textColor=PALETTE["body"],
        ),
        "card_title_light": ParagraphStyle(
            "card_title_light",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=12.4,
            leading=16,
            textColor=colors.white,
        ),
        "card_body_light": ParagraphStyle(
            "card_body_light",
            parent=base["Normal"],
            fontName=FONT_REGULAR,
            fontSize=9.6,
            leading=13.5,
            textColor=colors.white,
        ),
        "card_title_dark": ParagraphStyle(
            "card_title_dark",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=12.4,
            leading=16,
            textColor=PALETTE["primary"],
        ),
        "card_body_dark": ParagraphStyle(
            "card_body_dark",
            parent=base["Normal"],
            fontName=FONT_REGULAR,
            fontSize=9.6,
            leading=13.5,
            textColor=PALETTE["primary"],
        ),
        "metric_label": ParagraphStyle(
            "metric_label",
            parent=base["Normal"],
            fontName=FONT_REGULAR,
            fontSize=9.2,
            leading=12.2,
            textColor=PALETTE["muted"],
        ),
        "metric_value": ParagraphStyle(
            "metric_value",
            parent=base["Normal"],
            fontName=FONT_BOLD,
            fontSize=10.3,
            leading=12.2,
            textColor=PALETTE["primary"],
        ),
    }


S = styles()


def header_block() -> list:
    row = Table(
        [[Paragraph("SUNPARK", S["brand"]), Paragraph("Confidential teaser for discussion", S["meta"])]],
        colWidths=[85 * mm, 90 * mm],
    )
    row.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    rule = Table([[""]], colWidths=[175 * mm], rowHeights=[0.4 * mm])
    rule.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), PALETTE["hairline"])]))
    return [row, Spacer(1, 4.5 * mm), rule, Spacer(1, 5.5 * mm)]


def signature_card(title: str, body_lines: list[str], background: colors.Color, light: bool = True) -> Table:
    title_style = S["card_title_light"] if light else S["card_title_dark"]
    body_style = S["card_body_light"] if light else S["card_body_dark"]
    body = f"{bullet_lines(body_lines)}"
    card = Table(
        [[Paragraph(title, title_style)], [Paragraph(body, body_style)]],
        colWidths=[175 * mm],
    )
    card.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), background),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return card


def side_card(
    width_mm: float,
    title: str,
    lines: list[str],
    background: colors.Color,
    light: bool = True,
) -> Table:
    title_style = S["card_title_light"] if light else S["card_title_dark"]
    body_style = S["card_body_light"] if light else S["card_body_dark"]
    body = Paragraph(bullet_lines(lines), body_style)
    card = Table([[Paragraph(title, title_style)], [body]], colWidths=[width_mm * mm])
    card.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), background),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return card


def metric_table() -> Table:
    rows = [
        ("Client upfront capex", "GBP 0 in the source model"),
        ("Source-modelled PPA tariff", "GBP 0.069/kWh"),
        ("Commercial grid benchmark", "Approx. GBP 0.086/kWh"),
        ("Typical annual generation", "Approx. 1.25M kWh per site"),
        ("Illustrative site size", "Around 300 kWp"),
    ]

    data = [[Paragraph("Metric", S["metric_label"]), Paragraph("Source-backed value", S["metric_label"])]]
    data += [[Paragraph(label, S["metric_label"]), Paragraph(value, S["metric_value"])] for label, value in rows]
    t = Table(data, colWidths=[66 * mm, 109 * mm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), PALETTE["surface_strong"]),
                ("BACKGROUND", (0, 1), (-1, -1), PALETTE["surface_soft"]),
                ("LINEBELOW", (0, 0), (-1, -1), 0.5, PALETTE["hairline"]),
                ("LINEABOVE", (0, 0), (-1, 0), 0.5, PALETTE["hairline"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8.5),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    return t


def build_story() -> list:
    story = []

    story += header_block()
    story.append(Paragraph("Solar Carport as a Service", S["h1"]))
    story.append(
        Paragraph(
            "Turn existing commercial parking in Morocco into shaded solar power with no upfront client capex.",
            S["subtitle"],
        )
    )
    story.append(Spacer(1, 5 * mm))

    story.append(
        signature_card(
            "Business proposition",
            [
                "SunPark funds, builds, owns, and operates modular solar canopies over commercial parking surfaces.",
                "Customers buy generated electricity through long-term PPAs instead of buying and operating infrastructure assets.",
                "The model addresses three adoption barriers highlighted in source material: upfront capex, split ownership, and non-standardized PPA structures.",
            ],
            PALETTE["signature_coral"],
            light=True,
        )
    )
    story.append(Spacer(1, 5 * mm))

    left = [
        Paragraph("OPPORTUNITY", S["kicker"]),
        Paragraph("Why this matters now", S["h2"]),
        Paragraph(
            bullet_lines(
                [
                    "Morocco imports approximately 90% of its energy, creating structural exposure to energy-market pressure.",
                    "Law 82-21 created a framework for distributed self-generation and third-party PPAs.",
                    "Installations below 5 MW benefit from simplified licensing pathways.",
                    "National policy references include 52% installed renewable capacity by 2030 and SR500 with a 500 MW C&I target by 2030.",
                ]
            ),
            S["bullets"],
        ),
    ]
    right = [
        Paragraph("MODEL STRUCTURE", S["kicker"]),
        Paragraph("Service model in one view", S["h2"]),
        Paragraph(
            bullet_lines(
                [
                    "SunPark carries project capex and asset ownership.",
                    "Site hosts buy electricity via a long-term PPA structure.",
                    "Execution scope includes feasibility, regulatory coordination, EPC oversight, and operations.",
                    "Infrastructure is designed over existing parking with EV-readiness included in source architecture.",
                ]
            ),
            S["bullets"],
        ),
    ]
    two_col = Table([[left, "", right]], colWidths=[84 * mm, 7 * mm, 84 * mm])
    two_col.setStyle(
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
    story.append(two_col)
    story.append(Spacer(1, 5 * mm))

    story.append(Paragraph("ECONOMICS SNAPSHOT", S["kicker"]))
    story.append(Paragraph("Source-modelled commercial indicators", S["h2"]))
    story.append(metric_table())
    story.append(Spacer(1, 3.2 * mm))
    story.append(
        Paragraph(
            "Sources: Entrepreneurship Doc (1).pdf and SunPark_Deck_GBP.pptx (1).pptx. Figures are source-modelled and not audited operating results.",
            S["meta"],
        )
    )

    story.append(PageBreak())

    story += header_block()
    story.append(Paragraph("Execution, sectors, and team coverage", S["h1"]))
    story.append(
        Paragraph(
            "Built for commercial retail, logistics, hospitality, and office sites in Morocco under a repeatable service-delivery model.",
            S["subtitle"],
        )
    )
    story.append(Spacer(1, 5 * mm))

    left_col = [
        Paragraph("TARGET SEGMENTS", S["kicker"]),
        Paragraph("Commercial sectors in scope", S["h2"]),
        Paragraph(
            bullet_lines(
                [
                    "Retail: shaded customer parking and lower-cost energy procurement.",
                    "Logistics: large paved surfaces with operational energy demand.",
                    "Hospitality: guest comfort plus visible clean-energy infrastructure.",
                    "Offices: employee parking converted into on-site generation support.",
                ]
            ),
            S["bullets"],
        ),
        Spacer(1, 3 * mm),
        Paragraph("DELIVERY SEQUENCE", S["kicker"]),
        Paragraph("From site review to long-term service", S["h2"]),
        Paragraph(
            bullet_lines(
                [
                    "1) Site review and technical feasibility.",
                    "2) Commercial proposal and PPA structuring.",
                    "3) Regulatory and grid coordination under Law 82-21.",
                    "4) EPC delivery and commissioning.",
                    "5) Monitoring, maintenance coordination, and ongoing customer service.",
                ]
            ),
            S["bullets"],
        ),
    ]

    right_col = [
        side_card(
            66.5,
            "Execution ownership",
            [
                "Youssef: Commercial access and PPA negotiations.",
                "Fariha: Financial model, capital structure, and SPV architecture.",
                "Akilesh: Technical feasibility, system sizing, and EPC oversight.",
                "Sybil: Operations, regulation, and stakeholder coordination.",
                "Ahmad: Partnerships, investor access, and expansion mapping.",
            ],
            PALETTE["signature_forest"],
            light=True,
        ),
        Spacer(1, 3 * mm),
        side_card(
            66.5,
            "Fundraising context from source material",
            [
                "Current raise referenced in source material: GBP 420K.",
                "Stated objective: move from preparation into validated execution milestones.",
                "This teaser is prepared for early investor, advisor, and board-level discussions.",
            ],
            PALETTE["signature_cream"],
            light=False,
        ),
    ]

    execution_grid = Table([[left_col, right_col]], colWidths=[108.5 * mm, 66.5 * mm])
    execution_grid = Table([[left_col, "", right_col]], colWidths=[103 * mm, 5.5 * mm, 66.5 * mm])
    execution_grid.setStyle(
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
    story.append(execution_grid)
    story.append(Spacer(1, 5 * mm))

    next_step = Table(
        [
            [Paragraph("Next-step discussion", S["h2"])],
            [
                Paragraph(
                    "SunPark can provide deeper technical, legal, and financial working materials in a follow-up meeting and data-room package. Contact details can be provided directly by the team.",
                    S["body"],
                )
            ],
        ],
        colWidths=[175 * mm],
    )
    next_step.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALETTE["surface_soft"]),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
            ]
        )
    )
    story.append(next_step)
    story.append(Spacer(1, 2.5 * mm))
    story.append(
        Paragraph(
            "Prepared for early-stage investor/advisor review. This document is informational and not an offer document.",
            S["meta"],
        )
    )

    return story


def build_pdf() -> Path:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUT_PATH),
        pagesize=A4,
        leftMargin=17.5 * mm,
        rightMargin=17.5 * mm,
        topMargin=15.5 * mm,
        bottomMargin=12.5 * mm,
    )
    doc.build(build_story())
    return OUT_PATH


if __name__ == "__main__":
    result = build_pdf()
    print(f"Generated: {result}")
