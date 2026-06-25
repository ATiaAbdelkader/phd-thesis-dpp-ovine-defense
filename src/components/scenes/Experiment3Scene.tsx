"use client";

import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Microscope, Target, TrendingUp, Activity, Zap, Heart } from "lucide-react";
import { motion } from "framer-motion";
import SpeakerNotes, { SpeakerNote } from "@/components/SpeakerNotes";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend, ReferenceDot, BarChart, Bar, Cell, LabelList } from "recharts";

const motilityData = [{ time: "0h", control: 78.5, dpp40: 79.8, dpp80: 80.2 }, { time: "24h", control: 68.2, dpp40: 72.5, dpp80: 74.8 }, { time: "48h", control: 58.3, dpp40: 63.1, dpp80: 67.5 }];
const progressiveData = [{ time: "0h", control: 62.4, dpp40: 63.5, dpp80: 64.1 }, { time: "24h", control: 53.8, dpp40: 58.2, dpp80: 60.5 }, { time: "48h", control: 45.5, dpp40: 50.6, dpp80: 54.7 }];
const hostData = [{ time: "0h", control: 76.2, dpp40: 77.5, dpp80: 78.1 }, { time: "24h", control: 65.4, dpp40: 69.8, dpp80: 72.5 }, { time: "48h", control: 55.1, dpp40: 60.2, dpp80: 63.9 }];
const doseResponseData = [
  { dose: "0 mg/mL", total: 58.3, progressive: 45.5, host: 55.1, color: "#9C4942" },
  { dose: "40 mg/mL", total: 63.1, progressive: 50.6, host: 60.2, color: "#8B6914" },
  { dose: "80 mg/mL", total: 67.5, progressive: 54.7, host: 63.9, color: "#2D5016" },
];

const notes: SpeakerNote[] = [
  { type: "key", text: "Open with: 'This is the core experiment of my thesis — the dose-response validation of DPPE as a post-slaughter sperm preservation agent. Every result here is statistically significant with large effect sizes.'" },
  { type: "key", text: "Total motility at 48h: DPPE-80 = 67.5% vs Control = 58.3%. That's +9.2 percentage points — a 16% relative improvement. Effect size η² = 0.76 (treatment main effect). This is a LARGE effect (Cohen's threshold for large = 0.14)." },
  { type: "key", text: "Significant treatment × time interaction (p = 0.024) means DPPE's protective effect STRENGTHENS over time. The gap widens from 1.7 pp at 0h to 9.2 pp at 48h. This is consistent with sustained-release antioxidant mechanism." },
  { type: "key", text: "Membrane integrity (HOST): +8.8 pp at 48h. Critical because ram sperm membranes are 30-40% DHA — most vulnerable to peroxidation. The amphiphilic polyphenols (caffeic acid, quercetin) integrate at the membrane interface." },
  { type: "key", text: "Biological significance: For a typical post-slaughter recovery of 5-15 billion sperm, +9.2 pp = 0.46-1.38 BILLION additional motile sperm = 2-14 additional AI doses per rescued ram. Substantial practical gain." },
  { type: "qa", text: "If asked 'Why not cryopreservation?': Chilled storage was chosen for field applicability — El Oued lacks reliable liquid nitrogen infrastructure. The 48h window aligns with realistic AI application timelines in remote pastoral systems. Cryopreservation trials are priority next step." },
  { type: "qa", text: "If asked 'Why n=5 rams?': Adequate power for detecting large effects (η² > 0.70 → power > 0.85). Acknowledge underpowered for subtle dose-response variations — expanded trials (n ≥ 20) planned for Phase 1 of research roadmap." },
  { type: "qa", text: "If asked 'In vivo fertility?': Acknowledge limitation — no AI trials conducted. Motility/membrane integrity are strong predictors (r > 0.7 with field fertility in literature), but prediction ≠ confirmation. In vivo validation is priority next step." },
  { type: "transition", text: "Transition: 'The technical efficacy is validated. Now let me show you why this matters in the real world — the climate urgency that elevates the conservation imperative.' → Move to Experiment 4." },
  { type: "timing", text: "Spend 5-6 minutes — this is the FOCAL scene. Don't rush. Walk through each chart, emphasize effect sizes, and translate to biological significance (AI doses generated)." },
];

type ViewType = "total" | "progressive" | "host";

export default function Experiment3Scene() {
  const [view, setView] = useState<ViewType>("total");
  const chartData = view === "total" ? motilityData : view === "progressive" ? progressiveData : hostData;
  const chartTitle = view === "total" ? "Total Motility (%)" : view === "progressive" ? "Progressive Motility (%)" : "Membrane Integrity - HOST (%)";
  const gain48h = view === "total" ? 9.2 : view === "progressive" ? 9.2 : 8.8;
  const viewConfig = {
    total: { label: "Total Motility", icon: Activity, color: "#2D5016" },
    progressive: { label: "Progressive Motility", icon: Zap, color: "#8B6914" },
    host: { label: "Membrane Integrity", icon: Heart, color: "#9C4942" },
  };

  return (
    <div className="p-6 md:p-10 max-w-7xl mx-auto">
      <div className="mb-6">
        <div className="flex items-center gap-2 mb-2">
          <Badge variant="outline" className="text-accent border-accent/40 font-num">EXPERIMENT 03 · CORE RESULTS</Badge>
          <Badge variant="secondary" className="text-[10px] gap-1"><Microscope className="h-3 w-3" /> n=5 rams · 3×3 design</Badge>
        </div>
        <h2 className="font-heading text-3xl md:text-4xl font-bold text-primary mb-2">Sperm Preservation Trial Results</h2>
        <p className="text-muted-foreground text-sm">Dose-dependent DPPE conservative effects on post-slaughter ovine epididymal sperm — the central findings</p>
      </div>

      <Card className="p-4 mb-6 bg-primary/5 border-primary/30">
        <div className="flex items-start gap-3">
          <Target className="h-5 w-5 text-primary flex-shrink-0 mt-0.5" />
          <div>
            <div className="text-[10px] uppercase tracking-witer font-bold text-primary mb-1">Hypothesis Ha3 (Supported ✓) — Central Thesis Claim</div>
            <p className="text-sm text-foreground">DPPE-80 (80 mg/mL) significantly preserves total motility, progressive motility, and membrane integrity compared to control across 0, 24, and 48 hours of chilled storage at 4°C. <span className="font-num font-bold text-primary">η² = 0.72–0.76 · p &lt; 0.01 · all effects significant</span></p>
          </div>
        </div>
      </Card>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-3 mb-6">
        <Card className="p-4 bg-primary/5 border-primary/20"><div className="font-num text-3xl font-bold text-primary">+9.2 pp</div><div className="text-[10px] uppercase tracking-witer text-muted-foreground">Total Motility Gain (48h)</div></Card>
        <Card className="p-4 bg-accent/5 border-accent/20"><div className="font-num text-3xl font-bold text-accent">+9.2 pp</div><div className="text-[10px] uppercase tracking-witer text-muted-foreground">Progressive Motility Gain</div></Card>
        <Card className="p-4 bg-destructive/5 border-destructive/20"><div className="font-num text-3xl font-bold text-destructive">+8.8 pp</div><div className="text-[10px] uppercase tracking-witer text-muted-foreground">Membrane Integrity Gain</div></Card>
        <Card className="p-4 bg-secondary border-border"><div className="font-num text-3xl font-bold text-foreground">η² = 0.76</div><div className="text-[10px] uppercase tracking-witer text-muted-foreground">Largest Effect Size</div></Card>
      </div>

      <Card className="p-5 mb-6">
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-2">
            <TrendingUp className="h-4 w-4 text-primary" />
            <h3 className="font-heading text-sm font-bold text-primary">Treatment × Time — Toggle Between Endpoints</h3>
          </div>
          <div className="flex gap-1 p-1 bg-secondary rounded-md">
            {(Object.keys(viewConfig) as ViewType[]).map((v) => {
              const cfg = viewConfig[v];
              const Icon = cfg.icon;
              return (
                <button key={v} onClick={() => setView(v)} className={`flex items-center gap-1.5 px-3 py-1.5 rounded text-xs font-bold transition-all ${view === v ? "text-primary-foreground shadow-sm" : "text-muted-foreground hover:text-foreground"}`} style={view === v ? { backgroundColor: cfg.color } : {}}>
                  <Icon className="h-3 w-3" />{cfg.label}
                </button>
              );
            })}
          </div>
        </div>
        <div style={{ height: "340px" }}>
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={chartData} margin={{ top: 10, right: 30, left: 0, bottom: 20 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#D2CEC0" />
              <XAxis dataKey="time" stroke="#6B6B6B" fontSize={12} label={{ value: "Storage time at 4°C", position: "insideBottom", offset: -10, style: { fontSize: 11, fill: "#6B6B6B" } }} />
              <YAxis stroke="#6B6B6B" fontSize={11} domain={[40, 85]} label={{ value: chartTitle, angle: -90, position: "insideLeft", style: { fontSize: 11, fill: "#6B6B6B" } }} />
              <Tooltip contentStyle={{ backgroundColor: "#FBFAF7", border: "1px solid #D2CEC0", borderRadius: "8px", fontSize: "12px" }} labelStyle={{ color: "#2D5016", fontWeight: 700 }} />
              <Legend wrapperStyle={{ fontSize: 11 }} />
              <Line type="monotone" dataKey="control" name="DPPE-0 (Control)" stroke="#9C4942" strokeWidth={2} dot={{ r: 4 }} />
              <Line type="monotone" dataKey="dpp40" name="DPPE-40 (40 mg/mL)" stroke="#8B6914" strokeWidth={2} dot={{ r: 4 }} />
              <Line type="monotone" dataKey="dpp80" name="DPPE-80 (80 mg/mL)" stroke="#2D5016" strokeWidth={3} dot={{ r: 5 }} />
              <ReferenceDot x="48h" y={view === "total" ? 67.5 : view === "progressive" ? 54.7 : 63.9} r={8} fill="#2D5016" stroke="#FBFAF7" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
        </div>
        <div className="mt-3 p-3 bg-primary/5 rounded-md border border-primary/20">
          <p className="text-xs text-foreground"><strong className="text-primary">At 48h:</strong> DPPE-80 maintains <span className="font-num font-bold text-primary">{view === "total" ? "67.5%" : view === "progressive" ? "54.7%" : "63.9%"}</span> vs control <span className="font-num font-bold text-destructive">{view === "total" ? "58.3%" : view === "progressive" ? "45.5%" : "55.1%"}</span> — a <span className="font-num font-bold text-primary">+{gain48h} pp</span> advantage. The gap WIDENS over time, indicating sustained-release antioxidant mechanism.</p>
        </div>
      </Card>

      <Card className="p-5 mb-6">
        <div className="flex items-center justify-between mb-3">
          <h3 className="font-heading text-sm font-bold text-primary">Dose-Response at 48 Hours — Monotonic Improvement</h3>
          <Badge variant="outline" className="text-[10px] font-num text-primary border-primary/40">No plateau within tested range</Badge>
        </div>
        <div style={{ height: "260px" }}>
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={doseResponseData} margin={{ top: 10, right: 20, left: 0, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#D2CEC0" />
              <XAxis dataKey="dose" stroke="#6B6B6B" fontSize={11} />
              <YAxis stroke="#6B6B6B" fontSize={11} domain={[40, 75]} />
              <Tooltip contentStyle={{ backgroundColor: "#FBFAF7", border: "1px solid #D2CEC0", borderRadius: "8px", fontSize: "11px" }} />
              <Legend wrapperStyle={{ fontSize: 11 }} />
              <Bar dataKey="total" name="Total Motility (%)" radius={[3, 3, 0, 0]}>
                {doseResponseData.map((entry, i) => <Cell key={i} fill={entry.color} opacity={0.8} />)}
                <LabelList dataKey="total" position="top" style={{ fontSize: 10, fill: "#2D5016", fontWeight: 700 }} />
              </Bar>
              <Bar dataKey="progressive" name="Progressive Motility (%)" radius={[3, 3, 0, 0]} fill="#8B6914" />
              <Bar dataKey="host" name="Membrane Integrity (%)" radius={[3, 3, 0, 0]} fill="#9C4942" />
            </BarChart>
          </ResponsiveContainer>
        </div>
        <div className="mt-3 grid md:grid-cols-3 gap-2">
          {doseResponseData.map((d, i) => (
            <div key={i} className="p-2 rounded-md border-l-4" style={{ borderLeftColor: d.color, backgroundColor: `${d.color}08` }}>
              <div className="font-bold text-xs" style={{ color: d.color }}>{d.dose}</div>
              <div className="text-[10px] text-muted-foreground font-num">Total: {d.total}% · Prog: {d.progressive}% · HOST: {d.host}%</div>
            </div>
          ))}
        </div>
      </Card>

      <Card className="p-5 mb-6">
        <div className="flex items-center gap-2 mb-3">
          <Activity className="h-4 w-4 text-primary" />
          <h3 className="font-heading text-sm font-bold text-primary">Two-Way RM-ANOVA Summary — All Effects Large & Significant</h3>
        </div>
        <div className="overflow-x-auto">
          <table className="w-full text-xs">
            <thead>
              <tr className="bg-primary text-primary-foreground">
                <th className="text-left p-2">Parameter</th>
                <th className="p-2">Treatment F(2,8)</th>
                <th className="p-2">p</th>
                <th className="p-2">η²</th>
                <th className="p-2">Time F(2,8)</th>
                <th className="p-2">p</th>
                <th className="p-2">η²</th>
                <th className="p-2">Interaction p</th>
                <th className="p-2">η²</th>
              </tr>
            </thead>
            <tbody className="font-num">
              <tr className="border-b border-border"><td className="p-2 font-bold text-foreground">Total Motility</td><td className="p-2 text-center">12.42</td><td className="p-2 text-center text-primary">&lt;0.01**</td><td className="p-2 text-center font-bold text-primary">0.76</td><td className="p-2 text-center">89.34</td><td className="p-2 text-center">&lt;0.001***</td><td className="p-2 text-center font-bold">0.96</td><td className="p-2 text-center">0.024*</td><td className="p-2 text-center">0.49</td></tr>
              <tr className="border-b border-border bg-secondary/30"><td className="p-2 font-bold text-foreground">Progressive Motility</td><td className="p-2 text-center">11.85</td><td className="p-2 text-center text-primary">0.004**</td><td className="p-2 text-center font-bold text-primary">0.75</td><td className="p-2 text-center">76.21</td><td className="p-2 text-center">&lt;0.001***</td><td className="p-2 text-center font-bold">0.95</td><td className="p-2 text-center">0.018*</td><td className="p-2 text-center">0.51</td></tr>
              <tr><td className="p-2 font-bold text-foreground">Membrane Integrity</td><td className="p-2 text-center">10.32</td><td className="p-2 text-center text-primary">0.006**</td><td className="p-2 text-center font-bold text-primary">0.72</td><td className="p-2 text-center">82.15</td><td className="p-2 text-center">&lt;0.001***</td><td className="p-2 text-center font-bold">0.95</td><td className="p-2 text-center">0.031*</td><td className="p-2 text-center">0.47</td></tr>
            </tbody>
          </table>
        </div>
        <p className="text-[10px] text-muted-foreground mt-2 italic">* p&lt;0.05 · ** p&lt;0.01 · *** p&lt;0.001 — All treatment effects exceed η²&gt;0.70 (large effect threshold = 0.14). Bonferroni post-hoc confirms DPPE-80 ≠ Control at p&lt;0.05 for all parameters at 24h and 48h.</p>
      </Card>

      <Card className="p-5 mb-6 bg-gradient-to-br from-primary/10 to-accent/5 border-primary/30">
        <div className="flex items-center gap-2 mb-3">
          <Heart className="h-5 w-5 text-primary" />
          <h3 className="font-heading text-base font-bold text-primary">Biological Significance — Translating Motility to AI Doses</h3>
        </div>
        <div className="grid md:grid-cols-3 gap-4">
          <div className="text-center"><div className="font-num text-3xl font-bold text-primary">5–15 billion</div><div className="text-[10px] uppercase tracking-witer text-muted-foreground mt-1">Sperm recovered per ram</div><p className="text-[10px] text-foreground mt-1">From paired cauda epididymides</p></div>
          <div className="text-center"><div className="font-num text-3xl font-bold text-accent">+0.46–1.38 billion</div><div className="text-[10px] uppercase tracking-witer text-muted-foreground mt-1">Additional motile sperm</div><p className="text-[10px] text-foreground mt-1">9.2 pp × recovered cells</p></div>
          <div className="text-center"><div className="font-num text-3xl font-bold text-destructive">+2–14 doses</div><div className="text-[10px] uppercase tracking-witer text-muted-foreground mt-1">Additional AI doses per ram</div><p className="text-[10px] text-foreground mt-1">At 100–200M motile/dose</p></div>
        </div>
        <div className="mt-4 p-3 bg-background rounded-md border border-primary/20">
          <p className="text-xs text-foreground leading-relaxed"><strong className="text-primary">National scale projection:</strong> Algeria loses ~200,000 breeding rams annually to mortality. At DPPE-80 adoption, this represents <strong className="text-accent">0.5–4.2 million additional AI doses per year</strong> — genetic value that would otherwise be irreversibly lost.</p>
        </div>
      </Card>

      <SpeakerNotes notes={notes} defaultOpen={true} />
    </div>
  );
}
