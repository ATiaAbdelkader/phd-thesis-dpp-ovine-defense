"use client";

import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Users, TrendingUp, Target, Brain, FlaskConical, BarChart3 } from "lucide-react";
import SpeakerNotes, { SpeakerNote } from "@/components/SpeakerNotes";
import MethodologyTimeline from "@/components/MethodologyTimeline";
import { EXP1_METHODS } from "@/components/methodologyData";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell, Legend, LineChart, Line } from "recharts";

const ageData = [{ age: "<25", pct: 11 }, { age: "25-35", pct: 24.5 }, { age: "36-45", pct: 28.5 }, { age: "46-55", pct: 22 }, { age: ">55", pct: 14 }];
const flockData = [
  { size: "<20 (Smallholder)", pct: 27, color: "#8B6914" },
  { size: "20-50 (Medium)", pct: 52.5, color: "#2D5016" },
  { size: "50-100 (Large)", pct: 14.5, color: "#5C8A3E" },
  { size: ">100 (Commercial)", pct: 6, color: "#9C4942" },
];
const traitData = [
  { trait: "Breed identity", ram: 27, ewe: 22 },
  { trait: "Body conformation", ram: 21.5, ewe: 16.5 },
  { trait: "Growth rate", ram: 18, ewe: 9.5 },
  { trait: "Drought tolerance", ram: 12.5, ewe: 16 },
  { trait: "Disease resistance", ram: 9, ewe: 11.5 },
  { trait: "Reproductive perf.", ram: 7, ewe: 17.5 },
  { trait: "Coat/wool quality", ram: 5, ewe: 7 },
];
const interactionData = [
  { experience: "Low (<5y)", "Full-time breeder": 3.2, "Breeder + farmer": 2.9, "Breeder + employee": 2.5 },
  { experience: "Medium (5-15y)", "Full-time breeder": 4.1, "Breeder + farmer": 3.4, "Breeder + employee": 2.8 },
  { experience: "High (>15y)", "Full-time breeder": 4.8, "Breeder + farmer": 3.9, "Breeder + employee": 3.1 },
];

const notes: SpeakerNote[] = [
  { type: "key", text: "Open with: 'Before we evaluate technical efficacy, we must understand who the conservation stakeholders are and what they value.' Emphasize the male-dominated (100%) aging demographic — only 11% under 25." },
  { type: "key", text: "Highlight the 79.5% of keepers with <50 head — this is not a commercial industry, it's a smallholder livelihood system. The DPPE protocol must be accessible to this demographic." },
  { type: "key", text: "Trait preferences reveal strategic resilience orientation: breed identity (27% rams) + drought tolerance (16% ewes) over rapid growth. This is rational adaptation to arid conditions." },
  { type: "key", text: "MANOVA result: η² = 0.070, p = 0.009. Explain that human capital variables operate SYNERGISTICALLY — highly educated, experienced, full-time breeders prioritize resilience traits." },
  { type: "qa", text: "If asked about generalizability: the 100% male sample reflects structural gender barriers in North African pastoral systems — a limitation, but it accurately represents the stakeholder group conservation programs must engage." },
  { type: "transition", text: "Transition: 'Now that we know who the stakeholders are and what they value, the next question is: does the local DPP resource actually possess the biochemical profile to serve as a preservation agent?' → Move to Experiment 2." },
  { type: "timing", text: "Spend ~3 minutes on this scene. Don't dwell on demographic details — focus on trait preferences and the MANOVA interaction, which are the most novel findings." },
];

export default function Experiment1Scene() {
  const [view, setView] = useState<"rams" | "ewes">("rams");
  const [mode, setMode] = useState<"methodology" | "results">("methodology");

  return (
    <div className="p-6 md:p-10 max-w-7xl mx-auto">
      <div className="mb-4">
        <div className="flex items-center gap-2 mb-2">
          <Badge variant="outline" className="text-accent border-accent/40 font-num">EXPERIMENT 01</Badge>
          <Badge variant="secondary" className="text-[10px] gap-1"><Users className="h-3 w-3" /> n=200 · 8 municipalities</Badge>
        </div>
        <h2 className="font-heading text-3xl md:text-4xl font-bold text-primary mb-2">Socioeconomic Context & Trait Preferences</h2>
        <p className="text-muted-foreground text-sm">Survey of 200 sheep keepers across El Oued region — establishing conservation priorities</p>
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
            <h3 className="font-heading text-lg font-bold text-primary">Experiment 1 Methodology — Step by Step</h3>
          </div>
          <MethodologyTimeline steps={EXP1_METHODS} color="#8B6914" experimentTitle="Socioeconomic Survey" />
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
            <div className="text-[10px] uppercase tracking-wider font-bold text-accent mb-1">Hypothesis Ha1 (Supported ✓)</div>
            <p className="text-sm text-foreground">Education, experience, and occupation interact significantly to shape trait preferences among El Oued sheep keepers. <span className="font-num font-bold text-accent">Pillai&apos;s Trace = 0.070 · p = 0.009 · η² = 0.070</span></p>
          </div>
        </div>
      </Card>

      <div className="grid md:grid-cols-2 gap-4 mb-6">
        <Card className="p-5">
          <div className="flex items-center gap-2 mb-3">
            <Users className="h-4 w-4 text-primary" />
            <h3 className="font-heading text-sm font-bold text-primary">Age Distribution</h3>
            <Badge variant="outline" className="ml-auto text-[10px] font-num text-destructive border-destructive/40">Only 11% &lt; 25 years</Badge>
          </div>
          <div style={{ height: "200px" }}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={ageData} margin={{ top: 5, right: 10, left: -20, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#D2CEC0" />
                <XAxis dataKey="age" stroke="#6B6B6B" fontSize={11} />
                <YAxis stroke="#6B6B6B" fontSize={11} />
                <Tooltip contentStyle={{ backgroundColor: "#FBFAF7", border: "1px solid #D2CEC0", borderRadius: "8px", fontSize: "11px" }} />
                <Bar dataKey="pct" name="Keepers (%)" radius={[4, 4, 0, 0]}>
                  {ageData.map((_, i) => <Cell key={i} fill={i === 0 ? "#9C4942" : "#8B6914"} />)}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
          <p className="text-[10px] text-muted-foreground mt-2 italic">Aging population — generational succession crisis</p>
        </Card>

        <Card className="p-5">
          <div className="flex items-center gap-2 mb-3">
            <TrendingUp className="h-4 w-4 text-primary" />
            <h3 className="font-heading text-sm font-bold text-primary">Flock Size Distribution</h3>
            <Badge variant="outline" className="ml-auto text-[10px] font-num text-primary border-primary/40">79.5% &lt; 50 head</Badge>
          </div>
          <div style={{ height: "200px" }}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={flockData} margin={{ top: 5, right: 10, left: -20, bottom: 0 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#D2CEC0" />
                <XAxis dataKey="size" stroke="#6B6B6B" fontSize={10} />
                <YAxis stroke="#6B6B6B" fontSize={11} />
                <Tooltip contentStyle={{ backgroundColor: "#FBFAF7", border: "1px solid #D2CEC0", borderRadius: "8px", fontSize: "11px" }} />
                <Bar dataKey="pct" name="Keepers (%)" radius={[4, 4, 0, 0]}>
                  {flockData.map((entry, i) => <Cell key={i} fill={entry.color} />)}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
          <p className="text-[10px] text-muted-foreground mt-2 italic">Medium flocks (20–50) = vulnerability sweet spot (OR=24.86 in Exp 4)</p>
        </Card>
      </div>

      <Card className="p-5 mb-6">
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-2">
            <Brain className="h-4 w-4 text-primary" />
            <h3 className="font-heading text-sm font-bold text-primary">Trait Preferences — Rams vs. Ewes</h3>
          </div>
          <div className="flex gap-1 p-1 bg-secondary rounded-md">
            <button onClick={() => setView("rams")} className={`px-3 py-1 rounded text-xs font-bold transition-all ${view === "rams" ? "bg-primary text-primary-foreground" : "text-muted-foreground"}`}>Rams</button>
            <button onClick={() => setView("ewes")} className={`px-3 py-1 rounded text-xs font-bold transition-all ${view === "ewes" ? "bg-accent text-accent-foreground" : "text-muted-foreground"}`}>Ewes</button>
          </div>
        </div>
        <div style={{ height: "280px" }}>
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={traitData} margin={{ top: 5, right: 10, left: -20, bottom: 30 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#D2CEC0" />
              <XAxis dataKey="trait" stroke="#6B6B6B" fontSize={10} angle={-25} textAnchor="end" height={60} />
              <YAxis stroke="#6B6B6B" fontSize={11} />
              <Tooltip contentStyle={{ backgroundColor: "#FBFAF7", border: "1px solid #D2CEC0", borderRadius: "8px", fontSize: "11px" }} />
              <Legend wrapperStyle={{ fontSize: 11 }} />
              <Bar dataKey="ram" name="Rams (%)" fill="#2D5016" radius={[3, 3, 0, 0]} />
              <Bar dataKey="ewe" name="Ewes (%)" fill="#8B6914" radius={[3, 3, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
        <div className="grid md:grid-cols-2 gap-3 mt-3">
          <div className="bg-primary/5 rounded-md p-3 border border-primary/20">
            <div className="text-[10px] uppercase tracking-wider font-bold text-primary mb-1">Rams Priority</div>
            <p className="text-xs text-foreground">Breed identity (27%) &gt; Body conformation (21.5%) &gt; Growth rate (18%) — keepers prioritize male breeding value signals.</p>
          </div>
          <div className="bg-accent/5 rounded-md p-3 border border-accent/20">
            <div className="text-[10px] uppercase tracking-witer font-bold text-accent mb-1">Ewes Priority</div>
            <p className="text-xs text-foreground">Breed identity (22%) &gt; Reproductive performance (17.5%) &gt; Drought tolerance (16%) — maternal traits dominate ewe selection.</p>
          </div>
        </div>
      </Card>

      <Card className="p-5 mb-6">
        <div className="flex items-center justify-between mb-3">
          <div>
            <h3 className="font-heading text-sm font-bold text-primary">MANOVA: Three-Way Interaction</h3>
            <p className="text-[11px] text-muted-foreground">Education × Experience × Occupation on adaptive trait priority</p>
          </div>
          <Badge className="bg-primary text-primary-foreground text-[10px] font-num">η² = 0.070 · p = 0.009**</Badge>
        </div>
        <div style={{ height: "280px" }}>
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={interactionData} margin={{ top: 5, right: 20, left: -20, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#D2CEC0" />
              <XAxis dataKey="experience" stroke="#6B6B6B" fontSize={11} />
              <YAxis stroke="#6B6B6B" fontSize={11} domain={[2, 5.5]} label={{ value: "Adaptive Trait Priority Score", angle: -90, position: "insideLeft", style: { fontSize: 10, fill: "#6B6B6B" } }} />
              <Tooltip contentStyle={{ backgroundColor: "#FBFAF7", border: "1px solid #D2CEC0", borderRadius: "8px", fontSize: "11px" }} />
              <Legend wrapperStyle={{ fontSize: 10 }} />
              <Line type="monotone" dataKey="Full-time breeder" stroke="#2D5016" strokeWidth={2.5} dot={{ r: 5 }} />
              <Line type="monotone" dataKey="Breeder + farmer" stroke="#8B6914" strokeWidth={2.5} dot={{ r: 5 }} />
              <Line type="monotone" dataKey="Breeder + employee" stroke="#9C4942" strokeWidth={2.5} dot={{ r: 5 }} />
            </LineChart>
          </ResponsiveContainer>
        </div>
        <div className="bg-primary/5 rounded-md p-3 mt-3 border border-primary/20">
          <div className="text-[10px] uppercase tracking-witer font-bold text-primary mb-1">Interpretation</div>
          <p className="text-xs text-foreground leading-relaxed">Highly educated, experienced, full-time breeders prioritize long-term resilience traits (drought tolerance, disease resistance, breed identity). Less experienced keepers and those with secondary occupations focus on visible morphological attributes (body conformation, coat quality). <strong className="text-primary">Conservation interventions should target full-time breeders with substantial experience as the most receptive audience.</strong></p>
        </div>
      </Card>

        </>
      )}

      <SpeakerNotes notes={notes} defaultOpen={false} />
    </div>
  );
}
