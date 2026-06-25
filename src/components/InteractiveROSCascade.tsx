"use client";

import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Zap, Clock, AlertTriangle } from "lucide-react";
import { motion } from "framer-motion";

interface Stage {
  id: number;
  time: string;
  title: string;
  description: string;
  consequence: string;
  color: string;
  icon: string;
}

const STAGES: Stage[] = [
  { id: 0, time: "T+0", title: "Somatic Death", description: "Cessation of systemic metabolic support. Oxygen delivery stops. ATP production halts.", consequence: "Cellular ischemia begins. The 48-hour countdown starts.", color: "#9C4942", icon: "☠" },
  { id: 1, time: "T+0 to 2h", title: "Ischemia & ATP Depletion", description: "Anaerobic glycolysis activated. Lactic acid accumulates. pH drops. ATP reserves exhausted within minutes.", consequence: "Ion pumps fail → ionic dysregulation → cellular swelling begins.", color: "#A85A3A", icon: "⚡" },
  { id: 2, time: "T+2 to 6h", title: "Mitochondrial ROS Generation", description: "Electron transport chain complexes I & III leak electrons to oxygen. Superoxide (O₂•⁻) production increases sharply.", consequence: "Mitochondrial membranes (PUFA-rich) become primary ROS targets.", color: "#8B6914", icon: "🔥" },
  { id: 3, time: "T+4 to 12h", title: "Fenton Chemistry", description: "Cellular compartmentalization breaks down. Free Fe²⁺ released from hemoglobin, myoglobin, iron-sulfur proteins. Fe²⁺ + H₂O₂ → OH• (hydroxyl radical).", consequence: "Hydroxyl radical initiates lipid peroxidation at diffusion-limited rates.", color: "#6B5530", icon: "⚠" },
  { id: 4, time: "T+6 to 24h", title: "Lipid Peroxidation", description: "Chain reaction propagates across DHA-rich membranes (30-40% of phospholipids). Malondialdehyde, 4-HNE produced. Membrane integrity lost.", consequence: "Motility lost. Membrane integrity lost. DNA damage accumulates. Irreversible.", color: "#4A3A1F", icon: "💀" },
];

const DOWNSTREAM = [
  { label: "Membrane Damage", color: "#9C4942" },
  { label: "Midpiece Degradation", color: "#A85A3A" },
  { label: "Axonemal Disruption", color: "#8B6914" },
  { label: "DNA Fragmentation", color: "#6B5530" },
  { label: "Fertilizing Capacity Loss", color: "#4A3A1F" },
];

export default function InteractiveROSCascade() {
  const [activeStage, setActiveStage] = useState(0);
  const stage = STAGES[activeStage];

  return (
    <div>
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-2">
          <Zap className="h-5 w-5 text-accent" />
          <h3 className="font-heading text-base font-bold text-primary">Post-Mortem Biochemical Cascade — Interactive</h3>
        </div>
        <Badge variant="secondary" className="text-[10px]">Click each stage to explore</Badge>
      </div>

      <div className="flex items-center gap-1 mb-6 overflow-x-auto pb-2">
        {STAGES.map((s, i) => (
          <div key={s.id} className="flex items-center flex-shrink-0">
            <button
              onClick={() => setActiveStage(s.id)}
              className={`flex flex-col items-center gap-1 p-3 rounded-lg border-2 transition-all min-w-[110px] ${
                activeStage === s.id ? "border-primary bg-primary/10 scale-105 shadow-md" : "border-border bg-secondary/50 hover:border-primary/40"
              }`}
              style={activeStage === s.id ? { borderColor: s.color, backgroundColor: `${s.color}10` } : {}}
            >
              <div className="w-10 h-10 rounded-full flex items-center justify-center text-xl" style={{ backgroundColor: `${s.color}20`, color: s.color }}>{s.icon}</div>
              <div className="font-num text-[10px] text-muted-foreground">{s.time}</div>
              <div className="text-[11px] font-bold text-foreground text-center leading-tight">{s.title}</div>
            </button>
            {i < STAGES.length - 1 && (
              <svg width="20" height="12" className="flex-shrink-0 text-muted-foreground">
                <path d="M2 6 L18 6 M14 2 L18 6 L14 10" stroke="currentColor" strokeWidth="1.5" fill="none" />
              </svg>
            )}
          </div>
        ))}
      </div>

      <motion.div key={activeStage} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.3 }} className="grid md:grid-cols-2 gap-4 mb-6">
        <Card className="p-5" style={{ borderLeft: `4px solid ${stage.color}` }}>
          <div className="flex items-center gap-2 mb-2">
            <span className="w-8 h-8 rounded-full flex items-center justify-center text-lg" style={{ backgroundColor: `${stage.color}20`, color: stage.color }}>{stage.icon}</span>
            <div>
              <div className="font-num text-[10px] text-muted-foreground">{stage.time}</div>
              <h4 className="font-heading text-lg font-bold" style={{ color: stage.color }}>{stage.title}</h4>
            </div>
          </div>
          <p className="text-sm text-foreground leading-relaxed mb-3">{stage.description}</p>
          <div className="bg-secondary/50 rounded-md p-3">
            <div className="text-[10px] uppercase tracking-wider text-muted-foreground font-bold mb-1">Consequence</div>
            <p className="text-xs text-foreground leading-relaxed">{stage.consequence}</p>
          </div>
        </Card>

        <Card className="p-5 bg-primary/5 border-primary/20">
          <div className="flex items-center gap-2 mb-3">
            <AlertTriangle className="h-4 w-4 text-primary" />
            <h4 className="font-heading text-sm font-bold text-primary">Downstream Cellular Consequences</h4>
          </div>
          <div className="space-y-1.5">
            {DOWNSTREAM.map((d, i) => {
              const isReached = i <= activeStage;
              return (
                <div key={i} className={`flex items-center gap-2 p-2 rounded-md transition-all ${isReached ? "bg-background opacity-100" : "opacity-30"}`} style={isReached ? { borderLeft: `3px solid ${d.color}` } : {}}>
                  <span className={`w-2 h-2 rounded-full ${isReached ? "" : "bg-muted-foreground"}`} style={isReached ? { backgroundColor: d.color } : {}} />
                  <span className="text-xs text-foreground font-medium">{d.label}</span>
                  {isReached && <Badge variant="outline" className="ml-auto text-[9px] font-num">Activated</Badge>}
                </div>
              );
            })}
          </div>
        </Card>
      </motion.div>

      <Card className="p-4 border-dashed border-2 border-primary/40 bg-primary/5">
        <div className="flex items-center gap-3">
          <Clock className="h-6 w-6 text-primary" />
          <div className="flex-1">
            <div className="font-heading text-sm font-bold text-primary">The Golden Hour Intervention Window (0–24h post-mortem)</div>
            <p className="text-xs text-foreground mt-0.5">Antioxidant supplementation during this window can partially mitigate oxidative damage before proteolytic and oxidative damage becomes irreversible. The DPPE protocol validated in this thesis extends effective preservation to 48 hours.</p>
          </div>
        </div>
      </Card>
    </div>
  );
}
