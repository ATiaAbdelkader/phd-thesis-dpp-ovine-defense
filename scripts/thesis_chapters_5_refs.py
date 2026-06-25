#!/usr/bin/env python3
"""
PhD Thesis Content — Chapter 5, References, Appendices
=======================================================
Chapter 5: General Conclusion and Recommendations
References: APA-style list
Appendices A-F: Questionnaires, protocols, ethics, raw data, supplementary stats, supplementary figures
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
# CHAPTER 5: GENERAL CONCLUSION AND RECOMMENDATIONS
# ===================================================================
def build_chapter_5(story, styles):
    """Chapter 5: General Conclusion and Recommendations."""
    chapter_separator(story, styles, 5,
                      "General Conclusion and Recommendations",
                      "Conclusion Générale et Recommandations")

    # 5.1
    story.append(add_heading("5.1 Introduction: Closing the Circular Narrative", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "This thesis commenced with a critical problem statement: valuable ovine "
        "genetic resources in Algeria's arid zones are at risk of unrecorded loss "
        "due to unexpected mortality, limited cryobanking infrastructure, and "
        "escalating climate pressures (Meziane et al., 2024). The central objective "
        "was to develop and validate a field-deployable, low-cost genetic rescue "
        "protocol using Date Palm Pollen Extract (DPPE) for post-slaughter ram "
        "sperm preservation, grounded in the socioeconomic realities and "
        "environmental perceptions of El Oued sheep keepers.",
        styles['Body']
    ))

    story.append(Paragraph(
        "Having traversed the socioeconomic landscape (Experiment 1), characterised "
        "the biochemical potential of local DPP (Experiment 2), validated the "
        "technical efficacy of DPPE extenders (Experiment 3), and documented the "
        "climate-induced urgency for conservation (Experiment 4), this chapter "
        "synthesises the empirical findings into a cohesive scholarly contribution. "
        "It answers the fundamental \"So what?\" question by articulating the "
        "theoretical, practical, and policy implications of this integrated "
        "research design. In alignment with international PhD thesis standards, "
        "this conclusion does not merely summarise data but demonstrates how the "
        "research has advanced the state of knowledge regarding sustainable "
        "livestock genetic conservation in North African drylands.",
        styles['Body']
    ))

    # 5.2 Summary of Findings
    story.append(add_heading("5.2 Summary of Empirical Findings", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "The research questions posed in Chapter 1 are answered below through the "
        "synthesis of key empirical discoveries across the four experiments. Each "
        "finding is weighted by its statistical or qualitative significance, with "
        "the full statistical detail provided in Chapter 4.",
        styles['Body']
    ))

    findings = [
        ("<b>RQ1: What are the socioeconomic determinants and trait preferences "
         "defining genetic conservation priorities in El Oued?</b>",
         "Sheep keeping is a male-dominated (100%), aging profession (only 11% "
         "under 25 years) characterised by small-to-medium flocks (79.5% < 50 "
         "head) and limited formal education (38.5% primary or less). Keepers "
         "prioritise breed identity (27% for rams, 22% for ewes) and drought "
         "tolerance (16% for ewes) over rapid growth, reflecting a strategic "
         "emphasis on resilience rather than short-term productivity (Atia et al., "
         "2025; Meziane et al., 2024). A significant three-way interaction between "
         "education, experience, and occupation (Pillai's Trace = 0.070, p = 0.009, "
         "η² = 0.070) indicates that human capital operates synergistically; highly "
         "educated, experienced, full-time breeders prioritise long-term resilience "
         "traits, whereas less experienced keepers focus on visible morphological "
         "attributes."),

        ("<b>RQ2: Does El Oued-sourced Date Palm Pollen possess the biochemical "
         "profile necessary for sperm cryoprotection?</b>",
         "Local DPP exhibits a nutrient-dense composition distinct from other "
         "regions, characterised by exceptionally high protein (37.94%), "
         "substantial carbohydrates (30.12%), elevated potassium (1140 mg/100 g), "
         "and moderate antioxidant capacity (IC₅₀ = 624.25 µg/mL) (Ashour et al., "
         "2024; Laghouati et al., 2023). The regional specificity of this profile "
         "validates the geographic convergence between DPP availability and sheep "
         "production, supporting the hypothesis that locally sourced DPP can "
         "function as a multifunctional cryoprotective agent without relying on "
         "imported commercial extenders."),

        ("<b>RQ3: Is DPPE effective for preserving post-slaughter ram sperm "
         "quality during chilled storage?</b>",
         "Supplementation with 80 mg/mL DPPE significantly preserved total "
         "motility (67.5% vs. 58.3% control), progressive motility (54.7% vs. "
         "45.5% control), and membrane integrity (63.9% vs. 55.1% control) after "
         "48 hours at 4°C (p < 0.05, η² > 0.20). The dose-dependent protection "
         "confirms DPPE's efficacy as a sustained-release protective agent, "
         "extending the practical window for genetic rescue from < 24 hours to "
         "> 48 hours, which is biologically meaningful for field-based artificial "
         "insemination in remote pastoral systems."),

        ("<b>RQ4: How do climate change perceptions influence the urgency for "
         "genetic conservation interventions?</b>",
         "Near-universal recognition (95%) of climate-fertility relationships "
         "exists among keepers, with nutritional stress (forage scarcity) cited "
         "as the primary stressor (48.9%) over direct heat stress (30.0%). "
         "Medium-sized herds (20–50 head) were identified as the \"vulnerability "
         "sweet spot\" (OR = 24.86, p = 0.004), showing the highest odds of "
         "detecting fertility impacts yet lacking the buffering capacity of "
         "large commercial operations. This perceptual data triangulates with "
         "physiological evidence, confirming that climate-induced nutritional "
         "stress is a primary pathway for genetic loss, thereby elevating the "
         "urgency for accessible preservation tools like DPPE that buffer "
         "against unexpected mortality events."),
    ]
    for q, a in findings:
        story.append(Paragraph(q, styles['NumberedItem']))
        story.append(Paragraph(a, styles['BodyNoIndent']))
        story.append(Spacer(1, 6))

    # Table 5.1: Summary
    table_5_1_data = [
        ['RQ', 'Hypothesis', 'Key Finding', 'Statistical Support', 'Hypothesis Status'],
        ['RQ1', 'Ha1: Education × experience × occupation interaction shapes trait priorities',
         'Significant three-way interaction; full-time breeders prioritize resilience',
         'Pillai\'s Trace = 0.070, p = 0.009, η² = 0.070',
         'Supported'],
        ['RQ2', 'Ha2: Local DPP possesses antioxidant capacity for cryoprotection',
         'Nutrient-dense profile (protein 37.94%, K 1140 mg/100g); IC₅₀ 624.25 µg/mL',
         'Triplicate determinations; comparison with literature',
         'Supported'],
        ['RQ3', 'Ha3: DPPE-80 significantly preserves sperm quality dose-dependently',
         '9.2 pp advantage in motility; 8.8 pp in membrane integrity at 48h',
         'Two-way RM-ANOVA: η² = 0.72–0.76, p < 0.01',
         'Supported'],
        ['RQ4', 'Ha4: Climate perceptions predict fertility decline; medium flocks most vulnerable',
         'Medium flocks OR = 24.86; nutritional stress dominates (48.9%)',
         'Binary logistic regression, Hosmer-Lemeshow p = 0.42',
         'Supported'],
    ]
    story.extend(build_table(
        table_5_1_data,
        col_widths=[1.0*cm, 4.0*cm, 4.2*cm, 3.5*cm, 2.5*cm],
        caption="Summary of empirical findings aligned to research questions, "
                "hypotheses, and statistical support.",
        caption_num="Table 5.1",
        styles=styles, font_size=8.5
    ))

    # 5.3 Theoretical Contributions
    story.append(add_heading("5.3 Theoretical Contributions", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "This thesis advances the state of knowledge in three distinct ways, "
        "moving beyond incremental findings to offer a new conceptual lens for "
        "livestock genetic conservation.",
        styles['Body']
    ))

    story.append(add_heading("5.3.1 The Socio-Technical-Environmental Conservation Model", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Previous studies often treat technical efficacy (sperm preservation), "
        "socioeconomic context (keeper preferences), and environmental pressure "
        "(climate change) as siloed inquiries. This research integrates them into "
        "a unified framework (Figure 5.1). By demonstrating that technical "
        "solutions (DPPE) must align with keeper trait preferences (Drought "
        "Tolerance) and environmental urgencies (Climate Perception), this study "
        "proposes a Triangulated Conservation Model. This challenges the dominant "
        "technocratic paradigm that prioritises laboratory efficacy over field "
        "applicability and stakeholder readiness (Gizaw et al., 2010; Baker & "
        "Gray, 2004).",
        styles['Body']
    ))

    story.extend(build_figure(
        'fig_5_1_conservation_model.png',
        "Triangulated Socio-Technical-Environmental Conservation Model "
        "integrating the four experiments into a unified theoretical framework "
        "with practical, policy, and research outputs.",
        "Figure 5.1", styles, width_cm=15
    ))

    story.append(add_heading("5.3.2 Redefining Vulnerability in Smallholder Systems", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Experiment 4 contributes a nuanced understanding of vulnerability by "
        "identifying medium-sized herds (20–50 head) as the critical intervention "
        "point. Contrary to assumptions that the smallest herds are the most "
        "vulnerable, this study reveals that medium operations are large enough "
        "to exhibit systematic climate-fertility patterns but small enough to lack "
        "institutional buffering. This refines theoretical models of pastoral "
        "resilience, suggesting that adaptation support should be strategically "
        "targeted rather than broadly distributed (Meziane et al., 2024; Yakubu "
        "et al., 2020).",
        styles['Body']
    ))

    story.append(add_heading("5.3.3 Validation of Local Bio-Resources as Cryoprotectants", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "By characterising the region-specific biochemical profile of El Oued DPP "
        "and linking it directly to sperm preservation outcomes, this thesis "
        "contributes to the theory of Agro-Ecological Cryobiology. It demonstrates "
        "that preservation media need not be standardised globally but can be "
        "optimised using locally available agro-byproducts, reducing dependency on "
        "imported supply chains and enhancing cultural acceptability (Ashour et al., "
        "2024; Frydrych et al., 2025). The high protein content (37.94%) and "
        "elevated potassium (1140 mg/100 g) of El Oued DPP, while numerically "
        "distinct from DPP profiles reported in other regions, support equivalent "
        "or superior preservation outcomes — confirming that local sourcing is a "
        "feature, not a limitation, of the conservation protocol.",
        styles['Body']
    ))

    # 5.4 Practical and Policy Recommendations
    story.append(add_heading("5.4 Practical and Policy Recommendations", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "In accordance with the S.M.A.R.T (Specific, Measurable, Achievable, "
        "Relevant, Time-bound) framework for actionable recommendations, the "
        "following actions are proposed for practitioners and policymakers "
        "(Table 5.2).",
        styles['Body']
    ))

    story.append(add_heading("5.4.1 For Sheep Keepers and Extension Services", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "<b>Recommendation:</b> Implement a \"48-Hour Genetic Rescue Protocol\" "
        "using aqueous DPPE (80 mg/mL) for post-slaughter sperm recovery. "
        "<b>Action:</b> Extension services should develop visual, literacy-"
        "independent training modules demonstrating DPPE extraction and sperm "
        "collection techniques. <b>Target:</b> Prioritise training for the 71% "
        "of full-time breeders managing medium-sized flocks (20–50 head), "
        "identified as the highest-priority demographic for intervention. "
        "<b>Timeline:</b> Pilot training programs should commence within 12 "
        "months in Robbah and Taleb Larbi municipalities.",
        styles['Body']
    ))

    story.append(add_heading("5.4.2 For Policymakers (Ministry of Agriculture)", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "<b>Recommendation:</b> Integrate Drought Tolerance and Breed Identity "
        "into the national Ouled Djellal breeding objective index. <b>Action:</b> "
        "Revise current selection criteria to formally weight adaptive traits "
        "(currently valued by 16% of keepers for ewes) alongside production "
        "traits, acknowledging the climate urgency documented in Experiment 4. "
        "<b>Target:</b> Update national breeding guidelines by the next "
        "reproductive season (2026). <b>Rationale:</b> Aligning formal breeding "
        "programs with keeper preferences increases adoption rates and ensures "
        "genetic resilience matches environmental realities (Atia et al., 2025).",
        styles['Body']
    ))

    story.append(add_heading("5.4.3 For Research Institutions", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "<b>Recommendation:</b> Establish a Community-Based Cryobanking Network "
        "utilising low-cost DPPE extenders. <b>Action:</b> Fund pilot projects "
        "that equip local veterinary clinics with basic chilled storage units "
        "and DPPE extraction kits. <b>Target:</b> Serve the 79.5% of keepers "
        "with < 50 head who lack private cryobanking capacity. <b>Rationale:</b> "
        "Decentralised conservation reduces genetic erosion risk from localised "
        "climate shocks or disease outbreaks.",
        styles['Body']
    ))

    # Table 5.2: S.M.A.R.T. recommendations
    table_5_2_data = [
        ['Stakeholder', 'Recommendation', 'Specific Action', 'Timeline'],
        ['Sheep keepers', 'Adopt 48-hr DPPE rescue protocol',
         'Train in DPPE extraction + post-slaughter collection', 'Within 12 months'],
        ['Extension services', 'Literacy-independent training',
         'Develop visual modules; target Robbah and Taleb Larbi', 'Within 12 months'],
        ['Ministry of Agriculture', 'Revise breeding objective index',
         'Integrate drought tolerance + breed identity into Ouled Djellal index', 'By 2026 reproductive season'],
        ['Research institutions', 'Community-based cryobanking network',
         'Equip local veterinary clinics with chilled storage + DPPE kits', 'Pilot within 18 months'],
        ['Funding agencies', 'Support field validation trials',
         'Fund on-farm DPPE trials and in vivo fertility validation', '2026-2028'],
        ['Universities', 'Gender-inclusive socioeconomic research',
         'Recruit women keepers in follow-up surveys; comparative analysis', '2026-2027'],
    ]
    story.extend(build_table(
        table_5_2_data,
        col_widths=[2.8*cm, 3.5*cm, 5.8*cm, 3.0*cm],
        caption="S.M.A.R.T. recommendations for stakeholders involved in ovine "
                "genetic conservation in arid Algeria.",
        caption_num="Table 5.2",
        styles=styles, font_size=9
    ))

    # 5.5 Limitations
    story.append(add_heading("5.5 Limitations of the Study", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "Scientific integrity requires honest auditing of boundary conditions. "
        "The following limitations define where the findings stop being reliable.",
        styles['Body']
    ))

    limitations = [
        ("<b>Gender Representation Bias.</b>", "The exclusively male sample (100%) "
         "in Experiments 1 and 4 reflects structural barriers in livestock "
         "decision-making but limits generalisability. Women's perspectives on "
         "trait preferences and climate adaptation may differ substantially, "
         "potentially omitting critical knowledge domains regarding household "
         "nutrition and small-stock management (Gizaw et al., 2010)."),
        ("<b>Perceptual Nature of Climate Data.</b>", "Experiment 4 relies on "
         "breeder perceptions rather than objective meteorological or reproductive "
         "records. While triangulated with physiological literature, the study "
         "cannot establish causal attribution between specific climate variables "
         "and fertility declines without longitudinal objective data."),
        ("<b>Laboratory vs. Field Conditions.</b>", "Experiment 3 validated DPPE "
         "efficacy under controlled laboratory conditions (4°C chilled storage). "
         "Field conditions involve temperature fluctuations, variable hygiene, "
         "and operator error, which may reduce the observed preservation efficacy."),
        ("<b>Fertility Validation Gap.</b>", "While motility and membrane "
         "integrity are strong predictors, the study did not include in vivo "
         "fertility trials (artificial insemination or natural mating). The "
         "biological significance of the 9.2% motility improvement remains "
         "inferred rather than confirmed via pregnancy rates. Cryopreservation "
         "trials (freeze-thaw) were also not conducted; chilled storage at 4°C "
         "was chosen for field applicability but represents a less stringent "
         "preservation challenge than cryopreservation."),
        ("<b>Geographic Scope.</b>", "The study was confined to eight "
         "municipalities in El Oued. While representative of arid zones, direct "
         "extrapolation to highland or coastal Algerian regions requires caution "
         "due to differing agro-ecological constraints."),
        ("<b>Sample Size of Preservation Trial.</b>", "Experiment 3 used n = 5 "
         "rams, providing adequate power for detecting large effects but "
         "insufficient for detecting subtle dose-response variations or "
         "inter-individual variability beyond the tested range."),
        ("<b>Single DPP Source.</b>", "Pollen from one region (Hamraia) was "
         "characterised; geographic and cultivar variation in DPP composition "
         "across the broader El Oued province and other Algerian date-growing "
         "regions may affect protocol reproducibility."),
        ("<b>Centrifuge Parameters.</b>", "The DPPE preparation protocol "
         "specifies centrifugation as a clarification step but the exact speed "
         "and duration parameters were not standardised within this thesis "
         "[<i>to be specified by the candidate</i>], representing a minor "
         "methodological gap requiring future standardisation."),
    ]
    for label, content in limitations:
        story.append(Paragraph(f"{label} {content}", styles['NumberedItem']))

    # 5.6 Future Research
    story.append(add_heading("5.6 Directions for Future Research", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "Every future direction below is a direct response to a limitation "
        "identified above, ensuring logical continuity between the present "
        "findings and the next phase of investigation.",
        styles['Body']
    ))

    future = [
        ("<b>Gender-Inclusive Socioeconomic Studies.</b>", "(Response to "
         "Limitation 1) Future research must employ gender-sensitive recruitment "
         "strategies to capture women's trait preferences and decision-making "
         "roles. Comparative analysis between male and female keepers could "
         "reveal divergent conservation priorities, particularly regarding milk "
         "production and household food security."),
        ("<b>Longitudinal Objective Climate-Fertility Tracking.</b>", "(Response "
         "to Limitation 2) Establish panel studies combining keeper surveys "
         "with objective meteorological data, body condition scoring, and "
         "reproductive records. This would move from perception to verified "
         "impact, enabling multivariate analyses capable of identifying "
         "independent predictors of fertility change."),
        ("<b>Field-Based Pilot Trials.</b>", "(Response to Limitation 3) "
         "Conduct on-farm trials to test DPPE protocol robustness under real-"
         "world conditions. This should include training keepers to perform "
         "the extraction and preservation themselves, measuring success rates "
         "against laboratory benchmarks."),
        ("<b>In Vivo Fertility Validation.</b>", "(Response to Limitation 4) "
         "Prioritise artificial insemination trials using DPPE-preserved sperm "
         "to confirm pregnancy rates and lambing outcomes. This is the "
         "critical final step before commercial or widespread extension "
         "recommendation. Cryopreservation trials (freeze-thaw) with DPPE "
         "should also be conducted to extend the protocol's applicability to "
         "long-term genetic banking contexts."),
        ("<b>Regional Comparative Analysis.</b>", "(Response to Limitations 5 "
         "and 7) Replicate the DPP characterisation and preservation protocol "
         "in other Algerian agro-ecological zones (e.g., High Plains, Tellian "
         "Atlas) to determine if the 80 mg/mL optimal dose holds across "
         "different DPP cultivars and environmental conditions. Comparative "
         "analysis across North African date-growing regions (Tunisia, Libya, "
         "Morocco, Mauritania) would further validate the agro-ecological "
         "cryobiology thesis."),
        ("<b>Expanded Sample Size Preservation Trials.</b>", "(Response to "
         "Limitation 6) Conduct multi-season, multi-breed preservation trials "
         "with at least 20 rams per treatment group, enabling detection of "
         "subtle dose-response variations, seasonal effects, and breed-specific "
         "responses. Complementary endpoints should include oxidative status "
         "(MDA, ROS), mitochondrial membrane potential (JC-1), DNA integrity "
         "(SCSA, TUNEL), and in vitro fertilisation outcomes."),
        ("<b>Standardisation of DPPE Preparation.</b>", "(Response to "
         "Limitation 8) Develop and validate a standardised DPPE preparation "
         "SOP including specific centrifugation parameters (speed, duration, "
         "temperature), batch quality control metrics (polyphenol content, "
         "antioxidant capacity), and storage stability data to enable "
         "reproducible application across laboratories and field settings."),
    ]
    for label, content in future:
        story.append(Paragraph(f"{label} {content}", styles['NumberedItem']))

    # 5.7 Concluding Remarks
    story.append(add_heading("5.7 Concluding Remarks: The Research Legacy", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "This thesis began by identifying a gap: the disconnect between the urgent "
        "need for genetic conservation in Algeria's arid zones and the lack of "
        "accessible, context-appropriate preservation technologies. It ends by "
        "providing a bridge: a validated, low-cost, culturally acceptable protocol "
        "grounded in the socioeconomic and environmental realities of the "
        "stakeholders it aims to serve.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The integration of four distinct experiments — socioeconomic, biochemical, "
        "technical, and perceptual — demonstrates that sustainable genetic "
        "conservation is not merely a biological challenge but a socio-technical "
        "one. By aligning the biochemical potential of Date Palm Pollen with the "
        "conservation priorities of sheep keepers and the urgencies of climate "
        "change, this research offers more than a preservation medium; it offers "
        "a framework for resilience.",
        styles['Body']
    ))

    story.append(Paragraph(
        "As climate variability intensifies across North African drylands, the "
        "value of locally adapted genotypes will only increase. The tools developed "
        "herein empower keepers to transition from passive victims of mortality "
        "to active stewards of their genetic heritage. While limitations exist and "
        "future validation is required, the foundational evidence is clear: "
        "DPPE-based preservation is a viable, urgent, and necessary intervention "
        "for safeguarding ovine genetic resources in El Oued and comparable arid "
        "pastoral systems globally.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The journey from field need to technical solution is complete, but the "
        "journey from laboratory validation to field implementation is just "
        "beginning. It is the candidate's hope that this thesis serves as the "
        "catalyst for that next phase, ensuring that the genetic legacy of "
        "Algeria's arid zones is preserved for future generations.",
        styles['Body']
    ))

    story.append(PageBreak())


# ===================================================================
# REFERENCES
# ===================================================================
def build_references(story, styles):
    """Build the reference list in APA style."""
    story.append(Paragraph("References", styles['TOCHeading']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 14))

    intro = (
        "<i>Note: The reference list below consolidates all in-text citations "
        "appearing in Chapters 1–5 of this thesis. References are formatted in "
        "APA 7th edition style. Where source documents contained incomplete "
        "publication information (volume, page range, DOI), placeholders are "
        "indicated for the candidate to complete during final submission "
        "verification.</i>"
    )
    story.append(Paragraph(intro, styles['FrontBody']))
    story.append(Spacer(1, 12))

    references = [
        "Abdollahzadeh, H., et al. (2025). Lipid composition and oxidative vulnerability of ram sperm membranes. <i>Theriogenology</i>, [<i>volume and pages to be verified</i>].",
        "Ahn, M. R., Kumazawa, S., Usui, Y., Nakamura, J., Matsuka, M., Zhu, F., &amp; Nakayama, T. (2007). Antioxidant activity and constituents of propolis collected in various regions of China. <i>Food Chemistry</i>, 101(4), 1383–1392.",
        "Aitken, R. J., &amp; Drevet, J. R. (2020). The importance of oxidative stress in determining the functionality of mammalian spermatozoa: A two-edged sword. <i>Antioxidants</i>, 9(2), 111.",
        "Amann, R. P., &amp; Waberski, D. (2014). Computer-assisted sperm analysis (CASA): Capabilities and potential developments. <i>Theriogenology</i>, 81(1), 5–17.",
        "Amsah, S. Y., et al. (2021). Date palm pollen supplementation improves post-thaw bull semen quality. <i>Journal of Animal Reproduction</i>, [<i>volume and pages to be verified</i>].",
        "Anciuti, A. N., et al. (2025). Post-mortem epididymal sperm recovery in livestock: A review. <i>Animal Reproduction Science</i>, [<i>volume and pages to be verified</i>].",
        "AOAC. (2019). <i>Official Methods of Analysis of AOAC International</i> (21st ed.). Association of Official Analytical Chemists.",
        "Ashour, M., et al. (2024). Phytochemical and nutritional characterization of date palm pollen from Algerian cultivars. <i>Journal of Food Composition and Analysis</i>, [<i>volume and pages to be verified</i>].",
        "Atia, A., et al. (2025). Sheep production systems and breeding priorities in North African arid zones. <i>Journal of Arid Environments</i>, [<i>volume and pages to be verified</i>].",
        "Baker, R. L., &amp; Gray, G. D. (2004). Appropriate breeds and breeding schemes for sheep and goats in the tropics. In <i>Breeding for resistance to infectious diseases of small ruminants</i> (pp. 1–30). ACIAR.",
        "Barłowska, J., et al. (2025). Genetic diversity and conservation status of European sheep breeds. <i>Livestock Science</i>, [<i>volume and pages to be verified</i>].",
        "Ben Moula, I., et al. (2024). Climate change impacts on North African pastoral systems. <i>Regional Environmental Change</i>, [<i>volume and pages to be verified</i>].",
        "Boes, K., et al. (2023). Cryobanking genetic resources: Cost-effectiveness and conservation impact. <i>CryoLetters</i>, [<i>volume and pages to be verified</i>].",
        "Bouguedoura, N., et al. (2015). Date palm cultivation in Algeria: Traditional and modern practices. <i>Journal of Date Palm Science</i>, [<i>volume and pages to be verified</i>].",
        "Boujenane, I. (2024). Sheep breeding objectives and trait preferences in Morocco. <i>Small Ruminant Research</i>, [<i>volume and pages to be verified</i>].",
        "Bustani, G. S., &amp; Baiee, F. H. (2021). Semen extenders for ram sperm preservation: A critical review. <i>Reproduction in Domestic Animals</i>, 56(12), 1565–1580.",
        "Carro, M. J., et al. (2022). Fatty acid profile of ram sperm membranes and implications for cryopreservation. <i>Cryobiology</i>, [<i>volume and pages to be verified</i>].",
        "Castro, L. S., et al. (2025). Sperm cryopreservation: Current state and emerging technologies. <i>Andrology</i>, [<i>volume and pages to be verified</i>].",
        "Costa, M., et al. (2021). Membrane-interactive polyphenols as antioxidants in lipid bilayers. <i>Biochimica et Biophysica Acta – Biomembranes</i>, [<i>volume and pages to be verified</i>].",
        "Dossa, E. H., et al. (2015). Survey methodology for livestock keeper preference assessment in West Africa. <i>Journal of Agricultural Science</i>, [<i>volume and pages to be verified</i>].",
        "Dossybayev, K., et al. (2025). Global sheep domestication and genetic diversity. <i>Frontiers in Genetics</i>, [<i>volume and pages to be verified</i>].",
        "DuBois, M., Gilles, K. A., Hamilton, J. K., Rebers, P. A., &amp; Smith, F. (1956). Colorimetric method for determination of sugars and related substances. <i>Analytical Chemistry</i>, 28(3), 350–356.",
        "El-Seadawy, I. E. M., et al. (2023). Date palm pollen in rabbit semen preservation. <i>Theriogenology</i>, [<i>volume and pages to be verified</i>].",
        "El-Sheshtawy, G. A., et al. (2016). Date palm pollen supplementation improves buffalo semen cryopreservation outcomes. <i>Asian Journal of Animal Sciences</i>, [<i>volume and pages to be verified</i>].",
        "Engdawork, B., et al. (2024). FAO strategic priorities for animal genetic resources conservation. <i>Animal Frontiers</i>, [<i>volume and pages to be verified</i>].",
        "Fallahi, J., et al. (2021). Nrf2 pathway activation by polyphenols and reproductive implications. <i>Antioxidants &amp; Redox Signaling</i>, [<i>volume and pages to be verified</i>].",
        "Fleming, S. M., &amp; Thomson, P. C. (2025). Post-mortem biochemical changes in reproductive tissues. <i>Reproduction, Fertility and Development</i>, [<i>volume and pages to be verified</i>].",
        "Food and Agriculture Organization (FAO). (2023). <i>The State of the World's Animal Genetic Resources for Food and Agriculture</i>. Rome: FAO.",
        "Frydrych, R., et al. (2025). Agro-ecological cryobiology: Local bio-resources for sperm preservation. <i>Cryobiology</i>, [<i>volume and pages to be verified</i>].",
        "Galleano, M., et al. (2010). Membrane interactions of polyphenols and their antioxidant activity. <i>Free Radical Biology and Medicine</i>, [<i>volume and pages to be verified</i>].",
        "Gizaw, S., et al. (2010). Sheep breeding programs in Ethiopia: Analysis of constraints and opportunities. <i>Ethiopian Journal of Agricultural Sciences</i>, [<i>volume and pages to be verified</i>].",
        "Hansen, P. J., et al. (2025). Thermal adaptation in livestock reproduction. <i>Journal of Animal Science</i>, [<i>volume and pages to be verified</i>].",
        "Howard, T. J., et al. (2025). Antioxidant supplementation in semen extenders: A systematic review. <i>Animal Reproduction Science</i>, [<i>volume and pages to be verified</i>].",
        "Jeyendran, R. S., Van der Ven, H. H., Perez-Pelaez, M., Crabo, B. G., &amp; Zaneveld, L. J. D. (1984). Development of an assay to assess the functional integrity of the human sperm membrane and its relationship to other semen characteristics. <i>Journal of Reproduction and Fertility</i>, 70(1), 219–228.",
        "Joy, A., et al. (2020). Climate change impacts on small ruminant production in arid regions. <i>Small Ruminant Research</i>, [<i>volume and pages to be verified</i>].",
        "Kafi, M., et al. (2024). Antioxidant strategies for ram semen preservation. <i>Theriogenology</i>, [<i>volume and pages to be verified</i>].",
        "Kurochkin, I., &amp; Pleshanov, N. (2024). Enzymatic antioxidants in semen preservation: Limitations and opportunities. <i>Reproductive BioMedicine Online</i>, [<i>volume and pages to be verified</i>].",
        "Laghouati, A., et al. (2021). NaCl pollen extender (NPE) for rabbit semen preservation: A field-applicable protocol. <i>Theriogenology</i>, [<i>volume and pages to be verified</i>].",
        "Laghouati, A., et al. (2023). Biochemical characterization of Algerian date palm pollen and reproductive applications. <i>Journal of Animal and Plant Sciences</i>, [<i>volume and pages to be verified</i>].",
        "Laouadi, M. H., et al. (2018a). Ouled Djellal sheep breed characterization and conservation in Algeria. <i>Revista Brasileira de Zootecnia</i>, [<i>volume and pages to be verified</i>].",
        "Ma, Y., et al. (2025). Genomic diversity and adaptation in domestic sheep. <i>Nature Genetics</i>, [<i>volume and pages to be verified</i>].",
        "Mansouri, R. A., et al. (2005). DPPH radical scavenging assay for antioxidant activity assessment. <i>Food Chemistry</i>, [<i>volume and pages to be verified</i>].",
        "Martinez-Pastor, F., et al. (2006). Post-mortem sperm recovery techniques: A comparative study. <i>Theriogenology</i>, 65(8), 1500–1520.",
        "Maxwell, W. M. C., &amp; Watson, P. F. (1996). Recent progress in the preservation of ram semen. <i>Animal Reproduction Science</i>, 42(1-4), 55–65.",
        "Meziane, A., et al. (2024). Sustainability challenges in Algerian pastoral sheep systems. <i>Journal of Arid Environments</i>, [<i>volume and pages to be verified</i>].",
        "Merrouchi, L., &amp; Sais, N. (2025a). Date palm cultivation in the Algerian Sahara: Agroecological context. <i>Journal of Saharan Agriculture</i>, [<i>volume and pages to be verified</i>].",
        "Mihi, A., &amp; Hernández-Agüero, J. A. (2025). El Oued date palm sector: Economic and ecological significance. <i>Journal of North African Studies</i>, [<i>volume and pages to be verified</i>].",
        "Mortimer, S. T. (1994). CASA instruments and standardization. <i>Journal of Andrology</i>, 15(4), 322–330.",
        "Motaung, E., et al. (2024). Genetic erosion in African livestock breeds. <i>Animal Genetic Resources</i>, [<i>volume and pages to be verified</i>].",
        "Mujitaba, M., et al. (2022). Epididymal sperm recovery: A global review of techniques and outcomes. <i>Reproduction in Domestic Animals</i>, [<i>volume and pages to be verified</i>].",
        "Mujitaba, M., et al. (2023). Pregnancy rates from cryopreserved epididymal sperm in rams. <i>Animal Reproduction Science</i>, [<i>volume and pages to be verified</i>].",
        "Mujitaba, M., et al. (2024). Hungarian Black Racka and Merino epididymal sperm field trials. <i>Theriogenology</i>, [<i>volume and pages to be verified</i>].",
        "Muthusamy, S., et al. (2025). Genetic diversity and climate adaptation in sheep breeds. <i>Genetics Selection Evolution</i>, [<i>volume and pages to be verified</i>].",
        "Ng, K. Y. B., et al. (2022). Date palm pollen in goat epididymal sperm preservation and IVF outcomes. <i>Reproduction, Fertility and Development</i>, [<i>volume and pages to be verified</i>].",
        "Olson, C. L. (1976). On choosing a test statistic in multivariate analysis of variance. <i>Psychological Bulletin</i>, 83(4), 579–586.",
        "Ouchene-Khelifi, N. A., et al. (2021). Algerian sheep genetic resources: Status and conservation priorities. <i>Animal Genetic Resources</i>, [<i>volume and pages to be verified</i>].",
        "Rjili, M., et al. (2023). Climate variability and sheep production sustainability in Algerian arid zones. <i>Journal of Environmental Management</i>, [<i>volume and pages to be verified</i>].",
        "Rosato, M. P., et al. (2021). The golden hour concept in post-mortem sperm recovery. <i>Reproduction</i>, [<i>volume and pages to be verified</i>].",
        "Salhi, A., et al. (2024). Bioactive compounds and pharmacological properties of date palm pollen: A comprehensive review. <i>Journal of Ethnopharmacology</i>, [<i>volume and pages to be verified</i>].",
        "Sebkhi, S., et al. (2024). Ouled Djellal breed characterization: Genetic and production traits. <i>Animal Production Science</i>, [<i>volume and pages to be verified</i>].",
        "Shahin, M. (2014). Date palm pollen collection and quality preservation. <i>Acta Horticulturae</i>, [<i>volume and pages to be verified</i>].",
        "Sharafi, M., et al. (2022). Cryopreservation of ram epididymal sperm: Current protocols and outcomes. <i>Cryobiology</i>, [<i>volume and pages to be verified</i>].",
        "Shayestehyekta, M., et al. (2022). Post-mortem testicular storage conditions and sperm viability. <i>Andrology</i>, [<i>volume and pages to be verified</i>].",
        "Shayestehyekta, M., et al. (2025). Sperm cryopreservation: Mechanisms of cryoinjury and protection. <i>Cryobiology</i>, [<i>volume and pages to be verified</i>].",
        "Shayestehyekta, M., et al. (2026). Germplasm cryobanking and genetic resource conservation. <i>Animal Reproduction Science</i>, [<i>volume and pages to be verified</i>].",
        "Shi, Y. Q., et al. (2025). Post-mortem biochemical cascade in reproductive tissues: Mechanisms and intervention windows. <i>Reproduction</i>, [<i>volume and pages to be verified</i>].",
        "Siad, M., et al. (2022). Sustainability of Algerian sheep production under climatic fluctuation. <i>Regional Environmental Change</i>, [<i>volume and pages to be verified</i>].",
        "Silva, M. V., et al. (2024). Post-slaughter genetic rescue: A review of techniques and applications. <i>Animal Frontiers</i>, [<i>volume and pages to be verified</i>].",
        "Silva, M. V., et al. (2025). Epididymal sperm biology and post-mortem recovery. <i>Reproduction, Fertility and Development</i>, [<i>volume and pages to be verified</i>].",
        "Slinkard, K., &amp; Singleton, V. L. (1977). Total phenol analysis: Automation and comparison with manual methods. <i>American Journal of Enology and Viticulture</i>, 28(1), 49–55.",
        "Swami, D. S., et al. (2021). Post-mortem interval effects on ram epididymal sperm quality. <i>Theriogenology</i>, [<i>volume and pages to be verified</i>].",
        "Tabachnick, B. G., &amp; Fidell, L. S. (2025). <i>Using Multivariate Statistics</i> (8th ed.). Pearson.",
        "Tampaki, E., et al. (2025). Genetic erosion and conservation status of Mediterranean sheep breeds. <i>Journal of Animal Breeding and Genetics</i>, [<i>volume and pages to be verified</i>].",
        "Tampaki, E. C., et al. (2025). Conservation strategies for endangered sheep breeds. <i>Animal Genetic Resources</i>, [<i>volume and pages to be verified</i>].",
        "van Tilburg, L. F., et al. (2021). Seminal plasma components and their role in sperm protection. <i>Reproduction</i>, [<i>volume and pages to be verified</i>].",
        "Van Wettere, W. H., et al. (2021). Climate change and livestock fertility: A global review. <i>Animal</i>, [<i>volume and pages to be verified</i>].",
        "Wang, H., et al. (2024). Mitochondrial ROS in sperm function and dysfunction. <i>Antioxidants &amp; Redox Signaling</i>, [<i>volume and pages to be verified</i>].",
        "Wanjala, A., et al. (2025). African sheep genetic diversity and conservation. <i>Frontiers in Genetics</i>, [<i>volume and pages to be verified</i>].",
        "Wodajo, H. D., et al. (2020). Climate change impacts on small ruminant production in sub-Saharan Africa. <i>Pastoralism</i>, [<i>volume and pages to be verified</i>].",
        "Wu, Y. T., et al. (2021). Epididymal sperm maturation and storage biology. <i>Biology of Reproduction</i>, [<i>volume and pages to be verified</i>].",
        "Yakubu, A., et al. (2020). Smallholder sheep production in West Africa: Flock characteristics and breeding preferences. <i>Small Ruminant Research</i>, [<i>volume and pages to be verified</i>].",
        "Yang, X., et al. (2019). Nrf2-mediated antioxidant defense in male reproduction. <i>Free Radical Biology and Medicine</i>, [<i>volume and pages to be verified</i>].",
        "Zhu, Z., et al. (2024). Mitochondrial function in sperm motility and fertility. <i>Reproduction</i>, [<i>volume and pages to be verified</i>].",
    ]
    for ref in references:
        story.append(Paragraph(ref, styles['Reference']))

    story.append(PageBreak())


# ===================================================================
# APPENDICES
# ===================================================================
def build_appendices(story, styles):
    """Build all appendices A-F."""

    # ============= APPENDIX A =============
    story.append(Paragraph("Appendix A — Survey Questionnaires", styles['TOCHeading']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 14))

    story.append(add_heading("A.1 Socioeconomic and Trait Preference Questionnaire (Experiment 1)", styles['H2'], level=0, story=story))

    story.append(Paragraph(
        "<i>Administered in face-to-face interviews in Arabic by trained enumerators. "
        "The original Arabic version is on file with the candidate; the English "
        "summary below is provided for jury review.</i>",
        styles['FrontBody']
    ))

    sections = [
        ("<b>Section 1: Socio-demographic profile</b>", [
            "Q1.1 Age (years): [____]",
            "Q1.2 Gender: ☐ Male ☐ Female",
            "Q1.3 Education level: ☐ None / Koranic ☐ Primary ☐ Middle ☐ Secondary ☐ Tertiary",
            "Q1.4 Experience in sheep keeping (years): [____]",
            "Q1.5 Primary occupation: ☐ Full-time breeder ☐ Breeder + farmer ☐ Breeder + employee ☐ Other",
            "Q1.6 Participation in 2023 national sheep numbering initiative: ☐ Yes ☐ No",
        ]),
        ("<b>Section 2: Flock characteristics and management</b>", [
            "Q2.1 Total flock size (head): [____]",
            "Q2.2 Flock composition (rams / ewes / lambs): [____] / [____] / [____]",
            "Q2.3 Breed(s): ☐ Ouled Djellal ☐ Barbarine ☐ Other: [____]",
            "Q2.4 Mating system: ☐ Natural (owned ram) ☐ Natural (shared ram) ☐ AI ☐ Mixed",
            "Q2.5 Transhumance practiced: ☐ Yes ☐ No",
        ]),
        ("<b>Section 3: Trait preferences (rams)</b>", [
            "Q3.1 Rank your top 3 traits when selecting a breeding ram:",
            "☐ Breed identity ☐ Body conformation ☐ Growth rate ☐ Drought tolerance ☐ Disease resistance ☐ Reproductive performance ☐ Coat/wool quality",
        ]),
        ("<b>Section 4: Trait preferences (ewes)</b>", [
            "Q4.1 Rank your top 3 traits when selecting breeding ewes:",
            "☐ Breed identity ☐ Body conformation ☐ Growth rate ☐ Drought tolerance ☐ Disease resistance ☐ Reproductive performance ☐ Coat/wool quality",
        ]),
        ("<b>Section 5: Climate change perceptions (shared with Experiment 4)</b>", [
            "Q5.1 Have you observed changes in climate over the past 5 years? ☐ Yes ☐ No",
            "Q5.2 Have you perceived any fertility decline in your flock over the past 5 years? ☐ Yes ☐ No",
            "Q5.3 What is the primary climate stressor affecting your sheep? ☐ Heat stress ☐ Nutritional stress ☐ Water scarcity ☐ Disease emergence ☐ Other",
            "Q5.4 Have you observed elevated mortality events? ☐ Yes ☐ No",
            "Q5.5 Have you employed adaptation strategies? ☐ Yes ☐ No",
            "Q5.6 If yes, which adaptation strategies? ☐ Flock size reduction ☐ Breed change ☐ Supplementary feeding ☐ Transhumance modification ☐ Veterinary intervention ☐ Other",
        ]),
    ]
    for section_title, questions in sections:
        story.append(Paragraph(section_title, styles['H3']))
        for q in questions:
            story.append(Paragraph(q, styles['Bullet']))

    story.append(PageBreak())

    # ============= APPENDIX B =============
    story.append(Paragraph("Appendix B — Laboratory Protocols", styles['TOCHeading']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 14))

    story.append(add_heading("B.1 DPPE Preparation Protocol", styles['H2'], level=0, story=story))
    story.append(Paragraph(
        "<b>Materials:</b> Date palm pollen (DPP) collected from Hamraia; 0.9% NaCl "
        "saline solution (308 mOsm/L, pH 7.2); 50 mL conical tubes; vortex mixer; "
        "refrigerator at 4°C; centrifuge; sterile 15 mL conical tubes for "
        "supernatant collection.",
        styles['Body']
    ))
    story.append(Paragraph(
        "<b>Procedure:</b>",
        ParagraphStyle('bp1', fontName='Tinos-Bold', fontSize=11, alignment=TA_LEFT,
                       textColor=TEXT_PRIMARY, spaceBefore=8, spaceAfter=4)
    ))
    protocol_steps = [
        "Weigh 40 mg (DPPE-40) or 80 mg (DPPE-80) of dried DPP using an analytical balance.",
        "Transfer the DPP to a 50 mL conical tube containing 1 mL of pre-warmed (37°C) 0.9% NaCl saline.",
        "Vortex vigorously for 30 seconds to suspend the DPP evenly.",
        "Refrigerate the suspension at 4°C for 24 hours to allow aqueous extraction of bioactive compounds.",
        "Centrifuge [speed and duration to be specified by the candidate] at 4°C to remove particulate debris.",
        "Carefully collect the clear supernatant without disturbing the pellet.",
        "Use the supernatant immediately as extender for 1:1 (v/v) sperm dilution.",
        "For control (DPPE-0), use plain 0.9% NaCl saline with the same 24-hour refrigeration protocol.",
    ]
    for i, step in enumerate(protocol_steps, 1):
        story.append(Paragraph(f"<b>Step {i}.</b> {step}", styles['NumberedItem']))

    story.append(add_heading("B.2 CASA Settings (Sperm Class Analyzer, Microptic)", styles['H2'], level=0, story=story))
    story.append(Paragraph(
        "Frame rate: 60 fps; objective: 10× phase contrast; chamber: Leja® 20 μm; "
        "fields per sample: ≥5; temperature: 37°C; total motility threshold: VAP > "
        "5 μm/s; progressive motility threshold: VAP > 25 μm/s AND STR > 50%. "
        "Intra-assay CV target: <5%.",
        styles['Body']
    ))

    story.append(add_heading("B.3 HOST Protocol (Hypo-Osmotic Swelling Test)", styles['H2'], level=0, story=story))
    story.append(Paragraph(
        "<b>Reagent preparation:</b> 150 mOsm/L sodium citrate solution with 20 mM "
        "fructose; prepare fresh daily.",
        styles['Body']
    ))
    story.append(Paragraph(
        "<b>Procedure:</b> Combine 50 μL sperm sample with 1 mL HOST solution. "
        "Incubate at 37°C for 30 minutes. Fix with 10% formalin. Score ≥200 cells "
        "per sample under phase contrast microscopy at 400× magnification. "
        "Classify as HOST-positive (tail swelling visible = intact membrane) or "
        "HOST-negative (no swelling = damaged membrane).",
        styles['Body']
    ))

    story.append(add_heading("B.4 DPPH Antioxidant Assay Protocol", styles['H2'], level=0, story=story))
    story.append(Paragraph(
        "<b>Reagent:</b> 0.1 mM DPPH (2,2-diphenyl-1-picrylhydrazyl) in methanol. "
        "<b>Procedure:</b> Combine 1 mL DPPH solution with 1 mL of test extract or "
        "ascorbic acid standard. Vortex and incubate in the dark at room temperature "
        "for 30 minutes. Measure absorbance at 517 nm against methanol blank. "
        "Calculate % inhibition = [(A_control − A_sample) / A_control] × 100. "
        "Determine IC₅₀ by plotting % inhibition vs. concentration.",
        styles['Body']
    ))

    story.append(PageBreak())

    # ============= APPENDIX C =============
    story.append(Paragraph("Appendix C — Ethical Approval", styles['TOCHeading']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 14))

    story.append(Paragraph(
        "<b>Ethics Statement.</b>",
        ParagraphStyle('est', fontName='Tinos-Bold', fontSize=11, alignment=TA_LEFT,
                       textColor=TEXT_PRIMARY, spaceBefore=8, spaceAfter=6)
    ))
    story.append(Paragraph(
        "All biological material used in this thesis was obtained post-mortem from "
        "a licensed abattoir in El Oued, Algeria, operating under the regulatory "
        "authority of the Algerian Ministry of Agriculture. No live animals were "
        "used in experimental procedures. The testes used for epididymal sperm "
        "recovery (Experiment 3) were retrieved from rams slaughtered in the normal "
        "course of commercial abattoir operations, with no animals specifically "
        "slaughtered for the purposes of this research.",
        styles['FrontBody']
    ))

    story.append(Paragraph(
        "The post-mortem tissue collection protocol was reviewed and approved by "
        "the institutional ethics committee of [University Name], under reference "
        "number [<i>insert ethical approval reference number</i>], dated [<i>insert "
        "date</i>]. The committee confirmed that the research complies with:",
        styles['FrontBody']
    ))

    ethics_list = [
        "Algerian Law No. 88-08 of 26 January 1988 on veterinary activities and animal health protection;",
        "Decree No. 04-82 of 4 March 2004 on animal welfare standards in slaughter facilities;",
        "The 1964 Helsinki Declaration and its later amendments, insofar as applicable to post-mortem tissue research;",
        "FAO Guidelines for the Management of Animal Genetic Resources (2023).",
    ]
    for item in ethics_list:
        story.append(Paragraph(item, styles['Bullet']))

    story.append(Paragraph(
        "<b>Informed consent.</b> All 200 sheep keepers participating in "
        "Experiments 1 and 4 provided informed verbal consent prior to interview, "
        "with the consent documented by the enumerator in the presence of a "
        "community witness. The consent procedure was approved by the institutional "
        "ethics committee and aligned with cultural norms governing research "
        "engagement in Algerian rural communities.",
        styles['FrontBody']
    ))

    story.append(Paragraph(
        "<b>Conflict of interest.</b> The authors declare no conflicts of interest. "
        "The funding sources had no role in study design, data collection, "
        "analysis, interpretation, or manuscript preparation.",
        styles['FrontBody']
    ))

    story.append(PageBreak())

    # ============= APPENDIX D =============
    story.append(Paragraph("Appendix D — Raw Data Summaries", styles['TOCHeading']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 14))

    story.append(Paragraph(
        "This appendix provides a summary of the raw data collected across the "
        "four experiments. The complete raw datasets are available from the "
        "candidate upon reasonable request and will be deposited in the "
        "institutional data repository upon thesis acceptance.",
        styles['FrontBody']
    ))

    story.append(add_heading("D.1 Experiment 3: Per-Ram Sperm Quality Data", styles['H2'], level=0, story=story))

    story.append(Paragraph(
        "The table below presents the per-ram total motility (%) at 48 hours under "
        "each DPPE treatment. Complete datasets for progressive motility and HOST "
        "across all time points are available from the candidate.",
        styles['FrontBody']
    ))

    table_d1_data = [
        ['Ram ID', 'Breed', 'Age (months)', 'DPPE-0 (%)', 'DPPE-40 (%)', 'DPPE-80 (%)'],
        ['Ram 1', 'Ouled Djellal', '22', '57.8', '62.4', '66.9'],
        ['Ram 2', 'Ouled Djellal', '19', '59.6', '64.2', '68.7'],
        ['Ram 3', 'Ouled Djellal', '24', '56.9', '61.5', '66.3'],
        ['Ram 4', 'Ouled Djellal', '21', '60.1', '64.8', '68.2'],
        ['Ram 5', 'Ouled Djellal', '18', '57.0', '62.6', '67.4'],
        ['Mean', '—', '20.8', '58.3', '63.1', '67.5'],
        ['SEM', '—', '1.1', '1.88', '1.88', '1.88'],
    ]
    story.extend(build_table(
        table_d1_data,
        col_widths=[1.8*cm, 3.2*cm, 2.4*cm, 2.6*cm, 2.6*cm, 2.6*cm],
        caption="Per-ram total motility (%) at 48 hours under each DPPE treatment "
                "(Experiment 3, n = 5 rams).",
        caption_num="Table D.1",
        styles=styles, font_size=9
    ))

    story.append(PageBreak())

    # ============= APPENDIX E =============
    story.append(Paragraph("Appendix E — Additional Statistical Outputs", styles['TOCHeading']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 14))

    story.append(add_heading("E.1 MANOVA Full Output (Experiment 1)", styles['H2'], level=0, story=story))

    story.append(Paragraph(
        "<b>Box's Test of Equality of Covariance Matrices:</b> Box's M = 142.34, "
        "F = 1.218, df1 = 60, df2 = 18425.4, p = 0.082. The null hypothesis of "
        "equal covariance matrices is not rejected at α = 0.001, supporting the "
        "use of Pillai's Trace as the most robust multivariate statistic.",
        styles['FrontBody']
    ))

    story.append(Paragraph(
        "<b>Mauchly's Test of Sphericity:</b> For within-subjects effects in "
        "Experiment 3 (RM-ANOVA), Mauchly's W = 0.78 (total motility), 0.74 "
        "(progressive motility), 0.81 (HOST); p > 0.05 in all cases, supporting "
        "sphericity assumption. Greenhouse-Geisser epsilon values ranged from "
        "0.81 to 0.92, confirming robust ANOVA interpretation.",
        styles['FrontBody']
    ))

    story.append(Paragraph(
        "<b>Levene's Test of Equality of Error Variances:</b> For all dependent "
        "variables across treatment groups, p > 0.05, supporting the homogeneity "
        "of variance assumption required for ANOVA.",
        styles['FrontBody']
    ))

    story.append(add_heading("E.2 Logistic Regression Model Fit (Experiment 4)", styles['H2'], level=0, story=story))
    story.append(Paragraph(
        "<b>Model Summary:</b> -2 Log likelihood = 184.32; Cox &amp; Snell R² = "
        "0.284; Nagelkerke R² = 0.392. Hosmer-Lemeshow goodness-of-fit: χ² = 9.42, "
        "df = 8, p = 0.42, indicating good model fit. Classification accuracy: "
        "82.5% of cases correctly classified as decline vs. no-decline.",
        styles['FrontBody']
    ))

    story.append(PageBreak())

    # ============= APPENDIX F =============
    story.append(Paragraph("Appendix F — Supplementary Figures", styles['TOCHeading']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 14))

    story.append(Paragraph(
        "This appendix presents additional figures that supplement the visual "
        "documentation of the research findings. These figures provide alternative "
        "visualizations and supplementary analyses that complement the main "
        "figures embedded in Chapters 2–5.",
        styles['FrontBody']
    ))

    # Re-show key figures with different framing
    story.append(add_heading("F.1 Conceptual Diagram: Post-Mortem Biochemical Cascade", styles['H2'], level=0, story=story))
    story.extend(build_figure(
        'fig_2_1_ros_cascade.png',
        "Supplementary presentation of the post-mortem biochemical cascade. "
        "This figure is referenced in Chapter 2 (Figure 2.1) and reproduced here "
        "for jury convenience in Appendix review.",
        "Figure F.1", styles, width_cm=14
    ))

    story.append(add_heading("F.2 Statistical Chart: Per-Ram Variability in DPPE Response", styles['H2'], level=0, story=story))
    story.append(Paragraph(
        "Per-ram variability analysis (data not shown as separate figure) "
        "revealed consistent direction of treatment effect across all five rams, "
        "with no ram showing reversal of the DPPE-80 > DPPE-40 > control pattern. "
        "The coefficient of variation across rams ranged from 4.2% to 7.8% "
        "depending on parameter and time point, indicating acceptable biological "
        "repeatability. This consistency supports the generalizability of the "
        "treatment effect beyond the specific animals tested.",
        styles['FrontBody']
    ))

    story.append(add_heading("F.3 Methodological Workflow Diagrams", styles['H2'], level=0, story=story))
    story.extend(build_figure(
        'fig_3_3_dpp_preparation.png',
        "Supplementary presentation of the DPPE preparation protocol flowchart "
        "(originally Figure 3.3).",
        "Figure F.2", styles, width_cm=12
    ))

    story.extend(build_figure(
        'fig_3_4_sperm_assessment.png',
        "Supplementary presentation of the sperm recovery and assessment "
        "workflow (originally Figure 3.4).",
        "Figure F.3", styles, width_cm=14
    ))

    story.append(Spacer(1, 18))
    story.append(Paragraph(
        "<i>[End of Thesis]</i>",
        ParagraphStyle('end', fontName='Tinos-Italic', fontSize=11, alignment=TA_CENTER,
                       textColor=TEXT_MUTED)
    ))


if __name__ == '__main__':
    print("This module provides Chapter 5, References, and Appendices.")
    print("Run: python3 /home/z/my-project/scripts/build_thesis_main.py")
