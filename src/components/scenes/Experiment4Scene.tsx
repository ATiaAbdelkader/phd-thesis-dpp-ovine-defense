"use client";

import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Cloud, Target, AlertTriangle, TrendingDown, Brain } from "lucide-react";
import { motion } from "framer-motion";
import SpeakerNotes, { SpeakerNote } from "@/components/SpeakerNotes";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell, PieChart, Pie, Legend } from "recharts";

const stressorData = [
  { name: "Nutritional stress (forage scarcity)", value: 48.9, color: "#2D5016" },
  { name: "Direct heat stress", value: 30.0, color: "#9C4942" },
  { name: "Water scarcity", value: 11.5, color: "#8B6914" },
  { name: "Disease emergence", value: 6.0, color: "#A85A3A" },
  { name: "Other", value: 3.6, color: "#6B5530" },
];

const awarenessData = [
  { metric: "Climate-fertility awareness", pct: 95, color: "#2D5016" },
  { metric: "Reported fertility decline (5yr)", pct: 78.5, color: "#9C4942" },
  { metric: "Reported mortality events", pct: 62, color: "#8B6914" },
  { metric: "Use adaptation strategies", pct: 41.5, color: "#A85A3A" },
];

const orData = [
  { predictor: "Medium flock (20-50)", or: 24.86, ci_low: 4.85, ci_high: 127.45, p: 0.004, sig: true, color: "#2D5016" },
  { predictor: "Older age (>45y)", or: 3.42, ci_low: 1.42, ci_high: 8.24, p: 0.018, sig: true, color: "#5C8A3E" },
  { predictor: "Heat-stress events", or: 2.78, ci_low: 1.12, ci_high: 6.92, p: 0.024, sig: true, color: "#8B6914" },
  { predictor: "Low education (≤primary)", or: 2.15, ci_low: 0.95, ci_high: 4.85, p: 0.082, sig: false, color: "#C4A858" },
  { predictor: "Full-time breeding", or: 1.87, ci_low: 0.85, ci_high: 4.12, p: 0.124, sig: false, color: "#A85A3A" },
  { predictor: "High experience (>15y)", or: 1.45, ci_low: 0.65, ci_high: 3.22, p: 0.364, sig: false, color: "#9C4942" },
];

const notes: SpeakerNote[] = [
  { type: "key", text: "Open with: '95% of El Oued sheep keepers perceive the climate-fertility link. This is not a population that needs convincing — they need tools. The DPPE protocol is that tool.'" },
  { type: "key", text: "Nutritional stress (48.9%) dominates over direct heat stress (30%). Keepers perceive the INDIRECT climate pathway — through forage scarcity — as more consequential than direct thermal effects on spermatogenesis." },
  { type: "key", text: "The 'vulnerability sweet spot': Medium flocks (20-50 head) show OR = 24.86 for perceived fertility decline. This challenges the assumption that the SMALLEST flocks are most vulnerable. Medium flocks are large enough to exhibit systematic patterns but small enough to lack institutional buffering." },
  { type: "key", text: "Adaptation gap: 95% awareness + 78.5% perceived decline + only 41.5% adaptation = STRUCTURAL BARRIERS. Keepers know the problem but lack feed resources, veterinary infrastructure, credit access, and appropriate technologies. The DPPE protocol addresses this gap." },
  { type: "qa", text: "If asked 'Is the OR=24.86 credible with such wide CI (4.85-127.45)?': Yes — the wide CI reflects small commercial category sample (n=12). But three lines of evidence support it: (1) consistent across model specifications, (2) Hosmer-Lemeshow p=0.42 indicates good fit, (3) theoretically plausible — medium flocks lack institutional buffering. Replication with larger samples is recommended." },
  { type: "qa", text: "If asked 'Why rely on perceptions rather than objective data?': Acknowledge limitation — perceptual data cannot establish causal attribution. But triangulates with physiological literature. Objective longitudinal data (meteorological + reproductive records) is priority for future research." },
  { type: "transition", text: "Transition: 'Now let me show you the interactive climate simulator — you can adjust heat days and rainfall deficit to see how vulnerability changes across flock categories.' → Move to Climate Simulator scene." },
  { type: "timing", text: "Spend ~3 minutes. Focus on the vulnerability sweet spot finding (medium flocks) — it's the most policy-relevant result and challenges conventional wisdom." },
];

export default function Experiment4Scene() {
  const [selectedPredictor, setSelectedPredictor] = useState(orData[0]);

  return (
    <div className="p-6 md:p-10 max-w-7xl mx-auto">
      <div className="mb-6">
        <div className="flex items-center gap-2 mb-2">
          <Badge variant="outline" className="text-accent border-accent/40 font-num">EXPERIMENT 04</Badge>
          <Badge variant="secondary" className="text-[10px] gap-1"><Cloud className="h-3 w-3" /> Same 200-keeper cohort · 5-yr recall</Badge>
        </div>
        <h2 className="font-heading text-3xl md:text-4xl font-bold text-primary mb-2">Climate Perceptions & Vulnerability Mapping</h2>
        <p className="text-muted-foreground text-sm">Binary logistic regression identifies the flock-size vulnerability sweet spot</p>
      </div>

      <Card className="p-4 mb-6 bg-destructive/5 border-destructive/30">
        <div className="flex items-start gap-3">
          <Target className="h-5 w-5 text-destructive flex-shrink-0 mt-0.5" />
          <div>
            <div className="text-[10px] uppercase tracking-witer font-bold text-destructive mb-1">Hypothesis Ha4 (Supported ✓)</div>
            <p className="text-sm text-foreground">Climate change perceptions significantly predict perceived fertility decline among sheep keepers, with medium-sized flocks (20–50 head) showing the highest vulnerability. <span className="font-num font-bold text-destructive">OR = 24.86 · p = 0.004 · Hosmer-Lemeshow p = 0.42</span></p>
          </div>
        </div>
      </Card>

      <Card className="p-5 mb-6">
        <div className="flex items-center gap-2 mb-3">
          <Brain className="h-4 w-4 text-primary" />
          <h3 className="font-heading text-sm font-bold text-primary">Climate-Fertility Awareness & Adaptation Gap</h3>
        </div>
        <div style={{ height: "220px" }}>
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={awarenessData} layout="vertical" margin={{ top: 5, right: 30, left: 100, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#D2CEC0" horizontal={false} />
              <XAxis type="number" stroke="#6B6B6B" fontSize={11} domain={[0, 100]} unit="%" />
              <YAxis dataKey="metric" type="category" stroke="#6B6B6B" fontSize={10} width={100} />
              <Tooltip contentStyle={{ backgroundColor: "#FBFAF7", border: "1px solid #D2CEC0", borderRadius: "8px", fontSize: "11px" }} />
              <Bar dataKey="pct" name="% of keepers" radius={[0, 4, 4, 0]}>
                {awarenessData.map((entry, i) => <Cell key={i} fill={entry.color} />)}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
        <div className="bg-destructive/5 rounded-md p-3 mt-3 border border-destructive/20">
          <div className="flex items-start gap-2">
            <AlertTriangle className="h-4 w-4 text-destructive flex-shrink-0 mt-0.5" />
            <p className="text-xs text-foreground leading-relaxed"><strong className="text-destructive">Adaptation Gap:</strong> 95% awareness + 78.5% perceived decline + only 41.5% adaptation = structural barriers (feed access, vet infrastructure, credit, appropriate technologies). The DPPE protocol directly addresses this gap as a low-cost, accessible intervention.</p>
          </div>
        </div>
      </Card>

      <div className="grid md:grid-cols-2 gap-4 mb-6">
        <Card className="p-5">
          <div className="flex items-center gap-2 mb-3">
            <Cloud className="h-4 w-4 text-accent" />
            <h3 className="font-heading text-sm font-bold text-primary">Primary Climate Stressors</h3>
          </div>
          <div style={{ height: "240px" }}>
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie data={stressorData} cx="50%" cy="50%" labelLine={false} label={({ value }) => `${value}%`} outerRadius={80} fill="#8884d8" dataKey="value">
                  {stressorData.map((entry, i) => <Cell key={i} fill={entry.color} />)}
                </Pie>
                <Tooltip contentStyle={{ backgroundColor: "#FBFAF7", border: "1px solid #D2CEC0", borderRadius: "8px", fontSize: "11px" }} />
              </PieChart>
            </ResponsiveContainer>
          </div>
          <div className="space-y-1">
            {stressorData.map((s, i) => (
              <div key={i} className="flex items-center gap-2 text-xs">
                <div className="w-3 h-3 rounded-sm" style={{ backgroundColor: s.color }} />
                <span className="text-foreground">{s.name}</span>
                <span className="font-num font-bold ml-auto">{s.value}%</span>
              </div>
            ))}
          </div>
        </Card>

        <Card className="p-5">
          <div className="flex items-center gap-2 mb-3">
            <TrendingDown className="h-4 w-4 text-destructive" />
            <h3 className="font-heading text-sm font-bold text-primary">Key Insight: Indirect Pathway Dominates</h3>
          </div>
          <div className="space-y-4">
            <div className="bg-primary/5 rounded-md p-4 border border-primary/20">
              <div className="text-[10px] uppercase tracking-witer font-bold text-primary mb-1">Nutritional Stress (48.9%)</div>
              <p className="text-xs text-foreground leading-relaxed">Keepers perceive the <strong>indirect</strong> climate-fertility pathway — through forage scarcity, maternal body condition, lamb survival — as more consequential than direct thermal effects on spermatogenesis.</p>
            </div>
            <div className="bg-accent/5 rounded-md p-4 border border-accent/20">
              <div className="text-[10px] uppercase tracking-witer font-bold text-accent mb-1">Direct Heat Stress (30.0%)</div>
              <p className="text-xs text-foreground leading-relaxed">Still significant — heat stress disrupts spermatogenesis 6-8 weeks post-exposure. Ouled Djellal breed has enhanced thermotolerance, but climate change imposes novel thermal regimes.</p>
            </div>
            <div className="bg-secondary rounded-md p-3">
              <p className="text-[11px] text-foreground leading-relaxed"><strong>Conservation implication:</strong> Strategies must preserve BOTH thermotolerance genes AND drought-tolerance traits. DPPE addresses both by enabling genetic rescue of climate-adapted genotypes regardless of mortality cause.</p>
            </div>
          </div>
        </Card>
      </div>

      <Card className="p-5 mb-6">
        <div className="flex items-center justify-between mb-3">
          <div>
            <h3 className="font-heading text-sm font-bold text-primary">Predictors of Perceived Fertility Decline — Interactive Forest Plot</h3>
            <p className="text-[11px] text-muted-foreground">Binary logistic regression · click each predictor for details</p>
          </div>
          <div className="flex gap-2">
            <Badge className="bg-primary text-primary-foreground text-[10px] font-num">H-L p = 0.42 (good fit)</Badge>
            <Badge variant="outline" className="text-[10px] font-num">Classification: 82.5%</Badge>
          </div>
        </div>

        <div className="grid md:grid-cols-2 gap-4">
          <div style={{ height: "300px" }}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={orData} layout="vertical" margin={{ top: 5, right: 30, left: 100, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#D2CEC0" horizontal={false} />
                <XAxis type="number" stroke="#6B6B6B" fontSize={10} domain={[0, 30]} scale="log" label={{ value: "Odds Ratio (log scale)", position: "insideBottom", offset: -5, style: { fontSize: 10, fill: "#6B6B6B" } }} />
                <YAxis dataKey="predictor" type="category" stroke="#6B6B6B" fontSize={10} width={100} />
                <Tooltip contentStyle={{ backgroundColor: "#FBFAF7", border: "1px solid #D2CEC0", borderRadius: "8px", fontSize: "11px" }} formatter={(_value: any, _name: any, props: any) => { const d = props.payload; return [`${d.or} (95% CI: ${d.ci_low}–${d.ci_high}, p=${d.p})`, `OR: ${d.predictor}`]; }} />
                <Bar dataKey="or" name="Odds Ratio" radius={[0, 4, 4, 0]}>
                  {orData.map((entry, i) => <Cell key={i} fill={entry.color} opacity={selectedPredictor.predictor === entry.predictor ? 1 : 0.5} onClick={() => setSelectedPredictor(entry)} />)}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>

          <motion.div key={selectedPredictor.predictor} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="bg-secondary/30 rounded-md p-4 border-l-4" style={{ borderLeftColor: selectedPredictor.color }}>
            <div className="flex items-center gap-2 mb-2">
              <div className="w-3 h-3 rounded-full" style={{ backgroundColor: selectedPredictor.color }} />
              <span className="font-heading text-base font-bold" style={{ color: selectedPredictor.color }}>{selectedPredictor.predictor}</span>
              {selectedPredictor.sig ? <Badge className="bg-primary text-primary-foreground text-[9px] ml-auto">Significant</Badge> : <Badge variant="outline" className="text-[9px] ml-auto">Not significant</Badge>}
            </div>
            <div className="grid grid-cols-3 gap-2 mb-3">
              <div><div className="text-[10px] uppercase tracking-witer text-muted-foreground">OR</div><div className="font-num text-2xl font-bold" style={{ color: selectedPredictor.color }}>{selectedPredictor.or}</div></div>
              <div><div className="text-[10px] uppercase tracking-witer text-muted-foreground">95% CI</div><div className="font-num text-xs font-bold text-foreground">{selectedPredictor.ci_low}–{selectedPredictor.ci_high}</div></div>
              <div><div className="text-[10px] uppercase tracking-witer text-muted-foreground">p-value</div><div className={`font-num text-sm font-bold ${selectedPredictor.sig ? "text-primary" : "text-muted-foreground"}`}>{selectedPredictor.p}</div></div>
            </div>
            <div className="bg-background rounded-md p-3 border border-border">
              <div className="text-[10px] uppercase tracking-witer font-bold mb-1" style={{ color: selectedPredictor.color }}>Interpretation</div>
              <p className="text-xs text-foreground leading-relaxed">
                {selectedPredictor.predictor.includes("Medium") ? "Medium flocks (20-50 head) are 24.86× more likely to report fertility decline. They are large enough to exhibit systematic patterns but small enough to lack institutional buffering of large commercial operations. → Priority intervention target."
                  : selectedPredictor.predictor.includes("Older") ? "Older keepers (>45y) are 3.42× more likely to perceive decline — likely reflects longer observation periods and cumulative experiential knowledge to recognize subtle fertility trends."
                  : selectedPredictor.predictor.includes("Heat") ? "Keepers reporting heat-stress events are 2.78× more likely to perceive decline. Validates the direct thermal stress pathway alongside the dominant nutritional stress pathway."
                  : "Not statistically significant at α=0.05. Contributes to overall model fit (Hosmer-Lemeshow p=0.42) but is not an independent predictor of perceived fertility decline."}
              </p>
            </div>
          </motion.div>
        </div>
      </Card>

      <SpeakerNotes notes={notes} defaultOpen={false} />
    </div>
  );
}
