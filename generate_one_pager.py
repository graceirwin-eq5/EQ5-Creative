from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import os

OUTPUT = os.path.expanduser("~/Documents/GitHub/eq5-creative/EQ5_One_Pager.pdf")

# Brand colors
MIDNIGHT  = colors.HexColor("#0A1020")
BRAND_BLUE= colors.HexColor("#3079E9")
BRAND_CYAN= colors.HexColor("#00D3D3")
SLATE     = colors.HexColor("#6577A5")
WHITE     = colors.white
CARD_DARK = colors.HexColor("#0F1D33")
DIVIDER   = colors.HexColor("#1A2540")

W, H = letter  # 8.5 x 11 inches

def hex_to_rgb(hex_color):
    h = hex_color.hexval()[1:]
    return tuple(int(h[i:i+2], 16)/255 for i in (0, 2, 4))

def make_pdf():
    c = canvas.Canvas(OUTPUT, pagesize=letter)
    c.setPageSize((W, H))

    # ── Background ──────────────────────────────────────────────
    c.setFillColor(MIDNIGHT)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Subtle cyan glow top-right
    from reportlab.lib.colors import Color
    for r, alpha in [(2.5*inch, 0.04), (2.0*inch, 0.03), (1.3*inch, 0.025)]:
        glow = Color(0, 0.83, 0.83, alpha=alpha)
        c.setFillColor(glow)
        c.circle(W - 0.5*inch, H - 0.3*inch, r, fill=1, stroke=0)

    # ── Header bar ───────────────────────────────────────────────
    c.setFillColor(CARD_DARK)
    c.rect(0, H - 1.05*inch, W, 1.05*inch, fill=1, stroke=0)

    # Cyan accent line under header
    c.setStrokeColor(BRAND_CYAN)
    c.setLineWidth(2)
    c.line(0, H - 1.07*inch, W, H - 1.07*inch)

    # Company name
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(0.45*inch, H - 0.58*inch, "EQUALS 5")

    # Cyan accent on "5" — draw a small cyan bar under "5"
    c.setStrokeColor(BRAND_CYAN)
    c.setLineWidth(2)
    name_w = c.stringWidth("EQUALS 5", "Helvetica-Bold", 22)
    five_w = c.stringWidth("5", "Helvetica-Bold", 22)
    c.line(0.45*inch + name_w - five_w, H - 0.62*inch,
           0.45*inch + name_w, H - 0.62*inch)

    # Tagline
    c.setFillColor(colors.HexColor("#00D3D3"))
    c.setFont("Helvetica", 9)
    c.drawString(0.45*inch, H - 0.80*inch, "The All-In-One Healthcare Marketing Platform")

    # Contact right-aligned in header
    c.setFillColor(SLATE)
    c.setFont("Helvetica", 7.5)
    contact_x = W - 0.45*inch
    c.drawRightString(contact_x, H - 0.44*inch, "equals5.com")
    c.drawRightString(contact_x, H - 0.57*inch, "info@equals5.com")
    c.drawRightString(contact_x, H - 0.70*inch, "(201) 305-0150")
    c.drawRightString(contact_x, H - 0.83*inch, "5 Penn Plaza, 23rd Fl, New York, NY")

    # ── Positioning statement ────────────────────────────────────
    y = H - 1.35*inch
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(0.45*inch, y, "Precisely Target HCPs on Social Media — 100% NPI-Level. 20+ Channels. One Platform.")

    y -= 0.22*inch
    c.setFillColor(colors.HexColor("#FFFFFF"))
    style = ParagraphStyle("body", fontName="Helvetica", fontSize=8.5,
                           textColor=colors.HexColor("#AABBCC"),
                           leading=13, leftIndent=0)
    pos_text = (
        "Equals 5 is the first and only platform with 100% deterministic, physician-level targeting on social media. "
        "Built on the insight that <b><font color='#00D3D3'>Doctors Are People Too</font></b>, EQ5 reaches HCPs in their personal, "
        "consumer moments — on Facebook, Instagram, LinkedIn, TikTok, and 20+ channels — with the same NPI-level "
        "precision previously only available in endemic settings."
    )
    p = Paragraph(pos_text, style)
    p.wrapOn(c, W - 0.9*inch, 1*inch)
    p.drawOn(c, 0.45*inch, y - 0.42*inch)

    # ── Divider ──────────────────────────────────────────────────
    y -= 0.62*inch
    c.setStrokeColor(DIVIDER)
    c.setLineWidth(0.5)
    c.line(0.45*inch, y, W - 0.45*inch, y)

    # ── Two-column layout ─────────────────────────────────────────
    col1_x = 0.45*inch
    col2_x = W/2 + 0.15*inch
    col_w  = W/2 - 0.6*inch
    y -= 0.18*inch

    def section_header(cx, cy, text):
        c.setFillColor(BRAND_CYAN)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(cx, cy, text.upper())
        c.setStrokeColor(BRAND_BLUE)
        c.setLineWidth(1)
        c.line(cx, cy - 3, cx + col_w, cy - 3)
        return cy - 0.22*inch

    def bullet_row(cx, cy, label, value=None, value_color=None):
        c.setFillColor(BRAND_CYAN)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(cx, cy, "▸")
        c.setFillColor(WHITE)
        c.setFont("Helvetica", 8)
        if value:
            c.drawString(cx + 0.13*inch, cy, label)
            vc = value_color or BRAND_CYAN
            c.setFillColor(vc)
            c.setFont("Helvetica-Bold", 8)
            lw = c.stringWidth(label, "Helvetica", 8)
            c.drawString(cx + 0.13*inch + lw + 2, cy, value)
        else:
            c.drawString(cx + 0.13*inch, cy, label)
        return cy - 0.165*inch

    def body_text(cx, cy, text, width=None, color=None):
        st = ParagraphStyle("bt", fontName="Helvetica", fontSize=8,
                            textColor=color or colors.HexColor("#AABBCC"),
                            leading=11.5)
        p = Paragraph(text, st)
        w = width or col_w
        p.wrapOn(c, w, 2*inch)
        p.drawOn(c, cx, cy - p.height + 0.01*inch)
        return cy - p.height - 0.06*inch

    # ── LEFT COLUMN ──────────────────────────────────────────────

    # PROOF POINTS
    y1 = section_header(col1_x, y, "Scale & Performance")
    y1 = bullet_row(col1_x, y1, "Pharma brands served: ", "142")
    y1 = bullet_row(col1_x, y1, "Pharma clients: ", "66")
    y1 = bullet_row(col1_x, y1, "Rare disease brands: ", "65")
    y1 = bullet_row(col1_x, y1, "HCP NPI datagraph: ", "2.2M")
    y1 = bullet_row(col1_x, y1, "HCPs reached on social: ", "650,000+")
    y1 = bullet_row(col1_x, y1, "Avg NPI list match rate: ", "87%")
    y1 = bullet_row(col1_x, y1, "Avg click-through rate: ", "0.65%  (6.5× industry avg)")
    y1 = bullet_row(col1_x, y1, "Channels available: ", "20+")

    y1 -= 0.12*inch
    y1 = section_header(col1_x, y1, "Market Position")
    c.setFillColor(colors.HexColor("#AABBCC"))
    c.setFont("Helvetica-Oblique", 7.5)
    c.drawString(col1_x, y1 + 0.04*inch, "Three-lane HCP market — EQ5 owns the social lane:")
    y1 -= 0.14*inch

    lanes = [
        ("Lane 1", "DeepIntent", "Programmatic / White Coat", SLATE),
        ("Lane 2", "PulsePoint / Doceree", "Endemic / EHR", SLATE),
        ("Lane 3", "Equals 5", "Social HCP — Only NPI Player", BRAND_CYAN),
    ]
    for lane, player, desc, lc in lanes:
        c.setFillColor(lc)
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(col1_x, y1, f"{lane}  {player}")
        c.setFillColor(colors.HexColor("#8899AA"))
        c.setFont("Helvetica", 7)
        c.drawString(col1_x + 0.13*inch, y1 - 0.12*inch, desc)
        y1 -= 0.26*inch

    y1 -= 0.08*inch
    y1 = section_header(col1_x, y1, "Select Clients")
    clients = "J&J · Merck · BMS · Sanofi · Novartis · Amgen · Incyte · Genentech · AstraZeneca · Eli Lilly · AbbVie · Novo Nordisk · Bayer · Takeda"
    st = ParagraphStyle("cl", fontName="Helvetica", fontSize=7.5,
                        textColor=colors.HexColor("#AABBCC"), leading=12)
    p = Paragraph(clients, st)
    p.wrapOn(c, col_w, 1*inch)
    p.drawOn(c, col1_x, y1 - p.height)

    # ── RIGHT COLUMN ─────────────────────────────────────────────
    y2 = section_header(col2_x, y, "Platform Capabilities")
    caps = [
        "100% NPI-level HCP targeting on social media",
        "Activation across 20+ channels from one platform",
        "Full-service DTC media with claims-based patient audiences",
        "HCP + DTC coordination bridge — same physicians, both sides",
        "Real-time NPI-level reporting dashboard",
        "Self-service or fully managed campaign options",
        "CCPA / CPRA compliant — aggregate reporting only",
        "48-hour campaign deployment capability",
    ]
    for cap in caps:
        y2 = bullet_row(col2_x, y2, cap)

    y2 -= 0.12*inch
    y2 = section_header(col2_x, y2, "Product Suite")
    products = [
        ("Uni 5™", "Complete HCP Engagement Intelligence System"),
        ("Personi-5™", "Audience Intelligence Engine — NPI enrichment, tokenization & activation"),
        ("Identi-5™", "Identity Resolution Engine — attribution & NPI-level proof"),
        ("Agenti5™", "AI intelligence layer. We work while you sleep."),
    ]
    for name, desc in products:
        c.setFillColor(BRAND_CYAN)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(col2_x, y2, name)
        pw = c.stringWidth(name, "Helvetica-Bold", 8)
        c.setFillColor(colors.HexColor("#8899AA"))
        c.setFont("Helvetica", 7.5)
        # wrap description
        st2 = ParagraphStyle("pd", fontName="Helvetica", fontSize=7.5,
                             textColor=colors.HexColor("#8899AA"), leading=11)
        p2 = Paragraph(desc, st2)
        p2.wrapOn(c, col_w - 0.05*inch, 0.5*inch)
        p2.drawOn(c, col2_x + 0.05*inch, y2 - p2.height)
        y2 -= p2.height + 0.14*inch

    y2 -= 0.05*inch
    y2 = section_header(col2_x, y2, "Channels")
    channel_text = (
        "<b><font color='#00D3D3'>Social:</font></b> Facebook · Instagram · LinkedIn · TikTok · Reddit · Pinterest · X · Quora<br/>"
        "<b><font color='#00D3D3'>Programmatic:</font></b> IQM · The Trade Desk · DV360<br/>"
        "<b><font color='#00D3D3'>Other:</font></b> CTV · Geofencing · Amazon · Yahoo · Endemic Networks · Email"
    )
    st3 = ParagraphStyle("ch", fontName="Helvetica", fontSize=7.5,
                         textColor=colors.HexColor("#AABBCC"), leading=12)
    p3 = Paragraph(channel_text, st3)
    p3.wrapOn(c, col_w, 1*inch)
    p3.drawOn(c, col2_x, y2 - p3.height)

    # ── Footer ───────────────────────────────────────────────────
    c.setFillColor(CARD_DARK)
    c.rect(0, 0, W, 0.38*inch, fill=1, stroke=0)
    c.setStrokeColor(BRAND_BLUE)
    c.setLineWidth(1)
    c.line(0, 0.38*inch, W, 0.38*inch)

    c.setFillColor(SLATE)
    c.setFont("Helvetica", 7)
    c.drawString(0.45*inch, 0.14*inch, "Equals 5 Inc.  |  5 Pennsylvania Plaza, 23rd Floor, New York, NY 10001  |  equals5.com  |  info@equals5.com  |  (201) 305-0150")
    c.drawRightString(W - 0.45*inch, 0.14*inch, "Confidential  ·  © 2026 Equals 5 Inc.")

    c.save()
    print(f"Saved: {OUTPUT}")

make_pdf()
