"use client";

import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Users, Beaker, Microscope, Cloud, ArrowRight, CheckCircle2 } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

interface Experiment {
  id: string;
  num: string;
  title: string;
  icon: "users" | "beaker" | "microscope" | "cloud";
  color: string;
  question: string;
  method: string;
  sample: string;
  hypothesis: string;
  result: string;
  keyStat: string;
  output: string;
}

const EXPERIMENTS: Experiment[] = [
  { id: "exp1", num: "01", title: "Socioeconomic Survey", icon: "users", color: "#8B6914",
    question: "What socioeconomic determinants and trait preferences define genetic conservation priorities among El Oued sheep keepers?",
    method: "Stratified random sampling · Semi-structured questionnaires · Arabic face-to-face interviews",
    sample: "200 keepers · 8 municipalities · 4 flock-size categories",
    hypothesis: "Ha1: Education × experience × occupation interact to shape trait priorities",
    result: "Significant 3-way interaction; keepers prioritize breed identity (27%) and drought tolerance (16%) over rapid growth",
    keyStat: "Pillai's Trace = 0.070 · p = 0.009 · η² = 0.070",
    output: "Identifies conservation priorities and target demographics for intervention" },
  { id: "exp2", num: "02", title: "Phytochemical Characterization", icon: "beaker", color: "#2D5016",
    question: "Does El Oued-sourced DPP possess the biochemical profile necessary for sperm cryoprotection?",
    method: "AOAC 2019 proximate · Flame photometry · Folin-Ciocalteu · DPPH radical scavenging",
    sample: "Hamraia DPP · Triplicate determinations · March-April 2025",
    hypothesis: "Ha2: Local DPP possesses antioxidant capacity suitable for cryoprotection",
    result: "Nutrient-dense profile: protein 37.94% · K 1140 mg/100g · IC₅₀ 624.25 µg/mL",
    keyStat: "Multi-target matrix: polyphenols + minerals + vitamins + amino acids",
    output: "Validates DPP as multi-target cryoprotective agent · enables batch quality control" },
  { id: "exp3", num: "03", title: "Sperm Preservation Trial", icon: "microscope", color: "#2D5016",
    question: "Is aqueous DPPE effective for preserving post-slaughter ovine epididymal sperm quality during chilled storage at 4°C?",
    method: "Retrograde flushing · CASA motility · HOST membrane integrity · Two-way RM-ANOVA",
    sample: "n=5 rams · 3 treatments (0/40/80 mg/mL) × 3 time points (0/24/48h)",
    hypothesis: "Ha3: DPPE-80 significantly preserves sperm quality in dose-dependent manner",
    result: "+9.2 pp total motility · +9.2 pp progressive motility · +8.8 pp membrane integrity at 48h",
    keyStat: "η² = 0.72–0.76 · p < 0.01 · all main effects + interactions significant",
    output: "Validated 48-Hour Genetic Rescue Protocol · field-deployable" },
  { id: "exp4", num: "04", title: "Climate Perceptions", icon: "cloud", color: "#9C4942",
    question: "How do climate change perceptions influence the urgency for genetic conservation interventions, and which flock categories are most vulnerable?",
    method: "Same 200-keeper cohort · 4-module perception instrument · Binary logistic regression",
    sample: "200 keepers · 6 predictors · Hosmer-Lemeshow goodness-of-fit",
    hypothesis: "Ha4: Climate perceptions predict fertility decline; medium flocks most vulnerable",
    result: "95% climate-fertility awareness · nutritional stress dominates (48.9%) · medium flocks = vulnerability sweet spot",
    keyStat: "OR = 24.86 (95% CI: 4.85–127.45) · p = 0.004 · H-L p = 0.42",
    output: "Identifies medium flocks (20-50 head) as priority intervention target" },
];

const iconMap = { users: Users, beaker: Beaker, microscope: Microscope, cloud: Cloud };

export default function InteractiveResearchWorkflow() {
  const [selected, setSelected] = useState<Experiment>(EXPERIMENTS[0]);

  return (
    <div>
      <div className="flex items-center justify-between mb-4">
        <h3 className="font-heading text-base font-bold text-primary">Research Design Workflow — Click Each Experiment</h3>
        <Badge variant="secondary" className="text-[10px]">Context → Characterization → Efficacy → Urgency</Badge>
      </div>

      <div className="grid md:grid-cols-4 gap-3 mb-6">
        {EXPERIMENTS.map((exp, i) => {
          const Icon = iconMap[exp.icon];
          const isSelected = selected.id === exp.id;
          return (
            <div key={exp.id} className="relative">
              <button
                onClick={() => setSelected(exp)}
                className={`w-full text-left p-4 rounded-lg border-2 transition-all ${isSelected ? "shadow-md scale-105" : "hover:scale-[1.02]"}`}
                style={{ borderColor: isSelected ? exp.color : "#D2CEC0", backgroundColor: isSelected ? `${exp.color}10` : "#FBFAF7" }}
              >
                <div className="flex items-center gap-2 mb-2">
                  <div className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0" style={{ backgroundColor: `${exp.color}20`, color: exp.color }}>
                    <Icon className="h-4 w-4" />
                  </div>
                  <span className="font-num text-2xl font-bold" style={{ color: exp.color }}>{exp.num}</span>
                </div>
                <div className="font-heading text-sm font-bold text-foreground mb-1">{exp.title}</div>
                <div className="text-[10px] text-muted-foreground font-num">{exp.sample.split('·')[0].trim()}</div>
              </button>
              {i < EXPERIMENTS.length - 1 && (
                <div className="hidden md:block absolute top-1/2 -right-2 transform -translate-y-1/2 z-10">
                  <ArrowRight className="h-4 w-4 text-accent" />
                </div>
              )}
            </div>
          );
        })}
      </div>

      <Card className="p-4 mb-4 bg-primary/5 border-primary/20">
        <div className="flex items-center gap-3">
          <CheckCircle2 className="h-5 w-5 text-primary flex-shrink-0" />
          <div className="flex-1">
            <div className="font-heading text-sm font-bold text-primary">Integration & Synthesis</div>
            <p className="text-xs text-foreground mt-0.5">All four experiments converge on the triangulated conservation model — validated field-deployable DPPE protocol aligned with keeper priorities and climate urgency.</p>
          </div>
          <Badge className="bg-primary text-primary-foreground text-[10px] gap-1"><CheckCircle2 className="h-3 w-3" />4/4 hypotheses supported</Badge>
        </div>
      </Card>

      <AnimatePresence mode="wait">
        <motion.div key={selected.id} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0, y: -10 }} transition={{ duration: 0.3 }}>
          <Card className="p-6" style={{ borderLeft: `4px solid ${selected.color}` }}>
            <div className="flex items-start gap-4 mb-4">
              <div className="w-14 h-14 rounded-lg flex items-center justify-center flex-shrink-0" style={{ backgroundColor: `${selected.color}20`, color: selected.color }}>
                {(() => { const Icon = iconMap[selected.icon]; return <Icon className="h-7 w-7" />; })()}
              </div>
              <div className="flex-1">
                <div className="flex items-baseline gap-2 mb-1">
                  <span className="font-num text-2xl font-bold" style={{ color: selected.color }}>Experiment {selected.num}</span>
                  <h4 className="font-heading text-xl font-bold text-foreground">{selected.title}</h4>
                </div>
                <p className="text-sm text-muted-foreground italic">{selected.question}</p>
              </div>
            </div>

            <div className="grid md:grid-cols-2 gap-4 mb-4">
              <div>
                <div className="text-[10px] uppercase tracking-wider font-bold mb-1" style={{ color: selected.color }}>Methodology</div>
                <p className="text-xs text-foreground mb-3 leading-relaxed">{selected.method}</p>
                <div className="text-[10px] uppercase tracking-wider font-bold mb-1" style={{ color: selected.color }}>Sample</div>
                <p className="text-xs text-foreground leading-relaxed">{selected.sample}</p>
              </div>
              <div>
                <div className="text-[10px] uppercase tracking-wider font-bold mb-1" style={{ color: selected.color }}>Hypothesis</div>
                <p className="text-xs text-foreground mb-3 leading-relaxed italic">{selected.hypothesis}</p>
                <div className="text-[10px] uppercase tracking-witer font-bold mb-1" style={{ color: selected.color }}>Key Statistical Result</div>
                <div className="font-num text-sm font-bold p-2 rounded-md" style={{ backgroundColor: `${selected.color}10`, color: selected.color }}>{selected.keyStat}</div>
              </div>
            </div>

            <div className="border-t border-border pt-4">
              <div className="text-[10px] uppercase tracking-wider font-bold mb-1" style={{ color: selected.color }}>Key Finding</div>
              <p className="text-sm text-foreground leading-relaxed mb-3">{selected.result}</p>
              <div className="bg-secondary/50 rounded-md p-3">
                <div className="text-[10px] uppercase tracking-wider text-accent font-bold mb-1">Output / Contribution</div>
                <p className="text-xs text-foreground leading-relaxed">{selected.output}</p>
              </div>
            </div>
          </Card>
        </motion.div>
      </AnimatePresence>
    </div>
  );
}
