"use client";

import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Leaf, Zap, Shield, Atom, Beaker } from "lucide-react";
import { motion } from "framer-motion";

interface Bioactive {
  id: string;
  name: string;
  shortName: string;
  content: string;
  mechanism: string;
  target: string;
  color: string;
  icon: "leaf" | "zap" | "shield" | "atom" | "beaker";
}

const BIOACTIVES: Bioactive[] = [
  { id: "polyphenols", name: "Polyphenols", shortName: "Polyphenols", content: "12.85 mg GAE/g",
    mechanism: "Multi-target ROS scavenging — gallic acid (H-donation + Fe chelation), quercetin/rutin (mitochondrial targeting), caffeic acid (membrane interface)",
    target: "All cellular compartments", color: "#2D5016", icon: "leaf" },
  { id: "fatty-acids", name: "Fatty Acids", shortName: "Lipids", content: "4.32% w/w",
    mechanism: "Palmitic, linoleic, oleic acids provide membrane-stabilizing lipids. Linoleic acid supports membrane repair processes during chilled storage.",
    target: "Plasma membrane", color: "#5C8A3E", icon: "beaker" },
  { id: "minerals", name: "Minerals (Zn, Se, Cu)", shortName: "Minerals", content: "Zn 8.4 · Se 0.038 · Cu 1.12 mg/100g",
    mechanism: "Zn = SOD1 cofactor + protamine-2 chromatin stability. Se = GPx catalytic center. Cu = SOD1 + cytochrome c oxidase cofactor.",
    target: "Endogenous antioxidant enzymes", color: "#8B6914", icon: "atom" },
  { id: "vitamins", name: "Vitamins E + C", shortName: "Vitamins", content: "α-tocopherol 2.5–8.9 · Ascorbate 8.5–22.0 mg/100g",
    mechanism: "Synergistic pair: α-tocopherol scavenges peroxyl radicals in lipid membranes; ascorbate regenerates spent α-tocopherol at membrane-water interface.",
    target: "Membrane bilayer + aqueous phase", color: "#C4A858", icon: "shield" },
  { id: "amino-acids", name: "Amino Acids (Arginine)", shortName: "Amino Acids", content: "Protein 37.94%",
    mechanism: "Arginine = precursor for nitric oxide (NO) synthesis. NO at physiological concentrations regulates sperm capacitation and acrosome reaction.",
    target: "Sperm functional competence", color: "#9C4942", icon: "zap" },
];

const ROS_SOURCES = [
  { id: "mito", name: "Mitochondrial ROS", color: "#9C4942" },
  { id: "fenton", name: "Fenton Chemistry (OH•)", color: "#A85A3A" },
  { id: "enzymatic", name: "Enzymatic (XO, NADPHox)", color: "#8B6914" },
  { id: "lipid", name: "Lipid Peroxidation Chain", color: "#6B5530" },
];

const iconMap = { leaf: Leaf, zap: Zap, shield: Shield, atom: Atom, beaker: Beaker };

export default function InteractiveDPPMechanism() {
  const [selected, setSelected] = useState<Bioactive>(BIOACTIVES[0]);

  return (
    <div>
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <Leaf className="h-5 w-5 text-primary" />
          <h3 className="font-heading text-base font-bold text-primary">DPP Multi-Target Mechanism — Interactive Map</h3>
        </div>
        <Badge variant="secondary" className="text-[10px]">Click bioactive compounds to explore</Badge>
      </div>

      <div className="grid lg:grid-cols-3 gap-4 mb-4">
        <div className="space-y-2">
          <div className="text-[10px] uppercase tracking-wider text-accent font-bold mb-1">DPP Bioactive Compounds</div>
          {BIOACTIVES.map((b) => {
            const Icon = iconMap[b.icon];
            const isSelected = selected.id === b.id;
            return (
              <button
                key={b.id}
                onClick={() => setSelected(b)}
                className={`w-full text-left p-3 rounded-md border-2 transition-all flex items-center gap-3 ${isSelected ? "border-primary bg-primary/5 shadow-sm" : "border-border bg-secondary/30 hover:border-primary/40"}`}
                style={isSelected ? { borderColor: b.color, backgroundColor: `${b.color}10` } : {}}
              >
                <div className="w-9 h-9 rounded-md flex items-center justify-center flex-shrink-0" style={{ backgroundColor: `${b.color}20`, color: b.color }}>
                  <Icon className="h-4 w-4" />
                </div>
                <div className="flex-1 min-w-0">
                  <div className="text-sm font-bold text-foreground">{b.shortName}</div>
                  <div className="text-[10px] text-muted-foreground font-num">{b.content}</div>
                </div>
                {isSelected && <Badge className="text-[9px]" style={{ backgroundColor: b.color, color: "#FBFAF7" }}>Active</Badge>}
              </button>
            );
          })}
        </div>

        <div className="flex flex-col items-center justify-center min-h-[300px]">
          <motion.div key={selected.id} initial={{ scale: 0.8, opacity: 0 }} animate={{ scale: 1, opacity: 1 }} transition={{ duration: 0.3 }} className="text-center">
            <div className="w-24 h-24 rounded-full mx-auto mb-3 flex items-center justify-center shadow-lg" style={{ background: `linear-gradient(135deg, ${selected.color}, ${selected.color}cc)` }}>
              {(() => { const Icon = iconMap[selected.icon]; return <Icon className="h-10 w-10 text-white" />; })()}
            </div>
            <div className="font-heading text-sm font-bold text-foreground mb-1">{selected.name}</div>
            <div className="text-[10px] text-muted-foreground mb-3 font-num">{selected.content}</div>
            <svg width="120" height="60" className="mx-auto">
              <path d="M 10 10 Q 60 30, 110 50" stroke={selected.color} strokeWidth="2" strokeDasharray="4 4" fill="none" />
              <path d="M 100 45 L 110 50 L 105 40" stroke={selected.color} strokeWidth="2" fill="none" />
            </svg>
          </motion.div>
        </div>

        <div className="space-y-2">
          <div className="text-[10px] uppercase tracking-wider text-destructive font-bold mb-1">Multi-Source ROS Generation</div>
          {ROS_SOURCES.map((ros) => (
            <div key={ros.id} className="p-3 rounded-md border-2 border-border bg-secondary/30 transition-all" style={{ borderColor: `${ros.color}40` }}>
              <div className="flex items-center gap-2">
                <div className="w-2 h-2 rounded-full" style={{ backgroundColor: ros.color }} />
                <span className="text-xs font-bold text-foreground">{ros.name}</span>
              </div>
            </div>
          ))}
        </div>
      </div>

      <motion.div key={selected.id} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.3 }}>
        <Card className="p-5" style={{ borderLeft: `4px solid ${selected.color}` }}>
          <div className="grid md:grid-cols-2 gap-4">
            <div>
              <div className="text-[10px] uppercase tracking-wider font-bold mb-1" style={{ color: selected.color }}>Mechanism of Action</div>
              <p className="text-sm text-foreground leading-relaxed">{selected.mechanism}</p>
            </div>
            <div>
              <div className="text-[10px] uppercase tracking-wider font-bold mb-1" style={{ color: selected.color }}>Cellular Target</div>
              <p className="text-sm text-foreground leading-relaxed mb-3">{selected.target}</p>
              <div className="bg-secondary/50 rounded-md p-3">
                <div className="text-[10px] uppercase tracking-wider text-accent font-bold mb-1">Why This Matters</div>
                <p className="text-xs text-foreground leading-relaxed">Conventional single-mechanism antioxidants cannot address this combination of ROS sources and cellular compartments. DPP&apos;s multi-target action explains its biological efficacy despite lower per-mass DPPH potency.</p>
              </div>
            </div>
          </div>
        </Card>
      </motion.div>
    </div>
  );
}
