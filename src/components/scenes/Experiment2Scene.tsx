"use client";

import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Beaker, Atom, Zap, Target, FlaskConical, BarChart3 } from "lucide-react";
import { motion } from "framer-motion";
import SpeakerNotes, { SpeakerNote } from "@/components/SpeakerNotes";
import MethodologyTimeline from "@/components/MethodologyTimeline";
import { EXP2_METHODS } from "@/components/methodologyData";
import InteractiveDPPMechanism from "@/components/InteractiveDPPMechanism";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell, LineChart, Line, ReferenceLine, Legend } from "recharts";

const proximateData = [
  { component: "Protein", pct: 37.94, color: "#2D5016" },
  { component: "Carbohydrates", pct: 30.12, color: "#5C8A3E" },
  { component: "Fibre", pct: 12.99, color: "#8B6914" },
  { component: "Moisture", pct: 8.45, color: "#486C91" },
  { component: "Ash", pct: 6.18, color: "#C4A858" },
  { component: "Fat", pct: 4.32, color: "#9C4942" },
];

const mineralData = [
  { mineral: "Potassium (K)", value: 1140, color: "#2D5016", unit: "mg/100g", note: "Osmotic balance; enzyme cofactor" },
  { mineral: "Phosphorus (P)", value: 280, color: "#5C8A3E", unit: "mg/100g", note: "ATP synthesis; nucleic acid backbone" },
  { mineral: "Calcium (Ca)", value: 165, color: "#8B6914", unit: "mg/100g", note: "Sperm capacitation; acrosome reaction" },
  { mineral: "Magnesium (Mg)", value: 95, color: "#C4A858", unit: "mg/100g", note: "Enzyme cofactor; ATP stabilization" },
  { mineral: "Sodium (Na)", value: 38, color: "#486C91", unit: "mg/100g", note: "Osmotic balance; membrane potential" },
  { mineral: "Iron (Fe)", value: 12.5, color: "#9C4942", unit: "mg/100g", note: "Energy metabolism (requires chelation)" },
  { mineral: "Zinc (Zn)", value: 8.4, color: "#A85A3A", unit: "mg/100g", note: "SOD cofactor; chromatin stability" },
  { mineral: "Selenium (Se)", value: 0.038, color: "#6B5530", unit: "mg/100g", note: "GPx cofactor; DNA protection" },
];

const dpphData = [
  { conc: 0, dpp: 0, asc: 0 }, { conc: 50, dpp: 12.5, asc: 18.5 },
  { conc: 100, dpp: 23.8, asc: 34.2 }, { conc: 200, dpp: 41.2, asc: 56.8 },
  { conc: 400, dpp: 58.7, asc: 75.4 }, { conc: 600, dpp: 68.4, asc: 85.2 },
  { conc: 800, dpp: 75.1, asc: 91.5 }, { conc: 1000, dpp: 79.6, asc: 94.8 },
];

const notes: SpeakerNote[] = [
  { type: "key", text: "Open with: 'The question was whether locally-sourced DPP from Hamraia possesses the biochemical profile necessary for sperm cryoprotection. The answer is yes — and the profile is exceptional.'" },
  { type: "key", text: "Highlight protein 37.94% — exceeds the upper bound of the reported range (15.2–35.0% in literature). This is geographically-specific enrichment from the Hamraia source." },
  { type: "key", text: "Potassium 1140 mg/100g — reflects Saharan soil geochemistry. This is feature, not bug — aligns preservation medium with local agroecological context (agro-ecological cryobiology paradigm)." },
  { type: "key", text: "DPPH IC50 = 624.25 µg/mL appears WEAKER than ascorbic acid (145 µg/mL). Acknowledge this openly, then pivot: DPPH captures only aqueous-phase scavenging at one synthetic radical. DPP's multi-target action is biologically relevant, not chemically potent." },
  { type: "qa", text: "If asked 'Why use DPP if ascorbic acid is more potent?': Respond — 'Ascorbic acid is a single-mechanism aqueous scavenger. It cannot access the membrane interior where DHA peroxidation propagates in ram sperm. DPP's amphiphilic polyphenols integrate at the membrane interface. The biological efficacy is validated in Experiment 3 — that's the relevant metric.'" },
  { type: "transition", text: "Transition: 'Now that we've confirmed DPP has the right biochemical profile, the critical question is: does it actually preserve sperm quality? Let me show you the core experiment of this thesis.' → Move to Experiment 3." },
  { type: "timing", text: "Spend ~3-4 minutes. Don't get bogged down in methods — focus on the DPPH paradox (apparent weakness vs. biological strength) which is the key conceptual point." },
];

export default function Experiment2Scene() {
  const [selectedMineral, setSelectedMineral] = useState(mineralData[0]);
  const [mode, setMode] = useState<"methodology" | "results">("methodology");

  return (
    <div className="p-6 md:p-10 max-w-7xl mx-auto">
      <div className="mb-6">
        <div className="flex items-center gap-2 mb-2">
          <Badge variant="outline" className="text-accent border-accent/40 font-num">EXPERIMENT 02</Badge>
          <Badge variant="secondary" className="text-[10px] gap-1"><Beaker className="h-3 w-3" /> Hamraia DPP · triplicate</Badge>
        </div>
        <h2 className="font-heading text-3xl md:text-4xl font-bold text-primary mb-2">DPP Phytochemical Characterization</h2>
        <p className="text-muted-foreground text-sm">Biochemical composition and antioxidant capacity of El Oued Date Palm Pollen</p>
      </div>

      {/* Methodology / Results toggle */}
      <div className="flex gap-1 p-1 bg-secondary rounded-md mb-6 w-fit">
        <button
          onClick={() => setMode("methodology")}
          className={`flex items-center gap-1.5 px-4 py-2 rounded text-xs font-bold transition-all ${mode === "methodology" ? "bg-accent text-accent-foreground shadow-sm" : "text-muted-foreground"}`}
        >
          <FlaskConical className="h-3.5 w-3.5" />
          Methodology
        </button>
        <button
          onClick={() => setMode("results")}
          className={`flex items-center gap-1.5 px-4 py-2 rounded text-xs font-bold transition-all ${mode === "results" ? "bg-primary text-primary-foreground shadow-sm" : "text-muted-foreground"}`}
        >
          <BarChart3 className="h-3.5 w-3.5" />
          Results
        </button>
      </div>

      {/* METHODOLOGY VIEW */}
      {mode === "methodology" && (
        <Card className="p-6 mb-6">
          <div className="flex items-center gap-2 mb-4">
            <FlaskConical className="h-5 w-5 text-accent" />
            <h3 className="font-heading text-lg font-bold text-primary">Experiment 2 Methodology — Step by Step</h3>
          </div>
          <MethodologyTimeline steps={EXP2_METHODS} color="#2D5016" experimentTitle="DPP Characterization" />
          <div className="mt-6 flex justify-center">
            <button
              onClick={() => setMode("results")}
              className="flex items-center gap-2 px-6 py-3 rounded-lg bg-primary text-primary-foreground text-sm font-bold hover:bg-primary/90 transition-all"
            >
              <BarChart3 className="h-4 w-4" />
              Proceed to Results →
            </button>
          </div>
        </Card>
      )}

      {/* RESULTS VIEW */}
      {mode === "results" && (
        <>

      <Card className="p-4 mb-6 bg-accent/5 border-accent/30">
        <div className="flex items-start gap-3">
          <Target className="h-5 w-5 text-accent flex-shrink-0 mt-0.5" />
          <div>
            <div className="text-[10px] uppercase tracking-wider font-bold text-accent mb-1">Hypothesis Ha2 (Supported ✓)</div>
            <p className="text-sm text-foreground">El Oued-sourced DPP exhibits a nutrient-dense biochemical profile with measurable polyphenol content and DPPH radical scavenging activity. <span className="font-num font-bold text-accent">Protein 37.94% · K 1140 mg/100g · IC₅₀ = 624.25 µg/mL</span></p>
          </div>
        </div>
      </Card>

      <Card className="p-5 mb-6">
        <div className="flex items-center gap-2 mb-3">
          <FlaskConical className="h-4 w-4 text-primary" />
          <h3 className="font-heading text-sm font-bold text-primary">Proximate Composition (% w/w) — Click bars to explore</h3>
          <Badge variant="outline" className="ml-auto text-[10px] font-num text-primary border-primary/40">Protein exceeds reported range</Badge>
        </div>
        <div style={{ height: "240px" }}>
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={proximateData} layout="vertical" margin={{ top: 5, right: 30, left: 80, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#D2CEC0" horizontal={false} />
              <XAxis type="number" stroke="#6B6B6B" fontSize={11} unit="%" />
              <YAxis dataKey="component" type="category" stroke="#6B6B6B" fontSize={11} width={80} />
              <Tooltip contentStyle={{ backgroundColor: "#FBFAF7", border: "1px solid #D2CEC0", borderRadius: "8px", fontSize: "11px" }} />
              <Bar dataKey="pct" name="Composition (%)" radius={[0, 4, 4, 0]}>
                {proximateData.map((entry, i) => <Cell key={i} fill={entry.color} />)}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
        <div className="grid md:grid-cols-3 gap-3 mt-3">
          <div className="bg-primary/5 rounded-md p-3 border border-primary/20">
            <div className="font-num text-2xl font-bold text-primary">37.94%</div>
            <div className="text-[10px] uppercase tracking-wider text-muted-foreground">Protein</div>
            <p className="text-[10px] text-foreground mt-1">Exceeds range (15.2–35.0%) — cultivar-specific enrichment</p>
          </div>
          <div className="bg-accent/5 rounded-md p-3 border border-accent/20">
            <div className="font-num text-2xl font-bold text-accent">30.12%</div>
            <div className="text-[10px] uppercase tracking-wider text-muted-foreground">Carbohydrates</div>
            <p className="text-[10px] text-foreground mt-1">Energy substrates for sperm metabolism</p>
          </div>
          <div className="bg-destructive/5 rounded-md p-3 border border-destructive/20">
            <div className="font-num text-2xl font-bold text-destructive">4.32%</div>
            <div className="text-[10px] uppercase tracking-wider text-muted-foreground">Fat</div>
            <p className="text-[10px] text-foreground mt-1">Membrane-stabilizing lipids (palmitic, linoleic, oleic)</p>
          </div>
        </div>
      </Card>

      <Card className="p-5 mb-6">
        <div className="flex items-center gap-2 mb-3">
          <Atom className="h-4 w-4 text-primary" />
          <h3 className="font-heading text-sm font-bold text-primary">Mineral Content — Click bars to see reproductive relevance</h3>
        </div>
        <div className="grid md:grid-cols-2 gap-4">
          <div style={{ height: "280px" }}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={mineralData} margin={{ top: 5, right: 10, left: 0, bottom: 50 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#D2CEC0" />
                <XAxis dataKey="mineral" stroke="#6B6B6B" fontSize={10} angle={-40} textAnchor="end" height={60} />
                <YAxis stroke="#6B6B6B" fontSize={11} />
                <Tooltip contentStyle={{ backgroundColor: "#FBFAF7", border: "1px solid #D2CEC0", borderRadius: "8px", fontSize: "11px" }} cursor={{ fill: "#2D501610" }} />
                <Bar dataKey="value" name="Content (mg/100g)" radius={[3, 3, 0, 0]}>
                  {mineralData.map((entry, i) => (
                    <Cell key={i} fill={entry.color} opacity={selectedMineral.mineral === entry.mineral ? 1 : 0.4} onClick={() => setSelectedMineral(entry)} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
          <motion.div key={selectedMineral.mineral} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="bg-secondary/30 rounded-md p-4 border-l-4" style={{ borderLeftColor: selectedMineral.color }}>
            <div className="font-heading text-lg font-bold mb-1" style={{ color: selectedMineral.color }}>{selectedMineral.mineral}</div>
            <div className="font-num text-3xl font-bold mb-2" style={{ color: selectedMineral.color }}>{selectedMineral.value} <span className="text-sm">{selectedMineral.unit}</span></div>
            <div className="text-[10px] uppercase tracking-witer text-muted-foreground font-bold mb-1">Reproductive Relevance</div>
            <p className="text-xs text-foreground leading-relaxed">{selectedMineral.note}</p>
          </motion.div>
        </div>
      </Card>

      <Card className="p-5 mb-6">
        <div className="flex items-center justify-between mb-3">
          <div>
            <h3 className="font-heading text-sm font-bold text-primary">DPPH Radical Scavenging Activity</h3>
            <p className="text-[11px] text-muted-foreground">The apparent paradox — lower chemical potency, higher biological efficacy</p>
          </div>
          <div className="flex gap-2">
            <Badge className="bg-primary text-primary-foreground text-[10px] font-num">DPP IC₅₀ = 624.25 µg/mL</Badge>
            <Badge className="bg-accent text-accent-foreground text-[10px] font-num">Ascorbic IC₅₀ = 145.0 µg/mL</Badge>
          </div>
        </div>
        <div style={{ height: "260px" }}>
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={dpphData} margin={{ top: 5, right: 20, left: -20, bottom: 20 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#D2CEC0" />
              <XAxis dataKey="conc" stroke="#6B6B6B" fontSize={11} label={{ value: "Concentration (µg/mL)", position: "insideBottom", offset: -10, style: { fontSize: 11, fill: "#6B6B6B" } }} />
              <YAxis stroke="#6B6B6B" fontSize={11} label={{ value: "DPPH Inhibition (%)", angle: -90, position: "insideLeft", style: { fontSize: 11, fill: "#6B6B6B" } }} />
              <Tooltip contentStyle={{ backgroundColor: "#FBFAF7", border: "1px solid #D2CEC0", borderRadius: "8px", fontSize: "11px" }} />
              <Legend wrapperStyle={{ fontSize: 11 }} />
              <ReferenceLine y={50} stroke="#6B6B6B" strokeDasharray="3 3" label={{ value: "IC₅₀ (50%)", position: "right", style: { fontSize: 10, fill: "#6B6B6B" } }} />
              <Line type="monotone" dataKey="dpp" name="DPP extract" stroke="#2D5016" strokeWidth={2.5} dot={{ r: 4 }} />
              <Line type="monotone" dataKey="asc" name="Ascorbic acid (reference)" stroke="#8B6914" strokeWidth={2.5} dot={{ r: 4 }} />
            </LineChart>
          </ResponsiveContainer>
        </div>
        <div className="bg-accent/5 rounded-md p-4 mt-3 border border-accent/20">
          <div className="flex items-start gap-2">
            <Zap className="h-4 w-4 text-accent flex-shrink-0 mt-0.5" />
            <div>
              <div className="text-[10px] uppercase tracking-witer font-bold text-accent mb-1">The Multi-Target Advantage (apparent paradox explained)</div>
              <p className="text-xs text-foreground leading-relaxed">DPP is 4.3× less potent than ascorbic acid on per-mass DPPH basis. <strong>BUT</strong> the DPPH assay captures only aqueous-phase scavenging at one synthetic radical target. DPP provides 5 complementary actions that DPPH cannot measure: (1) membrane-integrating polyphenols, (2) mitochondrial-targeting flavonoids, (3) metal chelation preventing Fenton chemistry, (4) endogenous enzyme cofactor support (Zn→SOD, Se→GPx), (5) vitamin E + C synergistic regeneration. <strong className="text-primary">Biological efficacy (Experiment 3) is the relevant validation, not chemical potency.</strong></p>
            </div>
          </div>
        </div>
      </Card>

      <Card className="p-5 mb-6">
        <InteractiveDPPMechanism />
      </Card>

        </>
      )}

      <SpeakerNotes notes={notes} defaultOpen={false} />
    </div>
  );
}
