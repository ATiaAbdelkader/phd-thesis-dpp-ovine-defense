#!/usr/bin/env python3
"""
PhD Thesis Builder — Main Orchestrator
========================================
Combines:
- thesis_utils.py (infrastructure, front matter)
- thesis_chapters_1_2.py (Introduction + Literature Review)
- thesis_chapters_3_4.py (Materials & Methods + Results & Discussion)
- thesis_chapters_5_refs.py (Conclusion + References + Appendices)

Outputs: /home/z/my-project/download/thesis_body.pdf
"""

import sys
import os
sys.path.insert(0, '/home/z/my-project/scripts')

from thesis_utils import (
    register_fonts, make_styles, ThesisDocTemplate,
    build_title_page, build_declaration, build_dedication, build_acknowledgments,
    build_abstract_english, build_abstract_french, build_abstract_arabic,
    build_toc, build_list_of_tables, build_list_of_figures,
    build_abbreviations, build_list_of_symbols,
    BODY_PDF, OUTPUT_DIR
)
from thesis_chapters_1_2 import build_chapter_1, build_chapter_2
from thesis_chapters_3_4 import build_chapter_3, build_chapter_4
from thesis_chapters_5_refs import build_chapter_5, build_references, build_appendices
from thesis_expansion import (
    build_chapter_2_expansion, build_chapter_4_expansion, build_appendix_expansion
)
from thesis_expansion2 import (
    build_chapter_4_expansion_2, build_appendix_h, build_glossary
)
from thesis_expansion3 import (
    build_chapter_2_expansion_2, build_chapter_5_expansion, build_appendix_i
)
from thesis_expansion4 import (
    build_chapter_1_expansion, build_chapter_5_expansion_2, build_appendix_j
)


def main():
    print("=" * 60)
    print("Building PhD Thesis — Body PDF")
    print("=" * 60)

    # Step 1: Register fonts
    print("\n[1/4] Registering fonts...")
    register_fonts()

    # Step 2: Create styles
    print("[2/4] Creating paragraph styles...")
    styles = make_styles()

    # Step 3: Build story
    print("[3/4] Building thesis content...")
    story = []

    # ===== FRONT MATTER =====
    print("  - Title page")
    build_title_page(story, styles)

    print("  - Declaration of originality")
    build_declaration(story, styles)

    print("  - Dedication")
    build_dedication(story, styles)

    print("  - Acknowledgments")
    build_acknowledgments(story, styles)

    print("  - English abstract")
    build_abstract_english(story, styles)

    print("  - French résumé")
    build_abstract_french(story, styles)

    print("  - Arabic summary")
    build_abstract_arabic(story, styles)

    print("  - Table of contents")
    build_toc(story, styles)

    print("  - List of tables")
    build_list_of_tables(story, styles)

    print("  - List of figures")
    build_list_of_figures(story, styles)

    print("  - Abbreviations")
    build_abbreviations(story, styles)

    print("  - List of symbols")
    build_list_of_symbols(story, styles)

    # ===== CHAPTERS =====
    print("  - Chapter 1: General Introduction")
    build_chapter_1(story, styles)

    print("  - Chapter 1 expansion (extended background)")
    build_chapter_1_expansion(story, styles)

    print("  - Chapter 2: Literature Review")
    build_chapter_2(story, styles)

    print("  - Chapter 2 expansion (additional sections)")
    build_chapter_2_expansion(story, styles)

    print("  - Chapter 2 expansion 2 (conservation strategies)")
    build_chapter_2_expansion_2(story, styles)

    print("  - Chapter 3: Materials and Methods")
    build_chapter_3(story, styles)

    print("  - Chapter 4: Results and Discussion")
    build_chapter_4(story, styles)

    print("  - Chapter 4 expansion (integration & comparison)")
    build_chapter_4_expansion(story, styles)

    print("  - Chapter 4 expansion 2 (mechanistic interpretation)")
    build_chapter_4_expansion_2(story, styles)

    print("  - Chapter 5: General Conclusion")
    build_chapter_5(story, styles)

    print("  - Chapter 5 expansion (extended framework)")
    build_chapter_5_expansion(story, styles)

    print("  - Chapter 5 expansion 2 (global implications)")
    build_chapter_5_expansion_2(story, styles)

    # ===== BACK MATTER =====
    print("  - References")
    build_references(story, styles)

    print("  - Appendices A-F")
    build_appendices(story, styles)

    print("  - Appendix G (extended protocol notes)")
    build_appendix_expansion(story, styles)

    print("  - Appendix H (extended statistical outputs)")
    build_appendix_h(story, styles)

    print("  - Glossary")
    build_glossary(story, styles)

    print("  - Appendix I (supplementary tables)")
    build_appendix_i(story, styles)

    print("  - Appendix J (replication methodology)")
    build_appendix_j(story, styles)

    # Step 4: Build PDF
    print(f"\n[4/4] Building PDF: {BODY_PDF}")
    doc = ThesisDocTemplate(
        str(BODY_PDF),
        pagesize=(595.27, 841.89),  # A4 in points
        leftMargin=2.5*72/2.54,    # 2.5 cm
        rightMargin=2.5*72/2.54,
        topMargin=2.5*72/2.54,
        bottomMargin=2.5*72/2.54,
        title="Date Palm Pollen for Post-Slaughter Ovine Epididymal Sperm Preservation",
        author="[Candidate Name]",
        subject="PhD Thesis — University of El Oued, Algeria",
        creator="Z.ai Thesis Builder",
    )

    # multiBuild for TOC support
    print("  - Running multiBuild (passes for TOC)...")
    doc.multiBuild(story)

    # Get file size
    size_mb = os.path.getsize(BODY_PDF) / (1024*1024)
    print(f"\n{'='*60}")
    print(f"✓ Body PDF generated: {BODY_PDF}")
    print(f"  Size: {size_mb:.2f} MB")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
