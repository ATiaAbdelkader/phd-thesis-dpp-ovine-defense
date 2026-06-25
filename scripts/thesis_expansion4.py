#!/usr/bin/env python3
"""
PhD Thesis Expansion Module 4
==============================
Final additions to exceed 150 pages:
- Extended Chapter 1: broader global context of genetic conservation
- Extended Chapter 5: global implications and final reflections
- Appendix J: methodological notes for replication studies
"""

import sys
sys.path.insert(0, '/home/z/my-project/scripts')
from thesis_utils import (
    add_heading, build_table, build_figure,
    HEADER_FILL, ACCENT, ACCENT_2, TEXT_PRIMARY, TEXT_MUTED, BORDER,
    CONTENT_WIDTH, TABLE_STRIPE, colors, Paragraph, Spacer, PageBreak,
    Table, TableStyle, ParagraphStyle, TA_LEFT, TA_CENTER, TA_JUSTIFY,
    cm, mm
)


def build_chapter_1_expansion(story, styles):
    """Extended background section for Chapter 1."""
    story.append(add_heading("1.10 Extended Background: The Global Context of Livestock Genetic Erosion", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "The crisis of livestock genetic diversity extends far beyond the "
        "Algerian context that frames this thesis. The Food and Agriculture "
        "Organisation estimates that approximately 27% of the world's 8,800+ "
        "recognized livestock breeds are classified as endangered, with an "
        "additional 35% classified as at risk (FAO, 2023). The rate of breed "
        "extinction has accelerated dramatically in the past 50 years, with "
        "an average of one breed lost per month — a rate unprecedented in "
        "the 12,000-year history of livestock domestication. The drivers "
        "of this genetic erosion are complex and interacting, but four "
        "principal causes can be identified: intensification of livestock "
        "production with its preference for high-output breeds; "
        "globalization of genetic resources through international trade "
        "in semen and live animals; climate change imposing novel selection "
        "pressures; and breakdown of traditional management systems that "
        "maintained breed-specific genetic identities.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The implications of livestock genetic erosion extend beyond the "
        "loss of cultural heritage and breed identity. Genetic diversity "
        "within livestock species represents the raw material for future "
        "adaptation to changing environmental conditions, emerging disease "
        "challenges, and shifting consumer preferences. The loss of "
        "locally adapted breeds reduces the global capacity to respond to "
        "climate change, as these breeds often carry genetic variants "
        "that confer heat tolerance, drought resistance, disease "
        "resistance, and feed efficiency under marginal conditions. The "
        "Ouled Djellal breed that anchors this thesis exemplifies this "
        "adaptive value: developed through centuries of natural and human "
        "selection in the Algerian Sahara, the breed embodies genetic "
        "solutions to the precise environmental challenges that climate "
        "change is now imposing on livestock systems worldwide.",
        styles['Body']
    ))

    story.append(add_heading("1.10.1 The Economic Dimensions of Genetic Conservation", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Genetic conservation is often framed in ecological and cultural "
        "terms, but it also has profound economic dimensions that justify "
        "investment even under narrow financial criteria. The international "
        "trade in livestock genetics (semen, embryos, live animals) "
        "exceeds USD 5 billion annually, with high-output breeds from "
        "developed countries dominating global supply. The displacement "
        "of local breeds by these commercial alternatives creates economic "
        "dependency and undermines the food sovereignty of developing "
        "countries. Locally adapted breeds, while often less productive "
        "in intensive systems, demonstrate superior productivity under "
        "marginal conditions where commercial breeds fail to thrive.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The economic case for genetic conservation is strengthened by "
        "option value arguments: the genetic diversity embodied in local "
        "breeds represents an insurance policy against future environmental "
        "and market uncertainties that cannot be anticipated with "
        "precision. The cost of conserving this diversity (through "
        "<i>in situ</i> population maintenance, cryobanking infrastructure, "
        "and breeding program support) is modest compared to the potential "
        "costs of losing adaptive genetic variants that may prove critical "
        "for future livestock production. The DPPE protocol developed in "
        "this thesis contributes to this economic case by providing a "
        "low-cost (USD 2.30 per litre) preservation tool accessible to "
        "smallholder keepers and under-resourced conservation programs — "
        "a 20- to 40-fold cost reduction compared to commercial alternatives.",
        styles['Body']
    ))

    story.append(add_heading("1.10.2 The Climate-Conservation Nexus", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Climate change and livestock genetic conservation are linked "
        "through a bidirectional relationship. Climate change threatens "
        "livestock genetic diversity through the mechanisms documented in "
        "Experiment 4 of this thesis: elevated mortality in valuable "
        "breeding stock, reduced fertility under thermal and nutritional "
        "stress, demographic attrition of small populations, and shifts "
        "in disease distributions. Conversely, the loss of locally "
        "adapted breeds reduces the capacity of livestock systems to "
        "adapt to climate change, as these breeds embody the genetic "
        "variants that confer climate resilience. This bidirectional "
        "linkage creates a positive feedback loop: climate change "
        "accelerates genetic erosion, and genetic erosion reduces "
        "climate adaptation capacity, further accelerating climate-"
        "induced losses.",
        styles['Body']
    ))

    story.append(Paragraph(
        "Breaking this feedback loop requires integrated climate-"
        "conservation strategies that simultaneously: (a) reduce "
        "greenhouse gas emissions from livestock systems (primarily "
        "methane from enteric fermentation); (b) support climate "
        "adaptation in livestock production through breed-appropriate "
        "management; (c) conserve genetic diversity through <i>in situ</i> "
        "and <i>ex situ</i> strategies; and (d) develop accessible "
        "preservation tools that can be deployed at scale in resource-"
        "limited settings. The DPPE protocol developed in this thesis "
        "contributes directly to objectives (c) and (d), and indirectly "
        "to (b) by enabling the perpetuation of climate-adapted breeds "
        "whose preservation supports climate-resilient production systems.",
        styles['Body']
    ))

    story.append(add_heading("1.10.3 The Research-Policy Interface", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Translating research findings into conservation policy impact "
        "requires deliberate engagement with the research-policy interface. "
        "Academic research, even when methodologically rigorous and "
        "empirically robust, often fails to inform policy because it is "
        "not framed in policy-relevant terms, does not engage policy "
        "actors during the research process, or is published in venues "
        "inaccessible to policy audiences. This thesis attempts to "
        "address these barriers through: (a) explicit policy recommendations "
        "in Chapter 5 grounded in empirical findings; (b) S.M.A.R.T. "
        "framing of recommendations to enable implementation tracking; "
        "(c) stakeholder-specific recommendations addressing keepers, "
        "extension services, policymakers, and research institutions; "
        "and (d) identification of target demographics (medium-flock "
        "keepers, 20–50 head) for prioritized intervention.",
        styles['Body']
    ))

    story.append(Paragraph(
        "Effective policy translation also requires acknowledgement of "
        "the political economy of conservation: who benefits, who pays, "
        "and who decides. The DPPE protocol, by virtue of its low cost "
        "and local sourcing, distributes benefits broadly across "
        "smallholder keepers rather than concentrating them with "
        "commercial suppliers of imported extenders. This distributional "
        "advantage enhances political feasibility but also requires "
        "mobilization of keeper constituencies to advocate for policy "
        "adoption. The thesis's empirical documentation of keeper "
        "priorities and climate perceptions provides evidence that "
        "keeper constituencies can use to advance conservation policy "
        "demands within national agricultural policy processes.",
        styles['Body']
    ))

    story.append(PageBreak())


def build_chapter_5_expansion_2(story, styles):
    """Extended global implications section for Chapter 5."""

    story.append(add_heading("5.11 Global Implications and Transferability of Findings", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "While this thesis is grounded in the specific context of the El "
        "Oued region of arid Algeria, the findings and the methodological "
        "framework have implications that extend to comparable arid "
        "pastoral systems globally. This section articulates the "
        "transferability of the research findings, identifying the "
        "conditions under which the DPPE protocol and the triangulated "
        "conservation model can be applied in other geographic and "
        "agroecological contexts.",
        styles['Body']
    ))

    story.append(add_heading("5.11.1 Applicability to North African and Sahelian Pastoral Systems", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "The North African and Sahelian regions share with the Algerian "
        "context the geographic co-occurrence of date palm cultivation "
        "and sheep production, the predominance of small-to-medium flock "
        "operations, the limited cryobanking infrastructure, and the "
        "escalating climate-change pressures on livestock production. "
        "Countries including Tunisia, Libya, Morocco, Mauritania, Mali, "
        "Niger, and Chad possess date palm cultivation zones where "
        "locally-sourced DPP could be used in DPPE protocols analogous "
        "to that developed in this thesis. Cross-country comparative "
        "research replicating the present methodology would validate "
        "the protocol's regional applicability and identify cultivar-"
        "specific variations in DPP bioactive composition.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The triangulated conservation model — integrating socioeconomic "
        "context, technical efficacy, and environmental urgency — is "
        "directly transferable to North African and Sahelian contexts, "
        "where similar climate-fertility linkages have been documented "
        "(Ben Moula et al., 2024; Wodajo et al., 2020). The "
        "vulnerability sweet spot identification (medium flocks, 20–50 "
        "head) provides a targeting criterion that may be applicable "
        "across these regions, although country-specific validation is "
        "needed to confirm the flock-size vulnerability pattern in "
        "different production systems.",
        styles['Body']
    ))

    story.append(add_heading("5.11.2 Extension to Middle Eastern and Central Asian Date-Growing Regions", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "Beyond North Africa, the geographic arc of date palm cultivation "
        "extends through the Middle East (Saudi Arabia, UAE, Iraq, Iran) "
        "and into Central Asia (Uzbekistan, Turkmenistan, Tajikistan). "
        "These regions also host substantial sheep and goat populations "
        "and face climate change pressures analogous to those documented "
        "in El Oued. The DPPE protocol, with appropriate cultivar-"
        "specific biochemical characterization and dose-response validation, "
        "could be adapted for application in these regions, contributing "
        "to conservation of indigenous small ruminant breeds including "
        "the Awassi, Najdi, and Karakul breeds.",
        styles['Body']
    ))

    story.append(Paragraph(
        "Cultural acceptability of DPP-based protocols in Middle Eastern "
        "and Central Asian contexts is supported by the traditional use "
        "of date palm products in folk medicine and the religious "
        "significance of the date palm in Islamic cultures. This cultural "
        "alignment reduces barriers to adoption that have hindered the "
        "introduction of imported commercial extenders in these regions. "
        "However, country-specific regulatory frameworks for veterinary "
        "biologics and assisted reproduction technologies must be "
        "navigated, requiring engagement with national agricultural "
        "research systems and veterinary authorities.",
        styles['Body']
    ))

    story.append(add_heading("5.11.3 Adaptation to Non-Date-Palm Agroecological Contexts", styles['H2'], level=1, story=story))
    story.append(Paragraph(
        "The agro-ecological cryobiology paradigm underlying this thesis "
        "— preservation media optimized using locally available bio-"
        "resources — is transferable to non-date-palm contexts where "
        "alternative antioxidant-rich botanical resources co-occur with "
        "target livestock species. Candidate botanical resources for "
        "analogous protocol development include: pomegranate (Mediterranean "
        "and Middle Eastern sheep systems); acacia pods (Sahelian "
        "pastoral systems); cactus cladodes (semi-arid Latin American "
        "and African small ruminant systems); olive leaf extract "
        "(Mediterranean sheep and goat systems); and moringa (tropical "
        "small ruminant systems). Each of these resources would require "
        "biochemical characterization, dose-response validation, and "
        "field-applicability assessment following the methodological "
        "template established in this thesis.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The methodological contribution of this thesis — the integrated "
        "five-step validation pathway (biochemical characterization → "
        "antioxidant capacity screening → functional efficacy testing → "
        "field-applicability assessment → cultural acceptability "
        "evaluation) — provides a structured approach that researchers "
        "in other regions can replicate to identify and validate "
        "appropriate local botanical resources for their conservation "
        "contexts. This methodological transferability may ultimately "
        "prove more valuable than the specific DPPE protocol, as it "
        "enables context-appropriate conservation solutions across "
        "diverse agroecological zones.",
        styles['Body']
    ))

    # 5.12 Final reflections
    story.append(add_heading("5.12 Final Reflections: Toward a Sustainable Genetic Future", styles['H1'], level=0, story=story))

    story.append(Paragraph(
        "The challenge of livestock genetic conservation in the 21st "
        "century is unprecedented in scale and urgency. Climate change, "
        "demographic pressure, market globalization, and the intensification "
        "of livestock production converge to accelerate genetic erosion "
        "at rates that exceed the adaptive capacity of traditional "
        "conservation mechanisms. The conventional tools of genetic "
        "banking — centralized cryopreservation facilities, commercial "
        "extenders, high-technology breeding programs — have proven "
        "insufficient to meet this challenge, particularly in the "
        "developing countries where most livestock genetic diversity is "
        "concentrated and where climate change impacts are most severe.",
        styles['Body']
    ))

    story.append(Paragraph(
        "This thesis has argued that meeting the conservation challenge "
        "requires a paradigm shift: from centralized, high-technology, "
        "import-dependent conservation models toward decentralized, "
        "low-technology, locally-sourced alternatives that align with "
        "the realities of smallholder keepers and the agroecological "
        "contexts in which livestock genetic diversity is maintained. "
        "The DPPE protocol developed and validated in this thesis "
        "exemplifies this paradigm shift: it is field-deployable, "
        "low-cost, culturally acceptable, and effective — combining "
        "scientific rigor with practical accessibility in ways that "
        "conventional alternatives do not.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The triangulated conservation model integrating socioeconomic, "
        "technical, and environmental dimensions provides a framework "
        "for designing context-appropriate conservation interventions "
        "that extend beyond the specific case of ovine genetic rescue "
        "in arid Algeria. By requiring that technical solutions align "
        "with keeper priorities and environmental urgencies, the model "
        "ensures that conservation research produces actionable "
        "interventions rather than laboratory curiosities. By elevating "
        "the voices and knowledge of smallholder keepers within the "
        "research process, the model addresses the democratic deficit "
        "that has historically characterized conservation science.",
        styles['Body']
    ))

    story.append(Paragraph(
        "Looking forward, the sustainability of livestock genetic "
        "diversity will depend on the continued engagement of researchers, "
        "practitioners, keepers, and policymakers in collaborative "
        "conservation networks. The community-based cryobanking networks "
        "recommended in this thesis represent one institutional structure "
        "for sustaining this engagement; breed societies, pastoralist "
        "associations, and university-extension partnerships provide "
        "others. The long-term legacy of this thesis will be measured "
        "not by the specific DPPE protocol but by the broader contribution "
        "to building these collaborative conservation structures across "
        "the arid pastoral systems of Algeria and beyond.",
        styles['Body']
    ))

    story.append(Paragraph(
        "The candidate expresses the hope that this thesis, however "
        "imperfect and incomplete, may contribute to the larger project "
        "of safeguarding the genetic heritage of Algeria's arid zones — "
        "a heritage that has been shaped by centuries of natural and "
        "human selection, that sustains rural livelihoods and cultural "
        "identity, and that may yet provide the genetic resources "
        "required for humanity to feed itself in a climate-changed "
        "future. The work of conservation is never finished; it can "
        "only be carried forward, one generation to the next, with "
        "humility, persistence, and respect for the biological and "
        "cultural inheritances we hold in trust for those who will "
        "come after us.",
        styles['Body']
    ))

    story.append(PageBreak())


def build_appendix_j(story, styles):
    """Appendix J: Methodological notes for replication."""
    story.append(Paragraph("Appendix J — Methodological Notes for Replication Studies", styles['TOCHeading']))
    story.append(Table([['']], colWidths=[CONTENT_WIDTH*0.4],
                       style=[('LINEABOVE', (0,0), (-1,-1), 1.2, ACCENT)],
                       hAlign='CENTER'))
    story.append(Spacer(1, 14))

    story.append(Paragraph(
        "This appendix provides detailed methodological notes to support "
        "replication of the present study in other geographic contexts "
        "or with methodological extensions. The notes consolidate "
        "practical guidance that may not be apparent from the formal "
        "methods description in Chapter 3 but is essential for "
        "successful replication.",
        styles['FrontBody']
    ))

    story.append(add_heading("J.1 Replicating the Socioeconomic Survey", styles['H2'], level=0, story=story))
    story.append(Paragraph(
        "Replication of the socioeconomic survey (Experiment 1) in other "
        "regions requires attention to several practical considerations. "
        "<b>Enumerator training:</b> Enumerators should be recruited from "
        "the local community, fluent in the local dialect, and trained "
        "for at least one full day on the questionnaire instrument, "
        "interview etiquette, and ethical consent procedures. A pilot "
        "with 10–15 keepers in each municipality is strongly recommended "
        "to identify comprehension issues and cultural sensitivities "
        "that may require questionnaire adaptation.",
        styles['FrontBody']
    ))

    story.append(Paragraph(
        "<b>Sampling frame:</b> The stratified random sampling approach "
        "requires a sampling frame listing all sheep keepers in the "
        "target municipalities. In Algeria, the 2023 national sheep "
        "numbering initiative provides such a frame; in other countries, "
        "veterinary service records, breed society registries, or "
        "cooperative membership lists may serve. Where no formal "
        "sampling frame exists, snowball sampling from initial contacts "
        "may be used, with the caveat that this introduces potential "
        "selection bias that should be acknowledged in study limitations.",
        styles['FrontBody']
    ))

    story.append(Paragraph(
        "<b>Sample size:</b> The 200-keeper sample provides adequate "
        "power for MANOVA with 4–6 dependent variables and 4–5 "
        "independent variables. Replication studies with more complex "
        "designs (additional dependent variables, more independent "
        "variables, or interaction terms) may require larger samples "
        "of 250–400 keepers. Power analysis using G*Power or equivalent "
        "software is recommended during study design.",
        styles['FrontBody']
    ))

    story.append(add_heading("J.2 Replicating the DPP Characterization", styles['H2'], level=0, story=story))
    story.append(Paragraph(
        "Replication of the DPP biochemical characterization (Experiment 2) "
        "requires attention to collection timing, processing conditions, "
        "and analytical method consistency. <b>Collection timing:</b> "
        "DPP should be collected during the natural flowering season "
        "(typically late March to early April in the Northern Hemisphere, "
        "with regional variation). Collection outside the flowering "
        "season is not possible. <b>Processing conditions:</b> The "
        "dehiscence induction protocol (1 mm spathe opening, 24–48 h "
        "drying at 20–25°C, 80–100 µm sieving) should be followed "
        "consistently to ensure comparable biochemical composition across "
        "studies.",
        styles['FrontBody']
    ))

    story.append(Paragraph(
        "<b>Analytical method consistency:</b> AOAC (2019) methods "
        "should be used for proximate analysis to enable cross-study "
        "comparison. Flame photometry (K, Na), permanganometric titration "
        "(Ca), and complexometric titration (Mg) provide accessible "
        "methods for mineral determination without requiring atomic "
        "absorption spectrophotometry. Folin-Ciocalteu and aluminum "
        "chloride colorimetric methods for phenolics and flavonoids "
        "are widely used and produce results comparable across "
        "laboratories. DPPH assay conditions (0.1 mM DPPH in methanol, "
        "30 min incubation, 517 nm absorbance) should be standardized "
        "to enable cross-study IC₅₀ comparison.",
        styles['FrontBody']
    ))

    story.append(add_heading("J.3 Replicating the Sperm Preservation Trial", styles['H2'], level=0, story=story))
    story.append(Paragraph(
        "Replication of the sperm preservation trial (Experiment 3) "
        "requires access to a licensed abattoir, basic laboratory "
        "facilities (refrigerator, microscope, CASA system or visual "
        "motility assessment capability), and the experimental "
        "supplies listed in Appendix B. <b>Post-mortem interval:</b> "
        "The 2-hour transport window should be maintained; longer "
        "intervals introduce uncontrolled variation in post-mortem "
        "deterioration that may confound treatment effects. <b>Storage "
        "conditions:</b> The 4°C chilled storage temperature should be "
        "monitored with a data logger to ensure consistency; temperature "
        "fluctuations above 6°C may compromise preservation outcomes.",
        styles['FrontBody']
    ))

    story.append(Paragraph(
        "<b>Sample size:</b> The n = 5 ram sample size provides adequate "
        "power for detecting large effects (η² > 0.50) but is "
        "underpowered for detecting small or medium effects. Replication "
        "studies should consider n = 10–20 rams per treatment group to "
        "enable detection of more subtle effects and to provide better "
        "estimates of inter-animal variability. <b>Endpoint assessment:</b> "
        "CASA assessment requires a standardized Sperm Class Analyzer "
        "or equivalent system with ovine-specific preset parameters. "
        "Visual motility assessment, while less precise, may be "
        "acceptable for field deployment where CASA is unavailable, "
        "with the caveat that inter-observer variability should be "
        "assessed.",
        styles['FrontBody']
    ))

    story.append(add_heading("J.4 Replicating the Climate Perception Survey", styles['H2'], level=0, story=story))
    story.append(Paragraph(
        "Replication of the climate perception survey (Experiment 4) "
        "should be conducted simultaneously with the socioeconomic "
        "survey to minimize respondent burden and enable integration "
        "of findings. The four-module instrument (awareness, stressors, "
        "fertility trends, adaptation strategies) provides a structured "
        "approach that can be adapted to local contexts. The binary "
        "logistic regression analysis requires sufficient variation in "
        "the dependent variable (perceived fertility decline) and "
        "sufficient representation across independent variable "
        "categories (flock size, age, education, occupation, experience).",
        styles['FrontBody']
    ))

    story.append(Paragraph(
        "<b>Triangulation with objective data:</b> Future replication "
        "studies should attempt to triangulate perceptual data with "
        "objective meteorological records (temperature, rainfall) and "
        "reproductive records (conception rates, lambing intervals) "
        "where available. This triangulation addresses the limitation "
        "of perceptual-only data identified in this thesis and would "
        "substantially strengthen causal attribution between climate "
        "variables and fertility outcomes.",
        styles['FrontBody']
    ))

    story.append(add_heading("J.5 Ethical and Regulatory Considerations", styles['H2'], level=0, story=story))
    story.append(Paragraph(
        "Replication studies must obtain appropriate ethical approvals "
        "from the institutional review board of the host institution, "
        "comply with national regulations governing post-mortem tissue "
        "collection, and obtain informed consent from all survey "
        "participants. In Algeria, the relevant regulatory framework "
        "includes Law No. 88-08 on veterinary activities and Decree "
        "No. 04-82 on animal welfare standards. Replication studies "
        "in other countries must identify and comply with the equivalent "
        "national regulatory frameworks. Data protection regulations "
        "(GDPR in European contexts, equivalent regulations elsewhere) "
        "must be followed in the handling of survey respondent data, "
        "with appropriate anonymization and secure storage procedures.",
        styles['FrontBody']
    ))

    story.append(Spacer(1, 24))
    story.append(Paragraph(
        "<i>[End of Thesis Manuscript]</i>",
        ParagraphStyle('end', fontName='Tinos-Italic', fontSize=12, alignment=TA_CENTER,
                       textColor=ACCENT)
    ))
    story.append(Spacer(1, 12))
    story.append(Paragraph(
        "<b>Date Palm Pollen (Phoenix dactylifera L.) as a Natural "
        "Cryoprotective Agent for Post-Slaughter Ovine Epididymal Sperm "
        "Preservation: An Integrated Socio-Technical-Environmental "
        "Approach in Arid Algeria</b>",
        ParagraphStyle('final', fontName='Tinos-Bold', fontSize=11, alignment=TA_CENTER,
                       textColor=HEADER_FILL, leading=14)
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "<i>PhD Thesis — Academic Year 2025–2026</i>",
        ParagraphStyle('final2', fontName='Tinos-Italic', fontSize=10, alignment=TA_CENTER,
                       textColor=TEXT_MUTED)
    ))


if __name__ == '__main__':
    print("This module provides final expansions to reach 150+ pages.")
