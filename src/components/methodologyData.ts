import { MethodStep } from "@/components/MethodologyTimeline";

// ═══════════════════════════════════════════════════════════════
// EXPERIMENT 1 — Socioeconomic Survey Methodology
// ═══════════════════════════════════════════════════════════════
export const EXP1_METHODS: MethodStep[] = [
  {
    num: 1, title: "Study Area Selection", icon: "users", duration: "El Oued, Algeria",
    detail: "El Oued region (33°22'N, 6°50'E) — a key centre of date palm agriculture and sheep production in the Algerian Sahara. The region's arid environment, extensive pastoral systems, and geographic combination of date palm cultivation and sheep production make it a model for studying post-slaughter genetic rescue and field-applicable preservation measures.",
  },
  {
    num: 2, title: "Stratified Random Sampling", icon: "users", duration: "200 keepers",
    detail: "200 sheep keepers selected at random from 8 municipalities: El Oued (capital), Debila, Guemar, Hassi Khelifa, Mih Ouensa, Ourmes, Robbah, and Taleb Larbi. Selection criteria: (a) participation in 2023 national sheep numbering initiative, (b) grazing-based agricultural practices, (c) willingness to participate. Flock size categories: <20 (smallholder), 20-50 (medium), 50-100 (large), >100 (commercial).",
  },
  {
    num: 3, title: "Questionnaire Development", icon: "users", duration: "10 sections, 86 questions",
    detail: "Semi-structured questionnaire with open-ended and closed questions covering: (a) socioeconomic characteristics, (b) flock size/structure/management, (c) trait preferences for rams and ewes, (d) health and veterinary care, (e) environmental factors, (f) nutrition, (g) breed comparison, (h) male/female selection criteria, (i) reproductive technologies, (j) housing. Pre-tested with 10 keepers per municipality for comprehension and cultural sensitivity.",
  },
  {
    num: 4, title: "Face-to-Face Interviews", icon: "users", duration: "Arabic language",
    detail: "Administered in face-to-face interviews conducted in Arabic by trained enumerators. Responses recorded in both Arabic and French for cross-verification. Each interview took approximately 45-60 minutes. Informed verbal consent obtained from all participants, documented by enumerator in the presence of a community witness.",
  },
  {
    num: 5, title: "MANOVA Statistical Analysis", icon: "users", duration: "SPSS v27",
    detail: "Multivariate Analysis of Variance (MANOVA) used to determine effects of age, education, experience, and occupation on trait preferences. Pillai's Trace chosen as the major multivariate test statistic — robust to violations of assumptions (unequal sample sizes, heterogeneity of covariance matrices). Partial eta squared (η²) measures proportion of variance explained. Significance at α = 0.05. IBM SPSS Statistics v27.0.",
  },
];

// ═══════════════════════════════════════════════════════════════
// EXPERIMENT 2 — DPP Phytochemical Characterization Methodology
// ═══════════════════════════════════════════════════════════════
export const EXP2_METHODS: MethodStep[] = [
  {
    num: 1, title: "DPP Collection from Hamraia", icon: "beaker", duration: "March-April 2024",
    detail: "Date Palm Pollen collected at Hamraia commune, Reguiba District, El Oued Province (34°6'39\"N, 6°13'50\"E) during natural flowering season (late March to early April 2024). Healthy mature male date palm trees selected. Spathes separated before dehiscence to prevent contamination and ensure pollen maturity.",
  },
  {
    num: 2, title: "Dehiscence & Processing", icon: "beaker", duration: "24-48h drying",
    detail: "Mature spathes removed early morning to reduce temperature stress. Dehiscence induced: each spathe opened ~1mm, cut base immersed in water for hydration. Flowers manually removed after 24-48h drying at ambient temperature (20-25°C) with regular rotation (2-3× daily). Pollen sieved through 80-100μm mesh. Stored in airtight containers at 4°C, away from light, until analysis.",
  },
  {
    num: 3, title: "Proximate Composition Analysis", icon: "beaker", duration: "AOAC 2019 methods",
    detail: "Moisture: gravimetric (oven-drying at 105°C). Ash: dry ashing (muffle furnace 550°C, 6h). Fat: Soxhlet extraction (petroleum ether, 1h). Protein: Kjeldahl method (catalyst digestion at 420°C, distillation, titration with 0.1N HCl, 6.25 conversion factor). Carbohydrate: phenol-sulfuric acid colorimetric (DuBois et al., 1956; absorbance at 490nm). All analyses in triplicate, reported as mean ± SD.",
  },
  {
    num: 4, title: "Mineral Content Determination", icon: "beaker", duration: "4 methods",
    detail: "Calcium: permanganometric titration (NA 1655 / ISO 6058:1994) — dry ashing at 550°C, Ca oxalate precipitation, KMnO₄ titration. Magnesium: complexometric EDTA titration (NA 752 / ISO 6059:1989) — total hardness at pH 10 (Eriochrome Black T), Ca at pH 12 (murexide), Mg by difference. Potassium & Sodium: flame photometry (NA 1653) — HNO₃/HClO₄ wet digestion, emission at 766.5nm (K) and 589nm (Na).",
  },
  {
    num: 5, title: "Phenolic & Flavonoid Quantification", icon: "beaker", duration: "Folin-Ciocalteu + AlCl₃",
    detail: "Extract: 5g DPP macerated in 50mL 50% ethanol, 24h, filtered, dried at ≤45°C. Total phenolics: Folin-Ciocalteu method (Slinkard & Singleton, 1977) — 0.2mL extract + 1mL 10% Folin-Ciocalteu + 0.8mL saturated Na₂CO₃, 2h incubation, absorbance at 765nm. Gallic acid standard curve (0-200 μg/mL). Results: mg GAE/g. Total flavonoids: AlCl₃ colorimetric (Ahn et al., 2007) — 1mL extract + 1mL 2% AlCl₃, 30min, absorbance at 430nm. Quercetin standard (0-100 μg/mL). Results: mg QE/g.",
  },
  {
    num: 6, title: "DPPH Antioxidant Assay", icon: "beaker", duration: "IC₅₀ determination",
    detail: "DPPH radical scavenging assay (Mansouri et al., 2005). 1mL DPPH solution (0.1mM in methanol) + 1mL extract or ascorbic acid (positive control). Vortexed, incubated in dark at room temperature 30min. Absorbance at 517nm. Inhibition (%) = [(A_control − A_sample) / A_control] × 100. IC₅₀ determined by plotting % inhibition vs. concentration. Ascorbic acid as reference antioxidant.",
  },
];

// ═══════════════════════════════════════════════════════════════
// EXPERIMENT 3 — Sperm Preservation Trial Methodology
// ═══════════════════════════════════════════════════════════════
export const EXP3_METHODS: MethodStep[] = [
  {
    num: 1, title: "Post-Mortem Testes Collection", icon: "microscope", duration: "≤2h transport",
    detail: "Testes from 5 sexually mature Ouled Djellal rams (18-24 months) collected at licensed abattoir in El Oued. No live animals used — all material post-mortem. Testes removed immediately after slaughter, transported to laboratory within 2 hours in isotonic saline (0.9% NaCl) on ice at 4°C. This simulates field conditions where rapid cooling is critical for maintaining post-mortem sperm viability.",
  },
  {
    num: 2, title: "Cauda Epididymidis Dissection", icon: "microscope", duration: "Sterile technique",
    detail: "Upon arrival, cauda epididymides dissected and sterilely cleaned of connective tissue, blood vessels, and fat. The cauda was carefully targeted as the principal sperm storage area harboring mature, fertilizable spermatozoa (Wu et al., 2021). The cauda microenvironment preserves sperm viability for 24-48h post-mortem when testes are stored at 4-5°C.",
  },
  {
    num: 3, title: "Retrograde Flushing Recovery", icon: "microscope", duration: "Martinez-Pastor 2006",
    detail: "Spermatozoa recovered using retrograde flushing technique (Martinez-Pastor et al., 2006). Single incision at corpus-cauda junction. 1mL syringe with warm (37°C) saline (0.9% NaCl, 308 mOsm/kg, pH 7.2) introduced into vas deferens. Gentle consistent pressure applied to flush spermatozoa retrograde through cauda. Emerging fluid collected in sterile 15mL conical tubes. Method chosen for: (a) good recovery efficiency, (b) low contamination, (c) field applicability.",
  },
  {
    num: 4, title: "DPPE Extender Preparation", icon: "microscope", duration: "24h cold extraction",
    detail: "Three treatments prepared using Laghouati et al. (2021) NaCl Pollen Extender (NPE) method: DPPE-0 (Control): 1mL saline only. DPPE-40: 40mg DPP soaked in 1mL saline. DPPE-80: 80mg DPP soaked in 1mL saline. DPP suspended by vortexing, refrigerated at 4°C for 24h for bioactive component extraction. Centrifuged to remove debris. Clear supernatant collected as extender. No organic solvents — field-applicable protocol.",
  },
  {
    num: 5, title: "Dilution & Chilled Storage", icon: "microscope", duration: "4°C, 48h, mineral oil",
    detail: "Each ram's recovered sperm divided into 3 equal aliquots, diluted 1:1 (v/v) in one of three extenders (DPPE-0, DPPE-40, DPPE-80). Final concentration adjusted to 350 × 10⁶ cells/mL (Maxwell & Watson, 1996). 0.5mL aliquots placed in sterile tubes, coated with mineral oil (prevents evaporation and gas exchange), refrigerated at 4°C for 48 hours. Quality assessed at 0, 24, and 48 hours to capture immediate effects, mid-storage stability, and long-term preservation capacity.",
  },
  {
    num: 6, title: "CASA Motility Assessment", icon: "microscope", duration: "Sperm Class Analyzer",
    detail: "Samples gently mixed, equilibrated at 37°C for 5 minutes. 3μL loaded into 20-μm Leja® chamber. Analyzed using Sperm Class Analyzer® (SCA, Microptic, Barcelona) at 60 fps, 10× phase contrast objective, ovine-specific preset parameters. ≥5 fields per sample. Total motility (VAP > 5 μm/s) and progressive motility (VAP > 25 μm/s AND STR > 50%). Intra-assay CV < 5%.",
  },
  {
    num: 7, title: "HOST Membrane Integrity", icon: "microscope", duration: "200 cells/sample",
    detail: "Plasma membrane integrity evaluated by Hypo-Osmotic Swelling Test (HOST) (Jeyendran et al., 1984). 50μL sperm + 1mL HOST solution (150 mOsm/L sodium citrate + 20mM fructose). Incubated 37°C, 30min. Fixed with 10% formalin. ≥200 cells scored under phase contrast (400×) for tail swelling (intact membrane = functional) vs. non-swollen (damaged). HOST-positive proportion = membrane integrity indicator.",
  },
  {
    num: 8, title: "Two-Way RM-ANOVA", icon: "microscope", duration: "SPSS v27, α=0.05",
    detail: "Data presented as mean ± SEM. Effects of extender concentration (0, 40, 80 mg/mL), storage period (0, 24, 48h), and their interaction investigated using two-way repeated-measures ANOVA, with 'ram' as subject factor. Mauchly's sphericity test applied, Greenhouse-Geisser correction when violated. Bonferroni post-hoc pairwise comparisons. Partial eta squared (η²) as effect size measure (η² > 0.14 = large effect). Significance at α = 0.05. IBM SPSS v27.0.",
  },
];

// ═══════════════════════════════════════════════════════════════
// EXPERIMENT 4 — Climate Perceptions Methodology
// ═══════════════════════════════════════════════════════════════
export const EXP4_METHODS: MethodStep[] = [
  {
    num: 1, title: "Same 200-Keeper Cohort", icon: "cloud", duration: "Dual-purpose design",
    detail: "Building on the same 200-keeper cohort surveyed in Experiment 1, a complementary questionnaire module captured perceptions of climate change impacts on sheep fertility, mortality, and management over the preceding five years. The dual-purpose design — combining socioeconomic profile (Exp 1) with climate perception (Exp 4) in a single field visit — maximized research efficiency while minimizing respondent burden.",
  },
  {
    num: 2, title: "Four-Module Instrument", icon: "cloud", duration: "Climate perception survey",
    detail: "The climate-perception instrument comprised four modules: (a) Awareness of climate-fertility relationships (yes/no + open-ended elaboration). (b) Primary climate stressors affecting sheep production (multi-select: heat stress, nutritional stress, water scarcity, disease emergence, other). (c) Perceived fertility trends over past 5 years (declined/stable/increased + qualitative description). (d) Adaptation strategies employed (multi-select: flock size reduction, breed change, supplementary feeding, transhumance modification, veterinary intervention, other).",
  },
  {
    num: 3, title: "Binary Logistic Regression", icon: "cloud", duration: "6 predictors, OR + 95% CI",
    detail: "Binary logistic regression used to identify predictors of perceived fertility decline. Dependent variable: 1 (decline reported) vs. 0 (no decline). Independent variables: flock size category (smallholder/medium/large/commercial), keeper age (continuous), education level (ordinal), experience (continuous), primary occupation (categorical), reported heat-stress events (binary). Odds ratios (OR) with 95% confidence intervals computed. Model fit assessed using Hosmer-Lemeshow test. Significance at α = 0.05.",
  },
  {
    num: 4, title: "Vulnerability Mapping", icon: "cloud", duration: "Sweet spot identification",
    detail: "The regression results enabled identification of the flock-size category with highest vulnerability to perceived fertility decline. The 'vulnerability sweet spot' concept emerged from the data: medium-sized flocks (20-50 head) showed the highest odds ratio (OR = 24.86), challenging the conventional assumption that the smallest flocks are most vulnerable. This finding has direct policy implications for targeting conservation interventions.",
  },
];
