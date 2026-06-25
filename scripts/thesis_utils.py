#!/usr/bin/env python3
"""
PhD Thesis Builder — Part 1: Setup, Fonts, Styles, Front Matter
================================================================
Builds the front matter and infrastructure for the PhD thesis:
- Font registration (Tinos, Carlito, NotoArabic)
- TocDocTemplate with page numbering
- Paragraph styles
- Front matter: title page, declaration, dedication, acknowledgments,
  abstracts (EN/FR/AR), TOC, list of tables/figures, abbreviations

Run: python3 /home/z/my-project/scripts/build_thesis_part1.py
"""

import os
import sys
import hashlib
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm, inch
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    Image, KeepTogether, NextPageTemplate, PageTemplate, Frame, BaseDocTemplate,
    FrameBreak, CondPageBreak
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfgen import canvas

# Arabic text shaping
import arabic_reshaper
from bidi.algorithm import get_display

# ===================================================================
# PATHS
# ===================================================================
PROJECT_DIR = Path('/home/z/my-project')
FONTS_DIR = PROJECT_DIR / 'fonts'
FIGURES_DIR = PROJECT_DIR / 'figures'
OUTPUT_DIR = PROJECT_DIR / 'download'
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
BODY_PDF = OUTPUT_DIR / 'thesis_body.pdf'

# ===================================================================
# FONT REGISTRATION
# ===================================================================
def register_fonts():
    """Register Tinos (serif body), Carlito (sans heading), Noto Naskh Arabic."""
    # Tinos — Times-compatible serif, OFL
    pdfmetrics.registerFont(TTFont('Tinos', str(FONTS_DIR / 'Tinos-Regular.ttf')))
    pdfmetrics.registerFont(TTFont('Tinos-Bold', str(FONTS_DIR / 'Tinos-Bold.ttf')))
    pdfmetrics.registerFont(TTFont('Tinos-Italic', str(FONTS_DIR / 'Tinos-Italic.ttf')))
    pdfmetrics.registerFont(TTFont('Tinos-BoldItalic', str(FONTS_DIR / 'Tinos-BoldItalic.ttf')))
    registerFontFamily('Tinos', normal='Tinos', bold='Tinos-Bold',
                       italic='Tinos-Italic', boldItalic='Tinos-BoldItalic')

    # Carlito — Calibri-compatible sans-serif
    pdfmetrics.registerFont(TTFont('Carlito', '/usr/share/fonts/truetype/english/Carlito-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('Carlito-Bold', '/usr/share/fonts/truetype/english/Carlito-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('Carlito-Italic', '/usr/share/fonts/truetype/english/Carlito-Italic.ttf'))
    pdfmetrics.registerFont(TTFont('Carlito-BoldItalic', '/usr/share/fonts/truetype/english/Carlito-BoldItalic.ttf'))
    registerFontFamily('Carlito', normal='Carlito', bold='Carlito-Bold',
                       italic='Carlito-Italic', boldItalic='Carlito-BoldItalic')

    # Noto Naskh Arabic — for Arabic abstract
    pdfmetrics.registerFont(TTFont('NotoArabic', str(FONTS_DIR / 'NotoNaskhArabic-Regular.ttf')))
    pdfmetrics.registerFont(TTFont('NotoArabic-Bold', str(FONTS_DIR / 'NotoNaskhArabic-Bold.ttf')))
    registerFontFamily('NotoArabic', normal='NotoArabic', bold='NotoArabic-Bold')

    # DejaVu Sans Mono for code/variables
    pdfmetrics.registerFont(TTFont('Mono', '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'))

    print("✓ Fonts registered: Tinos, Carlito, NotoArabic, Mono")


# ===================================================================
# COLOR PALETTE (Cascade-generated)
# ===================================================================
PAGE_BG       = colors.HexColor('#FBFAF7')   # cream-white
SECTION_BG    = colors.HexColor('#F1EFE8')
CARD_BG       = colors.HexColor('#F5F2EB')
TABLE_STRIPE  = colors.HexColor('#F4F1E8')

HEADER_FILL   = colors.HexColor('#2D5016')   # date-palm green
COVER_BLOCK   = colors.HexColor('#4A7C1F')

BORDER        = colors.HexColor('#D2CEC0')
ICON          = colors.HexColor('#867237')

ACCENT        = colors.HexColor('#8B6914')   # ochre/gold
ACCENT_2      = colors.HexColor('#9C4942')   # dark red (control/contrast)

TEXT_PRIMARY  = colors.HexColor('#1A2A1F')
TEXT_MUTED    = colors.HexColor('#6B6B6B')

TABLE_HEADER_COLOR = HEADER_FILL
TABLE_HEADER_TEXT  = colors.white
TABLE_ROW_EVEN     = colors.white
TABLE_ROW_ODD      = TABLE_STRIPE

# Chart colors
CHART_CONTROL = colors.HexColor('#9C4942')
CHART_DPP40   = colors.HexColor('#887246')
CHART_DPP80   = colors.HexColor('#2D5016')


# ===================================================================
# PAGE LAYOUT
# ===================================================================
PAGE_W, PAGE_H = A4
LEFT_MARGIN   = 2.5 * cm
RIGHT_MARGIN  = 2.5 * cm
TOP_MARGIN    = 2.5 * cm
BOTTOM_MARGIN = 2.5 * cm
CONTENT_WIDTH = PAGE_W - LEFT_MARGIN - RIGHT_MARGIN

# ===================================================================
# PARAGRAPH STYLES
# ===================================================================
def make_styles():
    """Define all paragraph styles for the thesis."""
    styles = {}

    # Body text
    styles['Body'] = ParagraphStyle(
        name='Body', fontName='Tinos', fontSize=11, leading=16,
        textColor=TEXT_PRIMARY, alignment=TA_JUSTIFY,
        spaceBefore=2, spaceAfter=8, firstLineIndent=18
    )

    styles['BodyNoIndent'] = ParagraphStyle(
        name='BodyNoIndent', parent=styles['Body'], firstLineIndent=0
    )

    # Chapter title (large, centered)
    styles['ChapterTitle'] = ParagraphStyle(
        name='ChapterTitle', fontName='Tinos-Bold', fontSize=22, leading=28,
        textColor=HEADER_FILL, alignment=TA_CENTER,
        spaceBefore=0, spaceAfter=8
    )

    styles['ChapterNumber'] = ParagraphStyle(
        name='ChapterNumber', fontName='Carlito-Bold', fontSize=14, leading=18,
        textColor=ACCENT, alignment=TA_CENTER,
        spaceBefore=0, spaceAfter=4
    )

    styles['ChapterSubtitle'] = ParagraphStyle(
        name='ChapterSubtitle', fontName='Tinos-Italic', fontSize=12, leading=16,
        textColor=TEXT_MUTED, alignment=TA_CENTER,
        spaceBefore=4, spaceAfter=18
    )

    # Section heading (H1)
    styles['H1'] = ParagraphStyle(
        name='H1', fontName='Tinos-Bold', fontSize=15, leading=20,
        textColor=HEADER_FILL, alignment=TA_LEFT,
        spaceBefore=18, spaceAfter=8, keepWithNext=True
    )

    # Subsection (H2)
    styles['H2'] = ParagraphStyle(
        name='H2', fontName='Tinos-Bold', fontSize=12.5, leading=16,
        textColor=ACCENT, alignment=TA_LEFT,
        spaceBefore=12, spaceAfter=6, keepWithNext=True
    )

    # Sub-subsection (H3)
    styles['H3'] = ParagraphStyle(
        name='H3', fontName='Carlito-Bold', fontSize=11, leading=14,
        textColor=TEXT_PRIMARY, alignment=TA_LEFT,
        spaceBefore=8, spaceAfter=4, keepWithNext=True
    )

    # Results / Discussion sub-blocks
    styles['ResultsHead'] = ParagraphStyle(
        name='ResultsHead', fontName='Tinos-BoldItalic', fontSize=11, leading=14,
        textColor=HEADER_FILL, alignment=TA_LEFT,
        spaceBefore=10, spaceAfter=4, keepWithNext=True
    )

    styles['DiscussionHead'] = ParagraphStyle(
        name='DiscussionHead', fontName='Tinos-BoldItalic', fontSize=11, leading=14,
        textColor=ACCENT, alignment=TA_LEFT,
        spaceBefore=8, spaceAfter=4, keepWithNext=True
    )

    # Caption
    styles['Caption'] = ParagraphStyle(
        name='Caption', fontName='Carlito-Italic', fontSize=9, leading=12,
        textColor=TEXT_MUTED, alignment=TA_CENTER,
        spaceBefore=4, spaceAfter=12
    )

    styles['TableCaption'] = ParagraphStyle(
        name='TableCaption', fontName='Carlito-Bold', fontSize=9.5, leading=12,
        textColor=TEXT_PRIMARY, alignment=TA_LEFT,
        spaceBefore=10, spaceAfter=4, keepWithNext=True
    )

    # Front matter (title page)
    styles['FrontTitle'] = ParagraphStyle(
        name='FrontTitle', fontName='Tinos-Bold', fontSize=17, leading=22,
        textColor=TEXT_PRIMARY, alignment=TA_CENTER,
        spaceBefore=12, spaceAfter=8
    )

    styles['FrontSub'] = ParagraphStyle(
        name='FrontSub', fontName='Tinos-Italic', fontSize=12, leading=16,
        textColor=TEXT_MUTED, alignment=TA_CENTER,
        spaceBefore=4, spaceAfter=12
    )

    styles['FrontLabel'] = ParagraphStyle(
        name='FrontLabel', fontName='Carlito-Bold', fontSize=10, leading=13,
        textColor=ACCENT, alignment=TA_CENTER,
        spaceBefore=4, spaceAfter=4
    )

    styles['FrontBody'] = ParagraphStyle(
        name='FrontBody', fontName='Tinos', fontSize=11, leading=15,
        textColor=TEXT_PRIMARY, alignment=TA_JUSTIFY,
        spaceBefore=4, spaceAfter=8
    )

    # Abstract styles
    styles['AbstractTitle'] = ParagraphStyle(
        name='AbstractTitle', fontName='Tinos-Bold', fontSize=16, leading=20,
        textColor=HEADER_FILL, alignment=TA_CENTER,
        spaceBefore=0, spaceAfter=12
    )

    styles['AbstractBody'] = ParagraphStyle(
        name='AbstractBody', fontName='Tinos', fontSize=10.5, leading=15,
        textColor=TEXT_PRIMARY, alignment=TA_JUSTIFY,
        spaceBefore=2, spaceAfter=6, firstLineIndent=14
    )

    styles['Keywords'] = ParagraphStyle(
        name='Keywords', fontName='Tinos-Italic', fontSize=10, leading=13,
        textColor=TEXT_PRIMARY, alignment=TA_LEFT,
        spaceBefore=10, spaceAfter=6, leftIndent=0
    )

    # Arabic abstract (RTL)
    styles['ArabicTitle'] = ParagraphStyle(
        name='ArabicTitle', fontName='NotoArabic-Bold', fontSize=16, leading=22,
        textColor=HEADER_FILL, alignment=TA_CENTER,
        spaceBefore=0, spaceAfter=12
    )

    styles['ArabicBody'] = ParagraphStyle(
        name='ArabicBody', fontName='NotoArabic', fontSize=11, leading=18,
        textColor=TEXT_PRIMARY, alignment=TA_RIGHT,
        spaceBefore=2, spaceAfter=6
    )

    styles['ArabicKeywords'] = ParagraphStyle(
        name='ArabicKeywords', fontName='NotoArabic-Bold', fontSize=10.5, leading=15,
        textColor=TEXT_PRIMARY, alignment=TA_RIGHT,
        spaceBefore=10, spaceAfter=6
    )

    # TOC
    styles['TOCHeading'] = ParagraphStyle(
        name='TOCHeading', fontName='Tinos-Bold', fontSize=20, leading=24,
        textColor=HEADER_FILL, alignment=TA_CENTER,
        spaceBefore=0, spaceAfter=18
    )

    styles['TOCLevel0'] = ParagraphStyle(
        name='TOCLevel0', fontName='Tinos-Bold', fontSize=11.5, leading=18,
        textColor=TEXT_PRIMARY, alignment=TA_LEFT,
        leftIndent=0, spaceBefore=6, spaceAfter=2
    )

    styles['TOCLevel1'] = ParagraphStyle(
        name='TOCLevel1', fontName='Tinos', fontSize=10.5, leading=14,
        textColor=TEXT_PRIMARY, alignment=TA_LEFT,
        leftIndent=18, spaceBefore=1, spaceAfter=1
    )

    styles['TOCLevel2'] = ParagraphStyle(
        name='TOCLevel2', fontName='Tinos-Italic', fontSize=10, leading=13,
        textColor=TEXT_MUTED, alignment=TA_LEFT,
        leftIndent=36, spaceBefore=0, spaceAfter=0
    )

    # Reference list
    styles['Reference'] = ParagraphStyle(
        name='Reference', fontName='Tinos', fontSize=9.5, leading=13,
        textColor=TEXT_PRIMARY, alignment=TA_JUSTIFY,
        leftIndent=22, firstLineIndent=-22,
        spaceBefore=1, spaceAfter=4
    )

    # Quote / callout
    styles['Quote'] = ParagraphStyle(
        name='Quote', fontName='Tinos-Italic', fontSize=10.5, leading=15,
        textColor=TEXT_PRIMARY, alignment=TA_JUSTIFY,
        leftIndent=28, rightIndent=14,
        spaceBefore=8, spaceAfter=8, borderColor=ACCENT,
        borderWidth=0, borderPadding=4
    )

    # Bullet point
    styles['Bullet'] = ParagraphStyle(
        name='Bullet', fontName='Tinos', fontSize=11, leading=15,
        textColor=TEXT_PRIMARY, alignment=TA_LEFT,
        leftIndent=22, bulletIndent=10,
        spaceBefore=2, spaceAfter=2, bulletFontName='Carlito-Bold',
        firstLineIndent=0
    )

    styles['NumberedItem'] = ParagraphStyle(
        name='NumberedItem', fontName='Tinos', fontSize=11, leading=15,
        textColor=TEXT_PRIMARY, alignment=TA_JUSTIFY,
        leftIndent=24, firstLineIndent=-18,
        spaceBefore=3, spaceAfter=3
    )

    # Hypothesis
    styles['Hypothesis'] = ParagraphStyle(
        name='Hypothesis', fontName='Tinos', fontSize=10.5, leading=14,
        textColor=TEXT_PRIMARY, alignment=TA_JUSTIFY,
        leftIndent=24, firstLineIndent=-24,
        spaceBefore=4, spaceAfter=4
    )

    # Equation/formula
    styles['Formula'] = ParagraphStyle(
        name='Formula', fontName='Tinos-Italic', fontSize=11, leading=16,
        textColor=TEXT_PRIMARY, alignment=TA_CENTER,
        spaceBefore=6, spaceAfter=6
    )

    # Footer
    styles['Footer'] = ParagraphStyle(
        name='Footer', fontName='Carlito', fontSize=8, leading=10,
        textColor=TEXT_MUTED, alignment=TA_CENTER
    )

    # Cover info on first body page (title page duplicate)
    styles['TitlePageMain'] = ParagraphStyle(
        name='TitlePageMain', fontName='Tinos-Bold', fontSize=18, leading=24,
        textColor=TEXT_PRIMARY, alignment=TA_CENTER,
        spaceBefore=20, spaceAfter=10
    )

    return styles


# ===================================================================
# HELPER: Bookmarking headings for TOC
# ===================================================================
def add_heading(text, style, level=0, story=None):
    """Add a heading paragraph with TOC bookmark."""
    key = f'h_{hashlib.md5(text.encode()).hexdigest()[:10]}'
    p = Paragraph(f'<a name="{key}"/>{text}', style)
    p.bookmark_name = key
    p.bookmark_level = level
    p.bookmark_text = text
    p.bookmark_key = key
    return p


# ===================================================================
# HELPER: Arabic text shaping
# ===================================================================
def ar(text):
    """Reshape Arabic text for proper RTL display in ReportLab.
    Converts Latin digits to Arabic-Indic digits.
    Removes problematic ASCII chars (quotes, hyphens) that cause NULL markers."""
    # Convert Latin digits to Arabic-Indic digits before shaping
    arabic_indic_digits = '٠١٢٣٤٥٦٧٨٩'
    text = ''.join(arabic_indic_digits[int(c)] if c.isdigit() and c in '0123456789' else c for c in text)
    # REMOVE all double and single quotes (NotoNaskhArabic lacks U+201C/U+201D/U+2018/U+2019 glyphs)
    text = text.replace('"', '').replace('"', '').replace('"', '')
    text = text.replace("'", '').replace("'", '').replace("'", '')
    text = text.replace('\u201c', '').replace('\u201d', '')
    text = text.replace('\u2018', '').replace('\u2019', '')
    # Replace ASCII hyphen with hyphen (font has U+2010)
    text = text.replace('-', '\u2010')
    # Replace ASCII colon with Arabic semicolon (font has U+061B but ASCII colon also works)
    # Actually keep ASCII colon - it's in the font

    reshaped = arabic_reshaper.reshape(text)
    displayed = get_display(reshaped)
    # Remove NULL characters (U+0000) that appear as tofu squares
    displayed = displayed.replace('\u0000', ' ')
    # Strip bidi control characters that the NotoArabic font lacks glyphs for
    # U+202A-U+202E (LRE, RLE, PDF, LRO, RLO) and U+2066-U+2069 (LRI, RLI, FSI, PDI)
    bidi_controls = '\u202a\u202b\u202c\u202d\u202e\u2066\u2067\u2068\u2069'
    displayed = ''.join(c for c in displayed if c not in bidi_controls)
    # Also remove any other control characters
    import re
    displayed = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', displayed)
    return displayed


# ===================================================================
# PAGE HEADER & FOOTER
# ===================================================================
def draw_header_footer(canv, doc):
    """Draw page header and footer on each body page."""
    canv.saveState()

    # Header line (top)
    canv.setStrokeColor(BORDER)
    canv.setLineWidth(0.5)
    canv.line(LEFT_MARGIN, PAGE_H - 1.6*cm,
              PAGE_W - RIGHT_MARGIN, PAGE_H - 1.6*cm)

    # Header text - thesis short title
    canv.setFont('Carlito-Italic', 8.5)
    canv.setFillColor(TEXT_MUTED)
    canv.drawString(LEFT_MARGIN, PAGE_H - 1.4*cm,
                    'DPP for Post-Slaughter Ovine Epididymal Sperm Preservation')
    canv.drawRightString(PAGE_W - RIGHT_MARGIN, PAGE_H - 1.4*cm,
                         'PhD Thesis  |  2025-2026')

    # Footer line (bottom)
    canv.line(LEFT_MARGIN, 1.6*cm,
              PAGE_W - RIGHT_MARGIN, 1.6*cm)

    # Page number (footer center)
    page_num = canv.getPageNumber()
    canv.setFont('Carlito', 9)
    canv.setFillColor(TEXT_PRIMARY)
    canv.drawCentredString(PAGE_W / 2, 1.1*cm, f'— {page_num} —')

    # Footer text
    canv.setFont('Carlito-Italic', 8)
    canv.setFillColor(TEXT_MUTED)
    canv.drawString(LEFT_MARGIN, 1.1*cm, '[Candidate Name]')
    canv.drawRightString(PAGE_W - RIGHT_MARGIN, 1.1*cm,
                         '[University Name] — El Oued, Algeria')

    canv.restoreState()


def draw_chapter_separator(canv, doc):
    """Draw a chapter separator (no header/footer, just chapter title page treatment)."""
    canv.saveState()
    # Just a subtle bottom marker
    canv.setFont('Carlito', 8)
    canv.setFillColor(TEXT_MUTED)
    canv.drawCentredString(PAGE_W / 2, 1.0*cm, '— Chapter Separator —')
    canv.restoreState()


# ===================================================================
# CUSTOM DOCUMENT TEMPLATE
# ===================================================================
class ThesisDocTemplate(BaseDocTemplate):
    """Custom doc template with TOC support, multi-page templates."""

    def __init__(self, filename, **kwargs):
        BaseDocTemplate.__init__(self, filename, **kwargs)

        # Normal body page template (with header/footer)
        body_frame = Frame(
            LEFT_MARGIN, BOTTOM_MARGIN,
            CONTENT_WIDTH, PAGE_H - TOP_MARGIN - BOTTOM_MARGIN - 0.5*cm,
            id='body_frame', showBoundary=0
        )

        # Chapter separator template (minimal header/footer)
        sep_frame = Frame(
            LEFT_MARGIN, BOTTOM_MARGIN,
            CONTENT_WIDTH, PAGE_H - TOP_MARGIN - BOTTOM_MARGIN,
            id='sep_frame', showBoundary=0
        )

        # Title page template (no header/footer)
        title_frame = Frame(
            LEFT_MARGIN, BOTTOM_MARGIN,
            CONTENT_WIDTH, PAGE_H - TOP_MARGIN - BOTTOM_MARGIN,
            id='title_frame', showBoundary=0
        )

        self.addPageTemplates([
            PageTemplate(id='TitlePage', frames=[title_frame],
                         onPage=lambda c, d: None),
            PageTemplate(id='Body', frames=[body_frame],
                         onPage=draw_header_footer),
            PageTemplate(id='Separator', frames=[sep_frame],
                         onPage=draw_chapter_separator),
        ])

    def afterFlowable(self, flowable):
        """Capture TOC entries."""
        if hasattr(flowable, 'bookmark_name'):
            level = getattr(flowable, 'bookmark_level', 0)
            text = getattr(flowable, 'bookmark_text', '')
            key = getattr(flowable, 'bookmark_key', '')
            self.notify('TOCEntry', (level, text, self.page, key))


# ===================================================================
# FRONT MATTER BUILDERS
# ===================================================================
def build_title_page(story, styles):
    """Build a title page (body PDF's first page)."""
    story.append(NextPageTemplate('TitlePage'))
    story.append(Spacer(1, 1.5*cm))

    # Republic header
    story.append(Paragraph(
        "<b>PEOPLE'S DEMOCRATIC REPUBLIC OF ALGERIA</b>",
        ParagraphStyle('rp', fontName='Tinos-Bold', fontSize=12, alignment=TA_CENTER,
                       textColor=TEXT_PRIMARY, spaceAfter=2)
    ))
    story.append(Paragraph(
        "<i>République Algérienne Démocratique et Populaire</i>",
        ParagraphStyle('rpf', fontName='Tinos-Italic', fontSize=11, alignment=TA_CENTER,
                       textColor=TEXT_MUTED, spaceAfter=14)
    ))
    story.append(Paragraph(
        "Ministry of Higher Education and Scientific Research",
        ParagraphStyle('min', fontName='Tinos', fontSize=10.5, alignment=TA_CENTER,
                       textColor=TEXT_PRIMARY, spaceAfter=4)
    ))
    story.append(Paragraph(
        "<b>[UNIVERSITY NAME]</b>",
        ParagraphStyle('uni', fontName='Tinos-Bold', fontSize=15, alignment=TA_CENTER,
                       textColor=HEADER_FILL, spaceAfter=2)
    ))
    story.append(Paragraph(
        "Faculty of [Natural and Life Sciences]",
        ParagraphStyle('fac', fontName='Tinos', fontSize=11, alignment=TA_CENTER,
                       textColor=TEXT_PRIMARY, spaceAfter=1)
    ))
    story.append(Paragraph(
        "Department of [Agricultural Sciences / Biology]",
        ParagraphStyle('dep', fontName='Tinos', fontSize=10.5, alignment=TA_CENTER,
                       textColor=TEXT_PRIMARY, spaceAfter=1)
    ))
    story.append(Paragraph(
        "Laboratory of [Biodiversity and Conservation of Ecosystems]",
        ParagraphStyle('lab', fontName='Tinos-Italic', fontSize=10, alignment=TA_CENTER,
                       textColor=TEXT_MUTED, spaceAfter=18)
    ))

    # Divider
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.7],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.5, HEADER_FILL)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 12))

    story.append(Paragraph(
        "<b>THESIS</b>",
        ParagraphStyle('tt', fontName='Tinos-Bold', fontSize=14, alignment=TA_CENTER,
                       textColor=TEXT_PRIMARY, spaceAfter=2)
    ))
    story.append(Paragraph(
        "<i>Thèse de Doctorat en Sciences</i>",
        ParagraphStyle('ttf', fontName='Tinos-Italic', fontSize=11, alignment=TA_CENTER,
                       textColor=TEXT_MUTED, spaceAfter=14)
    ))

    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.5],
                       style=[('LINEABOVE', (0,0), (-1,-1), 0.7, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 16))

    story.append(Paragraph(
        "Submitted in partial fulfillment of the requirements<br/>"
        "for the degree of Doctor of Philosophy in Sciences",
        ParagraphStyle('tl', fontName='Carlito', fontSize=9.5, alignment=TA_CENTER,
                       textColor=TEXT_MUTED, spaceAfter=14)
    ))

    # Main title
    story.append(Paragraph(
        "Date Palm Pollen (<i>Phoenix dactylifera</i> L.) as a Natural "
        "Cryoprotective Agent for Post-Slaughter Ovine Epididymal Sperm "
        "Preservation: An Integrated Socio-Technical-Environmental "
        "Approach in Arid Algeria",
        styles['TitlePageMain']
    ))
    story.append(Paragraph(
        "<i>Pollen de Palmier Dattier (Phoenix dactylifera L.) comme Agent "
        "Cryoprotecteur Naturel pour la Préservation du Sperme Épididymaire "
        "Ovin Post-Abattage : Approche Socio-Technique-Environnementale "
        "Intégrée en Algérie Aride</i>",
        styles['FrontSub']
    ))
    story.append(Spacer(1, 12))

    # Fields
    field_data = [
        ['Candidate:', '[Candidate Full Name]'],
        ['Supervisor:', 'Pr. [Supervisor Full Name]'],
        ['Co-Supervisor:', 'Dr. [Co-supervisor Full Name]'],
    ]
    field_table = Table(field_data, colWidths=[3.5*cm, 9*cm], hAlign='CENTER')
    field_table.setStyle(TableStyle([
        ('FONT', (0,0), (0,-1), 'Tinos-Bold', 10.5),
        ('FONT', (1,0), (1,-1), 'Tinos-Italic', 10.5),
        ('TEXTCOLOR', (0,0), (0,-1), TEXT_PRIMARY),
        ('TEXTCOLOR', (1,0), (1,-1), TEXT_PRIMARY),
        ('LINEBELOW', (1,0), (1,-1), 0.4, BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (0,-1), 0),
        ('ALIGN', (0,0), (0,-1), 'LEFT'),
        ('ALIGN', (1,0), (1,-1), 'CENTER'),
    ]))
    story.append(field_table)
    story.append(Spacer(1, 16))

    # Jury
    story.append(Paragraph(
        "<b>MEMBERS OF THE EXAMINATION JURY</b>",
        ParagraphStyle('jh', fontName='Carlito-Bold', fontSize=10, alignment=TA_CENTER,
                       textColor=ACCENT, spaceAfter=6)
    ))
    jury_data = [
        ['Name & Affiliation', 'Role', 'Grade'],
        ['Pr. [President Name] — [University]', 'President', 'Professor'],
        ['Pr. [Supervisor Name] — [University]', 'Supervisor', 'Professor'],
        ['Dr. [Co-supervisor Name] — [University]', 'Co-Supervisor', 'MCB'],
        ['Pr. [Examiner 1 Name] — [University]', 'Examiner', 'Professor'],
        ['Dr. [Examiner 2 Name] — [University]', 'Examiner', 'MCB'],
        ['Dr. [Guest Name] — [University]', 'Invited', 'MCB'],
    ]
    jury_table = Table(jury_data, colWidths=[8*cm, 3*cm, 3*cm], hAlign='CENTER')
    jury_table.setStyle(TableStyle([
        ('FONT', (0,0), (-1,0), 'Carlito-Bold', 9),
        ('FONT', (0,1), (-1,-1), 'Tinos-Italic', 9),
        ('BACKGROUND', (0,0), (-1,0), HEADER_FILL),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('LINEABOVE', (0,0), (-1,0), 1.2, HEADER_FILL),
        ('LINEBELOW', (0,0), (-1,0), 1.2, HEADER_FILL),
        ('LINEBELOW', (0,-1), (-1,-1), 0.5, BORDER),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TEXTCOLOR', (0,1), (-1,-1), TEXT_PRIMARY),
    ]))
    story.append(jury_table)
    story.append(Spacer(1, 18))

    story.append(Paragraph(
        "<b>Academic Year 2025 – 2026</b>",
        ParagraphStyle('dy', fontName='Tinos-Bold', fontSize=11, alignment=TA_CENTER,
                       textColor=TEXT_PRIMARY, spaceAfter=2)
    ))
    story.append(Paragraph(
        "<i>Année Universitaire 2025 – 2026</i>",
        ParagraphStyle('dyf', fontName='Tinos-Italic', fontSize=9.5, alignment=TA_CENTER,
                       textColor=TEXT_MUTED)
    ))

    story.append(NextPageTemplate('Body'))
    story.append(PageBreak())


def build_declaration(story, styles):
    """Declaration of Originality."""
    story.append(Paragraph(
        "DECLARATION OF ORIGINALITY",
        styles['AbstractTitle']
    ))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 18))

    story.append(Paragraph(
        "I, the undersigned, <b>[Candidate Full Name]</b>, hereby declare that this thesis "
        "entitled <i>\"Date Palm Pollen (Phoenix dactylifera L.) as a Natural Cryoprotective "
        "Agent for Post-Slaughter Ovine Epididymal Sperm Preservation: An Integrated "
        "Socio-Technical-Environmental Approach in Arid Algeria\"</i> is my own original work "
        "carried out under the supervision of <b>Pr. [Supervisor Full Name]</b> and "
        "<b>Dr. [Co-supervisor Full Name]</b>. To the best of my knowledge and belief, "
        "this thesis contains no material previously published or written by another person, "
        "nor material which has been accepted for the award of any other degree or diploma "
        "of a university or other institution of higher learning, except where due "
        "acknowledgment has been made in the text.",
        styles['FrontBody']
    ))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "All sources of information, data, and ideas derived from the work of others "
        "have been properly cited in accordance with academic conventions. The experimental "
        "work was conducted in accordance with the ethical standards of the institutional "
        "research committee and with the 1964 Helsinki Declaration and its later amendments, "
        "as well as the principles of post-mortem tissue collection from a licensed "
        "abattoir facility.",
        styles['FrontBody']
    ))
    story.append(Spacer(1, 18))

    story.append(Paragraph(
        "Signed: __________________________________",
        ParagraphStyle('sig', fontName='Tinos', fontSize=11, alignment=TA_LEFT,
                       textColor=TEXT_PRIMARY, leftIndent=80)
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "Date: ___________________________________",
        ParagraphStyle('sig2', fontName='Tinos', fontSize=11, alignment=TA_LEFT,
                       textColor=TEXT_PRIMARY, leftIndent=80)
    ))
    story.append(Spacer(1, 18))
    story.append(Paragraph(
        "<b>Candidate:</b> [Candidate Full Name]<br/>"
        "<b>Institution:</b> [University Name], [Faculty], [Department]<br/>"
        "<b>Date of submission:</b> [Month, Year]",
        styles['FrontBody']
    ))

    story.append(Spacer(1, 24))

    # French version
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.0, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "DÉCLARATION D'ORIGINALITÉ",
        styles['AbstractTitle']
    ))
    story.append(Paragraph(
        "Je soussigné(e), <b>[Nom Complet du Candidat]</b>, déclare par la présente que "
        "cette thèse intitulée <i>« Pollen de Palmier Dattier (Phoenix dactylifera L.) "
        "comme Agent Cryoprotecteur Naturel pour la Préservation du Sperme Épididymaire "
        "Ovin Post-Abattage : Approche Socio-Technique-Environnementale Intégrée en "
        "Algérie Aride »</i> est mon propre travail original, réalisé sous la direction "
        "de <b>Pr. [Nom du Directeur]</b> et <b>Dr. [Nom du Co-directeur]</b>. À ma "
        "connaissance, cette thèse ne contient aucun matériel précédemment publié ou "
        "rédigé par une autre personne, ni aucun matériel ayant été accepté pour "
        "l'obtention d'un autre diplôme, sauf mention explicite dans le texte.",
        styles['FrontBody']
    ))

    story.append(PageBreak())


def build_dedication(story, styles):
    """Dedication page."""
    story.append(Spacer(1, 4*cm))
    story.append(Paragraph(
        "Dedication",
        styles['AbstractTitle']
    ))
    story.append(Spacer(1, 24))
    story.append(Paragraph(
        "<i>To my beloved family, whose unwavering support, patience, and sacrifices "
        "have made this academic journey possible.</i>",
        ParagraphStyle('ded', fontName='Tinos-Italic', fontSize=13, leading=18,
                       textColor=TEXT_PRIMARY, alignment=TA_CENTER,
                       leftIndent=60, rightIndent=60)
    ))
    story.append(Spacer(1, 18))
    story.append(Paragraph(
        "<i>To the memory of the indigenous Ouled Djellal sheep breed — a living "
        "testament to the genetic heritage of Algeria's arid lands, whose preservation "
        "inspired this work.</i>",
        ParagraphStyle('ded2', fontName='Tinos-Italic', fontSize=12, leading=17,
                       textColor=TEXT_MUTED, alignment=TA_CENTER,
                       leftIndent=60, rightIndent=60)
    ))
    story.append(Spacer(1, 18))
    story.append(Paragraph(
        "<i>To the sheep keepers of El Oued, whose ancestral knowledge and dedication "
        "to their flocks embody the spirit of sustainable stewardship.</i>",
        ParagraphStyle('ded3', fontName='Tinos-Italic', fontSize=12, leading=17,
                       textColor=TEXT_MUTED, alignment=TA_CENTER,
                       leftIndent=60, rightIndent=60)
    ))
    story.append(PageBreak())


def build_acknowledgments(story, styles):
    """Acknowledgments page."""
    story.append(Paragraph(
        "Acknowledgments",
        styles['AbstractTitle']
    ))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 14))

    story.append(Paragraph(
        "The completion of this doctoral thesis would not have been possible without "
        "the generous contributions, guidance, and support of numerous individuals and "
        "institutions to whom I owe my deepest gratitude.",
        styles['FrontBody']
    ))
    story.append(Spacer(1, 8))

    story.append(Paragraph(
        "<b>Supervisors.</b> My profound gratitude goes first to my thesis supervisor, "
        "<b>Pr. [Supervisor Full Name]</b>, whose scholarly insight, methodological "
        "rigor, and unwavering patience have shaped every stage of this research. "
        "His/Her commitment to scientific excellence has been both an intellectual "
        "guide and a personal inspiration. I extend equal appreciation to my "
        "co-supervisor, <b>Dr. [Co-supervisor Full Name]</b>, whose expertise in "
        "[specialization] and meticulous feedback on experimental design, data "
        "interpretation, and manuscript revision proved invaluable throughout the "
        "investigation.",
        styles['FrontBody']
    ))

    story.append(Paragraph(
        "<b>Jury members.</b> I am honored to acknowledge the members of the "
        "examination jury — <b>Pr. [President Name]</b>, <b>Pr. [Examiner 1 Name]</b>, "
        "<b>Dr. [Examiner 2 Name]</b>, and <b>Dr. [Guest Name]</b> — for accepting "
        "to evaluate this work. Their critical insights and constructive suggestions "
        "have substantially strengthened the final manuscript.",
        styles['FrontBody']
    ))

    story.append(Paragraph(
        "<b>Institutional support.</b> I thank <b>[University Name]</b>, the "
        "<b>Faculty of [Natural and Life Sciences]</b>, and the <b>Department of "
        "[Agricultural Sciences]</b> for providing the academic framework and "
        "infrastructural support that enabled this research. The <b>Laboratory of "
        "[Biodiversity and Conservation of Ecosystems]</b> provided access to "
        "essential analytical equipment and a collegial research environment. "
        "I gratefully acknowledge the Director and staff of the <b>licensed abattoir "
        "of El Oued</b> for granting access to biological material and facilitating "
        "post-slaughter sample collection under hygienic conditions.",
        styles['FrontBody']
    ))

    story.append(Paragraph(
        "<b>Field collaborators.</b> This research would have been impossible without "
        "the willing participation of the <b>200 sheep keepers across the eight "
        "municipalities of El Oued</b> — El Oued, Debila, Guemar, Hassi Khelifa, "
        "Mih Ouensa, Ourmes, Robbah, and Taleb Larbi — who generously shared their "
        "knowledge, time, and flocks with the research team. Their hospitality and "
        "willingness to engage with scientific inquiry represent the human foundation "
        "of this thesis. I also thank the agricultural extension agents of Hamraia "
        "and Reguiba who facilitated access to date palm pollen collection sites and "
        "shared their traditional knowledge of palm cultivation.",
        styles['FrontBody']
    ))

    story.append(Paragraph(
        "<b>Laboratory teams.</b> I am grateful to the technical staff of the "
        "biochemistry, phytochemistry, and reproductive biology laboratories for "
        "their assistance with proximate analysis, mineral determination, DPPH "
        "assays, CASA motility assessment, and HOST membrane integrity evaluation. "
        "Particular thanks are due to [Laboratory Technician Name(s)] for their "
        "meticulous technical support and patience with repeated measurements.",
        styles['FrontBody']
    ))

    story.append(Paragraph(
        "<b>Funding.</b> This research was supported by [funding agency / Ministry "
        "of Higher Education and Scientific Research of Algeria / PRFU project "
        "code, if applicable]. The financial support is gratefully acknowledged, "
        "as is the in-kind contribution of laboratory consumables from "
        "[University / Laboratory].",
        styles['FrontBody']
    ))

    story.append(Paragraph(
        "<b>Personal.</b> Finally, I owe an immeasurable debt of gratitude to my "
        "family — my parents, spouse, and children — whose patience, encouragement, "
        "and sacrifices sustained me through the long hours of fieldwork, "
        "laboratory analysis, and manuscript writing. To my friends and fellow "
        "doctoral students who walked alongside me in this journey, your "
        "camaraderie made the difficult moments bearable and the joyful moments "
        "more meaningful.",
        styles['FrontBody']
    ))

    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "<i>To all those I may have inadvertently failed to mention by name, "
        "please accept my sincere appreciation. Any errors or omissions in this "
        "thesis remain my own responsibility.</i>",
        styles['FrontBody']
    ))

    story.append(Spacer(1, 18))
    story.append(Paragraph(
        "<b>[Candidate Full Name]</b><br/>"
        "El Oued, Algeria<br/>"
        "[Month, Year]",
        ParagraphStyle('ack', fontName='Tinos-Italic', fontSize=10.5, alignment=TA_RIGHT,
                       textColor=TEXT_MUTED)
    ))

    story.append(PageBreak())


# ===================================================================
# MULTILINGUAL ABSTRACTS
# ===================================================================
def build_abstract_english(story, styles):
    """English abstract."""
    story.append(Paragraph("Abstract", styles['AbstractTitle']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 12))

    abstract_paragraphs = [
        "<b>Background.</b> The genetic diversity of sheep (Ovis aries L.) — over 1,300 "
        "breeds globally, of which approximately 27% are endangered — underpins food "
        "security and pastoral resilience in the face of accelerating climate change. "
        "In Algeria's arid zones, valuable ovine genotypes such as the Ouled Djellal "
        "breed are at risk of unrecorded loss when genetically elite rams die unexpectedly, "
        "because conventional cryobanking infrastructure relies on elective semen "
        "collection from live animals. Post-slaughter recovery of cauda epididymal "
        "spermatozoa offers a critical genetic rescue pathway, but its efficacy is "
        "constrained by oxidative deterioration during the narrow post-mortem \"golden hour\" "
        "window. Conventional single-mechanism antioxidants (TROLOX, cysteine) systematically "
        "fail to address the multi-source reactive oxygen species (ROS) generation "
        "characteristic of post-mortem cellular deterioration.",

        "<b>Objectives.</b> This thesis investigated whether Date Palm Pollen (DPP, "
        "Phoenix dactylifera L.) — a complex botanical matrix of polyphenols, fatty "
        "acids, minerals, and vitamins traditionally available in the Algerian Sahara "
        "— could serve as a field-deployable, low-cost conservative agent for "
        "post-slaughter ovine epididymal sperm. Four interconnected experiments were "
        "designed to (i) characterize the socioeconomic context and trait preferences "
        "of 200 sheep keepers in El Oued; (ii) biochemically characterize local DPP "
        "(proximate, mineral, phenolic, flavonoid, DPPH antioxidant capacity); "
        "(iii) evaluate the dose-dependent efficacy of aqueous DPP extenders (DPPE-0, "
        "DPPE-40, DPPE-80 mg/mL) on chilled-storage (4°C, 48 h) sperm quality; and "
        "(iv) quantify climate-change perceptions and their linkage to perceived "
        "fertility declines among keepers.",

        "<b>Materials and Methods.</b> A stratified random sample of 200 sheep keepers "
        "across eight municipalities of El Oued was surveyed via semi-structured "
        "questionnaires. DPP collected from Hamraia was characterized using AOAC (2019) "
        "proximate methods, flame photometry, Folin-Ciocalteu phenolic assay, and "
        "DPPH radical scavenging assay. Post-slaughter epididymal sperm from five "
        "sexually mature rams was recovered by retrograde flushing, diluted 1:1 in "
        "DPPE extenders, and stored at 4°C under mineral oil. Total motility, "
        "progressive motility (CASA), and membrane integrity (HOST) were assessed at "
        "0, 24, and 48 h. Statistical analyses included MANOVA (Experiment 1), "
        "two-way repeated-measures ANOVA (Experiment 3), and binary logistic regression "
        "(Experiment 4), with significance set at α = 0.05.",

        "<b>Results.</b> The socioeconomic survey revealed a male-dominated (100%), "
        "aging keeper population (only 11% under 25 years) with small-to-medium flocks "
        "(79.5% < 50 head), prioritizing breed identity (27% for rams) and drought "
        "tolerance (16% for ewes) over rapid growth — a significant three-way "
        "interaction (Pillai's Trace = 0.070, p = 0.009, η² = 0.070). Local DPP "
        "exhibited a nutrient-dense profile (protein 37.94%, carbohydrates 30.12%, "
        "potassium 1140 mg/100 g) with moderate antioxidant capacity (IC₅₀ = 624.25 "
        "µg/mL). DPPE-80 significantly preserved total motility (67.5% vs. 58.3% "
        "control), progressive motility (54.7% vs. 45.5%), and membrane integrity "
        "(63.9% vs. 55.1%) after 48 h (p < 0.05, η² > 0.20), confirming dose-dependent "
        "protection. Climate perception data showed near-universal recognition (95%) "
        "of climate-fertility relationships, with nutritional stress cited as the "
        "primary stressor (48.9%); medium-sized flocks (20-50 head) emerged as the "
        "vulnerability sweet spot (OR = 24.86, p = 0.004).",

        "<b>Conclusion.</b> This thesis establishes that aqueous Date Palm Pollen "
        "extender at 80 mg/mL provides a validated, field-deployable protocol for "
        "post-slaughter ovine genetic rescue, extending the practical preservation "
        "window from <24 h to >48 h. By integrating socioeconomic priorities, "
        "biochemical characterization, technical efficacy, and climate-change urgency "
        "into a triangulated conservation model, the research advances both theory "
        "(Agro-Ecological Cryobiology) and practice (community-based cryobanking). "
        "The DPPE protocol offers a culturally appropriate, low-cost intervention "
        "for safeguarding ovine genetic resources in arid Algeria and comparable "
        "pastoral systems globally.",
    ]
    for para in abstract_paragraphs:
        story.append(Paragraph(para, styles['AbstractBody']))

    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "<b>Keywords:</b> Date palm pollen; Ovine epididymal sperm; Post-slaughter "
        "recovery; Genetic conservation; Cryoprotection; Antioxidant; Chilled storage; "
        "El Oued; Algeria; Climate change; Ouled Djellal sheep; Socio-technical model.",
        styles['Keywords']
    ))

    story.append(PageBreak())


def build_abstract_french(story, styles):
    """French résumé."""
    story.append(Paragraph("Résumé", styles['AbstractTitle']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 12))

    paragraphs = [
        "<b>Contexte.</b> La diversité génétique des ovins (Ovis aries L.) — plus de "
        "1 300 races dans le monde, dont environ 27 % sont menacées — constitue le "
        "fondement de la sécurité alimentaire et de la résilience pastorale face au "
        "changement climatique accéléré. Dans les zones arides d'Algérie, des "
        "génotypes ovins précieux tels que la race Ouled Djellal sont exposés à une "
        "perte non documentée lorsque des béliers génétiquement supérieurs meurent "
        "de manière inattendue, car l'infrastructure conventionnelle de cryoconservation "
        "s'appuie sur la collecte élective de semence provenant d'animaux vivants. "
        "La récupération post-abattage des spermatozoïdes épididymaires caudaux offre "
        "une voie critique de sauvetage génétique, mais son efficacité est limitée par "
        "la détérioration oxydative pendant la fenêtre étroite de l'« heure dorée » "
        "post-mortem. Les antioxydants conventionnels à mécanisme unique (TROLOX, "
        "cystéine) échouent systématiquement à traiter la génération multi-source "
        "d'espèces réactives de l'oxygène (ROS) caractéristique de la détérioration "
        "cellulaire post-mortem.",

        "<b>Objectifs.</b> Cette thèse a examiné si le pollen de palmier dattier (DPP, "
        "Phoenix dactylifera L.) — une matrice botanique complexe de polyphénols, "
        "d'acides gras, de minéraux et de vitamines traditionnellement disponible "
        "dans le Sahara algérien — pouvait servir d'agent conservateur déployable "
        "sur le terrain et à faible coût pour le sperme épididymaire ovin post-abattage. "
        "Quatre expériences interconnectées ont été conçues pour (i) caractériser le "
        "contexte socioéconomique et les préférences de traits de 200 éleveurs ovins "
        "à El Oued ; (ii) caractériser biochimiquement le DPP local (composition "
        "proximale, minérale, phénolique, flavonoïque et capacité antioxydante DPPH) ; "
        "(iii) évaluer l'efficacité dose-dépendante des extendeurs aqueux de DPP "
        "(DPPE-0, DPPE-40, DPPE-80 mg/mL) sur la qualité du sperme en stockage "
        "réfrigéré (4 °C, 48 h) ; et (iv) quantifier les perceptions du changement "
        "climatique et leur lien avec les déclins de fertilité perçus.",

        "<b>Matériel et méthodes.</b> Un échantillon aléatoire stratifié de 200 "
        "éleveurs ovins à travers huit communes d'El Oued a été enquêté via des "
        "questionnaires semi-structurés. Le DPP collecté à Hamraia a été caractérisé "
        "en utilisant les méthodes proximales AOAC (2019), la photométrie de flamme, "
        "le dosage phénolique Folin-Ciocalteu et le test de piégeage du radical DPPH. "
        "Le sperme épididymaire post-abattage de cinq béliers sexuellement matures a "
        "été récupéré par rinçage rétrograde, dilué 1:1 dans les extendeurs DPPE, et "
        "stocké à 4 °C sous huile minérale. La motilité totale, la motilité "
        "progressive (CASA) et l'intégrité membranaire (HOST) ont été évaluées à 0, "
        "24 et 48 h. Les analyses statistiques comprenaient MANOVA (Expérience 1), "
        "ANOVA à mesures répétées à deux facteurs (Expérience 3) et régression "
        "logistique binaire (Expérience 4), avec seuil de signification α = 0,05.",

        "<b>Résultats.</b> L'enquête socioéconomique a révélé une population d'éleveurs "
        "dominée par les hommes (100 %), vieillissante (seulement 11 % de moins de "
        "25 ans) avec des troupeaux petits à moyens (79,5 % < 50 têtes), privilégiant "
        "l'identité de race (27 % pour les béliers) et la tolérance à la sécheresse "
        "(16 % pour les brebis) — une interaction tripartite significative (Trace de "
        "Pillai = 0,070, p = 0,009, η² = 0,070). Le DPP local présentait un profil "
        "riche en nutriments (protéines 37,94 %, glucides 30,12 %, potassium "
        "1 140 mg/100 g) avec une capacité antioxydante modérée (IC₅₀ = 624,25 µg/mL). "
        "Le DPPE-80 a significativement préservé la motilité totale (67,5 % vs 58,3 % "
        "témoin), la motilité progressive (54,7 % vs 45,5 %) et l'intégrité membranaire "
        "(63,9 % vs 55,1 %) après 48 h (p < 0,05, η² > 0,20). Les données de perception "
        "climatique ont montré une reconnaissance quasi-universelle (95 %) des relations "
        "climat-fertilité, les troupeaux moyens (20-50 têtes) émergeant comme point "
        "critique de vulnérabilité (OR = 24,86, p = 0,004).",

        "<b>Conclusion.</b> Cette thèse établit que l'extendeur aqueux de pollen de "
        "palmier dattier à 80 mg/mL fournit un protocole validé et déployable sur le "
        "terrain pour le sauvetage génétique ovin post-abattage, étendant la fenêtre "
        "pratique de préservation de <24 h à >48 h. En intégrant les priorités "
        "socioéconomiques, la caractérisation biochimique, l'efficacité technique et "
        "l'urgence climatique dans un modèle de conservation triangulé, la recherche "
        "fait progresser à la fois la théorie (cryobiologie agro-écologique) et la "
        "pratique (cryoconservation communautaire).",
    ]
    for para in paragraphs:
        story.append(Paragraph(para, styles['AbstractBody']))

    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "<b>Mots-clés :</b> Pollen de palmier dattier ; Sperme épididymaire ovin ; "
        "Récupération post-abattage ; Conservation génétique ; Cryoprotection ; "
        "Antioxydant ; Conservation réfrigérée ; El Oued ; Algérie ; Changement "
        "climatique ; Race Ouled Djellal ; Modèle socio-technique.",
        styles['Keywords']
    ))

    story.append(PageBreak())


def build_abstract_arabic(story, styles):
    """Arabic abstract — RTL with proper shaping."""
    story.append(Paragraph(ar("ملخص"), styles['ArabicTitle']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 12))

    # Arabic abstract paragraphs
    paragraphs_ar = [
        "الخلفية: يُعد التنوع الجيني للأغنام (Ovis aries L.) — بأكثر من 1300 سلالة في العالم، منها حوالي 27% مهددة بالانقراض — الركيزة الأساسية للأمن الغذائي ومرونة الرعي في مواجهة تغير المناخ المتسارع. وفي المناطق القاحلة بالجزائر، تواجه الأنماط الجينية القيّمة كالأغنام أولاد جلال خطر الفقد غير الموثّق عندما تنفق الكباش الوراثية المتميزة بشكل غير متوقع، لأن البنية التحتية التقليدية للحفظ بالتجميد تعتمد على جمع السائل المنوي اختياريًا من الحيوانات الحية. إن استرجاع النطاف البربخية الذيلية بعد الذبح يوفر مسارًا حاسمًا لإنقاذ الجينات، لكن فعاليته مقيدة بالتدهور التأكسدي خلال نافذة \"الساعة الذهبية\" الضيقة بعد الوفاة.",

        "الأهداف: بحثت هذه الأطروحة في ما إذا كان غبار طلع نخيل التمر (Phoenix dactylifera L.) — وهو مصفوفة نباتية معقدة من متعددات الفينول والأحماض الدهنية والمعادن والفيتامينات، متوفرة تقليديًا في الصحراء الجزائرية — يمكن أن يعمل كعامل حافظ ميداني منخفض التكلفة للنطاف البربخية للأغنام بعد الذبح. صُممت أربع تجارب مترابطة لـ: (1) توصيف السياق الاجتماعي والاقتصادي وتفضيلات السمات لدى 200 مربي أغنام في الوادي؛ (2) التوصيف الكيميائي الحيوي لغبار الطلع المحلي؛ (3) تقييم الفعالية المعتمدة على الجرعة لمستخلصات غبار الطلع المائية على جودة النطاف المخزنة على البرد (4°م، 48 ساعة)؛ (4) تحديد تصورات تغير المناخ وارتباطها بانخفاض الخصوبة المُلاحَظ.",

        "المواد والطرق: تم مسح عينة عشوائية طبقية مكونة من 200 مربي أغنام عبر ثماني بلديات في الوادي باستخدام استبيانات شبه منظمة. تم توصيف غبار الطلع المجموع من الحمرايا باستخدام طرق AOAC (2019) التقريبية، قياس الطيف اللهبي، اختبار الفينول Folin-Ciocalteu، واختبار DPPH الكسحي للجذور. تم استرجاع النطاف البربخية بعد الذبح من خمسة كباش ناضجة جنسيًا عن طريق الغسل الرجوعي، وتم تخفيفها 1:1 في مستخلصات غبار الطلع، وتخزينها عند 4°م تحت الزيوت المعدنية. تم تقييم الحركة الكلية والحركة التقدمية (CASA) وسلامة الغشاء (HOST) عند 0 و24 و48 ساعة. شملت التحليلات الإحصائية MANOVA وANOVA متكررة القياس ثنائية الاتجاه والانحدار اللوجستي الثنائي.",

        "النتائج: كشف المسح الاجتماعي والاقتصادي عن مجموعة من المربين يهيمن عليها الذكور (100%)، وشيخوخة السكان (11% فقط تحت 25 سنة) مع قطعان صغيرة إلى متوسطة (79.5% < 50 رأسًا)، مع إعطاء الأولوية لهوية السلالة (27% للكباش) وتحمل الجفاف (16% للنعاج) — تفاعل ثلاثي معنوي (أثر بيلاي = 0.070، p = 0.009، η² = 0.070). أظهر غبار الطلع المحلي ملفًا غذائيًا غنيًا (بروتين 37.94%، كربوهيدرات 30.12%، بوتاسيوم 1140 ملغ/100غ) مع قدرة مضادات أكسدة معتدلة (IC₅₀ = 624.25 ميكروغرام/مل). حافظ DPPE-80 بشكل معنوي على الحركة الكلية (67.5% مقابل 58.3% للشاهد)، الحركة التقدمية (54.7% مقابل 45.5%)، وسلامة الغشاء (63.9% مقابل 55.1%) بعد 48 ساعة (p < 0.05، η² > 0.20). أظهرت بيانات الإدراك المناخي اعترافًا شبه عالمي (95%) بعلاقات المناخ-الخصوبة، مع ظهور القطعان المتوسطة (20-50 رأسًا) كنقطة ضعف حرجة (OR = 24.86، p = 0.004).",

        "الخلاصة: تُثبت هذه الأطروحة أن مستخلص غبار طلع نخيل التمر المائي بتركيز 80 ملغ/مل يوفر بروتوكولًا مُتحقَّقًا منه وقابلًا للتطبيق ميدانيًا لإنقاذ الجينات الأغنامية بعد الذبح، مما يمد نافذة الحفظ العملي من <24 ساعة إلى >48 ساعة. ومن خلال دمج الأولويات الاجتماعية والاقتصادية، والتوصيف الكيميائي الحيوي، والفعالية التقنية، والإلحاح المناخي في نموذج حفظ مثلث، تُقدم البحث مساهمة نظرية (علم التبريد البيئي الزراعي) وعملية (الحفظ بالتجميد المجتمعي).",
    ]
    for para in paragraphs_ar:
        # Reshape each paragraph for proper Arabic rendering
        story.append(Paragraph(ar(para), styles['ArabicBody']))

    story.append(Spacer(1, 8))
    story.append(Paragraph(
        ar("<b>الكلمات المفتاحية:</b> غبار طلع نخيل التمر؛ النطاف البربخية للأغنام؛ الاسترجاع بعد الذبح؛ الحفظ الجيني؛ الحماية بالتجميد؛ مضادات الأكسدة؛ الحفظ المبرد؛ الوادي؛ الجزائر؛ تغير المناخ؛ سلالة أولاد جلال؛ النموذج الاجتماعي التقني."),
        styles['ArabicKeywords']
    ))

    story.append(PageBreak())


# ===================================================================
# TOC AND LISTS
# ===================================================================
def build_toc(story, styles):
    """Build table of contents."""
    story.append(Paragraph("Table of Contents", styles['TOCHeading']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 14))

    toc = TableOfContents()
    toc.levelStyles = [styles['TOCLevel0'], styles['TOCLevel1'], styles['TOCLevel2']]
    story.append(toc)
    story.append(PageBreak())


def build_list_of_tables(story, styles):
    """Build list of tables."""
    story.append(Paragraph("List of Tables", styles['TOCHeading']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 14))

    # Manual list (will be added as we build chapters)
    tables_list = [
        ("Table 1.1", "Research questions, objectives, hypotheses, and corresponding experiments"),
        ("Table 2.1", "Global status of sheep genetic diversity and conservation priorities"),
        ("Table 2.2", "Comparative composition of conventional antioxidants and their limitations"),
        ("Table 2.3", "Reported bioactive compounds in Date Palm Pollen across regions"),
        ("Table 2.4", "Cross-species evidence for DPP supplementation in reproduction"),
        ("Table 2.5", "Summary of climate change impacts on small ruminant fertility"),
        ("Table 3.1", "Integration of the four experiments and their data flow"),
        ("Table 3.2", "Proximate analysis methods and standards used for DPP characterization"),
        ("Table 3.3", "Mineral analysis methods and reference standards"),
        ("Table 3.4", "DPPE treatment groups and final concentrations"),
        ("Table 3.5", "CASA settings and parameters for ovine sperm analysis"),
        ("Table 4.1", "Socio-demographic profile of surveyed sheep keepers (n = 200)"),
        ("Table 4.2", "Flock size distribution and production system characteristics"),
        ("Table 4.3", "Trait preferences for breeding rams and ewes (% of keepers)"),
        ("Table 4.4", "MANOVA results: effects of education, experience, and occupation on trait priorities"),
        ("Table 4.5", "Proximate composition of El Oued DPP (mean ± SD, triplicate)"),
        ("Table 4.6", "Mineral content of El Oued DPP (mg/100 g, mean ± SD)"),
        ("Table 4.7", "Phenolic and flavonoid content of DPP extract"),
        ("Table 4.8", "DPPH radical scavenging activity and IC₅₀ of DPP vs. ascorbic acid"),
        ("Table 4.9", "Effect of DPPE treatment on total motility across storage time"),
        ("Table 4.10", "Effect of DPPE treatment on progressive motility across storage time"),
        ("Table 4.11", "Effect of DPPE treatment on membrane integrity (HOST) across storage time"),
        ("Table 4.12", "Two-way RM-ANOVA results for sperm quality parameters"),
        ("Table 4.13", "Climate-fertility awareness and stressor distribution among keepers"),
        ("Table 4.14", "Binary logistic regression: predictors of perceived fertility decline"),
        ("Table 5.1", "Summary of empirical findings aligned to research questions"),
        ("Table 5.2", "S.M.A.R.T. recommendations for stakeholders"),
    ]
    for tnum, ttitle in tables_list:
        story.append(Paragraph(
            f"<b>{tnum}.</b> {ttitle}",
            ParagraphStyle('lot', fontName='Tinos', fontSize=10, leading=14,
                           textColor=TEXT_PRIMARY, alignment=TA_LEFT,
                           leftIndent=14, firstLineIndent=-14,
                           spaceBefore=2, spaceAfter=2)
        ))

    story.append(PageBreak())


def build_list_of_figures(story, styles):
    """Build list of figures."""
    story.append(Paragraph("List of Figures", styles['TOCHeading']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 14))

    figures_list = [
        ("Figure 2.1", "Post-mortem biochemical cascade in epididymal sperm and the intervention window"),
        ("Figure 2.2", "Multi-target antioxidant mechanisms of Date Palm Pollen bioactive compounds"),
        ("Figure 2.3", "Conceptual framework integrating socioeconomic, technical, and environmental dimensions"),
        ("Figure 3.1", "Study area map: El Oued region showing eight municipalities and DPP collection site"),
        ("Figure 3.2", "Research design workflow connecting the four experiments"),
        ("Figure 3.3", "Date Palm Pollen Extender (DPPE) preparation protocol flowchart"),
        ("Figure 3.4", "Post-slaughter sperm recovery and assessment workflow"),
        ("Figure 4.1", "Demographic profile of sheep keepers (age, education, occupation)"),
        ("Figure 4.2", "Distribution of flock size categories among surveyed keepers"),
        ("Figure 4.3", "Trait preferences for breeding rams and ewes"),
        ("Figure 4.4", "MANOVA three-way interaction plot on adaptive trait priority"),
        ("Figure 4.5", "Proximate composition of El Oued Date Palm Pollen"),
        ("Figure 4.6", "Macro- and micro-mineral content of El Oued DPP"),
        ("Figure 4.7", "DPPH radical scavenging activity of DPP extract vs. ascorbic acid"),
        ("Figure 4.8", "Effect of DPPE treatment and storage time on total and progressive motility"),
        ("Figure 4.9", "Plasma membrane integrity (HOST) of sperm preserved in DPPE extenders"),
        ("Figure 4.10", "Dose-response curves for sperm quality parameters at 48 hours"),
        ("Figure 4.11", "Climate change perceptions among El Oued sheep keepers"),
        ("Figure 4.12", "Forest plot of odds ratios for predictors of perceived fertility decline"),
        ("Figure 5.1", "Triangulated Socio-Technical-Environmental Conservation Model"),
    ]
    for fnum, ftitle in figures_list:
        story.append(Paragraph(
            f"<b>{fnum}.</b> {ftitle}",
            ParagraphStyle('lof', fontName='Tinos', fontSize=10, leading=14,
                           textColor=TEXT_PRIMARY, alignment=TA_LEFT,
                           leftIndent=18, firstLineIndent=-18,
                           spaceBefore=2, spaceAfter=2)
        ))

    story.append(PageBreak())


def build_abbreviations(story, styles):
    """List of abbreviations and acronyms."""
    story.append(Paragraph("List of Abbreviations and Acronyms", styles['TOCHeading']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 14))

    abbreviations = [
        ("AI", "Artificial Insemination"),
        ("AnGR", "Animal Genetic Resources"),
        ("AOAC", "Association of Official Analytical Chemists"),
        ("ANOVA", "Analysis of Variance"),
        ("ATP", "Adenosine Triphosphate"),
        ("BMPR-IB", "Bone Morphogenetic Protein Receptor 1B"),
        ("CASA", "Computer-Assisted Sperm Analysis"),
        ("CAT", "Catalase"),
        ("CI", "Confidence Interval"),
        ("CV", "Coefficient of Variation"),
        ("DHA", "Docosahexaenoic Acid"),
        ("DPP", "Date Palm Pollen (Phoenix dactylifera L.)"),
        ("DPPH", "2,2-diphenyl-1-picrylhydrazyl"),
        ("DPPE", "Date Palm Pollen Extender"),
        ("EDTA", "Ethylenediaminetetraacetic Acid"),
        ("FAO", "Food and Agriculture Organization of the United Nations"),
        ("GAE", "Gallic Acid Equivalents"),
        ("GPx", "Glutathione Peroxidase"),
        ("HOST", "Hypo-Osmotic Swelling Test"),
        ("IC₅₀", "Half-maximal Inhibitory Concentration"),
        ("IVF", "In Vitro Fertilization"),
        ("MANOVA", "Multivariate Analysis of Variance"),
        ("MCB", "Maître de Conférences B"),
        ("NaCl", "Sodium Chloride"),
        ("NPE", "NaCl Pollen Extender"),
        ("Nrf2", "Nuclear factor erythroid 2-related factor 2"),
        ("OR", "Odds Ratio"),
        ("PUFA", "Polyunsaturated Fatty Acid"),
        ("QE", "Quercetin Equivalents"),
        ("RM-ANOVA", "Repeated-Measures Analysis of Variance"),
        ("ROS", "Reactive Oxygen Species"),
        ("SCA", "Sperm Class Analyzer"),
        ("SD", "Standard Deviation"),
        ("SEM", "Standard Error of the Mean"),
        ("SOD", "Superoxide Dismutase"),
        ("SPSS", "Statistical Package for the Social Sciences"),
        ("STR", "Straightness (CASA parameter)"),
        ("TROLOX", "6-hydroxy-2,5,7,8-tetramethylchroman-2-carboxylic acid (vitamin E analog)"),
        ("VAP", "Average Path Velocity (CASA parameter)"),
        ("VCL", "Curvilinear Velocity (CASA parameter)"),
        ("VSL", "Straight-line Velocity (CASA parameter)"),
    ]

    # Build as a 2-column table
    abbr_data = []
    for short, full in abbreviations:
        abbr_data.append([short, full])

    abbr_table = Table(abbr_data, colWidths=[3.0*cm, CONTENT_WIDTH - 3.0*cm])
    abbr_table.setStyle(TableStyle([
        ('FONT', (0,0), (0,-1), 'Carlito-Bold', 10),
        ('FONT', (1,0), (1,-1), 'Tinos', 10),
        ('TEXTCOLOR', (0,0), (0,-1), HEADER_FILL),
        ('TEXTCOLOR', (1,0), (1,-1), TEXT_PRIMARY),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LINEBELOW', (0,0), (-1,-1), 0.2, BORDER),
    ]))
    story.append(abbr_table)

    story.append(PageBreak())


def build_list_of_symbols(story, styles):
    """List of symbols (Greek letters, units)."""
    story.append(Paragraph("List of Symbols and Units", styles['TOCHeading']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 14))

    symbols = [
        ("α", "Alpha", "Significance level (Type I error rate), typically 0.05"),
        ("η²", "Eta-squared", "Effect size measure (partial eta-squared in MANOVA)"),
        ("μ", "Mu", "Population mean; also micro- (10⁻⁶ prefix)"),
        ("σ", "Sigma", "Population standard deviation"),
        ("χ²", "Chi-squared", "Statistical test for categorical data association"),
        ("p", "p-value", "Probability of observing data under null hypothesis"),
        ("OR", "Odds Ratio", "Measure of association in logistic regression"),
        ("CI", "Confidence Interval", "Range estimating population parameter"),
        ("n", "Sample size", "Number of observations in a sample"),
        ("°C", "Degree Celsius", "Temperature unit"),
        ("mg/mL", "Milligram per milliliter", "Concentration unit (DPPE treatments)"),
        ("μm/s", "Micrometer per second", "Sperm velocity unit (CASA)"),
        ("mOsm/kg", "Milliosmole per kilogram", "Osmolality unit"),
        ("nm", "Nanometer", "Wavelength unit (spectrophotometry)"),
        ("rpm", "Revolutions per minute", "Centrifugation speed"),
        ("g", "Relative centrifugal force", "Gravitational acceleration unit"),
        ("kHz", "Kilohertz", "Frequency unit"),
        ("µL", "Microliter", "Volume unit (1 µL = 10⁻⁶ L)"),
        ("mL", "Milliliter", "Volume unit (1 mL = 10⁻³ L)"),
        ("nmol", "Nanomole", "Amount of substance (1 nmol = 10⁻⁹ mol)"),
    ]
    sym_data = [[s, name, desc] for s, name, desc in symbols]
    sym_table = Table(sym_data, colWidths=[1.6*cm, 4.0*cm, CONTENT_WIDTH - 5.6*cm])
    sym_table.setStyle(TableStyle([
        ('FONT', (0,0), (0,-1), 'Tinos-Bold', 13),
        ('FONT', (1,0), (1,-1), 'Carlito-Bold', 10),
        ('FONT', (2,0), (2,-1), 'Tinos', 10),
        ('TEXTCOLOR', (0,0), (0,-1), ACCENT),
        ('TEXTCOLOR', (1,0), (1,-1), HEADER_FILL),
        ('TEXTCOLOR', (2,0), (2,-1), TEXT_PRIMARY),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINEBELOW', (0,0), (-1,-1), 0.2, BORDER),
    ]))
    story.append(sym_table)

    story.append(PageBreak())


# ===================================================================
# CHAPTER SEPARATOR UTILITY
# ===================================================================
def chapter_separator(story, styles, chapter_num, chapter_title_en, chapter_title_fr=""):
    """Insert a chapter separator page."""
    story.append(NextPageTemplate('Separator'))
    story.append(PageBreak())
    story.append(Spacer(1, 5*cm))
    story.append(Paragraph(
        f"CHAPTER {chapter_num}",
        ParagraphStyle('cn', fontName='Carlito-Bold', fontSize=14, alignment=TA_CENTER,
                       textColor=ACCENT, spaceAfter=4)
    ))
    story.append(Spacer(1, 8))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.3],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.5, HEADER_FILL)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 16))
    story.append(Paragraph(
        chapter_title_en,
        ParagraphStyle('ct', fontName='Tinos-Bold', fontSize=22, alignment=TA_CENTER,
                       textColor=HEADER_FILL, leading=28, spaceAfter=8)
    ))
    if chapter_title_fr:
        story.append(Paragraph(
            f"<i>{chapter_title_fr}</i>",
            ParagraphStyle('ctf', fontName='Tinos-Italic', fontSize=13, alignment=TA_CENTER,
                           textColor=TEXT_MUTED, spaceAfter=8)
        ))
    story.append(Spacer(1, 16))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.3],
                       style=[('LINEABOVE', (0,0), (-1,-1), 0.8, ACCENT)],
                       hAlign='CENTER'))
    story.append(NextPageTemplate('Body'))
    story.append(PageBreak())


# ===================================================================
# TABLE BUILDER UTILITY
# ===================================================================
def build_table(data, col_widths=None, header_rows=1, caption=None, caption_num=None,
                styles=None, font_size=9.5):
    """Build a formatted academic table."""
    elements = []

    if caption:
        cap_text = f"<b>{caption_num}.</b> {caption}"
        elements.append(Paragraph(cap_text, styles['TableCaption']))

    if col_widths is None:
        n_cols = len(data[0])
        col_widths = [CONTENT_WIDTH / n_cols] * n_cols

    # Wrap text in Paragraphs for proper wrapping
    table_data = []
    for ri, row in enumerate(data):
        new_row = []
        for ci, cell in enumerate(row):
            if isinstance(cell, str):
                if ri < header_rows:
                    p = Paragraph(f"<b>{cell}</b>",
                                  ParagraphStyle('th', fontName='Carlito-Bold', fontSize=font_size,
                                                 textColor=colors.white, alignment=TA_CENTER, leading=font_size+2))
                else:
                    p = Paragraph(cell,
                                  ParagraphStyle('td', fontName='Tinos', fontSize=font_size,
                                                 textColor=TEXT_PRIMARY, alignment=TA_LEFT, leading=font_size+2))
                new_row.append(p)
            else:
                new_row.append(cell)
        table_data.append(new_row)

    t = Table(table_data, colWidths=col_widths, repeatRows=header_rows)
    style_cmds = [
        # Header
        ('BACKGROUND', (0,0), (-1,header_rows-1), HEADER_FILL),
        ('TEXTCOLOR', (0,0), (-1,header_rows-1), colors.white),
        ('FONT', (0,0), (-1,header_rows-1), 'Carlito-Bold', font_size),
        ('ALIGN', (0,0), (-1,header_rows-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        # Body
        ('FONT', (0,header_rows), (-1,-1), 'Tinos', font_size),
        ('TEXTCOLOR', (0,header_rows), (-1,-1), TEXT_PRIMARY),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, BORDER),
        ('LINEABOVE', (0,0), (-1,0), 0.7, HEADER_FILL),
        ('LINEBELOW', (0,-1), (-1,-1), 0.7, HEADER_FILL),
    ]
    # Alternating row colors
    for i in range(header_rows, len(data)):
        if (i - header_rows) % 2 == 1:
            style_cmds.append(('BACKGROUND', (0,i), (-1,i), TABLE_STRIPE))
    t.setStyle(TableStyle(style_cmds))
    elements.append(t)
    elements.append(Spacer(1, 12))

    return elements


# ===================================================================
# FIGURE EMBEDDER
# ===================================================================
def build_figure(image_filename, caption_text, caption_num, styles, width_cm=14):
    """Embed a figure with caption."""
    elements = []
    img_path = FIGURES_DIR / image_filename
    if not img_path.exists():
        # Placeholder if figure not found
        elements.append(Paragraph(
            f"<i>[Figure {image_filename} not found]</i>",
            styles['Caption']
        ))
        return elements

    img = Image(str(img_path), width=width_cm*cm, height=width_cm*cm*0.7)
    img.hAlign = 'CENTER'
    elements.append(img)
    elements.append(Paragraph(
        f"<b>{caption_num}.</b> {caption_text}",
        styles['Caption']
    ))
    return elements


# ===================================================================
# MAIN BUILDER (will be called from main script)
# ===================================================================
if __name__ == '__main__':
    print("This module provides utilities for the thesis builder.")
    print("Run: python3 /home/z/my-project/scripts/build_thesis_main.py")
