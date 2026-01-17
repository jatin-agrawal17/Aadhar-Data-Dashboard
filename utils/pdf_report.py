from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak,
    Table,
    TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor


# ===============================
# COLOR PALETTE (GOVERNMENT SAFE)
# ===============================
PRIMARY = HexColor("#0F4C81")     # UIDAI Blue
ACCENT = HexColor("#198754")      # Green
TEXT = HexColor("#1F2937")        # Dark Grey
LIGHT_BG = HexColor("#F3F6FA")


# ===============================
# MAIN PDF FUNCTION
# ===============================
def create_pdf_report(output_path, report_text, chart_paths):
    styles = getSampleStyleSheet()
    story = []

    # ---------------------------
    # CUSTOM STYLES
    # ---------------------------
    cover_title = ParagraphStyle(
        "CoverTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=26,
        textColor=PRIMARY,
        spaceAfter=24
    )

    cover_subtitle = ParagraphStyle(
        "CoverSubtitle",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=14,
        spaceAfter=16
    )

    cover_text = ParagraphStyle(
        "CoverText",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=11,
        spaceAfter=12
    )

    section_header = ParagraphStyle(
        "SectionHeader",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=PRIMARY,
        spaceBefore=20,
        spaceAfter=8,
        fontName="Helvetica-Bold"
    )

    body_text = ParagraphStyle(
        "BodyText",
        parent=styles["Normal"],
        fontSize=10.5,
        textColor=TEXT,
        leading=15
    )

    chart_heading = ParagraphStyle(
        "ChartHeading",
        parent=styles["Heading2"],
        textColor=PRIMARY
    )

    # ---------------------------
    # SPLIT FRONT PAGE & BODY
    # ---------------------------
    front_page, body = report_text.split("--- PAGE BREAK ---")

    # ===========================
    # FRONT PAGE (FULL PAGE)
    # ===========================
    story.append(Spacer(1, 2 * inch))

    for line in front_page.strip().split("\n"):
        if not line.strip():
            continue

        if "Aadhaar Enrolment Analysis" in line:
            story.append(Paragraph(line, cover_title))
        elif "State-wise" in line:
            story.append(Paragraph(line, cover_subtitle))
        else:
            story.append(Paragraph(line, cover_text))

        story.append(Spacer(1, 0.3 * inch))

    story.append(PageBreak())

    # ===========================
    # MAIN REPORT CONTENT
    # ===========================
    exec_summary_done = False

    for line in body.strip().split("\n"):
        if not line.strip():
            continue

        # Section headers (1., 2., 3., ...)
        if line.strip()[0].isdigit() and line.strip()[1] == ".":
            story.append(Spacer(1, 14))
            story.append(Paragraph(line, section_header))
            story.append(Spacer(1, 6))

        else:
            story.append(Paragraph(line, body_text))
            story.append(Spacer(1, 0.15 * inch))

        # Insert KPI table after Executive Summary text
        if line.startswith("1. Executive Summary"):
            exec_summary_done = True

        if exec_summary_done and "This report details" in line:
            story.append(Spacer(1, 16))

            kpi_table_data = [
                ["Metric", "Value"],
                ["Reporting Days", "88"],
                ["Total Enrolments", "1,018,629"],
                ["Districts Reporting", "75 / 75"],
                ["Average Enrolments per Day", "11,575.33"]
            ]

            table = Table(kpi_table_data, colWidths=[260, 160])
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), PRIMARY),
                ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#FFFFFF")),
                ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BACKGROUND", (0, 1), (-1, -1), LIGHT_BG),
                ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#CBD5E1")),
                ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
                ("PADDING", (0, 0), (-1, -1), 8),
            ]))

            story.append(table)
            story.append(Spacer(1, 24))
            exec_summary_done = False

    # ===========================
    # CHARTS SECTION
    # ===========================
    if chart_paths:
        story.append(PageBreak())

        for chart_title, chart_path in chart_paths:
            story.append(Paragraph(chart_title, chart_heading))
            story.append(Spacer(1, 0.25 * inch))
            story.append(Image(chart_path, width=6.5 * inch, height=4 * inch))
            story.append(Spacer(1, 0.5 * inch))

    # ===========================
    # BUILD DOCUMENT
    # ===========================
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    doc.build(story)
