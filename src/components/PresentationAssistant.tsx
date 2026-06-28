"use client";

import { useState, useEffect, useRef } from "react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  Clock, Play, Pause, RotateCcw, ChevronUp, ChevronDown, X, Mic,
  AlertCircle, CheckCircle2, Timer, Eye,
} from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

export const SCENE_TIMING: Record<string, { recommended: number; label: string }> = {
  hero: { recommended: 1, label: "Cover" },
  background: { recommended: 3, label: "Background" },
  design: { recommended: 2, label: "Research Design" },
  exp1: { recommended: 3, label: "Experiment 1" },
  exp2: { recommended: 3, label: "Experiment 2" },
  exp3: { recommended: 6, label: "Experiment 3 (Core)" },
  exp4: { recommended: 3, label: "Experiment 4" },
  "dose-response": { recommended: 2, label: "Dose Mixer" },
  "sperm-3d": { recommended: 2, label: "3D Sperm" },
  ghsi: { recommended: 2, label: "GHSI Calc" },
  "rescue-simulator": { recommended: 2, label: "Rescue Game" },
  "climate-simulator": { recommended: 2, label: "Climate Sim" },
  conclusion: { recommended: 2, label: "Conclusion" },
};

export const SPEECH_SCRIPTS: Record<string, string[]> = {
  hero: [
    "Good morning, distinguished members of the jury.",
    "My name is [Candidate Name], and I am honored to present my PhD thesis:",
    "Date Palm Pollen as a Natural Cryoprotective Agent for Post-Slaughter Ovine Epididymal Sperm Preservation.",
    "This research integrates four experiments across socioeconomic, biochemical, technical, and environmental dimensions.",
    "The central finding: DPPE at 80 mg/mL preserves sperm motility with a 9.2 percentage point advantage over control at 48 hours.",
    "Let me walk you through this journey — from field need to validated conservation framework.",
  ],
  background: [
    "Let me begin with the crisis.",
    "Sheep constitute one of humanity's most genetically diverse livestock species — over 1,300 breeds worldwide.",
    "Yet 27% are endangered. We lose one breed per month.",
    "In Algeria, the Ouled Djellal breed — our national treasure — faces mounting pressure from climate change, crossbreeding, and demographic attrition.",
    "Now consider this scenario: a genetically elite ram dies unexpectedly of pneumonia.",
    "With live collection impossible, what genetic material can be salvaged?",
    "Within 24 to 48 hours, the cauda epididymides may yield 5 to 15 billion spermatozoa.",
    "Without intervention, this genetic line is permanently lost.",
    "The challenge: post-mortem deterioration initiates a rapid biochemical cascade — ischemia, mitochondrial ROS generation, Fenton chemistry, lipid peroxidation.",
    "Ram sperm are especially vulnerable — their membranes contain 30 to 40 percent DHA, the highest among domestic livestock.",
    "This creates exceptional susceptibility to peroxidation.",
    "Conventional antioxidants fail because they operate through single mechanisms. The research imperative: a multi-target botanical solution.",
    "Date Palm Pollen — Phoenix dactylifera — emerges as uniquely positioned. It is locally available, culturally accepted, and biochemically complex.",
  ],
  design: [
    "This thesis employed a four-experiment triangulated design.",
    "Experiment 1: A socioeconomic survey of 200 sheep keepers across 8 municipalities of El Oued.",
    "Experiment 2: Phytochemical characterization of locally-sourced Date Palm Pollen.",
    "Experiment 3: The core sperm preservation trial — dose-response at 0, 40, and 80 mg/mL across 0, 24, and 48 hours.",
    "Experiment 4: Climate change perceptions and their linkage to fertility decline.",
    "The design follows a logical flow: Context, Characterization, Efficacy, and Urgency.",
    "All four alternative hypotheses were supported. This consistency validates both the conceptual framework and the implementation.",
    "Let me walk you through each experiment in detail.",
  ],
  exp1: [
    "Experiment 1 surveyed 200 sheep keepers across 8 municipalities of El Oued.",
    "The demographic profile reveals a male-dominated, aging profession.",
    "Only 11 percent of keepers are under 25 years old — a generational succession crisis.",
    "79.5 percent have fewer than 50 head — this is a smallholder livelihood system, not a commercial industry.",
    "The trait preferences are striking. Keepers prioritize breed identity at 27 percent for rams.",
    "For ewes, drought tolerance ranks third at 16 percent — above rapid growth.",
    "This reveals a strategic resilience orientation. Keepers know what they need: adaptation, not just productivity.",
    "The MANOVA revealed a significant three-way interaction between education, experience, and occupation.",
    "Pillai's Trace equals 0.070, p equals 0.009.",
    "Highly educated, experienced, full-time breeders prioritize long-term resilience traits.",
    "Less experienced keepers focus on visible morphological attributes.",
    "This tells us: conservation interventions should target full-time breeders as the most receptive audience.",
  ],
  exp2: [
    "Experiment 2 characterized the biochemical profile of El Oued Date Palm Pollen.",
    "The results are exceptional.",
    "Protein content: 37.94 percent — exceeding the upper bound of the reported range in literature.",
    "Potassium: 1,140 milligrams per 100 grams — reflecting Saharan soil geochemistry.",
    "The DPPH IC50 is 624.25 micrograms per milliliter.",
    "Now, this appears weaker than ascorbic acid, which has an IC50 of 145.",
    "But here is the key insight: the DPPH assay captures only aqueous-phase scavenging at one synthetic radical.",
    "DPP provides five complementary actions that DPPH cannot measure:",
    "One — membrane-integrating polyphenols like caffeic acid and quercetin.",
    "Two — mitochondrial-targeting flavonoids.",
    "Three — metal chelation preventing Fenton chemistry.",
    "Four — endogenous enzyme cofactor support: zinc for SOD, selenium for GPx.",
    "Five — vitamin E and C synergistic regeneration.",
    "Biological efficacy — which we validate in Experiment 3 — is the relevant metric, not chemical potency.",
  ],
  exp3: [
    "This is the core experiment of my thesis.",
    "Three treatment groups: DPPE-0 control, DPPE-40, and DPPE-80.",
    "Assessed at 0, 24, and 48 hours of chilled storage at 4 degrees Celsius.",
    "Two endpoints: CASA motility and HOST membrane integrity.",
    "The results are unequivocal.",
    "At 48 hours, DPPE-80 maintains 67.5 percent total motility versus 58.3 percent for control.",
    "That is a 9.2 percentage point advantage — a 16 percent relative improvement.",
    "The effect size is eta-squared equals 0.76 — far exceeding the 0.14 threshold for large effects.",
    "The treatment-by-time interaction is significant at p equals 0.024.",
    "This means DPPE's protective effect strengthens over time. The gap widens from 1.7 points at baseline to 9.2 points at 48 hours.",
    "This is consistent with a sustained-release antioxidant mechanism.",
    "For membrane integrity: plus 8.8 percentage points at 48 hours.",
    "This is critical because ram sperm membranes are 30 to 40 percent DHA — the most vulnerable to peroxidation.",
    "The biological significance: for a typical recovery of 5 to 15 billion sperm, this translates to 2 to 14 additional AI doses per rescued ram.",
    "All four hypotheses were supported. The central thesis claim is validated.",
  ],
  exp4: [
    "Experiment 4 documented climate change perceptions among the same 200 keepers.",
    "95 percent recognize the climate-fertility link. This is not a population that needs convincing — they need tools.",
    "78.5 percent reported perceived fertility decline over the past five years.",
    "But only 41.5 percent employ adaptation strategies. This gap reflects structural barriers.",
    "The primary stressor is nutritional stress at 48.9 percent — not direct heat stress.",
    "Keepers perceive the indirect climate pathway through forage scarcity as more consequential.",
    "The binary logistic regression identified medium-sized flocks — 20 to 50 head — as the vulnerability sweet spot.",
    "The odds ratio is 24.86, with p equals 0.004.",
    "This challenges the conventional assumption that the smallest flocks are most vulnerable.",
    "Medium flocks are large enough to exhibit systematic climate-fertility patterns, yet small enough to lack institutional buffering.",
    "The policy implication: adaptation support should be strategically targeted at medium-sized flocks.",
  ],
  conclusion: [
    "To conclude.",
    "This thesis began by identifying a gap — the disconnect between urgent need for genetic conservation and lack of accessible preservation technologies.",
    "It ends by providing a bridge.",
    "A validated, low-cost, culturally acceptable protocol grounded in the realities of the stakeholders it aims to serve.",
    "The DPPE protocol at 80 mg/mL extends the practical preservation window from less than 24 hours to more than 48 hours.",
    "With a cost-benefit ratio of 3,000 to 1, it represents one of the highest-return conservation investments available.",
    "The triangulated conservation model integrates socioeconomic priorities, technical efficacy, and climate urgency.",
    "All four hypotheses were supported.",
    "The journey from field need to technical solution is complete.",
    "But the journey from laboratory validation to field implementation is just beginning.",
    "Thank you for your attention. I welcome your questions.",
  ],
};

interface QAItem { id: string; category: string; question: string; answer: string; }

export const QA_DATABASE: QAItem[] = [
  { id: "q1", category: "methodology", question: "Why chilled storage at 4°C rather than cryopreservation?", answer: "Chilled storage was chosen for field applicability — El Oued lacks cryopreservation infrastructure. The 48h window aligns with realistic AI timelines. Cryopreservation trials are the priority next step." },
  { id: "q2", category: "results", question: "How claim biological significance without in vivo fertility trials?", answer: "Motility/membrane integrity are strong predictors (r > 0.7 with field fertility in literature). However, prediction ≠ confirmation. In vivo AI trials are the priority next step in the research roadmap." },
  { id: "q3", category: "methodology", question: "Sample size of 5 rams — statistical justification?", answer: "n=5 with 3 aliquots × 3 time points = 45 data points per parameter. Power > 0.85 for detected effects (η² > 0.70). Underpowered for subtle variations — expanded trials (n ≥ 20) planned." },
  { id: "q4", category: "results", question: "DPPH IC₅₀ weaker than ascorbic acid — why does DPP outperform?", answer: "DPPH captures only aqueous-phase scavenging. DPP provides 5 complementary actions: membrane polyphenols, mitochondrial flavonoids, metal chelation, enzyme cofactors (Zn→SOD, Se→GPx), vitamin E+C synergy. Biological efficacy (Exp 3) is the relevant metric." },
  { id: "q5", category: "results", question: "Medium-flock OR=24.86 with wide CI — artifact?", answer: "Wide CI (4.85–127.45) reflects small commercial sample (n=12). Three lines of evidence support it: (1) consistent across model specs, (2) H-L p=0.42 good fit, (3) theoretically plausible — medium flocks lack institutional buffering." },
  { id: "q6", category: "limitations", question: "How generalizable beyond El Oued?", answer: "Three levels: (1) Direct — other Algerian arid regions. (2) Adapted — MENA date-growing regions. (3) Methodological — agro-ecological cryobiology paradigm transferable to any context with local botanical resources." },
  { id: "q7", category: "theory", question: "Single most important contribution?", answer: "The triangulated conservation model integrating socioeconomic priorities, technical efficacy, and environmental urgency. The DPPE protocol is the empirical demonstration; the model is the theoretical contribution that will outlast the protocol." },
  { id: "q8", category: "application", question: "Practical next step for field deployment?", answer: "48-Hour Genetic Rescue Protocol: (1) Testes retrieval ≤2h, (2) Cauda dissection + retrograde flushing, (3) Dilution 1:1 with DPPE-80, (4) Chilled storage 4°C under mineral oil, (5) Quality check CASA+HOST at 24h/48h, (6) AI within 48h." },
  { id: "q9", category: "limitations", question: "Centrifuge parameters not standardized — how address?", answer: "Acknowledged gap. Standardization is priority for Phase 1 roadmap. Initial recommendation: 3,000 × g for 10 minutes at 4°C, based on similar botanical extract protocols. Requires batch quality control validation." },
  { id: "q10", category: "theory", question: "How does work relate to One Health framework?", answer: "Contributes to all three domains: (1) Animal health — preserves genetic diversity. (2) Human health — sustains rural livelihoods/food security. (3) Environmental health — climate-adapted genotypes preserved. Plus: DPPE eliminates animal-product transmission pathway (no egg yolk), reducing zoonotic risk." },
  { id: "q11", category: "application", question: "Economic case for national scale adoption?", answer: "Algeria loses ~200,000 rams/year. At 30% capture: 60,000 rescued, 4.2M additional AI doses/year. At USD 20/dose = USD 84M annual value. Cost-benefit ratio 3,000:1 to 4,000:1." },
  { id: "q12", category: "results", question: "Treatment × time interaction significance — what does it tell us?", answer: "Interaction (p=0.024, η²=0.49) indicates DPPE's effect strengthens over time — gap widens from 1.7pp at 0h to 9.2pp at 48h. Consistent with sustained-release antioxidant mechanism: DPP compounds diffuse into sperm microenvironment, accumulating in mitochondrial/membrane compartments." },
];

const categoryColors: Record<string, string> = {
  methodology: "#2D5016", results: "#8B6914", limitations: "#9C4942", theory: "#5C8A3E", application: "#486C91",
};

export default function PresentationAssistant({ currentScene }: { currentScene: string }) {
  const [isOpen, setIsOpen] = useState(false);
  const [activeTab, setActiveTab] = useState<"timer" | "teleprompter" | "qa">("timer");
  const [isRunning, setIsRunning] = useState(false);
  const [elapsed, setElapsed] = useState(0);
  const [totalElapsed, setTotalElapsed] = useState(0);
  const [scrollSpeed, setScrollSpeed] = useState(1);
  const [isScrolling, setIsScrolling] = useState(false);
  const scrollRef = useRef<HTMLDivElement>(null);
  const scrollIntervalRef = useRef<ReturnType<typeof setInterval> | null>(null);

  useEffect(() => {
    let interval: ReturnType<typeof setInterval>;
    if (isRunning) {
      interval = setInterval(() => {
        setElapsed((e) => e + 1);
        setTotalElapsed((t) => t + 1);
      }, 1000);
    }
    return () => { if (interval) clearInterval(interval); };
  }, [isRunning]);

  // Reset elapsed time when scene changes
  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setElapsed(0);
  }, [currentScene]);

  useEffect(() => {
    if (isScrolling) {
      scrollIntervalRef.current = setInterval(() => {
        if (scrollRef.current) scrollRef.current.scrollTop += scrollSpeed;
      }, 50);
    } else if (scrollIntervalRef.current) {
      clearInterval(scrollIntervalRef.current);
    }
    return () => { if (scrollIntervalRef.current) clearInterval(scrollIntervalRef.current); };
  }, [isScrolling, scrollSpeed]);

  const timing = SCENE_TIMING[currentScene] || { recommended: 3, label: "Scene" };
  const recommendedSeconds = timing.recommended * 60;
  const progressPercent = Math.min((elapsed / recommendedSeconds) * 100, 100);
  const isOverTime = elapsed > recommendedSeconds;
  const isNearTime = elapsed > recommendedSeconds * 0.8 && !isOverTime;
  const timerColor = isOverTime ? "#9C4942" : isNearTime ? "#8B6914" : "#2D5016";
  const timerBg = isOverTime ? "bg-destructive/10" : isNearTime ? "bg-accent/10" : "bg-primary/10";

  const formatTime = (seconds: number) => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m.toString().padStart(2, "0")}:${s.toString().padStart(2, "0")}`;
  };

  const script = SPEECH_SCRIPTS[currentScene] || ["No script available for this scene."];

  const [qaFilter, setQaFilter] = useState("all");
  const [expandedQA, setExpandedQA] = useState<string | null>(null);
  const qaCategories = [
    { id: "all", label: "All", count: QA_DATABASE.length },
    { id: "methodology", label: "Method", count: QA_DATABASE.filter(q => q.category === "methodology").length },
    { id: "results", label: "Results", count: QA_DATABASE.filter(q => q.category === "results").length },
    { id: "limitations", label: "Limits", count: QA_DATABASE.filter(q => q.category === "limitations").length },
    { id: "theory", label: "Theory", count: QA_DATABASE.filter(q => q.category === "theory").length },
    { id: "application", label: "Applied", count: QA_DATABASE.filter(q => q.category === "application").length },
  ];
  const filteredQA = qaFilter === "all" ? QA_DATABASE : QA_DATABASE.filter(q => q.category === qaFilter);

  if (!isOpen) {
    return (
      <button
        onClick={() => setIsOpen(true)}
        className="fixed bottom-16 right-4 z-40 w-14 h-14 rounded-full bg-primary text-primary-foreground shadow-lg hover:bg-primary/90 transition-all flex items-center justify-center group"
        title="Presentation Assistant"
      >
        <Mic className="h-6 w-6" />
        <span className="absolute right-full mr-3 whitespace-nowrap bg-foreground text-background text-xs px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity">
          Presentation Assistant
        </span>
        {isRunning && (
          <span className="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-destructive border-2 border-background" />
        )}
      </button>
    );
  }

  return (
    <div className="fixed bottom-16 right-4 z-40 w-96 max-h-[80vh] flex flex-col">
      <Card className="flex flex-col shadow-2xl border-primary/30">
        <div className="flex items-center justify-between p-3 bg-primary text-primary-foreground rounded-t-lg">
          <div className="flex items-center gap-2">
            <Mic className="h-4 w-4" />
            <span className="text-sm font-bold">Presentation Assistant</span>
          </div>
          <button onClick={() => setIsOpen(false)} className="hover:bg-primary-foreground/20 p-1 rounded">
            <X className="h-4 w-4" />
          </button>
        </div>

        <div className="flex border-b border-border">
          {[
            { id: "timer" as const, label: "Timer", icon: Clock },
            { id: "teleprompter" as const, label: "Script", icon: Eye },
            { id: "qa" as const, label: "Q&A", icon: AlertCircle },
          ].map((tab) => {
            const Icon = tab.icon;
            return (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`flex-1 flex items-center justify-center gap-1.5 py-2 text-xs font-bold transition-all ${
                  activeTab === tab.id ? "bg-primary/10 text-primary border-b-2 border-primary" : "text-muted-foreground hover:text-foreground"
                }`}
              >
                <Icon className="h-3.5 w-3.5" />
                {tab.label}
              </button>
            );
          })}
        </div>

        <div className="flex-1 overflow-y-auto max-h-[60vh]">
          {/* TIMER TAB */}
          {activeTab === "timer" && (
            <div className="p-4 space-y-4">
              <div className={`rounded-lg p-4 ${timerBg} border`} style={{ borderColor: `${timerColor}40` }}>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-xs font-bold uppercase tracking-wider" style={{ color: timerColor }}>{timing.label}</span>
                  {isOverTime ? (
                    <Badge className="bg-destructive text-destructive-foreground text-[9px] gap-1"><AlertCircle className="h-2.5 w-2.5" /> Over time</Badge>
                  ) : isNearTime ? (
                    <Badge className="bg-accent text-accent-foreground text-[9px] gap-1"><Clock className="h-2.5 w-2.5" /> Wrap up</Badge>
                  ) : (
                    <Badge className="bg-primary text-primary-foreground text-[9px] gap-1"><CheckCircle2 className="h-2.5 w-2.5" /> On track</Badge>
                  )}
                </div>
                <div className="flex items-baseline gap-2 mb-2">
                  <span className="font-num text-4xl font-bold" style={{ color: timerColor }}>{formatTime(elapsed)}</span>
                  <span className="text-xs text-muted-foreground">/ {formatTime(recommendedSeconds)}</span>
                </div>
                <div className="w-full h-2 bg-secondary rounded-full overflow-hidden">
                  <div className="h-full rounded-full transition-all duration-1000" style={{ width: `${progressPercent}%`, backgroundColor: timerColor }} />
                </div>
              </div>

              <div className="rounded-lg p-3 bg-secondary/50 border border-border">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <Timer className="h-4 w-4 text-accent" />
                    <span className="text-xs font-bold uppercase tracking-wider text-accent">Total Elapsed</span>
                  </div>
                  <span className="font-num text-2xl font-bold text-foreground">{formatTime(totalElapsed)}</span>
                </div>
                <div className="text-[10px] text-muted-foreground mt-1">Target: ~30 min presentation + 15 min Q&A</div>
              </div>

              <div className="flex gap-2">
                <Button onClick={() => setIsRunning(!isRunning)} size="sm" className={`flex-1 gap-1 ${isRunning ? "bg-destructive hover:bg-destructive/90" : "bg-primary hover:bg-primary/90"}`}>
                  {isRunning ? <Pause className="h-3.5 w-3.5" /> : <Play className="h-3.5 w-3.5" />}
                  {isRunning ? "Pause" : "Start"}
                </Button>
                <Button onClick={() => { setElapsed(0); setTotalElapsed(0); setIsRunning(false); }} size="sm" variant="outline" className="gap-1">
                  <RotateCcw className="h-3.5 w-3.5" /> Reset
                </Button>
              </div>

              <div className="rounded-lg p-3 bg-background border border-border">
                <div className="text-[10px] uppercase tracking-wider font-bold text-muted-foreground mb-2">All Scene Timings</div>
                <div className="space-y-1">
                  {Object.entries(SCENE_TIMING).map(([id, t]) => (
                    <div key={id} className={`flex items-center justify-between text-[11px] py-1 px-2 rounded ${currentScene === id ? "bg-primary/10 font-bold" : ""}`}>
                      <span className={currentScene === id ? "text-primary" : "text-foreground"}>{t.label}</span>
                      <span className="font-num text-muted-foreground">{t.recommended} min</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          )}

          {/* TELEPROMPTER TAB */}
          {activeTab === "teleprompter" && (
            <div className="p-4 space-y-3">
              <div className="flex items-center justify-between">
                <div>
                  <div className="text-xs font-bold uppercase tracking-wider text-primary">Speech Script</div>
                  <div className="text-[10px] text-muted-foreground">{timing.label}</div>
                </div>
                <div className="flex items-center gap-1">
                  <button onClick={() => setScrollSpeed(Math.max(0.5, scrollSpeed - 0.5))} className="p-1 rounded hover:bg-secondary"><ChevronDown className="h-3.5 w-3.5" /></button>
                  <span className="font-num text-xs w-8 text-center">{scrollSpeed}x</span>
                  <button onClick={() => setScrollSpeed(Math.min(5, scrollSpeed + 0.5))} className="p-1 rounded hover:bg-secondary"><ChevronUp className="h-3.5 w-3.5" /></button>
                </div>
              </div>
              <Button onClick={() => setIsScrolling(!isScrolling)} size="sm" className="w-full gap-1" variant={isScrolling ? "destructive" : "default"}>
                {isScrolling ? <Pause className="h-3.5 w-3.5" /> : <Play className="h-3.5 w-3.5" />}
                {isScrolling ? "Stop Auto-Scroll" : "Start Auto-Scroll"}
              </Button>
              <div ref={scrollRef} className="h-[300px] overflow-y-auto rounded-lg p-4 bg-secondary/30 border border-border">
                {script.map((line, i) => (
                  <p key={i} className="text-sm text-foreground leading-relaxed mb-3 font-body">{line}</p>
                ))}
              </div>
              <div className="text-[10px] text-muted-foreground italic text-center">Adjust scroll speed with +/− buttons. Click auto-scroll for hands-free reading.</div>
            </div>
          )}

          {/* Q&A TAB */}
          {activeTab === "qa" && (
            <div className="p-3 space-y-2">
              <div className="flex flex-wrap gap-1 mb-2">
                {qaCategories.map((cat) => (
                  <button key={cat.id} onClick={() => setQaFilter(cat.id)}
                    className={`px-2 py-1 rounded text-[10px] font-bold transition-all ${qaFilter === cat.id ? "bg-primary text-primary-foreground" : "bg-secondary text-muted-foreground hover:text-foreground"}`}>
                    {cat.label} ({cat.count})
                  </button>
                ))}
              </div>
              <div className="space-y-2">
                {filteredQA.map((qa) => {
                  const isExpanded = expandedQA === qa.id;
                  return (
                    <div key={qa.id} className="rounded-md border border-border overflow-hidden" style={{ borderLeft: `3px solid ${categoryColors[qa.category]}` }}>
                      <button onClick={() => setExpandedQA(isExpanded ? null : qa.id)} className="w-full text-left p-2 hover:bg-secondary/50 transition-colors">
                        <div className="flex items-start gap-2">
                          <Badge className="text-[8px] flex-shrink-0" style={{ backgroundColor: categoryColors[qa.category], color: "#FBFAF7" }}>{qa.category}</Badge>
                          <span className="text-xs font-medium text-foreground leading-snug">{qa.question}</span>
                        </div>
                      </button>
                      <AnimatePresence>
                        {isExpanded && (
                          <motion.div initial={{ height: 0, opacity: 0 }} animate={{ height: "auto", opacity: 1 }} exit={{ height: 0, opacity: 0 }} transition={{ duration: 0.2 }}>
                            <div className="p-3 bg-secondary/30 border-t border-border">
                              <div className="text-[10px] uppercase tracking-wider font-bold text-accent mb-1">Recommended Response</div>
                              <p className="text-xs text-foreground leading-relaxed">{qa.answer}</p>
                            </div>
                          </motion.div>
                        )}
                      </AnimatePresence>
                    </div>
                  );
                })}
              </div>
            </div>
          )}
        </div>
      </Card>
    </div>
  );
}
