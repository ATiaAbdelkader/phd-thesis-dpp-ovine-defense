"use client";

import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { CheckCircle2 } from "lucide-react";
import InteractiveResearchWorkflow from "@/components/InteractiveResearchWorkflow";
import SpeakerNotes, { SpeakerNote } from "@/components/SpeakerNotes";

const notes: SpeakerNote[] = [
  { type: "key", text: "Open with: 'This is the integrated research design — four experiments that together address the empirical, methodological, and integration gaps identified in the literature review.'" },
  { type: "key", text: "Walk through each experiment card sequentially (click each one to expand the detail). Emphasize the triangulated design: Context (Exp 1) → Characterization (Exp 2) → Efficacy (Exp 3) → Urgency (Exp 4)." },
  { type: "key", text: "Highlight that ALL FOUR hypotheses were supported. This is unusual in PhD research — typically some hypotheses fail. The consistency validates both the conceptual framework and the implementation." },
  { type: "transition", text: "Transition: 'Let me walk you through each experiment in detail, starting with the socioeconomic survey.' → Move to Experiment 1." },
  { type: "timing", text: "Spend ~2 minutes here — this is an overview scene. The detail comes in the dedicated experiment scenes that follow." },
];

export default function ResearchDesignScene() {
  return (
    <div className="p-6 md:p-10 max-w-7xl mx-auto">
      <div className="mb-6">
        <Badge variant="outline" className="text-accent border-accent/40 mb-2 font-num">02 · RESEARCH DESIGN</Badge>
        <h2 className="font-heading text-3xl md:text-4xl font-bold text-primary mb-2">Four Interconnected Experiments</h2>
        <p className="text-muted-foreground text-sm">Click each experiment to explore question, method, hypothesis, and result</p>
      </div>

      <Card className="p-6 mb-6">
        <InteractiveResearchWorkflow />
      </Card>

      <Card className="p-5 mb-6 bg-secondary/30">
        <h3 className="font-heading text-base font-bold text-primary mb-3">Statistical Methods Summary</h3>
        <div className="grid md:grid-cols-4 gap-3">
          <div className="bg-background rounded-md p-3 border border-border"><div className="text-[10px] uppercase tracking-wider font-bold text-accent mb-1">Exp 1</div><div className="font-num text-sm font-bold text-primary">MANOVA</div><div className="text-[10px] text-muted-foreground">Pillai's Trace · α = 0.05</div></div>
          <div className="bg-background rounded-md p-3 border border-border"><div className="text-[10px] uppercase tracking-wider font-bold text-accent mb-1">Exp 2</div><div className="font-num text-sm font-bold text-primary">Descriptive</div><div className="text-[10px] text-muted-foreground">Mean ± SD · triplicate</div></div>
          <div className="bg-background rounded-md p-3 border border-border"><div className="text-[10px] uppercase tracking-wider font-bold text-accent mb-1">Exp 3</div><div className="font-num text-sm font-bold text-primary">Two-way RM-ANOVA</div><div className="text-[10px] text-muted-foreground">Bonferroni post-hoc · α = 0.05</div></div>
          <div className="bg-background rounded-md p-3 border border-border"><div className="text-[10px] uppercase tracking-wider font-bold text-accent mb-1">Exp 4</div><div className="font-num text-sm font-bold text-primary">Logistic Regression</div><div className="text-[10px] text-muted-foreground">Hosmer-Lemeshow · OR + 95% CI</div></div>
        </div>
        <div className="mt-3 text-[11px] text-muted-foreground italic">All analyses performed in IBM SPSS Statistics v27.0 (IBM Corp., Armonk, NY, USA)</div>
      </Card>

      <Card className="p-5 mb-6">
        <div className="flex items-center gap-2 mb-3">
          <CheckCircle2 className="h-5 w-5 text-primary" />
          <h3 className="font-heading text-base font-bold text-primary">Four Alternative Hypotheses — All Supported</h3>
        </div>
        <div className="grid md:grid-cols-2 gap-3">
          {[
            { h: "Ha1", text: "Education × experience × occupation interact to shape trait priorities", stat: "p = 0.009, η² = 0.070" },
            { h: "Ha2", text: "El Oued DPP exhibits nutrient-dense profile with measurable polyphenol content and DPPH scavenging activity", stat: "IC₅₀ = 624.25 µg/mL; protein 37.94%" },
            { h: "Ha3", text: "DPPE-80 (80 mg/mL) significantly preserves total motility, progressive motility, and membrane integrity across 0/24/48h at 4°C", stat: "η² = 0.72–0.76, p < 0.01" },
            { h: "Ha4", text: "Climate perceptions significantly predict perceived fertility decline; medium flocks (20–50 head) show highest vulnerability", stat: "OR = 24.86, p = 0.004" },
          ].map((hyp, i) => (
            <div key={i} className="flex items-start gap-3 p-3 bg-secondary/50 rounded-md">
              <div className="flex flex-col items-center flex-shrink-0">
                <Badge className="bg-primary text-primary-foreground font-num">{hyp.h}</Badge>
                <CheckCircle2 className="h-3 w-3 text-primary mt-1" />
              </div>
              <div className="flex-1 min-w-0">
                <p className="text-xs text-foreground leading-relaxed mb-1">{hyp.text}</p>
                <div className="font-num text-[11px] font-bold text-accent">{hyp.stat}</div>
              </div>
            </div>
          ))}
        </div>
      </Card>

      <SpeakerNotes notes={notes} defaultOpen={false} />
    </div>
  );
}
