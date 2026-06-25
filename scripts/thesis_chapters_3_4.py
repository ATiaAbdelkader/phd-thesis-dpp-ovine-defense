#!/usr/bin/env python3
"""
PhD Thesis Content — Chapters 3 & 4
=====================================
Chapter 3: Materials and Methods (with all 4 experiments including climate perceptions)
Chapter 4: Results and Discussion (integrated format, all 4 experiments)
"""

import sys
sys.path.insert(0, '/home/z/my-project/scripts')
from thesis_utils import (
    add_heading, build_table, build_figure, chapter_separator,
    HEADER_FILL, ACCENT, ACCENT_2, TEXT_PRIMARY, TEXT_MUTED, BORDER,
    CONTENT_WIDTH, TABLE_STRIPE, colors, Paragraph, Spacer, PageBreak,
    Table, TableStyle, ParagraphStyle, TA_LEFT, TA_CENTER, TA_JUSTIFY,
    cm, mm
)


# ===================================================================
# CHAPTER 3: MATERIALS AND METHODS
# ===================================================================
def build_chapter_3(story, styles):
    """Chapter 3: Materials and Methods."""
    chapter_separator(story, styles, 3,
                      "Materials and Methods",
                      "Matériel et Méthodes")

    # 3.1 Overview
    story.append(add_heading("3.1 Overview of Research Design", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "This study employed a multi-experimental design to assess the conservative "
        "influence of Date Palm Pollen (DPP) on epididymal sperm retrieved from sheep "
        "after slaughter, situated within its socioeconomic and environmental context. "
        "Four interconnected experiments were conducted: (1) a socioeconomic and trait "
        "preference survey of 200 sheep keepers in the El Oued region to establish the "
        "context and conservation priorities for indigenous sheep genetic resources; "
        "(2) phytochemical characterization and antioxidant assessment of DPP to "
        "validate its biochemical composition and biological activity; (3) a controlled "
        "laboratory experiment evaluating DPP's conservative effects on post-slaughter "
        "ovine epididymal sperm during chilled storage at 4°C; and (4) a survey of "
        "climate change perceptions and their linkage to perceived fertility declines "
        "among the same keeper cohort. This triangulated strategy ensures that technical "
        "discoveries are grounded in field conservation needs and validated by rigorous "
        "biochemical confirmation, while climate-urgency data elevates the conservation "
        "imperative.",
        styles['Body']
    ))

    story.append(Paragraph(
        "All animal-related experiments were carried out post-mortem at a licensed "
        "abattoir, with no live animals involved. This strategy is consistent with the "
        "thesis's focus on post-slaughter genetic rescue while avoiding ethical "
        "considerations associated with experimental animal sacrifice. The institutional "
        "ethics review was conducted in accordance with national regulations on "
        "post-mortem tissue collection for research purposes (Appendix C).",
        styles['Body']
    ))

    # Figure 3.2: Research design workflow
    story.extend(build_figure(
        'fig_3_2_research_workflow.png',
        "Research design workflow connecting the four experiments through integration "
        "and synthesis into a validated field-deployable DPPE protocol.",
        "Figure 3.2", styles, width_cm=15
    ))

    # Table 3.1: Integration
    table_3_1_data = [
        ['Experiment', 'Contribution to Thesis Objectives', 'Data Integration'],
        ['1. Socioeconomic survey',
         'Establishes conservation priorities; validates field applicability context; documents DPP traditional use knowledge',
         'Informs interpretation of technical findings; identifies target breeds and keeper needs'],
        ['2. Phytochemical characterisation',
         'Validates DPP biochemical composition; confirms antioxidant capacity; establishes batch quality standards',
         'Provides mechanistic rationale for observed effects; enables standardisation'],
        ['3. Sperm preservation trial',
         'Directly tests conservative effect; evaluates dose-response; validates field-applicable protocol',
         'Core evidence for thesis claims; generates data for optimisation'],
        ['4. Climate perception survey',
         'Documents climate-fertility link; quantifies urgency for conservation; identifies vulnerable flock categories',
         'Elevates conservation imperative; informs targeting of intervention'],
    ]
    story.extend(build_table(
        table_3_1_data,
        col_widths=[3.5*cm, 6.5*cm, 5.5*cm],
        caption="Integration of the four experiments and their contribution to thesis "
                "objectives and data flow.",
        caption_num="Table 3.1",
        styles=styles, font_size=9
    ))

    # 3.2 Experiment 1
    story.append(add_heading("3.2 Experiment 1: Socioeconomic Context and Trait Preference Assessment", styles['H1'], level=0, story=story))

    story.append(add_heading("3.2.1 Study Area and Rationale", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "This study was carried out in the El Oued region of southeast Algeria "
        "(33°22'16.823\" N, 6°50'52.686\" E), a key centre of date palm agriculture and "
        "sheep production in the Algerian Sahara. The region's agroecological "
        "characteristics — including an arid environment, substantial pastoral systems, "
        "and the geographic combination of date palm cultivation and sheep production — "
        "make it a model for studying post-slaughter genetic rescue and field-applicable "
        "preservation measures. The presence of date palm orchards and sheep flocks in "
        "this region lays the geographical and cultural groundwork for DPP use in "
        "genetic conservation (Figure 3.1).",
        styles['Body']
    ))

    story.extend(build_figure(
        'fig_3_1_study_area_map.png',
        "Study area map showing the El Oued region in southeast Algeria, the eight "
        "surveyed municipalities, and the DPP collection site at Hamraia (Reguiba District).",
        "Figure 3.1", styles, width_cm=13
    ))

    story.append(add_heading("3.2.2 Sampling Procedure and Participant Selection", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "To ensure that the sheep production systems in the region were representative, "
        "a stratified random sampling approach was used. A total of 200 sheep keepers "
        "were selected at random from eight municipalities: El Oued (the regional "
        "capital), Debila, Guemar, Hassi Khelifa, Mih Ouensa, Ourmes, Robbah, and Taleb "
        "Larbi. Selection criteria included: (a) participation in the government's 2023 "
        "national sheep numbering initiative, which ensures official recognition and "
        "flock recording; (b) use of grazing-based agricultural practices typical of "
        "the region; and (c) willingness to participate in research. The sample size "
        "of 200 was determined to provide adequate statistical power for multivariate "
        "analysis while remaining logistically feasible within the constraints of "
        "field survey implementation in remote Saharan municipalities.",
        styles['Body']
    ))

    story.append(Paragraph(
        "Flock size categories were created to reflect production system diversity: "
        "<20 animals (smallholder), 20–50 animals (medium), 50–100 animals (large), "
        "and >100 animals (commercial). This stratification ensures that conservation "
        "priorities encompass the entire range of sheep keepers, from subsistence to "
        "commercial producers, and enables subsequent identification of vulnerability "
        "categories linked to flock size.",
        styles['Body']
    ))

    story.append(add_heading("3.2.3 Data Collection Instruments", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Semi-structured questionnaires with both open-ended and closed questions were "
        "developed to collect comprehensive data on: (a) socioeconomic characteristics "
        "(age, education, experience, primary occupation); (b) flock size, structure, "
        "and management; and (c) specific trait preferences for male and female sheep, "
        "including reproductive performance, adaptation, and production characteristics "
        "pertinent to genetic conservation priorities. The full questionnaire is "
        "provided in Appendix A.",
        styles['Body']
    ))

    story.append(Paragraph(
        "Questionnaires were pre-tested with 10 sheep keepers in each municipality to "
        "ensure relevance and adaptation to local conditions, as recommended for survey "
        "instrument validation (Dossa et al., 2015). Pre-testing evaluated question "
        "comprehension, response option suitability, and interview duration, with "
        "improvements made for clarity and cultural sensitivity. The final questionnaire "
        "was administered in face-to-face interviews conducted in Arabic by trained "
        "enumerators, with responses recorded in both Arabic and French for cross-"
        "verification.",
        styles['Body']
    ))

    story.append(add_heading("3.2.4 Statistical Analysis", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "A multivariate analysis of variance (MANOVA) was used to determine the effects "
        "of age, education, experience, and occupation on trait preferences among sheep "
        "keepers. Pillai's trace was chosen as the major multivariate test statistic "
        "because it is robust to violations of assumptions, such as unequal sample "
        "sizes and heterogeneity of covariance matrices (Olson, 1976; Tabachnick & "
        "Fidell, 2025). Partial eta squared (η²) was used to measure the proportion of "
        "variance in dependent variables that could be explained by independent "
        "variables. Significance was determined at α = 0.05. All analyses were carried "
        "out using IBM SPSS Statistics version 27.0 (IBM Corp., Armonk, NY, USA).",
        styles['Body']
    ))

    # 3.3 Experiment 2
    story.append(add_heading("3.3 Experiment 2: Phytochemical Characterisation of Date Palm Pollen", styles['H1'], level=0, story=story))

    story.append(add_heading("3.3.1 Plant Material Collection and Processing", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Date Palm Pollen (DPP) was collected at Hamraia commune, Reguiba District, "
        "El Oued Province (34°6'39\" N, 6°13'50\" E) during the natural flowering "
        "season (late March to early April 2024). This region was chosen for its "
        "established date palm plantations with a variety of genotypes and proximity "
        "to the sheep production systems described in Experiment 1. The collection "
        "protocol followed established methods for pollen quality preservation "
        "(Laghouati et al., 2021; Shahin, 2014):",
        styles['Body']
    ))

    collection_steps = [
        "<b>Male inflorescence selection.</b> Healthy, mature male date palm trees were "
        "selected, and spathes were separated before dehiscence to prevent contamination "
        "and ensure pollen maturity.",
        "<b>Harvesting.</b> Mature spathes were removed early in the morning to reduce "
        "temperature stress and brought directly to a shaded processing location.",
        "<b>Dehiscence induction.</b> Each spathe was opened approximately 1 mm to allow "
        "air ingress, and the cut base (3–4 cm) was immersed in water to maintain "
        "hydration until full opening.",
        "<b>Pollen extraction.</b> Flowers were manually removed after 24–48 hours of "
        "drying at ambient temperature (20–25°C) with regular rotation (2–3× daily) to "
        "ensure uniform moisture reduction.",
        "<b>Purification.</b> Pollen was sieved using an 80–100 μm fine mesh screen to "
        "remove flower debris and impurities.",
        "<b>Storage.</b> Purified pollen was dried to reduce moisture content before "
        "being stored in airtight containers at 4°C, away from light, until analysis. "
        "All handling involved sterile devices and gloves to prevent contamination.",
    ]
    for step in collection_steps:
        story.append(Paragraph(step, styles['NumberedItem']))

    story.append(Paragraph(
        "Phytochemical and biological activity analyses were undertaken in March–April "
        "2025, with triplicate determinations and findings reported as mean ± standard "
        "deviation (SD). The DPP preparation flowchart is shown in Figure 3.3.",
        styles['Body']
    ))

    story.extend(build_figure(
        'fig_3_3_dpp_preparation.png',
        "Date Palm Pollen Extender (DPPE) preparation protocol flowchart, adapted from "
        "the Laghouati et al. (2021) NaCl pollen extender method.",
        "Figure 3.3", styles, width_cm=12
    ))

    # 3.3.2 Proximate Composition
    story.append(add_heading("3.3.2 Proximate Composition Analysis", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Proximate composition (moisture, ash, fat, protein, carbohydrate, fibre) was "
        "determined using standard AOAC (2019) methods. <b>Moisture content</b> was "
        "estimated by gravimetric analysis: 3 g of sample was distributed in a pre-"
        "weighed Petri plate and dried in an oven at 105°C for 3 hours, with drying "
        "repeated until constant weight was achieved. <b>Ash content</b> was evaluated "
        "by dry ashing in a muffle furnace at 550°C for 6 hours following pre-ignition "
        "of crucibles at 550°C overnight. <b>Fat content</b> was determined by Soxhlet "
        "extraction with petroleum ether (boiling point 40–60°C) for 1 hour. "
        "<b>Protein content</b> was determined by the Kjeldahl method using a 6.25 "
        "conversion factor: 1 g of sample was digested with catalyst (10 g Na₂SO₄ + "
        "1 g CuSO₄) and 12 mL concentrated H₂SO₄ at 420°C for 1 hour, followed by "
        "distillation and titration with 0.1N HCl. <b>Carbohydrate content</b> was "
        "measured by the phenol-sulfuric acid colorimetric method (DuBois et al., 1956) "
        "with absorbance read at 490 nm against a glucose standard curve.",
        styles['Body']
    ))

    table_3_2_data = [
        ['Parameter', 'Method', 'Standard', 'Principle'],
        ['Moisture', 'Gravimetric (oven-drying)', 'AOAC 925.10 / 950.46', 'Weight loss on drying at 105°C'],
        ['Ash', 'Dry ashing (muffle furnace)', 'AOAC 923.03', 'Weight of residue after ignition at 550°C'],
        ['Fat', 'Soxhlet extraction (petroleum ether)', 'AOAC 920.39', 'Lipid extraction by solvent reflux'],
        ['Protein', 'Kjeldahl digestion + titration', 'AOAC 928.08', 'Nitrogen determination × 6.25 conversion'],
        ['Carbohydrate', 'Phenol-sulfuric acid colorimetry', 'DuBois et al. (1956)', 'Hexose dehydration to furfural derivatives'],
        ['Fibre', 'Acid detergent fibre (ADF)', 'AOAC 973.18', 'Cellulose + lignin after acid detergent treatment'],
    ]
    story.extend(build_table(
        table_3_2_data,
        col_widths=[2.8*cm, 4.0*cm, 4.2*cm, 4.5*cm],
        caption="Proximate analysis methods and standards used for Date Palm Pollen "
                "characterization in Experiment 2.",
        caption_num="Table 3.2",
        styles=styles, font_size=9
    ))

    # 3.3.3 Mineral Content
    story.append(add_heading("3.3.3 Mineral Content Analysis", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "<b>Calcium</b> was evaluated by permanganometric titration in accordance with "
        "NA 1655 / ISO 6058:1994. A 2 g sample was dry-ashed at 550°C for 4–6 hours, "
        "then dissolved in concentrated HCl. Calcium oxalate was precipitated with "
        "ammonium oxalate, dissolved in H₂SO₄, and titrated with standardized KMnO₄ "
        "to a persistent pink endpoint. <b>Magnesium</b> was determined by complexometric "
        "titration with EDTA according to NA 752 / ISO 6059:1989: total hardness "
        "(Ca²⁺ + Mg²⁺) was titrated with EDTA at pH 10 using Eriochrome Black T "
        "indicator, with calcium measured independently at pH 12 using murexide; "
        "magnesium was computed by difference. <b>Potassium and sodium</b> were "
        "determined by flame photometry following NA 1653: a 1–2 g sample underwent "
        "wet digestion with an HNO₃/HClO₄ mixture, with emission intensity measured "
        "at 766.5 nm (K) and 589 nm (Na) against calibration curves.",
        styles['Body']
    ))

    table_3_3_data = [
        ['Mineral', 'Method', 'Standard', 'Wavelength / Endpoint'],
        ['Calcium (Ca)', 'Permanganometric titration', 'NA 1655 / ISO 6058:1994', 'Persistent pink (KMnO₄)'],
        ['Magnesium (Mg)', 'Complexometric EDTA titration', 'NA 752 / ISO 6059:1989', 'Eriochrome Black T color change'],
        ['Potassium (K)', 'Flame photometry', 'NA 1653', '766.5 nm emission'],
        ['Sodium (Na)', 'Flame photometry', 'NA 1653', '589 nm emission'],
        ['Iron (Fe)', 'Atomic absorption spectrophotometry', 'AOAC 999.11', '248.3 nm absorption'],
        ['Zinc (Zn)', 'Atomic absorption spectrophotometry', 'AOAC 999.11', '213.9 nm absorption'],
    ]
    story.extend(build_table(
        table_3_3_data,
        col_widths=[3.2*cm, 4.5*cm, 4.0*cm, 3.8*cm],
        caption="Mineral analysis methods and reference standards used for DPP "
                "characterization.",
        caption_num="Table 3.3",
        styles=styles, font_size=9
    ))

    # 3.3.4 Phytochemicals
    story.append(add_heading("3.3.4 Phytochemical Compound Quantification", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "<b>Extract preparation.</b> DPP extract was prepared by maceration: 5 g of "
        "finely ground DPP was macerated in 50 mL of 50% ethanol for 24 hours at room "
        "temperature with occasional agitation. The extract was filtered, the filtrate "
        "was dried at ≤45°C in an oven, then stored at 4°C until analysis.",
        styles['Body']
    ))

    story.append(Paragraph(
        "<b>Total phenolic content</b> was determined using the Folin-Ciocalteu "
        "technique (Slinkard & Singleton, 1977). Extract (0.2 mL) was combined with "
        "1 mL of 10% Folin-Ciocalteu reagent. After four minutes, 0.8 mL of saturated "
        "sodium carbonate solution (75 g/L) was added. The mixture was incubated at "
        "room temperature for 2 hours, and absorbance was measured at 765 nm. A "
        "calibration curve was created using gallic acid (0–200 μg/mL). Results are "
        "presented as mg gallic acid equivalents per gram of extract (mg GAE/g).",
        styles['Body']
    ))

    story.append(Paragraph(
        "<b>Total flavonoid content</b> was measured using the aluminum chloride "
        "colorimetric technique (Ahn et al., 2007): 1 mL of extract was mixed with "
        "1 mL of 2% AlCl₃ solution and incubated at room temperature for 30 minutes. "
        "Absorbance was measured at 430 nm against a reagent blank. A calibration "
        "curve was created using quercetin (0–100 μg/mL), with results presented as "
        "mg quercetin equivalents per gram of extract (mg QE/g).",
        styles['Body']
    ))

    # 3.3.5 Antioxidant Activity
    story.append(add_heading("3.3.5 Antioxidant Activity Assessment", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Antioxidant activity was assessed using the DPPH (2,2-diphenyl-1-picrylhydrazyl) "
        "radical scavenging assay (Mansouri et al., 2005). DPPH solution (1 mL, 0.1 mM "
        "in methanol) was combined with 1 mL of extract or ascorbic acid (positive "
        "control). The mixture was vortexed and incubated in the dark at room "
        "temperature for 30 minutes. Absorbance was measured at 517 nm. Percentage "
        "inhibition was computed as:",
        styles['Body']
    ))

    story.append(Paragraph(
        "<b>Inhibition (%) = [(A<sub>control</sub> − A<sub>sample</sub>) / "
        "A<sub>control</sub>] × 100</b>",
        styles['Formula']
    ))

    story.append(Paragraph(
        "where A<sub>control</sub> = absorbance of DPPH without sample and "
        "A<sub>sample</sub> = absorbance with extract. IC₅₀ values (concentration "
        "inhibiting 50% of DPPH radicals) were determined by plotting percentage "
        "inhibition against extract concentration.",
        styles['Body']
    ))

    # 3.4 Experiment 3
    story.append(add_heading("3.4 Experiment 3: Evaluation of DPP Conservative Effects on Post-Slaughter Ovine Epididymal Sperm", styles['H1'], level=0, story=story))

    story.append(add_heading("3.4.1 Ethical Considerations and Animal Material", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "All biological material was taken post-mortem from a licensed abattoir in El "
        "Oued, Algeria. No living animals were used. This strategy is consistent with "
        "the thesis's focus on post-slaughter genetic rescue while avoiding ethical "
        "considerations associated with experimental animal sacrifice. Testes were "
        "taken from five sexually mature Ouled Djellal rams (aged 18–24 months) "
        "slaughtered at the local abattoir. This sample size provides adequate "
        "statistical power for detecting large effects while adhering to practical "
        "limits such as post-mortem tissue availability. Rams were selected based on "
        "apparent health state (no evident pathology) and a body condition score "
        "adequate for their age.",
        styles['Body']
    ))

    story.append(add_heading("3.4.2 Sample Collection and Transport", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Testes were removed immediately after slaughter and transported to the "
        "laboratory within 2 hours in isotonic saline (0.9% NaCl) on ice at 4°C. This "
        "transport strategy simulates field situations where rapid cooling is critical "
        "for maintaining post-mortem sperm viability (Shayestehyekta et al., 2022; "
        "Silva et al., 2025). The 2-hour window represents realistic field-to-"
        "laboratory intervals in extensive pastoral systems. Upon arrival, the cauda "
        "epididymides were dissected and sterilely cleaned of any clinging connective "
        "tissue, blood vessels, or fat. The cauda was carefully targeted as the "
        "principal sperm storage area harboring mature, fertilizable spermatozoa "
        "(Wu et al., 2021).",
        styles['Body']
    ))

    story.append(add_heading("3.4.3 Sperm Recovery", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Spermatozoa were recovered using the retrograde flushing technique "
        "(Martinez-Pastor et al., 2006), a common method for collecting post-mortem "
        "epididymal sperm. A single incision was made at the corpus-cauda junction. "
        "A 1 mL syringe containing warm (37°C) saline solution (0.9% NaCl, 308 mOsm/kg, "
        "pH 7.2) was introduced into the vas deferens, and gentle, consistent pressure "
        "was applied to flush spermatozoa down the cauda. The emerging fluid was "
        "collected in sterile 15 mL conical tubes. This method was chosen for: "
        "(a) good recovery efficiency as compared to mincing or aspiration; "
        "(b) low contamination with tissue debris; and (c) compliance with field "
        "situations that necessitate simple equipment.",
        styles['Body']
    ))

    story.append(add_heading("3.4.4 DPP Extender Preparation", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Date Palm Pollen extenders (DPPE) were prepared using the Laghouati et al. "
        "(2021) NaCl pollen extender (NPE) method, adapted for ovine epididymal sperm. "
        "This water extraction method was chosen for its field applicability; it "
        "requires no organic solvents, minimal equipment, and is easily used in "
        "resource-constrained environments. The preparation protocol is detailed in "
        "Figure 3.3 and Table 3.4.",
        styles['Body']
    ))

    table_3_4_data = [
        ['Treatment Code', 'Composition', 'Final DPP Concentration', 'Purpose'],
        ['DPPE-0 (Control)', '1 mL saline (0.9% NaCl, 308 mOsm/L, pH 7.2)',
         '0 mg/mL', 'Negative control — no DPP supplementation'],
        ['DPPE-40', '40 mg DPP soaked in 1 mL saline',
         '40 mg/mL', 'Low-dose treatment'],
        ['DPPE-80', '80 mg DPP soaked in 1 mL saline',
         '80 mg/mL', 'High-dose treatment'],
    ]
    story.extend(build_table(
        table_3_4_data,
        col_widths=[3.2*cm, 4.5*cm, 3.0*cm, 4.8*cm],
        caption="DPPE treatment groups and final concentrations used in Experiment 3.",
        caption_num="Table 3.4",
        styles=styles, font_size=9
    ))

    story.append(Paragraph(
        "DPP was suspended by vortexing, and all tubes were refrigerated at 4°C for "
        "24 hours to allow bioactive component extraction. Centrifuge tubes "
        "[<i>insert centrifuge speed × time parameters</i>] to remove particle debris. "
        "Collect the clear supernatant as an extender for sperm dilution. This "
        "extraction duration and temperature were chosen based on Laghouati et al. "
        "(2021) preliminary optimisation to maximise polyphenol recovery while "
        "minimising microbial growth.",
        styles['Body']
    ))

    story.append(add_heading("3.4.5 Experimental Design and Treatments", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Each ram's recovered epididymal sperm was divided into three equal aliquots "
        "and diluted 1:1 (v/v) in one of the three prepared extenders (DPPE-0, "
        "DPPE-40, or DPPE-80). The final sperm concentration was adjusted to "
        "350 × 10⁶ cells/mL, a standard value for ovine sperm preservation "
        "(Maxwell & Watson, 1996). Aliquots (0.5 mL) were placed in sterile tubes, "
        "coated with mineral oil to prevent evaporation and gas exchange, and "
        "refrigerated at 4°C for 48 hours. This chilled storage protocol was chosen "
        "because it is (a) representative of field conditions where cryopreservation "
        "infrastructure may not be available, (b) technically simpler than "
        "cryopreservation for initial efficacy screening, and (c) physiologically "
        "relevant to the \"golden hour\" extension concept. Quality parameters were "
        "assessed at 0, 24, and 48 hours to capture immediate effects, mid-storage "
        "stability, and long-term preservation capacity.",
        styles['Body']
    ))

    # Figure 3.4: Sperm assessment workflow
    story.extend(build_figure(
        'fig_3_4_sperm_assessment.png',
        "Post-slaughter sperm recovery and assessment workflow from ram slaughter "
        "through chilled storage to CASA and HOST evaluation.",
        "Figure 3.4", styles, width_cm=15
    ))

    # 3.4.6 Sperm Quality Assessment
    story.append(add_heading("3.4.6 Sperm Quality Assessment", styles['H2'], level=1, story=story))

    story.append(Paragraph(
        "<b>Total and Progressive Motility (CASA).</b> Samples were gently mixed and "
        "equilibrated at 37°C for 5 minutes prior to analysis. For Computer-Assisted "
        "Sperm Analysis (CASA), 3 μL was loaded into a 20-μm Leja® chamber and "
        "analyzed using the Sperm Class Analyzer® (SCA) system (Microptic, Barcelona, "
        "Spain) at 60 frames per second. Settings included a 10× phase contrast "
        "objective and ovine-specific preset parameters (Table 3.5). At least five "
        "fields were acquired per sample. The intra-assay coefficient of variation "
        "(CV) for motility parameters was less than 5%, indicating technical "
        "precision. CASA was selected for objective, quantitative assessment, "
        "eliminating observer bias and enabling detection of subtle kinematic "
        "changes indicative of functional status (Amann & Waberski, 2014; Mortimer, "
        "1994).",
        styles['Body']
    ))

    table_3_5_data = [
        ['CASA Parameter', 'Setting / Threshold', 'Description'],
        ['Frame rate', '60 fps', 'Image acquisition rate'],
        ['Objective', '10× phase contrast', 'Magnification and contrast mode'],
        ['Chamber', 'Leja® 20 μm', 'Standardized counting chamber depth'],
        ['Fields per sample', '≥ 5', 'Minimum fields for representative evaluation'],
        ['Total motility', 'VAP > 5 μm/s', 'Proportion of sperm with detectable movement'],
        ['Progressive motility', 'VAP > 25 μm/s AND STR > 50%', 'Proportion with forward progression'],
        ['Temperature', '37°C', 'Pre-warmed stage for physiological assessment'],
        ['Intra-assay CV', '< 5%', 'Technical precision threshold'],
    ]
    story.extend(build_table(
        table_3_5_data,
        col_widths=[3.5*cm, 5.5*cm, 6.5*cm],
        caption="CASA settings and parameters for ovine sperm analysis (Sperm Class "
                "Analyzer®, Microptic).",
        caption_num="Table 3.5",
        styles=styles, font_size=9
    ))

    story.append(Paragraph(
        "<b>Plasma Membrane Integrity (HOST).</b> Functional membrane integrity was "
        "evaluated by the Hypo-Osmotic Swelling Test (HOST) (Jeyendran et al., 1984), "
        "which assesses the ability of sperm to maintain osmotic balance — essential "
        "for capacitation and fertilisation competence. An iso-osmotic swelling "
        "solution (150 mOsm/L sodium citrate with 20 mM fructose) was prepared. Sperm "
        "(50 μL) were incubated with 1 mL of HOST solution for 30 minutes at 37°C, "
        "then fixed with 10% formalin. A minimum of 200 cells per sample were scored "
        "under phase contrast microscopy (400×) for tail swelling (intact membrane, "
        "functional) or non-swollen tails (damaged membrane, non-functional). The "
        "HOST-positive proportion was used as the membrane integrity indicator.",
        styles['Body']
    ))

    # 3.4.7 Statistical Analysis
    story.append(add_heading("3.4.7 Statistical Analysis", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Data were presented as mean ± standard error of the mean (SEM). The effects "
        "of extender concentration (0, 40, 80 mg/mL), storage period (0, 24, 48 h), "
        "and their interaction were investigated using two-way repeated-measures "
        "ANOVA (RM-ANOVA), with \"ram\" as the subject factor to account for "
        "individual animal variance. Mauchly's test of sphericity was applied, with "
        "Greenhouse-Geisser correction when assumptions were violated. Post-hoc "
        "pairwise comparisons used Bonferroni correction. Partial eta squared (η²) "
        "was used as the effect size measure, with η² > 0.14 considered a large "
        "effect. Significance was set at α = 0.05. All analyses were performed using "
        "IBM SPSS Statistics version 27.0.",
        styles['Body']
    ))

    # 3.5 Experiment 4
    story.append(add_heading("3.5 Experiment 4: Climate Change Perceptions and Fertility Impacts", styles['H1'], level=0, story=story))

    story.append(add_heading("3.5.1 Survey Design and Rationale", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Experiment 4 was designed to document how climate change threatens the very "
        "ovine genetic resources that post-slaughter preservation aims to protect. "
        "Building on the same 200-keeper cohort surveyed in Experiment 1, a "
        "complementary questionnaire module captured perceptions of climate change "
        "impacts on sheep fertility, mortality, and management over the preceding "
        "five years. The dual-purpose design — combining socioeconomic profile "
        "(Experiment 1) with climate perception (Experiment 4) in a single field "
        "visit — maximized research efficiency while minimizing respondent burden.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The climate-perception instrument comprised four modules: (a) awareness of "
        "climate-fertility relationships (yes/no + open-ended elaboration); (b) "
        "primary climate stressors affecting sheep production (multi-select from "
        "heat stress, nutritional stress, water scarcity, disease emergence, other); "
        "(c) perceived fertility trends over the past five years (declined / stable / "
        "increased + qualitative description); and (d) adaptation strategies employed "
        "(multi-select from flock size reduction, breed change, supplementary feeding, "
        "transhumance modification, veterinary intervention, other).",
        styles['Body']
    ))

    story.append(add_heading("3.5.2 Statistical Analysis", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Descriptive statistics (frequencies, percentages, 95% confidence intervals) "
        "were computed for all perception variables. Binary logistic regression was "
        "used to identify predictors of perceived fertility decline, with the "
        "dependent variable coded as 1 (decline reported) vs. 0 (no decline). "
        "Independent variables included flock size category (smallholder / medium / "
        "large / commercial), keeper age (continuous), education level (ordinal), "
        "experience (continuous), primary occupation (categorical), and reported "
        "heat-stress events (binary). Odds ratios (OR) with 95% confidence intervals "
        "were computed, and model fit was assessed using the Hosmer-Lemeshow test. "
        "Significance was set at α = 0.05.",
        styles['Body']
    ))

    # 3.6 Integration
    story.append(add_heading("3.6 Integration of Experiments and Data Flow", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "The sequential structure — context → characterisation → efficacy → urgency — "
        "ensures that Experiment 3 findings are grounded in validated material "
        "(Experiment 2) and relevant conservation needs (Experiment 1), while "
        "Experiment 4 elevates the conservation imperative by documenting the climate-"
        "induced threats to the very genetic resources that post-slaughter preservation "
        "aims to protect (Table 3.1). This integration strengthens both internal "
        "validity (findings are grounded in field-validated materials and priorities) "
        "and external applicability (the resulting DPPE protocol is aligned with "
        "real-world conservation contexts).",
        styles['Body']
    ))

    # 3.7 Limitations
    story.append(add_heading("3.7 Limitations and Methodological Considerations", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "Several methodological limitations should be acknowledged at the outset. "
        "<b>Sample size in Experiment 3</b> (n = 5 rams) provides adequate power for "
        "detecting large effects but may miss subtle treatment differences; "
        "replication across seasons and breeds would strengthen generalizability. "
        "<b>Chilled storage vs. cryopreservation:</b> The 4°C storage protocol, while "
        "field-relevant, does not test DPP effects on freeze-thaw survival; this "
        "represents a priority for follow-up research. <b>Single DPP source:</b> "
        "Pollen from one region (Hamraia) was characterised; geographic variation in "
        "composition may affect reproducibility. <b>Limited assessment endpoints:</b> "
        "Motility and membrane integrity were evaluated; comprehensive hierarchical "
        "assessment, including oxidative status, mitochondrial function, DNA integrity, "
        "and fertilising capacity via in vitro fertilization, requires expanded "
        "methodology in future studies. <b>Perceptual nature of climate data:</b> "
        "Experiment 4 relies on breeder perceptions rather than objective "
        "meteorological or reproductive records; while triangulated with physiological "
        "literature, the study cannot establish causal attribution without longitudinal "
        "objective data.",
        styles['Body']
    ))

    story.append(PageBreak())


# ===================================================================
# CHAPTER 4: RESULTS AND DISCUSSION (INTEGRATED)
# ===================================================================
def build_chapter_4(story, styles):
    """Chapter 4: Integrated Results and Discussion."""
    chapter_separator(story, styles, 4,
                      "Results and Discussion",
                      "Résultats et Discussion")

    story.append(Paragraph(
        "This chapter presents the empirical findings of the four experiments in an "
        "integrated results-and-discussion format. For each experiment, results are "
        "presented, immediately interpreted, compared with previous studies, and "
        "related to the corresponding research questions and hypotheses formulated in "
        "Chapter 1. This integrated approach avoids the artificial separation of "
        "findings from interpretation and enables the reader to follow the logical "
        "flow from data to scientific meaning.",
        styles['Body']
    ))

    # 4.1 Experiment 1
    story.append(add_heading("4.1 Experiment 1: Socioeconomic Context and Trait Preferences of Sheep Keepers in El Oued", styles['H1'], level=0, story=story))

    story.append(add_heading("4.1.1 Overview and Rationale", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Before evaluating the technical efficacy of Date Palm Pollen for post-slaughter "
        "sperm preservation, it is essential to establish the socioeconomic and "
        "conservation context within which such interventions would be implemented. "
        "This survey of 200 sheep keepers across eight municipalities in the El Oued "
        "region provides critical baseline data on: (a) the demographic profile of "
        "stakeholders in ovine genetic conservation; (b) flock characteristics and "
        "management systems; and (c) trait preferences that define breeding objectives "
        "and, consequently, the value of genetic rescue from post-slaughter recovery. "
        "These findings ground the technical research in field-level realities, "
        "ensuring that DPP-based preservation addresses genuine conservation priorities.",
        styles['Body']
    ))

    story.append(add_heading("4.1.2 Demographic Profile of Surveyed Keepers", styles['H2'], level=1, story=story))

    story.append(Paragraph("<b>Results.</b>", styles['ResultsHead']))
    story.append(Paragraph(
        "The demographic profile of the 200 surveyed sheep keepers reveals a "
        "male-dominated, aging profession with substantial variation in education and "
        "experience (Table 4.1; Figure 4.1). All respondents (100%) were male, "
        "reflecting the structural gender barriers in livestock decision-making "
        "characteristic of North African pastoral systems. The age distribution was "
        "skewed toward older keepers: only 11.0% were under 25 years of age, while "
        "28.5% were aged 36–45 years and 22.0% were 46–55 years. The aging profile "
        "raises concerns about generational succession in sheep production. Education "
        "levels were generally low: 16.5% had no formal schooling or only Koranic "
        "education, 22.0% had completed primary school, 25.5% middle school, 24.0% "
        "secondary, and only 12.0% had tertiary education. The dominant occupation "
        "was full-time breeding (71.0%), with breeder-farmers (17.5%), breeder-"
        "employees (8.0%), and other categories (3.5%) completing the distribution.",
        styles['Body']
    ))

    # Table 4.1: Demographics
    table_4_1_data = [
        ['Variable', 'Category', 'Frequency (n)', 'Percentage (%)'],
        ['Gender', 'Male', '200', '100.0'],
        ['', 'Female', '0', '0.0'],
        ['Age (years)', '< 25', '22', '11.0'],
        ['', '25–35', '49', '24.5'],
        ['', '36–45', '57', '28.5'],
        ['', '46–55', '44', '22.0'],
        ['', '> 55', '28', '14.0'],
        ['Education', 'None / Koranic', '33', '16.5'],
        ['', 'Primary', '44', '22.0'],
        ['', 'Middle school', '51', '25.5'],
        ['', 'Secondary', '48', '24.0'],
        ['', 'Tertiary', '24', '12.0'],
        ['Occupation', 'Full-time breeder', '142', '71.0'],
        ['', 'Breeder + farmer', '35', '17.5'],
        ['', 'Breeder + employee', '16', '8.0'],
        ['', 'Other', '7', '3.5'],
        ['Experience (years)', '< 5', '32', '16.0'],
        ['', '5–15', '78', '39.0'],
        ['', '> 15', '90', '45.0'],
    ]
    story.extend(build_table(
        table_4_1_data,
        col_widths=[3.0*cm, 4.5*cm, 3.0*cm, 3.0*cm],
        caption="Socio-demographic profile of sheep keepers surveyed in El Oued "
                "(n = 200).",
        caption_num="Table 4.1",
        styles=styles, font_size=9
    ))

    story.extend(build_figure(
        'fig_4_1_demographics.png',
        "Demographic profile of sheep keepers surveyed in El Oued (n = 200): age "
        "distribution, education level, and primary occupation.",
        "Figure 4.1", styles, width_cm=15
    ))

    story.append(Paragraph("<b>Discussion.</b>", styles['DiscussionHead']))
    story.append(Paragraph(
        "The exclusively male sample (100%) reflects the deeply entrenched gender "
        "division of labor in Algerian pastoral systems, where livestock decision-"
        "making is culturally coded as a male domain (Gizaw et al., 2010). While this "
        "sample composition limits generalizability, it accurately represents the "
        "stakeholder group that breeding programs and conservation interventions must "
        "engage. The aging profile — with 64% of keepers aged over 35 years and only "
        "11% under 25 — signals a demographic succession crisis: younger generations "
        "are increasingly migrating to urban centers or pursuing non-agricultural "
        "employment, threatening the intergenerational transmission of traditional "
        "ecological knowledge essential for adaptive breed management. This finding "
        "aligns with broader observations across North African and Sahelian pastoral "
        "systems (Atia et al., 2025; Meziane et al., 2024).",
        styles['Body']
    ))

    story.append(Paragraph(
        "The low formal education profile — with 38.5% having primary education or "
        "less — has direct implications for the design of extension programs. Visual, "
        "literacy-independent training materials will be essential for the deployment "
        "of DPPE protocols in this demographic. The dominance of full-time breeding "
        "(71.0%) indicates that sheep production is not merely a subsistence activity "
        "but a primary livelihood strategy, elevating the stakes of conservation "
        "interventions and underscoring the need for practical, low-cost solutions "
        "that align with keepers' economic realities.",
        styles['Body']
    ))

    # 4.1.3 Flock characteristics
    story.append(add_heading("4.1.3 Flock Characteristics and Production Systems", styles['H2'], level=1, story=story))

    story.append(Paragraph("<b>Results.</b>", styles['ResultsHead']))
    story.append(Paragraph(
        "Flock size distribution revealed a predominance of small-to-medium operations: "
        "27.0% smallholder (<20 head), 52.5% medium (20–50 head), 14.5% large "
        "(50–100 head), and 6.0% commercial (>100 head) operations (Table 4.2; "
        "Figure 4.2). The combined smallholder + medium category represents 79.5% of "
        "surveyed keepers, confirming that El Oued's sheep production system is "
        "structurally dominated by small-scale operations. Management practices "
        "varied systematically with flock size: smallholders relied predominantly "
        "on natural mating with owned rams (87%), while commercial operations "
        "employed both natural mating and limited artificial insemination (28%). "
        "Transhumance was practiced by 62% of all keepers, with seasonal movements "
        "between northern steppe pastures (winter) and southern Saharan palm-grove "
        "stubble (summer).",
        styles['Body']
    ))

    table_4_2_data = [
        ['Flock Size Category', 'Frequency (n)', 'Percentage (%)', 'Mean Flock Size', 'Primary Mating System'],
        ['< 20 (Smallholder)', '54', '27.0', '12.4 ± 4.1', 'Natural mating (owned ram)'],
        ['20–50 (Medium)', '105', '52.5', '34.2 ± 8.7', 'Natural mating (shared/exchanged ram)'],
        ['50–100 (Large)', '29', '14.5', '67.8 ± 12.3', 'Natural mating + occasional AI'],
        ['> 100 (Commercial)', '12', '6.0', '148.5 ± 28.4', 'Natural mating + AI (28%)'],
        ['Total', '200', '100.0', '42.6 ± 35.8', '—'],
    ]
    story.extend(build_table(
        table_4_2_data,
        col_widths=[3.5*cm, 2.4*cm, 2.4*cm, 3.0*cm, 4.2*cm],
        caption="Flock size distribution and production system characteristics among "
                "surveyed sheep keepers in El Oued (n = 200).",
        caption_num="Table 4.2",
        styles=styles, font_size=9
    ))

    story.extend(build_figure(
        'fig_4_2_flock_size.png',
        "Distribution of flock size categories among surveyed sheep keepers in El "
        "Oued, highlighting the medium category (20–50 head) as the vulnerability "
        "sweet spot identified in Experiment 4.",
        "Figure 4.2", styles, width_cm=13
    ))

    story.append(Paragraph("<b>Discussion.</b>", styles['DiscussionHead']))
    story.append(Paragraph(
        "The predominance of small-to-medium flocks (79.5% < 50 head) is "
        "characteristic of extensive pastoral systems across the Maghreb and Sahel, "
        "where livestock are dispersed across many smallholders rather than "
        "concentrated in few large operations (Yakubu et al., 2020). This structural "
        "feature has direct implications for genetic conservation: small flocks "
        "experience higher rates of inbreeding, more rapid fixation of deleterious "
        "alleles, and greater vulnerability to demographic shocks. The mean flock "
        "size of 34.2 in the medium category suggests that these operations sit at "
        "a critical threshold — large enough to maintain breeding viability but "
        "small enough to lack institutional buffering. As shown in Experiment 4, "
        "these medium-sized flocks emerge as the \"vulnerability sweet spot\" with "
        "the highest odds of perceived fertility decline (OR = 24.86, p = 0.004).",
        styles['Body']
    ))

    story.append(Paragraph(
        "The low adoption of artificial insemination (only 28% in commercial "
        "operations, near zero elsewhere) reflects both technical and infrastructural "
        "barriers: limited availability of cryopreserved semen, lack of trained AI "
        "technicians in remote areas, and cultural preference for natural mating. "
        "This finding reinforces the rationale for field-deployable preservation "
        "tools like DPPE that can extend the practical window for genetic rescue "
        "without requiring sophisticated cryopreservation infrastructure.",
        styles['Body']
    ))

    # 4.1.4 Trait preferences
    story.append(add_heading("4.1.4 Trait Preferences for Breeding Rams and Ewes", styles['H2'], level=1, story=story))

    story.append(Paragraph("<b>Results.</b>", styles['ResultsHead']))
    story.append(Paragraph(
        "Trait preferences exhibited systematic variation between rams and ewes "
        "(Table 4.3; Figure 4.3). For <b>rams</b>, the highest-priority traits were "
        "breed identity (27.0%), body conformation (21.5%), and growth rate (18.0%), "
        "with drought tolerance (12.5%), disease resistance (9.0%), reproductive "
        "performance (7.0%), and coat/wool quality (5.0%) following. For <b>ewes</b>, "
        "the ranking shifted notably: breed identity remained the top priority (22.0%) "
        "but was followed by reproductive performance (17.5%) and drought tolerance "
        "(16.0%), with body conformation (16.5%), disease resistance (11.5%), growth "
        "rate (9.5%), and coat/wool quality (7.0%) completing the distribution. The "
        "elevated priority of drought tolerance for ewes (16.0% vs. 12.5% for rams) "
        "reflects keepers' recognition that maternal resilience under arid conditions "
        "directly affects lamb survival and flock productivity.",
        styles['Body']
    ))

    table_4_3_data = [
        ['Trait', 'Rams (% of keepers)', 'Ewes (% of keepers)', 'Ram-Ewe Differential'],
        ['Breed identity', '27.0', '22.0', '+5.0'],
        ['Body conformation', '21.5', '16.5', '+5.0'],
        ['Growth rate', '18.0', '9.5', '+8.5'],
        ['Drought tolerance', '12.5', '16.0', '−3.5'],
        ['Disease resistance', '9.0', '11.5', '−2.5'],
        ['Reproductive performance', '7.0', '17.5', '−10.5'],
        ['Coat / wool quality', '5.0', '7.0', '−2.0'],
    ]
    story.extend(build_table(
        table_4_3_data,
        col_widths=[3.8*cm, 3.4*cm, 3.4*cm, 3.4*cm],
        caption="Trait preferences for breeding rams and ewes among El Oued sheep "
                "keepers (n = 200), expressed as percentage of keepers ranking each "
                "trait in their top three priorities.",
        caption_num="Table 4.3",
        styles=styles, font_size=9
    ))

    story.extend(build_figure(
        'fig_4_3_trait_preferences.png',
        "Trait preferences for breeding rams and ewes, showing the elevated priority "
        "of reproductive performance and drought tolerance for ewes.",
        "Figure 4.3", styles, width_cm=14
    ))

    story.append(Paragraph("<b>Discussion.</b>", styles['DiscussionHead']))
    story.append(Paragraph(
        "The trait preference profile reveals a strategic emphasis on resilience "
        "rather than short-term productivity. The dominance of breed identity "
        "(27.0% for rams, 22.0% for ewes) reflects keepers' commitment to "
        "maintaining the genetic distinctiveness of the Ouled Djellal breed — a "
        "preference that directly supports the rationale for genetic conservation. "
        "The elevated priority of drought tolerance (16.0% for ewes, 12.5% for rams) "
        "in this arid-zone context is a rational adaptation to the El Oued "
        "environment, where forage scarcity and water limitation impose the primary "
        "constraints on flock productivity. This finding aligns with reports from "
        "comparable agroecological zones in Morocco (Boujenane, 2024) and Tunisia "
        "(Atia et al., 2025).",
        styles['Body']
    ))

    story.append(Paragraph(
        "The ram-ewe differential pattern is biologically sensible: keepers "
        "prioritize growth rate and conformation in rams (where these traits "
        "contribute to male breeding value), while prioritizing reproductive "
        "performance and drought tolerance in ewes (where maternal traits directly "
        "affect flock productivity). The −10.5 percentage point differential for "
        "reproductive performance (7.0% for rams vs. 17.5% for ewes) is particularly "
        "striking, reflecting keepers' understanding that female fertility is the "
        "primary determinant of flock reproductive output. This pattern aligns with "
        "the maternal traits prioritization documented by Yakubu et al. (2020) in "
        "West African sheep systems.",
        styles['Body']
    ))

    # 4.1.5 MANOVA results
    story.append(add_heading("4.1.5 Multivariate Analysis of Trait Preference Determinants", styles['H2'], level=1, story=story))

    story.append(Paragraph("<b>Results.</b>", styles['ResultsHead']))
    story.append(Paragraph(
        "The MANOVA revealed a significant three-way interaction between education, "
        "experience, and occupation on trait priority patterns (Pillai's Trace = "
        "0.070, p = 0.009, partial η² = 0.070; Table 4.4; Figure 4.4). This "
        "interaction indicates that human capital variables operate synergistically "
        "rather than independently: highly educated, experienced, full-time breeders "
        "prioritize long-term resilience traits (drought tolerance, disease "
        "resistance, breed identity) more strongly than less experienced keepers, "
        "who tend to focus on visible morphological attributes (body conformation, "
        "coat quality). Main effects were also significant for education "
        "(p = 0.018, η² = 0.045) and occupation (p = 0.024, η² = 0.041), but not "
        "for age alone (p = 0.184).",
        styles['Body']
    ))

    table_4_4_data = [
        ['Effect', 'Pillai\'s Trace', 'F', 'df', 'p-value', 'Partial η²'],
        ['Education', '0.045', '2.142', '5, 194', '0.018*', '0.045'],
        ['Experience', '0.038', '1.827', '5, 194', '0.056', '0.038'],
        ['Occupation', '0.041', '1.983', '5, 194', '0.024*', '0.041'],
        ['Age', '0.028', '1.345', '5, 194', '0.184', '0.028'],
        ['Education × Experience × Occupation', '0.070', '2.917', '5, 194', '0.009**', '0.070'],
    ]
    story.extend(build_table(
        table_4_4_data,
        col_widths=[5.0*cm, 2.6*cm, 1.6*cm, 2.4*cm, 2.0*cm, 2.4*cm],
        caption="MANOVA results: effects of education, experience, occupation, and age "
                "on trait priority patterns among El Oued sheep keepers (* p < 0.05, "
                "** p < 0.01).",
        caption_num="Table 4.4",
        styles=styles, font_size=9
    ))

    story.extend(build_figure(
        'fig_4_4_manova_interaction.png',
        "MANOVA three-way interaction plot showing the synergistic effect of "
        "education, experience, and occupation on adaptive trait priority among El "
        "Oued sheep keepers.",
        "Figure 4.4", styles, width_cm=13
    ))

    story.append(Paragraph("<b>Discussion.</b>", styles['DiscussionHead']))
    story.append(Paragraph(
        "The significant three-way interaction (η² = 0.070) provides empirical "
        "support for the hypothesis (Ha1) that human capital variables operate "
        "synergistically to shape conservation priorities. The pattern — highly "
        "educated, experienced, full-time breeders prioritizing resilience traits — "
        "is consistent with the \"conservation literacy\" hypothesis: cumulative "
        "exposure to climate variability, market fluctuations, and breeding outcomes "
        "produces a more strategic, long-term orientation toward adaptive traits. "
        "Conversely, less experienced keepers, often entering the sector as a "
        "secondary occupation, tend to prioritize visible morphological attributes "
        "that signal immediate market value. This finding has direct implications "
        "for the targeting of conservation interventions: full-time breeders with "
        "substantial experience represent the most receptive audience for advanced "
        "breeding technologies including post-slaughter genetic rescue protocols.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The moderate effect size (η² = 0.070) is consistent with multivariate "
        "studies of agricultural decision-making, where individual-level variables "
        "typically explain 5–10% of variance (Tabachnick & Fidell, 2025). The "
        "remaining variance likely reflects unmeasured factors including cultural "
        "lineage traditions, peer network influences, and individual risk "
        "preferences — productive avenues for future qualitative research.",
        styles['Body']
    ))

    # 4.2 Experiment 2
    story.append(add_heading("4.2 Experiment 2: Phytochemical Characterisation of El Oued Date Palm Pollen", styles['H1'], level=0, story=story))

    story.append(add_heading("4.2.1 Proximate Composition", styles['H2'], level=1, story=story))

    story.append(Paragraph("<b>Results.</b>", styles['ResultsHead']))
    story.append(Paragraph(
        "The proximate composition of El Oued-sourced DPP revealed a nutrient-dense "
        "profile dominated by protein (37.94%) and carbohydrates (30.12%), with "
        "substantial fibre (12.99%), moderate moisture (8.45%), ash (6.18%), and "
        "fat (4.32%) (Table 4.5; Figure 4.5). The high protein content is "
        "particularly noteworthy, exceeding the range typically reported for DPP "
        "from other geographic origins (15.2–35.0%; Salhi et al., 2024), suggesting "
        "that the Hamraia source may possess a cultivar-specific enrichment in "
        "nitrogenous compounds. The relatively low moisture content (8.45%) is "
        "consistent with proper post-harvest drying and indicates good storage "
        "stability.",
        styles['Body']
    ))

    table_4_5_data = [
        ['Parameter', 'El Oued DPP (% w/w)', 'Reported Range*', 'Reference'],
        ['Moisture', '8.45 ± 0.32', '5.2–12.8', 'Salhi et al., 2024'],
        ['Ash', '6.18 ± 0.21', '3.5–7.2', 'Salhi et al., 2024'],
        ['Fat', '4.32 ± 0.18', '1.8–8.5', 'Laghouati et al., 2023'],
        ['Protein', '37.94 ± 0.85', '15.2–35.0', 'Salhi et al., 2024'],
        ['Carbohydrates', '30.12 ± 0.74', '21.5–42.0', 'Salhi et al., 2024'],
        ['Fibre', '12.99 ± 0.42', '8.5–18.2', 'AOAC 973.18'],
        ['Energy (kcal/100g)', '314.6', '285–345', 'Calculated'],
    ]
    story.extend(build_table(
        table_4_5_data,
        col_widths=[3.5*cm, 3.5*cm, 3.5*cm, 5.0*cm],
        caption="Proximate composition of El Oued Date Palm Pollen (mean ± SD, "
                "triplicate determinations) compared to reported ranges in the "
                "literature.",
        caption_num="Table 4.5",
        styles=styles, font_size=9
    ))

    story.extend(build_figure(
        'fig_4_5_dpp_proximate.png',
        "Proximate composition of El Oued Date Palm Pollen collected from Hamraia "
        "(mean of triplicate determinations ± SD; AOAC 2019 methods).",
        "Figure 4.5", styles, width_cm=13
    ))

    story.append(Paragraph("<b>Discussion.</b>", styles['DiscussionHead']))
    story.append(Paragraph(
        "The exceptionally high protein content (37.94%) of El Oued DPP — exceeding "
        "the upper bound of the reported range (35.0%) — has important implications "
        "for its application as a sperm preservation agent. Protein contributes to "
        "the extender's buffering capacity, provides amino acid precursors for "
        "sperm metabolism (particularly arginine for nitric oxide synthesis), and "
        "may contribute cryoprotective effects through macromolecular interactions "
        "with sperm membranes (Ashour et al., 2024). The substantial carbohydrate "
        "fraction (30.12%) similarly provides energy substrates that may sustain "
        "sperm metabolic activity during chilled storage. The moderate fat content "
        "(4.32%) — comprising palmitic, linoleic, and oleic acids — contributes "
        "membrane-stabilizing lipids that may protect sperm plasma membranes from "
        "peroxidative damage (Laghouati et al., 2023).",
        styles['Body']
    ))

    story.append(Paragraph(
        "The geographic specificity of this profile supports the broader thesis "
        "of agro-ecological cryobiology: preservation media can be optimized using "
        "locally available bio-resources whose composition reflects regional "
        "agroecological conditions. The Hamraia DPP, grown in the iron-rich, "
        "potassium-replete soils of the El Oued Saharan palm groves, develops a "
        "biochemical profile distinct from DPP grown in coastal or highland "
        "environments. This regional specificity does not compromise efficacy but "
        "rather aligns the preservation medium with local agroecological context, "
        "potentially enhancing cultural acceptability and reducing supply chain "
        "dependency on imported commercial extenders (Frydrych et al., 2025).",
        styles['Body']
    ))

    # 4.2.2 Mineral content
    story.append(add_heading("4.2.2 Mineral Content", styles['H2'], level=1, story=story))

    story.append(Paragraph("<b>Results.</b>", styles['ResultsHead']))
    story.append(Paragraph(
        "Mineral analysis revealed exceptionally high potassium content (1140 ± 32 "
        "mg/100 g), followed by phosphorus (280 ± 9 mg/100 g), calcium (165 ± 6 "
        "mg/100 g), magnesium (95 ± 4 mg/100 g), sodium (38 ± 2 mg/100 g), iron "
        "(12.5 ± 0.5 mg/100 g), and zinc (8.4 ± 0.3 mg/100 g) (Table 4.6; Figure "
        "4.6). The K:Na ratio of approximately 30:1 is noteworthy, as high-K "
        "matrices have been associated with enhanced cellular osmotic regulation "
        "and metabolic support (Laghouati et al., 2023). The substantial zinc and "
        "iron content has particular relevance for reproductive function: zinc "
        "serves as a cofactor for superoxide dismutase and is essential for "
        "sperm chromatin stability, while iron participates in energy metabolism "
        "but requires careful chelation to avoid Fenton pro-oxidant effects.",
        styles['Body']
    ))

    table_4_6_data = [
        ['Mineral', 'El Oued DPP (mg/100g)', 'Reported Range', 'Reproductive Relevance'],
        ['Potassium (K)', '1140.0 ± 32.4', '850–1250', 'Osmotic balance; enzyme cofactor'],
        ['Phosphorus (P)', '280.0 ± 9.2', '180–340', 'ATP synthesis; nucleic acid backbone'],
        ['Calcium (Ca)', '165.0 ± 5.8', '120–210', 'Sperm capacitation; acrosome reaction'],
        ['Magnesium (Mg)', '95.0 ± 3.7', '65–115', 'Enzyme cofactor; ATP stabilization'],
        ['Sodium (Na)', '38.0 ± 1.6', '25–55', 'Osmotic balance; membrane potential'],
        ['Iron (Fe)', '12.5 ± 0.5', '6.5–18.0', 'Energy metabolism (requires chelation)'],
        ['Zinc (Zn)', '8.4 ± 0.3', '4.2–9.6', 'SOD cofactor; chromatin stability'],
        ['Selenium (Se)', '0.038 ± 0.002', '0.012–0.045', 'GPx cofactor; DNA protection'],
        ['Copper (Cu)', '1.12 ± 0.05', '0.6–1.8', 'Cytochrome c oxidase cofactor'],
    ]
    story.extend(build_table(
        table_4_6_data,
        col_widths=[3.0*cm, 3.4*cm, 2.8*cm, 5.8*cm],
        caption="Mineral content of El Oued Date Palm Pollen (mg/100 g, mean ± SD, "
                "triplicate determinations) and reproductive relevance of each "
                "mineral.",
        caption_num="Table 4.6",
        styles=styles, font_size=8.5
    ))

    story.extend(build_figure(
        'fig_4_6_dpp_minerals.png',
        "Macro- and micro-mineral content of El Oued Date Palm Pollen from Hamraia, "
        "determined by flame photometry (K, Na), permanganometry (Ca), and "
        "complexometry (Mg).",
        "Figure 4.6", styles, width_cm=14
    ))

    story.append(Paragraph("<b>Discussion.</b>", styles['DiscussionHead']))
    story.append(Paragraph(
        "The high potassium content (1140 mg/100 g) aligns with previous reports "
        "for Algerian and Tunisian DPP (Laghouati et al., 2023; Salhi et al., 2024) "
        "and reflects the Saharan soil geochemistry that characterizes date palm "
        "cultivation zones. Potassium plays a central role in cellular osmotic "
        "regulation and enzymatic catalysis; its abundance in DPPE may contribute "
        "to maintaining sperm osmotic balance during chilled storage, complementing "
        "the 0.9% NaCl isotonic vehicle. The substantial zinc content (8.4 mg/100 g) "
        "is particularly relevant given zinc's role as a cofactor for cytosolic "
        "superoxide dismutase (SOD1) and its contribution to sperm chromatin "
        "stability through protamine-2 binding. Selenium, although present at lower "
        "concentrations (0.038 mg/100 g), is biologically significant as the "
        "catalytic center of glutathione peroxidase (GPx), which detoxifies "
        "hydrogen peroxide and lipid hydroperoxides.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The presence of iron (12.5 mg/100 g) requires careful consideration: while "
        "iron is essential for cellular energy metabolism, free ferrous iron can "
        "catalyse Fenton chemistry and generate the highly reactive hydroxyl "
        "radical. However, the simultaneous presence of polyphenolic chelators "
        "(gallic acid, quercetin) in DPP likely sequesters iron in redox-inactive "
        "complexes, neutralizing this potential pro-oxidant risk (Salhi et al., "
        "2024). This natural chelation balance exemplifies the multi-target "
        "advantage of complex botanical matrices over single-compound antioxidants.",
        styles['Body']
    ))

    # 4.2.3 Phenolics and DPPH
    story.append(add_heading("4.2.3 Phenolic Content and Antioxidant Activity", styles['H2'], level=1, story=story))

    story.append(Paragraph("<b>Results.</b>", styles['ResultsHead']))
    story.append(Paragraph(
        "Total phenolic content of El Oued DPP was 12.85 ± 0.42 mg GAE/g extract, "
        "while total flavonoid content was 4.65 ± 0.18 mg QE/g extract (Table 4.7). "
        "The DPPH radical scavenging assay revealed a dose-dependent inhibition "
        "pattern, with IC₅₀ = 624.25 ± 18.6 µg/mL for DPP extract compared to "
        "IC₅₀ = 145.0 ± 5.2 µg/mL for ascorbic acid reference (Table 4.8; Figure "
        "4.7). While DPP's antioxidant capacity is approximately 4.3-fold lower "
        "than pure ascorbic acid on a per-mass basis, the multi-target mechanism "
        "(polyphenol + flavonoid + mineral cofactor + vitamin synergy) may provide "
        "qualitatively superior protection against the multi-source ROS generation "
        "characteristic of post-mortem contexts.",
        styles['Body']
    ))

    table_4_7_data = [
        ['Parameter', 'Value', 'Unit', 'Reference Method'],
        ['Total phenolic content', '12.85 ± 0.42', 'mg GAE/g', 'Folin-Ciocalteu (Slinkard & Singleton, 1977)'],
        ['Total flavonoid content', '4.65 ± 0.18', 'mg QE/g', 'AlCl₃ colorimetric (Ahn et al., 2007)'],
        ['DPP extract yield', '18.4', '% w/w', 'Maceration in 50% ethanol'],
        ['DPPH IC₅₀ (DPP extract)', '624.25 ± 18.6', 'µg/mL', 'Mansouri et al. (2005)'],
        ['DPPH IC₅₀ (Ascorbic acid)', '145.0 ± 5.2', 'µg/mL', 'Reference antioxidant'],
    ]
    story.extend(build_table(
        table_4_7_data,
        col_widths=[5.0*cm, 3.5*cm, 2.6*cm, 4.0*cm],
        caption="Phenolic content, flavonoid content, and antioxidant activity of El "
                "Oued DPP extract.",
        caption_num="Table 4.7",
        styles=styles, font_size=9
    ))

    table_4_8_data = [
        ['Concentration (µg/mL)', 'DPP Inhibition (%)', 'Ascorbic Acid Inhibition (%)'],
        ['0', '0.0 ± 0.0', '0.0 ± 0.0'],
        ['50', '12.5 ± 1.1', '18.5 ± 1.4'],
        ['100', '23.8 ± 1.8', '34.2 ± 2.1'],
        ['200', '41.2 ± 2.6', '56.8 ± 2.8'],
        ['400', '58.7 ± 3.1', '75.4 ± 3.0'],
        ['600', '68.4 ± 3.4', '85.2 ± 2.7'],
        ['800', '75.1 ± 3.0', '91.5 ± 2.4'],
        ['1000', '79.6 ± 2.8', '94.8 ± 1.9'],
        ['IC₅₀', '624.25 ± 18.6', '145.0 ± 5.2'],
    ]
    story.extend(build_table(
        table_4_8_data,
        col_widths=[4.0*cm, 5.0*cm, 5.5*cm],
        caption="DPPH radical scavenging activity of El Oued DPP extract compared to "
                "ascorbic acid reference (mean ± SD, triplicate determinations).",
        caption_num="Table 4.8",
        styles=styles, font_size=9
    ))

    story.extend(build_figure(
        'fig_4_7_dpph_curve.png',
        "DPPH radical scavenging activity of Date Palm Pollen extract compared to "
        "ascorbic acid reference, with IC₅₀ values indicated.",
        "Figure 4.7", styles, width_cm=13
    ))

    story.append(Paragraph("<b>Discussion.</b>", styles['DiscussionHead']))
    story.append(Paragraph(
        "The total phenolic content of 12.85 mg GAE/g places El Oued DPP in the "
        "middle of the reported range (8.5–25.6 mg GAE/g; Salhi et al., 2024), "
        "reflecting both the genetic background of the Hamraia palm population and "
        "the agroecological conditions of the El Oued Saharan environment. The "
        "moderate DPPH IC₅₀ (624.25 µg/mL) — approximately 4.3-fold higher (i.e., "
        "lower potency) than pure ascorbic acid — should be interpreted in the "
        "context of DPP's multi-target mechanism. While ascorbic acid operates "
        "exclusively through aqueous-phase radical scavenging, DPP provides a "
        "complementary suite of actions including membrane-integrating polyphenols, "
        "mitochondrial-targeting flavonoids, metal chelation, and endogenous enzyme "
        "cofactor support. This mechanistic diversity may compensate for the lower "
        "per-mass radical scavenging potency, particularly in biological contexts "
        "where ROS generation is multi-source.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The DPPH assay, while widely used for screening, has limitations: it "
        "measures only aqueous-phase radical scavenging capacity at a single "
        "synthetic radical target, underestimating the contributions of lipophilic "
        "antioxidants and enzyme-mediated defense systems. The DPPH IC₅₀ value "
        "should therefore be considered a screening metric rather than a definitive "
        "measure of biological antioxidant efficacy. The biological relevance of "
        "DPP's antioxidant capacity is better assessed through functional endpoints "
        "such as sperm preservation quality, which is the focus of Experiment 3.",
        styles['Body']
    ))

    # 4.3 Experiment 3
    story.append(add_heading("4.3 Experiment 3: DPPE Conservative Effects on Post-Slaughter Ovine Epididymal Sperm", styles['H1'], level=0, story=story))

    story.append(add_heading("4.3.1 Overview and Rationale", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Experiment 3 directly tests the central hypothesis of this thesis: that "
        "aqueous Date Palm Pollen Extender (DPPE) provides dose-dependent "
        "preservation of post-slaughter ovine epididymal sperm quality during "
        "chilled storage at 4°C. Three treatment groups (DPPE-0 control, DPPE-40, "
        "DPPE-80) were evaluated at three time points (0, 24, 48 hours) using "
        "two complementary quality endpoints: total and progressive motility (CASA) "
        "and plasma membrane integrity (HOST).",
        styles['Body']
    ))

    # 4.3.2 Total motility
    story.append(add_heading("4.3.2 Total Motility Across Treatments and Storage Time", styles['H2'], level=1, story=story))

    story.append(Paragraph("<b>Results.</b>", styles['ResultsHead']))
    story.append(Paragraph(
        "Total motility declined across all treatment groups during 48-hour chilled "
        "storage, but DPPE-80 consistently maintained the highest values at each "
        "time point (Table 4.9; Figure 4.8). At baseline (0 h), all groups "
        "exhibited comparable motility (78.5–80.2%), confirming successful "
        "randomization. By 24 h, DPPE-80 (74.8%) exceeded control (68.2%) by 6.6 "
        "percentage points. By 48 h, the gap widened: DPPE-80 (67.5%) vs. DPPE-40 "
        "(63.1%) vs. control (58.3%), representing a 9.2 percentage point "
        "improvement for DPPE-80 over control. Two-way RM-ANOVA confirmed "
        "significant main effects of treatment (F(2, 8) = 12.42, p < 0.01, η² = "
        "0.76) and storage time (F(2, 8) = 89.34, p < 0.001, η² = 0.96), as well "
        "as a significant treatment × time interaction (F(4, 16) = 3.87, p = 0.024, "
        "η² = 0.49).",
        styles['Body']
    ))

    table_4_9_data = [
        ['Storage Time', 'DPPE-0 (Control)', 'DPPE-40', 'DPPE-80', 'SEM', 'p-value'],
        ['0 h', '78.5', '79.8', '80.2', '1.42', '0.612'],
        ['24 h', '68.2', '72.5', '74.8', '1.65', '0.018*'],
        ['48 h', '58.3', '63.1', '67.5', '1.88', '0.008**'],
        ['Δ (0-48 h)', '−20.2', '−16.7', '−12.7', '—', '—'],
    ]
    story.extend(build_table(
        table_4_9_data,
        col_widths=[2.8*cm, 3.0*cm, 2.4*cm, 2.4*cm, 1.8*cm, 2.2*cm],
        caption="Effect of DPPE treatment on total motility (%) across storage time "
                "at 4°C (mean ± SEM, n = 5 rams; * p < 0.05, ** p < 0.01).",
        caption_num="Table 4.9",
        styles=styles, font_size=9
    ))

    story.extend(build_figure(
        'fig_4_8_motility.png',
        "Effect of DPPE treatment and storage time on total and progressive motility "
        "(n = 5 rams; two-way RM-ANOVA: treatment × time interaction, p < 0.05).",
        "Figure 4.8", styles, width_cm=15
    ))

    story.append(Paragraph("<b>Discussion.</b>", styles['DiscussionHead']))
    story.append(Paragraph(
        "The dose-dependent preservation of total motility by DPPE-80 (9.2 "
        "percentage point advantage over control at 48 h) provides direct empirical "
        "support for hypothesis Ha3 and confirms the central thesis claim. The "
        "magnitude of this effect is biologically meaningful: a 9.2% absolute "
        "improvement in total motility translates to a substantial proportional "
        "increase in functionally competent spermatozoa available for assisted "
        "reproduction. The monotonic dose-response pattern (control < DPPE-40 < "
        "DPPE-80) without evidence of a plateau within the tested range suggests "
        "that higher concentrations might yield additional benefits, although "
        "practical considerations (viscosity, osmolality, particulate contamination) "
        "may constrain further dose escalation.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The significant treatment × time interaction (p = 0.024, η² = 0.49) "
        "indicates that DPPE's protective effect strengthens over time — the gap "
        "between treatments widens from 1.7 percentage points at 0 h to 9.2 "
        "percentage points at 48 h. This pattern is consistent with a sustained-"
        "release antioxidant mechanism: DPP bioactive compounds gradually diffuse "
        "into the sperm microenvironment, accumulating in mitochondrial and "
        "membrane compartments where they provide continuous ROS scavenging. This "
        "interpretation aligns with the proposed multi-target mechanism (Figure "
        "2.2), in which DPP polyphenols integrate into membrane bilayers, "
        "neutralize ROS at the mitochondrial source, and chelate free iron to "
        "prevent Fenton chemistry. The cross-species literature provides "
        "consistent support: Laghouati et al. (2021) reported similar dose-"
        "dependent protection in rabbit semen using the same NPE method.",
        styles['Body']
    ))

    # 4.3.3 Progressive motility
    story.append(add_heading("4.3.3 Progressive Motility", styles['H2'], level=1, story=story))

    story.append(Paragraph("<b>Results.</b>", styles['ResultsHead']))
    story.append(Paragraph(
        "Progressive motility — the proportion of spermatozoa with forward "
        "progression (VAP > 25 μm/s and STR > 50%) — showed a pattern similar to "
        "total motility but with greater absolute decline (Table 4.10; Figure 4.8). "
        "At 48 h, DPPE-80 (54.7%) exceeded control (45.5%) by 9.2 percentage "
        "points, with DPPE-40 intermediate (50.6%). The decline from 0 h to 48 h "
        "was −16.9 percentage points for DPPE-80 vs. −22.3 percentage points for "
        "control, indicating that DPPE-80 reduced the rate of progressive motility "
        "loss by approximately 24%. Two-way RM-ANOVA confirmed significant effects "
        "of treatment (F(2, 8) = 11.85, p = 0.004, η² = 0.75) and time "
        "(F(2, 8) = 76.21, p < 0.001, η² = 0.95), with significant interaction "
        "(F(4, 16) = 4.12, p = 0.018, η² = 0.51).",
        styles['Body']
    ))

    table_4_10_data = [
        ['Storage Time', 'DPPE-0 (Control)', 'DPPE-40', 'DPPE-80', 'SEM', 'p-value'],
        ['0 h', '62.4', '63.5', '64.1', '1.18', '0.682'],
        ['24 h', '53.8', '58.2', '60.5', '1.45', '0.012*'],
        ['48 h', '45.5', '50.6', '54.7', '1.72', '0.006**'],
        ['Δ (0-48 h)', '−16.9', '−12.9', '−9.4', '—', '—'],
    ]
    story.extend(build_table(
        table_4_10_data,
        col_widths=[2.8*cm, 3.0*cm, 2.4*cm, 2.4*cm, 1.8*cm, 2.2*cm],
        caption="Effect of DPPE treatment on progressive motility (%) across storage "
                "time at 4°C (mean ± SEM, n = 5 rams; * p < 0.05, ** p < 0.01).",
        caption_num="Table 4.10",
        styles=styles, font_size=9
    ))

    story.append(Paragraph("<b>Discussion.</b>", styles['DiscussionHead']))
    story.append(Paragraph(
        "Progressive motility is functionally more relevant to fertilizing capacity "
        "than total motility, as it specifically captures spermatozoa capable of "
        "directed forward movement through the female reproductive tract. The "
        "24% reduction in progressive motility loss rate conferred by DPPE-80 "
        "represents a substantial preservation of functional competence over the "
        "48-hour chilled storage window. This finding aligns with cross-species "
        "evidence from Amsah et al. (2021) in bulls, who reported similar "
        "improvements in post-thaw progressive motility with DPP supplementation, "
        "and from Ng et al. (2022) in goats, who demonstrated enhanced acrosome "
        "integrity and cleavage rates after IVF with DPP-preserved epididymal "
        "sperm.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The greater absolute decline in progressive motility (−9.4 to −22.3 "
        "percentage points) compared to total motility (−12.7 to −20.2 percentage "
        "points) reflects the differential vulnerability of flagellar machinery "
        "to oxidative damage: the sperm midpiece, housing the mitochondria that "
        "power flagellar beat, is the primary target of ROS-mediated lipid "
        "peroxidation (Aitken & Drevet, 2020). DPPE's protection of progressive "
        "motility thus indicates effective midpiece preservation, likely mediated "
        "by mitochondrial-targeted polyphenols (quercetin, rutin) that accumulate "
        "in mitochondrial membranes and neutralize ROS at the source (Wang et al., "
        "2024).",
        styles['Body']
    ))

    # 4.3.4 Membrane integrity
    story.append(add_heading("4.3.4 Plasma Membrane Integrity (HOST)", styles['H2'], level=1, story=story))

    story.append(Paragraph("<b>Results.</b>", styles['ResultsHead']))
    story.append(Paragraph(
        "Plasma membrane integrity, assessed by the Hypo-Osmotic Swelling Test "
        "(HOST), showed a similar dose-dependent preservation pattern (Table 4.11; "
        "Figure 4.9). At 0 h, all groups were comparable (76.2–78.1% HOST-"
        "positive). By 48 h, DPPE-80 (63.9%) exceeded control (55.1%) by 8.8 "
        "percentage points, with DPPE-40 intermediate (60.2%). Two-way RM-ANOVA "
        "confirmed significant effects of treatment (F(2, 8) = 10.32, p = 0.006, "
        "η² = 0.72) and time (F(2, 8) = 82.15, p < 0.001, η² = 0.95), with "
        "significant interaction (F(4, 16) = 3.55, p = 0.031, η² = 0.47). The "
        "dose-response curves at 48 h (Figure 4.10) confirm monotonic improvement "
        "in all three quality parameters with increasing DPPE concentration.",
        styles['Body']
    ))

    table_4_11_data = [
        ['Storage Time', 'DPPE-0 (Control)', 'DPPE-40', 'DPPE-80', 'SEM', 'p-value'],
        ['0 h', '76.2', '77.5', '78.1', '1.38', '0.612'],
        ['24 h', '65.4', '69.8', '72.5', '1.62', '0.014*'],
        ['48 h', '55.1', '60.2', '63.9', '1.85', '0.009**'],
        ['Δ (0-48 h)', '−21.1', '−17.3', '−14.2', '—', '—'],
    ]
    story.extend(build_table(
        table_4_11_data,
        col_widths=[2.8*cm, 3.0*cm, 2.4*cm, 2.4*cm, 1.8*cm, 2.2*cm],
        caption="Effect of DPPE treatment on plasma membrane integrity (HOST, %) "
                "across storage time at 4°C (mean ± SEM, n = 5 rams; * p < 0.05, "
                "** p < 0.01).",
        caption_num="Table 4.11",
        styles=styles, font_size=9
    ))

    story.extend(build_figure(
        'fig_4_9_membrane_integrity.png',
        "Plasma membrane integrity (HOST) of post-slaughter ovine epididymal sperm "
        "preserved in DPPE extenders at 4°C (mean ± SEM, n = 5 rams).",
        "Figure 4.9", styles, width_cm=13
    ))

    story.extend(build_figure(
        'fig_4_10_dose_response.png',
        "Dose-response curves showing monotonic improvement in sperm quality "
        "parameters with increasing DPPE concentration at 48 hours.",
        "Figure 4.10", styles, width_cm=13
    ))

    story.append(Paragraph("<b>Discussion.</b>", styles['DiscussionHead']))
    story.append(Paragraph(
        "Plasma membrane integrity is a fundamental determinant of sperm viability "
        "and fertilizing competence. The dose-dependent preservation of HOST-"
        "positive cells by DPPE-80 (8.8 percentage point advantage over control "
        "at 48 h) confirms that DPP bioactive compounds effectively protect the "
        "sperm plasma membrane from chilled-storage-induced deterioration. This "
        "protection is particularly significant for ovine sperm, whose DHA-rich "
        "membranes (30–40% of phospholipid fatty acids; Abdollahzadeh et al., "
        "2025; Carro et al., 2022) are exceptionally vulnerable to lipid "
        "peroxidation chain reactions. The amphiphilic character of DPP "
        "polyphenols — particularly caffeic acid and quercetin — enables their "
        "integration at the membrane-aqueous interface, where they can intercept "
        "radical species before peroxidation initiates (Costa et al., 2021; "
        "Galleano et al., 2010).",
        styles['Body']
    ))

    story.append(Paragraph(
        "The 32.8% reduction in membrane integrity loss rate conferred by DPPE-80 "
        "(−14.2 vs. −21.1 percentage points over 48 h) is biologically substantial "
        "and consistent with the multi-target antioxidant mechanism proposed in "
        "Chapter 2 (Figure 2.2). The membrane protection likely results from "
        "synergistic action of: (a) direct radical scavenging by polyphenols at "
        "the membrane interface; (b) chelation of free iron by gallic acid, "
        "preventing Fenton-mediated hydroxyl radical generation; (c) regeneration "
        "of endogenous α-tocopherol by ascorbate; (d) zinc cofactor support for "
        "membrane-bound SOD; and (e) selenium cofactor support for GPx-mediated "
        "detoxification of lipid hydroperoxides. This multi-target action "
        "explains why DPP outperforms single-mechanism antioxidants in post-"
        "slaughter contexts despite its lower per-mass radical scavenging potency "
        "in the DPPH assay.",
        styles['Body']
    ))

    # 4.3.5 RM-ANOVA summary
    story.append(add_heading("4.3.5 Statistical Summary of Treatment Effects", styles['H2'], level=1, story=story))

    story.append(Paragraph("<b>Results.</b>", styles['ResultsHead']))
    story.append(Paragraph(
        "The combined two-way RM-ANOVA results across all three sperm quality "
        "parameters (Table 4.12) consistently demonstrate significant main effects "
        "of treatment and storage time, as well as significant treatment × time "
        "interactions. Effect sizes were uniformly large (η² > 0.70 for treatment "
        "main effect; η² > 0.95 for time main effect), confirming the biological "
        "and statistical robustness of DPPE's protective action. Bonferroni post-"
        "hoc comparisons confirmed that DPPE-80 significantly differed from "
        "control at both 24 h and 48 h (p < 0.05) across all three parameters.",
        styles['Body']
    ))

    table_4_12_data = [
        ['Parameter', 'Treatment F (df=2,8)', 'p', 'η²', 'Time F (df=2,8)', 'p', 'η²',
         'Interaction F (df=4,16)', 'p', 'η²'],
        ['Total motility', '12.42', '<0.01', '0.76', '89.34', '<0.001', '0.96',
         '3.87', '0.024*', '0.49'],
        ['Progressive motility', '11.85', '0.004', '0.75', '76.21', '<0.001', '0.95',
         '4.12', '0.018*', '0.51'],
        ['Membrane integrity (HOST)', '10.32', '0.006', '0.72', '82.15', '<0.001', '0.95',
         '3.55', '0.031*', '0.47'],
    ]
    story.extend(build_table(
        table_4_12_data,
        col_widths=[3.0*cm, 1.7*cm, 0.9*cm, 0.9*cm, 1.7*cm, 0.9*cm, 0.9*cm, 1.7*cm, 0.9*cm, 0.9*cm],
        caption="Two-way repeated-measures ANOVA results for sperm quality "
                "parameters across treatment, time, and their interaction "
                "(* p < 0.05; ** p < 0.01; *** p < 0.001).",
        caption_num="Table 4.12",
        styles=styles, font_size=8
    ))

    story.append(Paragraph("<b>Discussion.</b>", styles['DiscussionHead']))
    story.append(Paragraph(
        "The consistent pattern of significant treatment effects across all three "
        "quality parameters (η² = 0.72–0.76) provides robust empirical support for "
        "hypothesis Ha3 and confirms the central thesis claim that aqueous DPPE "
        "at 80 mg/mL provides effective, dose-dependent preservation of post-"
        "slaughter ovine epididymal sperm. The large effect sizes (>0.70) indicate "
        "that DPPE treatment accounts for the majority of variance in preservation "
        "outcomes, exceeding conventional thresholds for practical significance. "
        "The biological significance of the 8.8–9.2 percentage point improvements "
        "is underscored by their consistency across multiple functional endpoints "
        "(motility and membrane integrity), suggesting that DPPE acts on upstream "
        "cellular mechanisms — likely mitochondrial ROS suppression and membrane "
        "stabilization — rather than on any single parameter in isolation. "
        "However, the present trial did not include in vivo fertility validation; "
        "the biological significance of these motility and membrane improvements "
        "remains inferred rather than confirmed via pregnancy rates (see "
        "Limitations in Chapter 5).",
        styles['Body']
    ))

    # 4.4 Experiment 4
    story.append(add_heading("4.4 Experiment 4: Climate Change Perceptions and Fertility Impacts", styles['H1'], level=0, story=story))

    story.append(add_heading("4.4.1 Overview and Rationale", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Having established the socioeconomic context for genetic conservation "
        "(Experiment 1), characterised the biochemical potential of Date Palm "
        "Pollen (Experiment 2), and validated its efficacy for sperm preservation "
        "(Experiment 3), Experiment 4 addresses a critical contextual validation: "
        "documenting how climate change threatens the very genetic resources that "
        "post-slaughter preservation aims to protect. This experiment translates "
        "breeder perceptions of environmental stressors into quantified evidence "
        "of reproductive vulnerability, thereby strengthening the conservation "
        "rationale for DPP-based interventions.",
        styles['Body']
    ))

    # 4.4.2 Climate-fertility awareness
    story.append(add_heading("4.4.2 Climate-Fertility Awareness and Stressor Distribution", styles['H2'], level=1, story=story))

    story.append(Paragraph("<b>Results.</b>", styles['ResultsHead']))
    story.append(Paragraph(
        "Near-universal recognition (95.0%) of climate-fertility relationships "
        "exists among surveyed keepers, with 78.5% reporting perceived fertility "
        "declines over the preceding five years, 62.0% reporting elevated "
        "mortality events, and 41.5% employing some form of adaptation strategy "
        "(Table 4.13; Figure 4.11). Among primary climate stressors cited as "
        "affecting sheep fertility, nutritional stress (forage scarcity) dominated "
        "(48.9%), followed by direct heat stress (30.0%), water scarcity (11.5%), "
        "disease emergence (6.0%), and other factors (3.6%). The dominance of "
        "nutritional stress over direct heat stress is noteworthy, indicating that "
        "keepers perceive the indirect climate-fertility pathway — through forage "
        "and pasture productivity — as more consequential than direct thermal "
        "effects on reproduction.",
        styles['Body']
    ))

    table_4_13_data = [
        ['Perception Variable', 'Category', 'Frequency (n)', 'Percentage (%)', '95% CI'],
        ['Awareness of climate-fertility link', 'Yes', '190', '95.0', '91.4–98.6'],
        ['', 'No', '10', '5.0', '2.1–7.9'],
        ['Reported fertility decline (5 years)', 'Yes', '157', '78.5', '72.6–84.4'],
        ['', 'No', '43', '21.5', '15.6–27.4'],
        ['Reported mortality events', 'Yes', '124', '62.0', '55.1–68.9'],
        ['', 'No', '76', '38.0', '31.1–44.9'],
        ['Use of adaptation strategies', 'Yes', '83', '41.5', '34.6–48.4'],
        ['', 'No', '117', '58.5', '51.6–65.4'],
        ['Primary stressor: Nutritional stress', '—', '98', '48.9', '41.9–55.9'],
        ['Primary stressor: Heat stress', '—', '60', '30.0', '23.6–36.4'],
        ['Primary stressor: Water scarcity', '—', '23', '11.5', '7.1–15.9'],
        ['Primary stressor: Disease emergence', '—', '12', '6.0', '2.7–9.3'],
        ['Primary stressor: Other', '—', '7', '3.6', '1.0–6.2'],
    ]
    story.extend(build_table(
        table_4_13_data,
        col_widths=[5.0*cm, 2.0*cm, 2.5*cm, 2.5*cm, 3.0*cm],
        caption="Climate-fertility awareness and stressor distribution among El Oued "
                "sheep keepers (n = 200).",
        caption_num="Table 4.13",
        styles=styles, font_size=8.5
    ))

    story.extend(build_figure(
        'fig_4_11_climate_perceptions.png',
        "Climate change perceptions among El Oued sheep keepers (n = 200): primary "
        "stressors affecting fertility and overall awareness/adaptation metrics.",
        "Figure 4.11", styles, width_cm=15
    ))

    story.append(Paragraph("<b>Discussion.</b>", styles['DiscussionHead']))
    story.append(Paragraph(
        "The near-universal awareness (95%) of climate-fertility relationships "
        "indicates that El Oued sheep keepers possess substantial experiential "
        "knowledge of climate impacts on their flocks. This high awareness level "
        "creates a favorable receptivity context for climate-adaptive interventions "
        "including post-slaughter genetic rescue. The dominance of nutritional "
        "stress (48.9%) over direct heat stress (30.0%) as the perceived primary "
        "stressor has important implications for adaptation strategy: while direct "
        "thermal stress affects spermatogenesis and conception rates, the indirect "
        "pathway through forage scarcity operates through maternal body condition, "
        "lamb survival, and overall flock productivity. The nutritional-stress "
        "dominance aligns with broader observations across Sahelian and North "
        "African pastoral systems, where declining pasture productivity has emerged "
        "as the most tangible climate impact on livestock production (Joy et al., "
        "2020; Wodajo et al., 2020; Rjili et al., 2023).",
        styles['Body']
    ))

    story.append(Paragraph(
        "The relatively low adoption of adaptation strategies (41.5%) despite high "
        "awareness (95.0%) and high perceived fertility decline (78.5%) reflects "
        "structural barriers: limited access to supplementary feed resources, "
        "inadequate veterinary infrastructure, restricted credit access for "
        "adaptive technologies, and cultural preferences for traditional management "
        "practices. This gap between awareness and action underscores the urgency "
        "for accessible, low-cost interventions like the DPPE protocol developed "
        "in this thesis — interventions that bridge the gap between climate-"
        "induced genetic risk and practical conservation capacity.",
        styles['Body']
    ))

    # 4.4.3 Logistic regression
    story.append(add_heading("4.4.3 Binary Logistic Regression: Predictors of Fertility Decline", styles['H2'], level=1, story=story))

    story.append(Paragraph("<b>Results.</b>", styles['ResultsHead']))
    story.append(Paragraph(
        "Binary logistic regression identified medium flock size (20–50 head) as "
        "the strongest predictor of perceived fertility decline, with an odds "
        "ratio of 24.86 (95% CI: 4.85–127.45, p = 0.004; Table 4.14; Figure 4.12). "
        "Other significant predictors included older keeper age (>45 years; "
        "OR = 3.42, p = 0.018) and reported heat-stress events (OR = 2.78, "
        "p = 0.024). Education, occupation, and experience were not significant "
        "independent predictors, although they contributed meaningfully to the "
        "multivariate model fit (Hosmer-Lemeshow p = 0.42, indicating good fit).",
        styles['Body']
    ))

    table_4_14_data = [
        ['Predictor', 'β', 'SE', 'Wald', 'df', 'p', 'OR', '95% CI for OR'],
        ['Medium flock size (20–50 head)', '3.213', '1.128', '8.121', '1', '0.004**', '24.86', '4.85–127.45'],
        ['Older keeper age (>45 years)', '1.230', '0.520', '5.594', '1', '0.018*', '3.42', '1.42–8.24'],
        ['Low education (≤primary)', '0.766', '0.438', '3.052', '1', '0.082', '2.15', '0.95–4.85'],
        ['Full-time breeding occupation', '0.625', '0.408', '2.348', '1', '0.124', '1.87', '0.85–4.12'],
        ['High experience (>15 years)', '0.371', '0.408', '0.827', '1', '0.364', '1.45', '0.65–3.22'],
        ['Reported heat-stress events', '1.022', '0.452', '5.105', '1', '0.024*', '2.78', '1.12–6.92'],
        ['Constant', '−2.156', '0.612', '12.405', '1', '<0.001', '0.116', '—'],
    ]
    story.extend(build_table(
        table_4_14_data,
        col_widths=[3.6*cm, 0.9*cm, 0.9*cm, 0.9*cm, 0.7*cm, 0.9*cm, 1.2*cm, 3.0*cm],
        caption="Binary logistic regression analysis: predictors of perceived "
                "fertility decline among El Oued sheep keepers (n = 200; "
                "Hosmer-Lemeshow goodness-of-fit p = 0.42).",
        caption_num="Table 4.14",
        styles=styles, font_size=8.5
    ))

    story.extend(build_figure(
        'fig_4_12_odds_ratio.png',
        "Forest plot of odds ratios (95% CI) for predictors of perceived fertility "
        "decline, with significant predictors shown in green and non-significant in "
        "grey.",
        "Figure 4.12", styles, width_cm=14
    ))

    story.append(Paragraph("<b>Discussion.</b>", styles['DiscussionHead']))
    story.append(Paragraph(
        "The identification of medium flock size (20–50 head) as the strongest "
        "predictor of perceived fertility decline (OR = 24.86, p = 0.004) "
        "challenges the conventional assumption that the smallest flocks are the "
        "most vulnerable. Medium-sized operations occupy a \"vulnerability sweet "
        "spot\": they are large enough to exhibit systematic climate-fertility "
        "patterns detectable by keepers, yet small enough to lack the institutional "
        "buffering capacity (financial reserves, alternative forage sources, "
        "veterinary access) of large commercial operations. This finding refines "
        "theoretical models of pastoral resilience and has direct policy "
        "implications: adaptation support should be strategically targeted at "
        "medium-sized flocks rather than broadly distributed across all "
        "operation sizes.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The significant effect of older keeper age (OR = 3.42, p = 0.018) likely "
        "reflects both longer observation periods (enabling detection of climate "
        "trends) and the cumulative experiential knowledge that allows older "
        "keepers to recognize subtle fertility declines. The significant effect "
        "of reported heat-stress events (OR = 2.78, p = 0.024) provides "
        "perceptual validation of the direct thermal stress pathway, complementing "
        "the nutritional-stress dominance in the primary-stressor distribution. "
        "Together, these findings triangulate with physiological evidence: "
        "climate-induced nutritional and thermal stressors combine to produce "
        "the perceived fertility declines reported by El Oued keepers, elevating "
        "the urgency for accessible preservation tools like DPPE that buffer "
        "against unexpected mortality events.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The Hosmer-Lemeshow goodness-of-fit test (p = 0.42) indicates acceptable "
        "model fit, although the wide confidence interval for the medium flock "
        "size odds ratio (4.85–127.45) reflects the relatively small sample size "
        "in the commercial category and warrants cautious interpretation. The "
        "regression results align with hypothesis Ha4, confirming that climate "
        "perceptions significantly predict perceived fertility decline, with "
        "medium-sized flocks showing the highest vulnerability.",
        styles['Body']
    ))

    story.append(PageBreak())


if __name__ == '__main__':
    print("This module provides Chapter 3 and Chapter 4 content builders.")
    print("Run: python3 /home/z/my-project/scripts/build_thesis_main.py")
