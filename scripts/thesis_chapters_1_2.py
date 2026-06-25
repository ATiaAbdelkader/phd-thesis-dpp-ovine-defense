#!/usr/bin/env python3
"""
PhD Thesis Content — Chapters 1 & 2
====================================
Chapter 1: General Introduction (rewritten for actual 4-experiment scope)
Chapter 2: Literature Review (consolidated from source)
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
# CHAPTER 1: GENERAL INTRODUCTION
# ===================================================================
def build_chapter_1(story, styles):
    """Chapter 1: General Introduction (rewritten to align with actual 4-experiment scope)."""
    chapter_separator(story, styles, 1,
                      "General Introduction",
                      "Introduction Générale")

    # 1.1 Background of the Study
    story.append(add_heading("1.1 Background of the Study", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "Sheep (<i>Ovis aries</i> L.) constitute one of humanity's most genetically diverse "
        "livestock species, with more than 1,300 recognized breeds worldwide, each representing "
        "unique adaptations to extreme environmental conditions including high-altitude hypoxia, "
        "arid-zone heat stress, disease endemicity, and nutritional marginality (Wanjala, 2025; "
        "Dossybayev, 2025; Hansen, 2025). This genetic diversity underpins global food security, "
        "ecosystem resilience, and the capacity of pastoral systems to adapt to accelerating "
        "climate change (Muthusamy, 2025; Ma, 2025). Yet this biological heritage faces an "
        "unprecedented threat: approximately 27% of sheep breeds are currently classified as "
        "endangered, with demographic bottlenecks, uncontrolled crossbreeding, and intensifying "
        "environmental pressures accelerating genetic erosion (Motaung, 2024; Barłowska, 2025; "
        "Tampaki, 2025). The conservation of animal genetic resources (AnGR) has consequently "
        "emerged as a strategic global priority, with the Food and Agriculture Organisation "
        "(FAO) promoting integrated <i>in situ</i> and <i>ex situ</i> strategies to safeguard "
        "biodiversity and address economic, ecological, social, and cultural demands "
        "(Engdawork et al., 2024).",
        styles['Body']
    ))

    story.append(Paragraph(
        "Within the Algerian context, sheep production occupies a cornerstone position in the "
        "national agricultural economy and rural livelihoods. The Ouled Djellal breed, in "
        "particular, represents the dominant Algerian sheep population, prized for its adaptation "
        "to arid and semi-arid steppe environments, its meat production qualities, and its "
        "resilience under marginal nutritional conditions (Sebkhi et al., 2024; Laouadi et al., "
        "2018a). However, the breed faces mounting pressures from climate change, characterized "
        "by increasing frequency of droughts, declining pasture productivity, and intensified "
        "thermal stress — all of which elevate mortality rates in genetically valuable breeding "
        "stock and accelerate the risk of irreversible genetic loss. The El Oued region of "
        "southeast Algeria, situated at the heart of the Algerian Sahara, exemplifies these "
        "intersecting challenges: it is simultaneously a major centre of date palm cultivation "
        "and a substantial sheep production zone, creating a unique geographic convergence "
        "between an underexploited botanical resource (date palm pollen) and a pressing "
        "conservation need (ovine genetic rescue).",
        styles['Body']
    ))

    story.append(Paragraph(
        "Among <i>ex situ</i> conservation approaches, germplasm cryobanking — particularly "
        "sperm cryopreservation — provides a cost-effective, long-term solution enabling breed "
        "reconstitution, international genetic exchange, and targeted genetic improvement "
        "(Castro et al., 2025; Shayestehyekta et al., 2025; Boes et al., 2023). However, "
        "conventional cryobanking relies primarily on elective semen collection from live "
        "animals through electroejaculation or artificial vagina techniques. This approach "
        "cannot address the acute genetic emergencies posed by sudden mortality in valuable "
        "individuals or small endangered populations — exactly the scenarios that define the "
        "conservation challenge in arid Algeria's pastoral systems. When a genetically elite "
        "Ouled Djellal ram dies unexpectedly from pneumonia, heat stroke, or predation, the "
        "decades of selective breeding it embodies risk permanent loss unless alternative "
        "genetic salvage pathways are available.",
        styles['Body']
    ))

    # 1.2 Research Problem
    story.append(add_heading("1.2 Research Problem", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "Consider the concrete scenario that motivates this investigation: a genetically elite "
        "Ouled Djellal ram, bearing polymorphisms in genes associated with enhanced meat "
        "production qualities and adaptation capability, dies abruptly of severe pneumonia at "
        "a research station in Djelfa, Algeria. The animal represents years of selective "
        "breeding for improved growth rates, carcass quality, and resilience in semi-arid to "
        "arid steppe environments, all features increasingly valued under climate change "
        "(Sebkhi et al., 2024). With live collection impossible, what genetic material can "
        "be salvaged? Within 24–48 hours, if the carcass has been cooled appropriately, the "
        "cauda epididymides may yield 5–15 billion spermatozoa capable of fertilization via "
        "assisted reproduction (Anciuti et al., 2025; Mujitaba et al., 2024). Without "
        "intervention, this genetic line is permanently lost; with optimized post-slaughter "
        "recovery and preservation, the ram's genetic contribution may extend across decades "
        "and geographies.",
        styles['Body']
    ))

    story.append(Paragraph(
        "Post-slaughter sperm recovery — specifically the retrieval and preservation of "
        "epididymal spermatozoa from animals that die unexpectedly, are culled, or are "
        "euthanized — constitutes an increasingly critical strategy for genetic conservation "
        "(Engdawork et al., 2024; Silva et al., 2025). Unlike elective germplasm collection "
        "through electroejaculation, post-slaughter recovery captures genetic material that "
        "would otherwise be irretrievably lost. The technique has demonstrated practical "
        "success: pregnancy rates of 87.5% have been achieved with cryopreserved epididymal "
        "sperm from Hungarian Black Racka and Merino rams in artificial insemination and "
        "in vitro fertilization programs (Mujitaba et al., 2024; Sharafi et al., 2022). The "
        "epididymis functions as a natural reservoir of mature spermatozoa, recoverable "
        "within 24–48 hours post-mortem with minimal quality deterioration when testes are "
        "stored at 4–5°C, providing a practical genetic \"insurance policy\" in both "
        "slaughterhouse and conservation settings (Shayestehyekta et al., 2022; Silva et al., 2025).",
        styles['Body']
    ))

    story.append(Paragraph(
        "However, the efficacy of genetic rescue hinges on a narrow temporal window and the "
        "quality of preservation achieved within that window — a constraint that defines the "
        "central challenge of this thesis. Upon somatic death, the cessation of systemic "
        "metabolic support initiates a rapid biochemical cascade: ischemia forces anaerobic "
        "glycolysis and ATP depletion; mitochondrial electron transport chain disruption "
        "generates reactive oxygen species (ROS); iron-catalysed Fenton chemistry produces "
        "hydroxyl radicals; and lipid peroxidation propagates membrane damage (Fleming & "
        "Thomson, 2025; Shi et al., 2025). This \"golden hour\" framework creates both "
        "opportunity and imperative for intervention. The systematic failure of conventional "
        "single-mechanism antioxidants (TROLOX, cysteine) to address multi-source ROS "
        "generation in post-mortem contexts creates a specific research imperative: the "
        "identification of antioxidant interventions capable of multi-target action, membrane "
        "integration, mitochondrial protection, metal chelation, and sustainable field "
        "implementation in resource-limited genetic banking contexts.",
        styles['Body']
    ))

    # 1.3 Research Gap
    story.append(add_heading("1.3 Research Gap", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "Three interlocking gaps converge to define the research opportunity addressed by "
        "this thesis. First, an <b>empirical gap</b>: despite extensive cross-species evidence "
        "demonstrating reproductive benefits of Date Palm Pollen (DPP) supplementation in "
        "bulls (Amsah et al., 2021), goats (Ng et al., 2022), buffalo (El-Sheshtawy et al., "
        "2016), and rabbits (El-Seadawy et al., 2023; Laghouati et al., 2021, 2023), no "
        "studies have evaluated DPP specifically in ovine sperm, and no studies have tested "
        "DPP in post-slaughter epididymal contexts in any species. This translational gap "
        "between demonstrated general efficacy and specific application to the unique "
        "biological context of post-mortem ovine genetic rescue remains unaddressed in the "
        "literature.",
        styles['Body']
    ))

    story.append(Paragraph(
        "Second, a <b>methodological gap</b>: existing preservation protocols designed for "
        "healthy ejaculated semen systematically fail to address the dual insult — "
        "post-mortem deterioration compounded by cryoinjury or chilled-storage deterioration "
        "— characteristic of post-slaughter contexts. Chemical antioxidants such as TROLOX "
        "and cysteine operate through single mechanisms that cannot address the multi-source "
        "ROS generation (mitochondrial, enzymatic, Fenton chemistry) typical of post-mortem "
        "deterioration (Kafi et al., 2024). TROLOX's aqueous solubility restricts membrane "
        "integration and mitochondrial access; cysteine requires metabolic activation "
        "compromised by post-mortem metabolic decline. Enzymatic antioxidants are "
        "membrane-impermeable, temperature-sensitive, and impractical for field application "
        "(Kurochkin & Pleshanov, 2024).",
        styles['Body']
    ))

    story.append(Paragraph(
        "Third, an <b>integration gap</b>: previous studies treat technical efficacy "
        "(sperm preservation), socioeconomic context (keeper preferences), and environmental "
        "pressure (climate change) as siloed inquiries. No prior research has integrated "
        "these three dimensions into a unified conservation framework for arid-zone ovine "
        "genetic resources. Without such integration, technical solutions risk "
        "field-inapplicability, conservation priorities risk misalignment with keeper "
        "needs, and climate-induced urgency remains disconnected from actionable "
        "preservation tools. This thesis addresses all three gaps simultaneously through "
        "a multi-experimental design integrating socioeconomic survey, phytochemical "
        "characterization, controlled preservation trials, and climate-perception "
        "documentation.",
        styles['Body']
    ))

    # 1.4 Research Questions
    story.append(add_heading("1.4 Research Questions", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "This thesis is guided by four interconnected research questions (RQs), each "
        "corresponding to one of the four experiments:",
        styles['Body']
    ))

    rqs = [
        ("<b>RQ1.</b>", "What are the socioeconomic determinants and trait preferences "
         "defining genetic conservation priorities among sheep keepers in the El Oued "
         "region of arid Algeria?"),
        ("<b>RQ2.</b>", "Does Date Palm Pollen sourced from El Oued possess the biochemical "
         "composition and antioxidant capacity necessary to function as a sperm "
         "cryoprotective agent?"),
        ("<b>RQ3.</b>", "Is aqueous Date Palm Pollen Extender (DPPE) effective for preserving "
         "post-slaughter ovine epididymal sperm quality during chilled storage at 4°C, "
         "and does the effect follow a dose-dependent pattern?"),
        ("<b>RQ4.</b>", "How do climate change perceptions among sheep keepers influence the "
         "urgency for genetic conservation interventions, and which flock-size categories "
         "are most vulnerable to perceived fertility impacts?"),
    ]
    for label, q in rqs:
        story.append(Paragraph(f"{label} {q}", styles['NumberedItem']))

    story.append(Spacer(1, 6))

    # 1.5 Research Objectives
    story.append(add_heading("1.5 Research Objectives", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "Aligned with the four research questions, four specific objectives guide the "
        "research, each operationalized through a dedicated experiment:",
        styles['Body']
    ))

    objectives = [
        ("<b>Objective 1 (Experiment 1).</b>", "Establish the socioeconomic context and "
         "trait preferences defining genetic conservation priorities among 200 sheep keepers "
         "across eight municipalities of El Oued, with stratification by flock size, age, "
         "education, and occupation."),
        ("<b>Objective 2 (Experiment 2).</b>", "Characterize the phytochemical profile of "
         "El Oued-sourced Date Palm Pollen through proximate analysis (moisture, ash, fat, "
         "protein, carbohydrate, fibre), mineral determination (Ca, Mg, K, Na), quantification "
         "of total phenolics and flavonoids, and assessment of DPPH radical scavenging "
         "activity."),
        ("<b>Objective 3 (Experiment 3).</b>", "Evaluate the dose-dependent efficacy of "
         "aqueous DPPE extenders at 0 (control), 40, and 80 mg/mL on post-slaughter ovine "
         "epididymal sperm quality (total motility, progressive motility via CASA, and "
         "membrane integrity via HOST) during chilled storage at 4°C over 0, 24, and 48 "
         "hours."),
        ("<b>Objective 4 (Experiment 4).</b>", "Document climate change perceptions and "
         "their linkage to perceived fertility declines among El Oued sheep keepers, "
         "identifying vulnerable flock-size categories through binary logistic regression "
         "of perceived fertility decline predictors."),
    ]
    for label, o in objectives:
        story.append(Paragraph(f"{label} {o}", styles['NumberedItem']))

    story.append(Spacer(1, 6))

    # Table 1.1: Research questions, objectives, hypotheses
    table_data = [
        ['Exp.', 'Research Question', 'Objective', 'Hypothesis', 'Statistical Test'],
        ['1', 'Socioeconomic determinants and trait preferences',
         'Profile 200 keepers across 8 municipalities',
         'Ha1: Education, experience, and occupation interact to shape trait priorities',
         'MANOVA (Pillai\'s Trace)'],
        ['2', 'Biochemical profile of local DPP',
         'Proximate, mineral, phenolic, DPPH characterization',
         'Ha2: Local DPP possesses antioxidant capacity suitable for cryoprotection',
         'Descriptive (mean ± SD)'],
        ['3', 'DPPE efficacy for chilled sperm preservation',
         'Test DPPE-0/40/80 mg/mL × 0/24/48 h at 4°C',
         'Ha3: DPPE-80 significantly preserves sperm quality in dose-dependent manner',
         'Two-way RM-ANOVA'],
        ['4', 'Climate change perceptions and fertility link',
         'Quantify climate-fertility awareness and vulnerability',
         'Ha4: Climate perceptions significantly predict fertility decline; medium flocks most vulnerable',
         'Binary logistic regression'],
    ]
    story.extend(build_table(
        table_data,
        col_widths=[0.9*cm, 3.5*cm, 3.8*cm, 4.5*cm, 3.3*cm],
        caption="Alignment of research questions, objectives, hypotheses, and "
                "statistical tests across the four experiments.",
        caption_num="Table 1.1",
        styles=styles, font_size=8.5
    ))

    # 1.6 Hypotheses
    story.append(add_heading("1.6 Hypotheses", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "Four Alternative Hypotheses (Ha) and corresponding Null Hypotheses (H0) are "
        "proposed, each directly testable through the corresponding experiment:",
        styles['Body']
    ))

    hypotheses = [
        ("<b>Ha1:</b>", "Education, experience, and occupation interact significantly to "
         "shape trait preferences among El Oued sheep keepers (Pillai's Trace < 0.05). "
         "<b>H01:</b> There is no significant interaction effect."),
        ("<b>Ha2:</b>", "El Oued-sourced DPP exhibits a nutrient-dense biochemical profile "
         "with measurable polyphenol content and DPPH radical scavenging activity. "
         "<b>H02:</b> DPP lacks significant antioxidant capacity."),
        ("<b>Ha3:</b>", "DPPE-80 (80 mg/mL) significantly preserves total motility, "
         "progressive motility, and membrane integrity compared to control (DPPE-0) "
         "across 0, 24, and 48 hours of chilled storage at 4°C. <b>H03:</b> DPPE has no "
         "significant effect on sperm quality parameters."),
        ("<b>Ha4:</b>", "Climate change perceptions significantly predict perceived fertility "
         "decline among sheep keepers, with medium-sized flocks (20–50 head) showing the "
         "highest vulnerability. <b>H04:</b> There is no significant association between "
         "climate perceptions and fertility decline."),
    ]
    for label, h in hypotheses:
        story.append(Paragraph(f"{label} {h}", styles['Hypothesis']))

    story.append(Spacer(1, 8))

    # 1.7 Significance of the Study
    story.append(add_heading("1.7 Significance of the Study", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "This investigation represents the first systematic study of Date Palm Pollen's "
        "conservative effects specifically in post-slaughter ovine epididymal sperm in the "
        "Algerian Sahara, addressing a critical translational gap with implications spanning "
        "scientific understanding, technical development, conservation impact, and policy "
        "design. The significance is articulated through four complementary lenses:",
        styles['Body']
    ))

    story.append(Paragraph(
        "<b>Theoretical significance.</b> The thesis contributes to three theoretical domains. "
        "First, it establishes species-specific DPP efficacy data for ovine sperm, "
        "addressing the empirical gap created by the absence of ovine trials in the "
        "existing DPP literature. Second, it validates the polypharmacological antioxidant "
        "action of botanical matrices in post-mortem cells — a physiological context "
        "fundamentally different from the healthy ejaculated semen on which most antioxidant "
        "research has been conducted. Third, it advances the theory of Agro-Ecological "
        "Cryobiology by demonstrating that preservation media need not be standardized "
        "globally but can be optimized using locally available agro-byproducts, reducing "
        "dependency on imported supply chains.",
        styles['Body']
    ))

    story.append(Paragraph(
        "<b>Practical significance.</b> The research delivers a validated, field-applicable "
        "DPPE supplementation protocol for ovine genetic banking, including quality control "
        "parameters for standardization and a decision framework for practitioners. By "
        "extending the practical preservation window from less than 24 hours to more than "
        "48 hours, the protocol enables real-world application in remote pastoral systems "
        "where cryopreservation infrastructure is unavailable. The 48-Hour Genetic Rescue "
        "Protocol can be deployed in abattoirs, veterinary clinics, and on-farm emergency "
        "settings.",
        styles['Body']
    ))

    story.append(Paragraph(
        "<b>Conservation significance.</b> Enhanced genetic salvage rates from post-slaughter "
        "recovery reduce the irreversible loss of valuable genotypes when elite breeding "
        "stock die unexpectedly. The DPPE protocol reduces both cost and infrastructure "
        "requirements for genetic banking in developing regions, and the cultural "
        "appropriateness of DPP — traditionally used in regions where sheep and date palms "
        "co-occur — aligns with arid-zone agroecosystem realities. The intervention is "
        "particularly relevant for safeguarding the Ouled Djellal breed, whose genetic "
        "distinctiveness underpins Algerian pastoral livelihoods.",
        styles['Body']
    ))

    story.append(Paragraph(
        "<b>Policy significance.</b> By integrating socioeconomic priorities, climate-change "
        "urgency, and technical feasibility into a triangulated conservation model, the "
        "thesis informs national breeding program design, agricultural extension curricula, "
        "and climate adaptation policy. The identification of medium-sized flocks "
        "(20–50 head) as the vulnerability sweet spot enables targeted policy intervention "
        "rather than undifferentiated support distribution.",
        styles['Body']
    ))

    # 1.8 Scope and Limitations
    story.append(add_heading("1.8 Scope, Delimitations, and Limitations", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "The study is delimited along several dimensions to ensure methodological rigor and "
        "interpretable results. Geographically, the research is confined to the El Oued "
        "province of southeast Algeria, with the socioeconomic survey covering eight "
        "municipalities (El Oued, Debila, Guemar, Hassi Khelifa, Mih Ouensa, Ourmes, "
        "Robbah, and Taleb Larbi) and the DPP sourced from Hamraia commune in the Reguiba "
        "District. Biologically, the experimental trial is restricted to sexually mature "
        "Ouled Djellal rams aged 18–24 months, providing standardization of breed and age "
        "effects. Temporally, the post-mortem window is delimited to sperm recovered within "
        "2 hours of slaughter with carcass storage at 4°C, and the preservation trial "
        "covers 48 hours of chilled storage — a timeframe chosen for its field relevance "
        "and biological significance. Methodologically, the trial employs chilled storage "
        "at 4°C rather than cryopreservation; this choice reflects the field-applicability "
        "objective and acknowledges the limited cryopreservation infrastructure in target "
        "pastoral systems.",
        styles['Body']
    ))

    story.append(Paragraph(
        "Several limitations are acknowledged at the outset. The sample size in Experiment 3 "
        "(n = 5 rams) provides adequate statistical power for detecting large effects but "
        "may miss subtle treatment differences; replication across seasons and breeds would "
        "strengthen generalizability. The chilled-storage protocol, while field-relevant, "
        "does not test DPP effects on freeze-thaw survival; cryopreservation trials remain "
        "a priority for follow-up research. Single DPP source characterization (Hamraia) "
        "means geographic variation in composition cannot be assessed within this thesis. "
        "The assessment endpoints focus on motility and membrane integrity; comprehensive "
        "hierarchical assessment including oxidative status, mitochondrial function, DNA "
        "integrity, and fertilizing capacity via in vitro fertilization requires expanded "
        "methodology in future studies. Finally, the climate-perception data (Experiment 4) "
        "relies on breeder perceptions rather than objective meteorological or reproductive "
        "records, which limits causal attribution.",
        styles['Body']
    ))

    # 1.9 Thesis Organization
    story.append(add_heading("1.9 Thesis Organization", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "The thesis is organized into five chapters that follow a logical progression from "
        "problem framing through literature synthesis, methodological description, integrated "
        "results and discussion, and concluding synthesis with recommendations. Chapter 1 "
        "(General Introduction) establishes the research problem, gaps, questions, "
        "objectives, hypotheses, and significance. Chapter 2 (Literature Review) provides "
        "the theoretical and empirical foundation by synthesizing the global literature on "
        "ovine genetic diversity, post-slaughter sperm recovery, oxidative stress biology, "
        "conventional antioxidant limitations, DPP biochemistry and cross-species evidence, "
        "and climate change impacts on small ruminant fertility, culminating in a conceptual "
        "framework that integrates the three dimensions of the research.",
        styles['Body']
    ))

    story.append(Paragraph(
        "Chapter 3 (Materials and Methods) describes the four-experiment research design, "
        "study area, sampling strategy, data collection instruments, laboratory procedures, "
        "phytochemical characterization methods, sperm assessment protocols, and statistical "
        "analyses. Chapter 4 (Results and Discussion) presents the empirical findings of all "
        "four experiments in an integrated results-and-discussion format, with each result "
        "immediately interpreted, compared with previous studies, and related to the study "
        "objectives. Chapter 5 (General Conclusion and Recommendations) synthesizes the "
        "empirical findings into theoretical contributions, articulates practical and policy "
        "recommendations, candidly acknowledges study limitations, and proposes future "
        "research directions. The thesis is supported by multilingual abstracts (English, "
        "French, Arabic), a comprehensive list of abbreviations and symbols, six appendices "
        "(questionnaires, laboratory protocols, ethical approval, raw data summaries, "
        "additional statistical outputs, supplementary figures), and a complete reference "
        "list.",
        styles['Body']
    ))

    story.append(PageBreak())


# ===================================================================
# CHAPTER 2: LITERATURE REVIEW
# ===================================================================
def build_chapter_2(story, styles):
    """Chapter 2: Literature Review."""
    chapter_separator(story, styles, 2,
                      "Literature Review",
                      "Revue de la Littérature")

    # 2.1 The Conservation Imperative
    story.append(add_heading("2.1 The Conservation Imperative: Post-Slaughter Genetic Rescue in Sheep", styles['H1'], level=0, story=story))

    story.append(add_heading("2.1.1 The Scenario of Genetic Emergency", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Consider the following scenario: a genetically elite Ouled Djellal ram, bearing "
        "polymorphisms in genes associated with enhanced meat production qualities and "
        "adaptation capability, dies abruptly of severe pneumonia at a research station "
        "in Djelfa, Algeria. The animal represents years of selective breeding for improved "
        "growth rates, carcass quality, and resilience in semi-arid to arid steppe "
        "environments — all features increasingly valued under climate change (Sebkhi et al., "
        "2024). What genetic material may be saved while live harvesting is impossible? "
        "Within 24–48 hours, assuming the carcass has been properly refrigerated, the cauda "
        "epididymides may generate 5–15 billion spermatozoa capable of fertilization by "
        "assisted reproduction (Anciuti et al., 2025; Mujitaba et al., 2022). Without "
        "intervention, this genetic line will be forever lost. With optimal post-slaughter "
        "recovery and preservation, the ram's genetic contribution might span decades and "
        "countries.",
        styles['Body']
    ))

    story.append(Paragraph(
        "This scenario is not hypothetical; it is replayed with disturbing regularity in "
        "research stations, breeding farms, and pastoral systems worldwide. The Food and "
        "Agriculture Organisation estimates that approximately 27% of the world's 1,300+ "
        "sheep breeds are classified as endangered (FAO, 2023), and a substantial fraction "
        "of these breeds survive in small populations where the loss of a single breeding "
        "male can produce catastrophic genetic bottlenecks. In Algeria, the Ouled Djellal "
        "breed — although numerically dominant — faces insidious genetic erosion through "
        "uncontrolled crossbreeding, demographic attrition of purebred stocks, and the "
        "cumulative loss of genetically elite individuals to disease, predation, and "
        "climate-induced mortality.",
        styles['Body']
    ))

    story.append(add_heading("2.1.2 Global Status of Ovine Genetic Diversity", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Sheep were among the first domesticated livestock species, with archaeological "
        "evidence placing initial domestication in the Fertile Crescent approximately "
        "11,000 years ago (Dossybayev, 2025; Hansen, 2025). Over millennia, natural and "
        "human selection across diverse agroecological zones produced the remarkable "
        "phenotypic and genetic diversity observed today: from the high-altitude adapted "
        "Tibetan sheep to the heat-tolerant Awassi of the Middle East, from the "
        "fecund Booroola Merino to the wool-specialized Merino, from the milk-producing "
        "East Friesian to the fat-tailed Barbarine of North Africa. Each breed embodies "
        "a unique combination of genetic variants shaped by environmental pressure and "
        "human cultural preference, providing the raw material for future adaptation "
        "(Muthusamy, 2025; Ma, 2025).",
        styles['Body']
    ))

    story.append(Paragraph(
        "However, this diversity faces unprecedented threat. The intensification of "
        "livestock production has favoured a small number of high-output breeds at the "
        "expense of locally adapted varieties; demographic bottlenecks have reduced "
        "effective population sizes; uncontrolled crossbreeding has diluted breed-specific "
        "genetic signatures; and accelerating climate change has imposed novel selection "
        "pressures that exceed the adaptive capacity of many populations (Motaung, 2024; "
        "Barłowska, 2025; Tampaki, 2025). The conservation of animal genetic resources "
        "(AnGR) has consequently emerged as a strategic global priority, with the FAO "
        "promoting integrated <i>in situ</i> (live population conservation) and <i>ex situ</i> "
        "(germplasm banking) strategies to safeguard biodiversity (Engdawork et al., 2024).",
        styles['Body']
    ))

    # Figure 2.1: ROS cascade
    story.extend(build_figure(
        'fig_2_1_ros_cascade.png',
        "Biochemical cascade of post-mortem sperm deterioration and the critical "
        "intervention window during which antioxidant supplementation can partially "
        "mitigate oxidative damage.",
        "Figure 2.1", styles, width_cm=14
    ))

    # 2.2 Post-Slaughter Sperm Recovery
    story.append(add_heading("2.2 Post-Slaughter Sperm Recovery: Biology, Methods, and Field Applicability", styles['H1'], level=0, story=story))

    story.append(add_heading("2.2.1 The Cauda Epididymidis as a Genetic Reservoir", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "The mammalian epididymis is a long, convoluted tubule that connects the testis "
        "to the vas deferens, providing the environment in which spermatozoa acquire "
        "motility and fertilizing capacity (Wu et al., 2021). The cauda epididymidis — the "
        "distal segment — serves as the principal sperm storage reservoir in the male "
        "reproductive tract, harboring mature, fertilizable spermatozoa in a quiescent "
        "state maintained by low pH, high protein concentration, and specific inhibitory "
        "factors (Shi et al., 2025). At any given time, the paired caudae of a sexually "
        "mature ram contain approximately 5–15 billion spermatozoa, representing a "
        "substantial genetic reservoir recoverable after death.",
        styles['Body']
    ))

    story.append(Paragraph(
        "Crucially, spermatozoa within the cauda epididymidis are not immediately lost "
        "upon somatic death. If the testes are retrieved promptly and cooled appropriately, "
        "the cauda microenvironment continues to preserve sperm viability for 24–48 hours "
        "(Shayestehyekta et al., 2022; Silva et al., 2025). This post-mortem survival "
        "window creates the biological basis for post-slaughter genetic rescue: with "
        "appropriate intervention, the genetic material housed in the cauda can be "
        "salvaged, preserved, and used for assisted reproduction long after the donor "
        "animal has died. Pregnancy rates of 87.5% have been achieved with cryopreserved "
        "epididymal sperm from Hungarian Black Racka and Merino rams (Mujitaba et al., "
        "2024; Sharafi et al., 2022), demonstrating the practical feasibility of this "
        "approach.",
        styles['Body']
    ))

    story.append(add_heading("2.2.2 Recovery Techniques: Retrograde Flushing and Alternatives", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Several techniques have been developed for retrieving epididymal spermatozoa "
        "from post-mortem testes. The <i>mincing method</i> involves cutting the cauda "
        "into small fragments in a saline or extender solution, releasing sperm by "
        "mechanical disruption. While simple, this method yields sperm with significant "
        "contamination by tissue debris, blood cells, and lipid droplets that compromise "
        "subsequent analysis and preservation (Martinez-Pastor et al., 2006). The "
        "<i>aspiration method</i> uses a needle and syringe to withdraw sperm directly "
        "from the cauda lumen, producing cleaner samples but with lower recovery "
        "efficiency. The <i>retrograde flushing method</i>, employed in this thesis, "
        "introduces a saline solution into the vas deferens and applies gentle pressure "
        "to flush spermatozoa retrograde through the cauda, collecting them at the "
        "incised corpus-cauda junction (Martinez-Pastor et al., 2006). This method "
        "balances recovery efficiency (5–15 billion sperm per paired caudae) with low "
        "contamination and minimal equipment requirements, making it particularly "
        "suitable for field conditions in resource-limited settings.",
        styles['Body']
    ))

    story.append(Paragraph(
        "Regardless of retrieval method, the recovered epididymal spermatozoa share "
        "three biological characteristics that distinguish them from ejaculated semen "
        "and shape the requirements for preservation protocols. First, they lack "
        "exposure to seminal plasma — the complex mixture of accessory gland secretions "
        "that provides antioxidant buffering, membrane stabilizers, metabolic substrates, "
        "and immunological protection to ejaculated sperm (van Tilburg et al., 2021). "
        "Second, they have completed maturation but remain in a quiescent metabolic "
        "state, requiring activation before use in assisted reproduction. Third, they "
        "may have already sustained post-mortem oxidative damage during the interval "
        "between somatic death and recovery, particularly if cooling was delayed.",
        styles['Body']
    ))

    # 2.3 Oxidative Stress Biology
    story.append(add_heading("2.3 Oxidative Stress in Sperm Preservation: The Multi-Source ROS Challenge", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "Reactive oxygen species (ROS) encompass a family of oxygen-derived molecules "
        "with varying reactivity, including the superoxide anion (O₂•⁻), hydrogen "
        "peroxide (H₂O₂), hydroxyl radical (OH•), peroxyl radical (ROO•), and singlet "
        "oxygen (¹O₂). At physiological concentrations, ROS serve essential signaling "
        "functions in spermatozoa, including capacitation, hyperactivation, acrosome "
        "reaction, and sperm-oocyte fusion (Aitken & Drevet, 2020). However, when ROS "
        "production exceeds the buffering capacity of endogenous antioxidant systems, "
        "oxidative stress develops, leading to lipid peroxidation, protein oxidation, "
        "DNA damage, and ultimately cell death.",
        styles['Body']
    ))

    story.append(add_heading("2.3.1 The Ovine-Specific Vulnerability: DHA-Rich Membranes", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Ram spermatozoa possess the highest docosahexaenoic acid (DHA) content among "
        "domestic livestock, comprising 30–40% of plasma membrane phospholipid fatty "
        "acids (Abdollahzadeh et al., 2025; Carro et al., 2022). DHA, a 22-carbon "
        "polyunsaturated fatty acid with six double bonds, is essential for membrane "
        "fluidity and the membrane fusion events underlying fertilization. However, the "
        "multiple bis-allylic methylene groups in DHA provide prime targets for radical "
        "attack: each bis-allylic carbon has a bond dissociation energy approximately "
        "75 kJ/mol lower than that of a mono-allylic carbon, making DHA-enriched "
        "membranes exceptionally susceptible to lipid peroxidation chain reactions "
        "(Aitken & Drevet, 2020). Once initiated, lipid peroxidation propagates "
        "self-sustainingly across the membrane, generating lipid hydroperoxides, "
        "aldehydes (malondialdehyde, 4-hydroxynonenal), and volatile hydrocarbons "
        "that damage membrane integrity, enzyme function, and DNA.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The sperm midpiece, housing 70–80 mitochondria arranged in a helical sheath "
        "around the axoneme, is particularly vulnerable to oxidative damage. Mitochondrial "
        "membranes themselves are PUFA-rich, and mitochondrial electron transport chain "
        "complexes I and III constitute the primary endogenous source of cellular ROS "
        "under physiological conditions. When mitochondrial function is compromised — as "
        "occurs rapidly during ischemia, cryopreservation, or chilled storage — electron "
        "leakage increases, generating elevated superoxide that overwhelms mitochondrial "
        "superoxide dismutase (SOD2) capacity and propagates damage to the midpiece "
        "infrastructure (Wang et al., 2024; Zhu et al., 2024). The resulting ATP "
        "depletion compromises dynein arm function, impairing flagellar beat and "
        "progressive motility — the functional hallmark of oxidative midpiece damage.",
        styles['Body']
    ))

    story.append(add_heading("2.3.2 Multi-Source ROS Generation in Post-Mortem Contexts", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Post-mortem deterioration generates ROS through at least three distinct "
        "mechanisms, creating a multi-source oxidative challenge that overwhelms "
        "single-mechanism antioxidant defenses. First, <b>mitochondrial ROS</b> "
        "generation increases sharply upon cessation of systemic oxygen delivery. "
        "Ischemia forces anaerobic glycolysis, depleting ATP and elevating NADH/NAD⁺ "
        "ratios; upon any residual oxygen availability, electron transport chain "
        "complexes leak electrons to oxygen, generating superoxide (Shi et al., 2025; "
        "Fleming & Thomson, 2025). Second, <b>iron-catalysed Fenton chemistry</b> "
        "becomes significant as cellular compartmentalization breaks down: free "
        "ferrous iron (Fe²⁺) released from hemoglobin, myoglobin, and iron-sulfur "
        "proteins reacts with hydrogen peroxide to generate the highly reactive "
        "hydroxyl radical (OH•), which initiates lipid peroxidation at diffusion-"
        "limited rates.",
        styles['Body']
    ))

    story.append(Paragraph(
        "Third, <b>enzymatic ROS generation</b> by xanthine oxidase, NADPH oxidase, "
        "and lipoxygenase systems continues — and may accelerate — post-mortem as "
        "substrate accumulation and pH changes activate these enzymes. The convergence "
        "of these three ROS sources creates an oxidative environment qualitatively "
        "different from the primarily mitochondrial ROS generation characteristic of "
        "physiological sperm metabolism. Conventional antioxidant strategies designed "
        "for healthy, ejaculated semen — where ROS generation is predominantly "
        "mitochondrial and well-buffered by seminal plasma — systematically fail to "
        "address this multi-source challenge, creating the research imperative for "
        "multi-target antioxidant interventions.",
        styles['Body']
    ))

    # 2.4 Conventional Antioxidants
    story.append(add_heading("2.4 Conventional Antioxidant Strategies and Their Systematic Limitations", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "Extensive research has evaluated antioxidant supplementation of semen extenders, "
        "with demonstrated benefits for ejaculated semen cryopreservation (Shayestehyekta "
        "et al., 2025; Howard et al., 2025). However, critical analysis reveals fundamental "
        "limitations when conventional approaches are applied to post-slaughter contexts. "
        "These limitations, summarized in Table 2.2, define the specific research imperative "
        "for multi-target botanical alternatives.",
        styles['Body']
    ))

    table_2_2_data = [
        ['Antioxidant', 'Mechanism', 'Strengths', 'Limitations in Post-Slaughter Contexts'],
        ['TROLOX (vitamin E analog)',
         'Chain-breaking radical scavenging (aqueous)',
         'Potent peroxyl radical scavenger; well-characterized kinetics',
         'Aqueous solubility restricts membrane integration; cannot access mitochondrial interior; single-mechanism action insufficient for multi-source ROS'],
        ['Cysteine (thiol donor)',
         'Glutathione precursor; direct radical scavenging',
         'Replenishes intracellular GSH; supports GPx cycle',
         'Requires metabolic activation (compromised post-mortem); pro-oxidant risk with transition metals; needs cellular uptake machinery'],
        ['Enzymatic antioxidants (SOD, CAT, GPx)',
         'Enzymatic ROS detoxification',
         'High catalytic efficiency; biological compatibility',
         'Membrane-impermeable; temperature-sensitive; expensive; impractical for field application'],
        ['Vitamin C (ascorbate)',
         'Aqueous-phase radical scavenging; α-tocopherol regeneration',
         'Inexpensive; widely available; synergistic with vitamin E',
         'Pro-oxidant in presence of free iron (Fenton chemistry); aqueous solubility restricts membrane protection'],
        ['Synthetic phenolic antioxidants (BHT, BHA)',
         'Chain-breaking radical scavenging (lipophilic)',
         'Membrane-integrating; stable; inexpensive',
         'Synthetic origin raises regulatory concerns; limited multi-target action; potential toxicity at high doses'],
    ]
    story.extend(build_table(
        table_2_2_data,
        col_widths=[3.6*cm, 4.0*cm, 3.8*cm, 4.6*cm],
        caption="Comparative analysis of conventional antioxidants and their systematic "
                "limitations when applied to post-slaughter sperm preservation contexts.",
        caption_num="Table 2.2",
        styles=styles, font_size=8.5
    ))

    story.append(Paragraph(
        "The systematic failure pattern is clear: each conventional antioxidant operates "
        "through a single mechanism (chain-breaking scavenging, GSH precursor provision, "
        "enzymatic detoxification), restricting protection to one ROS source or cellular "
        "compartment. None addresses the integrated multi-source ROS generation "
        "characteristic of post-mortem deterioration. TROLOX's aqueous solubility restricts "
        "membrane integration and mitochondrial access; cysteine requires metabolic "
        "activation compromised by post-mortem metabolic decline and exhibits pro-oxidant "
        "risk with transition metal exposure; enzymatic antioxidants are "
        "membrane-impermeable, temperature-sensitive, and impractical for field "
        "application. Standard semen extenders, designed for ejaculated semen, incorporate "
        "antioxidant components calibrated for healthy cells with intact seminal plasma "
        "protection — insufficient for pre-damaged post-slaughter sperm (Bustani & Baiee, "
        "2021; Sharafi et al., 2022).",
        styles['Body']
    ))

    # 2.5 DPP Biochemistry
    story.append(add_heading("2.5 Date Palm Pollen: Botanical, Biochemical, and Ethnopharmacological Profile", styles['H1'], level=0, story=story))

    story.append(add_heading("2.5.1 Botanical and Geographic Context", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "The date palm (<i>Phoenix dactylifera</i> L., Arecaceae) is one of humanity's "
        "oldest cultivated plants, with archaeological evidence of domestication in the "
        "Gulf region dating back over 7,000 years (Bouguedoura et al., 2015; Merrouchi & "
        "Sais, 2025a). The tree is uniquely adapted to arid and semi-arid environments, "
        "tolerating extreme heat, drought, and saline soils, and is cultivated across a "
        "geographic arc extending from Morocco in the west to India in the east, with "
        "significant plantings in North Africa, the Middle East, and Central Asia. Date "
        "palm pollen (DPP), the male gametophyte produced in mature male inflorescences "
        "(spathes), is harvested during the spring flowering season and has been used "
        "traditionally in folk medicine, cosmetics, and as a dietary supplement across "
        "the date-growing world (Salhi et al., 2024).",
        styles['Body']
    ))

    story.append(Paragraph(
        "Algeria ranks among the world's leading date producers, with the El Oued "
        "province — situated in the Algerian Sahara — representing one of the country's "
        "principal date palm cultivation zones (Mihi & Hernández-Agüero, 2025). The "
        "geographic convergence of date palm cultivation and sheep production in this "
        "region creates a unique opportunity for the application of DPP as a "
        "locally-sourced, culturally-acceptable sperm preservation agent. The traditional "
        "knowledge of date palm cultivation among local farmers, combined with the "
        "increasing scientific characterization of DPP bioactive compounds, positions "
        "this botanical resource as a promising intervention for arid-zone ovine genetic "
        "conservation.",
        styles['Body']
    ))

    story.append(add_heading("2.5.2 Bioactive Composition of DPP", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "DPP is not a single compound but a complex matrix of bioactive molecules whose "
        "composition varies with cultivar, geographic origin, harvest time, and post-"
        "harvest processing. The principal bioactive classes include:",
        styles['Body']
    ))

    story.append(Paragraph(
        "<b>Polyphenols.</b> DPP contains diverse phenolic compounds including gallic "
        "acid, rutin, quercetin, caffeic acid, catechin, and chlorogenic acid (Salhi "
        "et al., 2024). Total phenolic content varies considerably across regions "
        "(8.5–25.6 mg GAE/g), with substantial variation among cultivars. The phenolic "
        "diversity enables multi-target ROS scavenging: gallic acid provides potent "
        "hydrogen donation and iron chelation; rutin and quercetin offer amphiphilic "
        "mitochondrial targeting; caffeic acid contributes lipophilic membrane "
        "stabilization. This mechanistic diversity addresses mitochondrial superoxide, "
        "hydroxyl radical prevention through metal chelation, and lipid peroxidation "
        "chain-breaking simultaneously.",
        styles['Body']
    ))

    story.append(Paragraph(
        "<b>Fatty acids.</b> DPP contains substantial lipid fractions (typically 4–8% "
        "by weight) dominated by palmitic, linoleic, oleic, and lauric acids. These "
        "fatty acids contribute to membrane stabilizing effects and provide energy "
        "substrates that may support sperm metabolism during chilled storage. The "
        "presence of essential fatty acids (linoleic, α-linolenic) may also contribute "
        "to membrane repair processes.",
        styles['Body']
    ))

    story.append(Paragraph(
        "<b>Minerals.</b> DPP is rich in potassium (often exceeding 1,000 mg/100 g), "
        "phosphorus, calcium, magnesium, and trace minerals including zinc, selenium, "
        "copper, and iron. Zinc and selenium are particularly important for reproductive "
        "function as cofactors for endogenous antioxidant enzymes: zinc is essential "
        "for superoxide dismutase activity, while selenium is incorporated into the "
        "active site of glutathione peroxidase. The mineral profile of DPP thus "
        "complements the direct antioxidant action of polyphenols by supporting "
        "endogenous defense systems.",
        styles['Body']
    ))

    story.append(Paragraph(
        "<b>Vitamins.</b> DPP contains vitamins A, E (α-tocopherol), C (ascorbic acid), "
        "and B-complex (particularly B1, B2, B6, and B9). Vitamins E and C act as "
        "synergistic antioxidant partners — α-tocopherol scavenges peroxyl radicals "
        "in lipid membranes while ascorbate regenerates reduced α-tocopherol at the "
        "membrane-water interface. Folate (B9) supports DNA methylation and synthesis, "
        "with potential implications for sperm chromatin integrity.",
        styles['Body']
    ))

    story.append(Paragraph(
        "<b>Amino acids.</b> DPP contains all essential amino acids, with particularly "
        "high concentrations of arginine. Arginine serves as the precursor for nitric "
        "oxide synthesis, which at physiological concentrations regulates sperm "
        "capacitation and acrosome reaction. The amino acid profile of DPP may "
        "thus support functional competence during preservation.",
        styles['Body']
    ))

    # Figure 2.2: DPP mechanism
    story.extend(build_figure(
        'fig_2_2_dpp_mechanism.png',
        "Multi-target antioxidant action of Date Palm Pollen bioactive compounds, "
        "integrating polyphenol ROS scavenging, membrane integration, mitochondrial "
        "protection, and Nrf2-mediated endogenous defense upregulation.",
        "Figure 2.2", styles, width_cm=14
    ))

    # Table 2.3: Reported DPP composition
    table_2_3_data = [
        ['Bioactive Component', 'Reported Range', 'Primary Mechanism', 'References'],
        ['Total phenolics', '8.5–25.6 mg GAE/g', 'Multi-target ROS scavenging', 'Salhi et al., 2024; Laghouati et al., 2023'],
        ['Total flavonoids', '2.1–7.8 mg QE/g', 'Mitochondrial targeting, chelation', 'Ahn et al., 2007'],
        ['Protein', '15.2–37.9%', 'Amino acid precursors (arginine)', 'Salhi et al., 2024'],
        ['Carbohydrates', '21.5–35.0%', 'Energy substrate for sperm metabolism', 'Salhi et al., 2024'],
        ['Potassium', '850–1,250 mg/100g', 'Osmotic balance, enzyme cofactor', 'Laghouati et al., 2023'],
        ['Zinc', '4.2–9.6 mg/100g', 'SOD cofactor; semen quality', 'Salhi et al., 2024'],
        ['Selenium', '12–45 µg/100g', 'GPx cofactor; DNA protection', 'Salhi et al., 2024'],
        ['α-tocopherol (vit. E)', '2.5–8.9 mg/100g', 'Chain-breaking lipid peroxyl scavenger', 'Salhi et al., 2024'],
        ['Ascorbate (vit. C)', '8.5–22.0 mg/100g', 'Aqueous radical scavenger; α-tocopherol recycling', 'Salhi et al., 2024'],
    ]
    story.extend(build_table(
        table_2_3_data,
        col_widths=[3.8*cm, 3.5*cm, 4.5*cm, 4.2*cm],
        caption="Reported bioactive compounds in Date Palm Pollen across different "
                "geographic regions and cultivars, with their primary antioxidant mechanisms.",
        caption_num="Table 2.3",
        styles=styles, font_size=8.5
    ))

    # 2.6 Cross-Species Evidence
    story.append(add_heading("2.6 Cross-Species Evidence for DPP in Reproduction", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "Although no studies have evaluated DPP specifically in ovine sperm or in "
        "post-slaughter epididymal contexts, substantial cross-species evidence supports "
        "DPP's reproductive benefits. This translational literature, summarized in Table "
        "2.4, provides the empirical foundation for the present investigation while "
        "highlighting the species-specific gap that this thesis addresses.",
        styles['Body']
    ))

    table_2_4_data = [
        ['Species', 'Study Design', 'DPP Treatment', 'Key Findings', 'Reference'],
        ['Bull', 'Semen extender supplementation',
         'Aqueous DPP extract (1–5 mg/mL)',
         'Significant improvement in post-thaw progressive motility, viability, and membrane integrity; reduced MDA',
         'Amsah et al., 2021'],
        ['Goat', 'Epididymal sperm preservation',
         '5% DPP in Tris extender',
         'Improved acrosome integrity; higher cleavage rate after IVF; reduced DNA fragmentation',
         'Ng et al., 2022'],
        ['Buffalo', 'Cryopreservation trial',
         'DPP aqueous extract (10 mg/mL)',
         'Enhanced antioxidant enzyme activity (SOD, GPx); improved post-thaw motility; reduced ROS',
         'El-Sheshtawy et al., 2016'],
        ['Rabbit', 'Chilled storage (4°C, 72h)',
         '2% DPP in Tris-glucose',
         'Higher progressive motility at 48-72h; improved HOST-positive rate; preserved acrosome',
         'El-Seadawy et al., 2023'],
        ['Rabbit', 'Cryopreservation trial',
         'NaCl pollen extender (NPE) at varying doses',
         'Dose-dependent protection of motility and membrane integrity; field-applicable protocol',
         'Laghouati et al., 2021, 2023'],
        ['Ram (this study)', 'Post-slaughter epididymal, chilled 4°C',
         'Aqueous DPPE 0/40/80 mg/mL',
         '[First study of its kind — see Chapter 4 for results]',
         'Present thesis'],
    ]
    story.extend(build_table(
        table_2_4_data,
        col_widths=[1.6*cm, 3.0*cm, 3.2*cm, 5.5*cm, 2.7*cm],
        caption="Cross-species evidence for Date Palm Pollen supplementation in "
                "reproduction, with the present thesis addressing the ovine gap.",
        caption_num="Table 2.4",
        styles=styles, font_size=8.5
    ))

    story.append(Paragraph(
        "Three observations emerge from this cross-species literature. First, DPP "
        "consistently demonstrates beneficial effects across diverse species and "
        "preservation contexts (chilled storage, cryopreservation, in vitro fertilization), "
        "suggesting a robust underlying mechanism. Second, the effective concentration "
        "varies substantially across studies (from 1 mg/mL aqueous extract to 5% whole "
        "DPP suspension), reflecting differences in DPP composition, extraction method, "
        "and species-specific dose-response. Third, the field-applicability emphasis "
        "introduced by Laghouati et al. (2021, 2023) — using simple aqueous NaCl-based "
        "extraction rather than organic solvents — directly informs the methodological "
        "choice in this thesis.",
        styles['Body']
    ))

    # 2.7 Climate Change Impacts
    story.append(add_heading("2.7 Climate Change and Livestock Genetic Erosion in Arid Algeria", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "Climate change poses escalating threats to livestock production in arid and "
        "semi-arid regions, with implications that extend beyond direct productivity "
        "losses to encompass genetic erosion of locally adapted breeds (Ben Moula et al., "
        "2024; Van Wettere et al., 2021). Small ruminants, including sheep, represent "
        "critical assets for food security and livelihood sustainability in extreme "
        "environments, yet they are particularly vulnerable to both direct thermal "
        "stress and indirect consequences through deteriorating feed and water resources "
        "(Joy et al., 2020; Wodajo et al., 2020). In Algeria's arid pastoral zones, "
        "where sheep production constitutes a cornerstone of agricultural activity, "
        "recent evaluations reveal significant sustainability challenges amid high "
        "climatic fluctuation and increasing environmental pressures (Rjili et al., "
        "2023; Siad et al., 2022).",
        styles['Body']
    ))

    story.append(Paragraph(
        "The pathways through which climate change threatens ovine genetic resources "
        "are multiple and interacting. <b>Direct heat stress</b> affects spermatogenesis, "
        "with elevated testicular temperatures impairing germ cell development and "
        "increasing sperm DNA fragmentation. <b>Nutritional stress</b>, driven by "
        "declining pasture productivity and forage scarcity during prolonged droughts, "
        "compromises body condition and reproductive competence. <b>Water scarcity</b> "
        "elevates dehydration risk, particularly in transhumant systems. <b>Disease "
        "emergence</b>, facilitated by climate-driven shifts in vector distributions, "
        "introduces novel pathogens to which local breeds lack immunity. The cumulative "
        "effect of these stressors is elevated mortality in genetically valuable "
        "breeding stock, accelerated demographic attrition of small populations, and "
        "reduced effective population sizes — all of which elevate the urgency for "
        "accessible genetic conservation tools.",
        styles['Body']
    ))

    table_2_5_data = [
        ['Climate Stressor', 'Mechanism of Impact', 'Fertility Consequence', 'Genetic Implication'],
        ['Heat stress', 'Elevated testicular temperature; impaired spermatogenesis',
         'Reduced semen quality; lower conception rates',
         'Loss of heat-sensitive alleles; selection against productive genotypes'],
        ['Drought / forage scarcity', 'Nutritional deficiency; body condition loss',
         'Delayed puberty; extended lambing intervals; anestrus',
         'Demographic attrition; reduced effective population size'],
        ['Water scarcity', 'Dehydration; electrolyte imbalance',
         'Reduced semen volume and sperm concentration',
         'Elevated mortality in genetically valuable breeding males'],
        ['Disease emergence', 'Vector-borne pathogen exposure; immune suppression',
         'Abortion; perinatal mortality; infertility',
         'Loss of disease-susceptible genotypes; population bottlenecks'],
        ['Pasture degradation', 'Reduced dietary diversity; mineral deficiency',
         'Poor fetal programming; impaired reproductive development',
         'Long-term reduction in adaptive genetic variation'],
    ]
    story.extend(build_table(
        table_2_5_data,
        col_widths=[2.8*cm, 4.3*cm, 3.8*cm, 5.0*cm],
        caption="Summary of climate change impact pathways on small ruminant fertility "
                "and genetic diversity, with implications for conservation priority-setting.",
        caption_num="Table 2.5",
        styles=styles, font_size=8.5
    ))

    # 2.8 Conceptual Framework
    story.append(add_heading("2.8 Conceptual Framework and Synthesis", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "The literature reviewed in this chapter converges on a triangulated conceptual "
        "framework that integrates the three dimensions examined in this thesis: "
        "socioeconomic context, technical preservation solution, and environmental "
        "pressure (Figure 2.3). The framework posits that sustainable genetic conservation "
        "in arid pastoral systems requires the simultaneous alignment of all three "
        "dimensions — technical solutions that are not field-deployable fail to address "
        "real-world needs; conservation priorities that ignore keeper preferences lack "
        "adoption; and interventions that ignore climate urgency misallocate limited "
        "resources.",
        styles['Body']
    ))

    story.extend(build_figure(
        'fig_2_3_conceptual_framework.png',
        "Conceptual framework integrating socioeconomic context, technical preservation "
        "solution, and environmental pressure into a unified triangulated conservation "
        "model for arid-zone ovine genetic resources.",
        "Figure 2.3", styles, width_cm=14
    ))

    story.append(add_heading("2.8.1 Research Gaps Revisited", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "The literature review confirms the three research gaps identified in Chapter 1. "
        "First, the empirical gap: despite extensive cross-species evidence for DPP "
        "supplementation in bulls, goats, buffalo, and rabbits, no studies have evaluated "
        "DPP in ovine sperm or in post-slaughter epididymal contexts. Second, the "
        "methodological gap: conventional single-mechanism antioxidants systematically "
        "fail to address the multi-source ROS generation characteristic of post-mortem "
        "deterioration. Third, the integration gap: technical efficacy, socioeconomic "
        "context, and environmental pressure have been studied in isolation but never "
        "integrated into a unified conservation framework. The present thesis addresses "
        "all three gaps through its multi-experimental design.",
        styles['Body']
    ))

    story.append(add_heading("2.8.2 Conceptual Model and Hypothesis Formulation", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "The conceptual model underlying this thesis posits that locally-sourced Date "
        "Palm Pollen, applied as an aqueous extender at optimal concentration, provides "
        "multi-target antioxidant protection that addresses the specific biological "
        "challenges of post-slaughter ovine epididymal sperm preservation. The model "
        "predicts dose-dependent protection, with higher DPP concentrations yielding "
        "superior preservation outcomes up to a plateau beyond which additional DPP "
        "provides diminishing returns. The model further predicts that this technical "
        "solution, grounded in socioeconomic priorities and climate urgency, can be "
        "translated into a field-deployable protocol with measurable conservation impact.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The four hypotheses (Ha1–Ha4) formulated in Chapter 1 operationalize this "
        "conceptual model into testable predictions. The next chapter describes the "
        "materials and methods by which these hypotheses are empirically evaluated "
        "across the four interconnected experiments.",
        styles['Body']
    ))

    story.append(PageBreak())


if __name__ == '__main__':
    print("This module provides Chapter 1 and Chapter 2 content builders.")
    print("Run: python3 /home/z/my-project/scripts/build_thesis_main.py")
