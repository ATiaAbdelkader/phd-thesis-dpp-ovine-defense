"use client";

import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Users, Beaker, Microscope, Cloud, ArrowRight, CheckCircle2, Sparkles, Network } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

interface Connection {
  from: string;
  to: string;
  label: string;
  detail: string;
}

const CONNECTIONS: Connection[] = [
  { from: "exp1", to: "exp2", label: "Field need → Solution validation", detail: "Experiment 1 identified that keepers prioritize breed identity (27%) and drought tolerance (16%) — confirming the need for genetic conservation tools. Experiment 2 validated that locally-available DPP possesses the biochemical profile to serve as that tool." },
  { from: "exp2", to: "exp3", label: "Composition → Efficacy", detail: "Experiment 2 characterized DPP's multi-target matrix (protein 37.94%, K 1140mg/100g, IC₅₀ 624.25 µg/mL). Experiment 3 tested whether this composition actually preserves sperm — translating biochemistry into functional efficacy." },
  { from: "exp3", to: "exp4", label: "Technical → Urgency", detail: "Experiment 3 validated the DPPE protocol (+9.2pp motility at 48h). Experiment 4 documented WHY this matters: 95% climate-fertility awareness, 78.5% perceived decline, medium flocks at OR=24.86 vulnerability — elevating conservation from technical possibility to urgent imperative." },
  { from: "exp1", to: "exp4", label: "Same cohort → Triangulation", detail: "Experiments 1 and 4 used the same 200-keeper cohort, enabling direct correlation between socioeconomic profile and climate perceptions. The medium-flock vulnerability sweet spot (Exp 4) aligns with the 52.5% of keepers in the medium category (Exp 1) — the exact demographic DPPE should target." },
  { from: "exp4", to: "exp1", label: "Urgency → Targeting", detail: "Experiment 4 identified medium flocks as the vulnerability sweet spot. Experiment 1 showed these keepers prioritize breed identity and drought tolerance. Together: DPPE deployment should target full-time breeders with medium flocks who value adaptive traits — the most receptive AND most vulnerable demographic." },
];

const EXPERIMENT_NODES = [
  { id: "exp1", num: "01", title: "Socioeconomic Survey", icon: Users, color: "#8B6914", x: 15, y: 20, finding: "Keepers prioritize breed identity (27%) + drought tolerance (16%)" },
  { id: "exp2", num: "02", title: "DPP Characterization", icon: Beaker, color: "#2D5016", x: 70, y: 20, finding: "Protein 37.94% · K 1140mg/100g · IC₅₀ 624.25 µg/mL" },
  { id: "exp3", num: "03", title: "Sperm Preservation", icon: Microscope, color: "#2D5016", x: 70, y: 65, finding: "+9.2pp motility · η²=0.76 · dose-dependent protection" },
  { id: "exp4", num: "04", title: "Climate Perceptions", icon: Cloud, color: "#9C4942", x: 15, y: 65, finding: "95% awareness · OR=24.86 (medium flocks) · vulnerability sweet spot" },
];

export default function InterconnectionScene() {
  const [selectedConnection, setSelectedConnection] = useState<Connection | null>(null);
  const [showAll, setShowAll] = useState(false);

  return (
    <div className="p-6 md:p-10 max-w-7xl mx-auto">
      <div className="mb-6">
        <div className="flex items-center gap-2 mb-2">
          <Badge variant="outline" className="text-accent border-accent/40 font-num">
            INTERCONNECTION
          </Badge>
          <Badge variant="secondary" className="text-[10px] gap-1">
            <Network className="h-3 w-3" /> 4 experiments · 5 connections
          </Badge>
        </div>
        <h2 className="font-heading text-3xl md:text-4xl font-bold text-primary mb-2">
          How the Four Experiments Connect
        </h2>
        <p className="text-muted-foreground text-sm">
          The triangulated design — each experiment informs and is informed by the others. Click each connection to explore.
        </p>
      </div>

      {/* Interactive network diagram */}
      <Card className="p-6 mb-6">
        <div className="relative" style={{ height: "400px" }}>
          {/* SVG connections */}
          <svg className="absolute inset-0 w-full h-full" style={{ zIndex: 1 }}>
            {CONNECTIONS.map((conn, i) => {
              const fromNode = EXPERIMENT_NODES.find(n => n.id === conn.from)!;
              const toNode = EXPERIMENT_NODES.find(n => n.id === conn.to)!;
              const isActive = selectedConnection === conn;
              return (
                <line
                  key={i}
                  x1={`${fromNode.x + 10}%`}
                  y1={`${fromNode.y + 10}%`}
                  x2={`${toNode.x + 10}%`}
                  y2={`${toNode.y + 10}%`}
                  stroke={isActive ? "#8B6914" : "#D2CEC0"}
                  strokeWidth={isActive ? 3 : 1.5}
                  strokeDasharray={isActive ? "0" : "5 5"}
                  style={{ cursor: "pointer", transition: "all 0.3s" }}
                  onClick={() => setSelectedConnection(conn)}
                />
              );
            })}
          </svg>

          {/* Experiment nodes */}
          {EXPERIMENT_NODES.map((node) => {
            const Icon = node.icon;
            return (
              <div
                key={node.id}
                className="absolute"
                style={{
                  left: `${node.x}%`,
                  top: `${node.y}%`,
                  width: "20%",
                  zIndex: 2,
                }}
              >
                <motion.div
                  initial={{ scale: 0, opacity: 0 }}
                  animate={{ scale: 1, opacity: 1 }}
                  transition={{ delay: 0.2 }}
                >
                  <Card
                    className="p-3 text-center hover-lift cursor-pointer"
                    style={{ borderLeft: `4px solid ${node.color}` }}
                  >
                    <div
                      className="w-10 h-10 rounded-lg flex items-center justify-center mx-auto mb-1"
                      style={{ backgroundColor: `${node.color}20` }}
                    >
                      <Icon className="h-5 w-5" style={{ color: node.color }} />
                    </div>
                    <div className="font-num text-[10px] font-bold" style={{ color: node.color }}>
                      EXP {node.num}
                    </div>
                    <div className="text-[11px] font-bold text-foreground leading-tight">
                      {node.title}
                    </div>
                    <div className="text-[9px] text-muted-foreground mt-1 leading-tight">
                      {node.finding}
                    </div>
                  </Card>
                </motion.div>
              </div>
            );
          })}
        </div>
      </Card>

      {/* Connection selector buttons */}
      <div className="grid md:grid-cols-5 gap-2 mb-6">
        {CONNECTIONS.map((conn, i) => {
          const isActive = selectedConnection === conn;
          return (
            <button
              key={i}
              onClick={() => setSelectedConnection(conn)}
              className={`p-2 rounded-md border-2 text-left transition-all ${
                isActive ? "border-accent bg-accent/5" : "border-border hover:border-accent/40"
              }`}
            >
              <div className="text-[10px] font-bold text-accent mb-0.5">
                {conn.from.replace("exp", "Exp ")} → {conn.to.replace("exp", "Exp ")}
              </div>
              <div className="text-[10px] text-foreground leading-tight">
                {conn.label}
              </div>
            </button>
          );
        })}
      </div>

      {/* Selected connection detail */}
      <AnimatePresence mode="wait">
        {selectedConnection && (
          <motion.div
            key={selectedConnection.label}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
          >
            <Card className="p-5 border-l-4 border-l-accent">
              <div className="flex items-center gap-2 mb-2">
                <ArrowRight className="h-4 w-4 text-accent" />
                <span className="text-xs font-bold uppercase tracking-wider text-accent">
                  {selectedConnection.from.replace("exp", "Experiment ")} → {selectedConnection.to.replace("exp", "Experiment ")}
                </span>
              </div>
              <h4 className="font-heading text-lg font-bold text-primary mb-2">
                {selectedConnection.label}
              </h4>
              <p className="text-sm text-foreground leading-relaxed">
                {selectedConnection.detail}
              </p>
            </Card>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Convergence summary */}
      <Card className="p-6 bg-gradient-to-br from-primary/10 to-accent/5 border-primary/30">
        <div className="flex items-center gap-2 mb-3">
          <Sparkles className="h-5 w-5 text-primary" />
          <h3 className="font-heading text-lg font-bold text-primary">
            The Triangulated Conservation Model
          </h3>
        </div>
        <p className="text-sm text-foreground leading-relaxed mb-4">
          All four experiments converge on a single, unified framework. No single experiment
          could produce this insight alone — it is the <strong>interconnection</strong> that
          creates the theoretical contribution.
        </p>
        <div className="grid md:grid-cols-3 gap-3">
          <div className="bg-background rounded-md p-3 border border-primary/20">
            <div className="text-[10px] uppercase tracking-wider font-bold text-primary mb-1">
              Socioeconomic (Exp 1+4)
            </div>
            <p className="text-xs text-foreground">
              Keepers prioritize resilience traits AND perceive climate urgency. Target: full-time
              breeders with medium flocks (20-50 head).
            </p>
          </div>
          <div className="bg-background rounded-md p-3 border border-accent/20">
            <div className="text-[10px] uppercase tracking-wider font-bold text-accent mb-1">
              Technical (Exp 2+3)
            </div>
            <p className="text-xs text-foreground">
              Local DPP has the biochemistry (Exp 2) AND preserves sperm quality (Exp 3).
              Protocol: DPPE-80 mg/mL, 48h chilled storage, +9.2pp motility advantage.
            </p>
          </div>
          <div className="bg-background rounded-md p-3 border border-destructive/20">
            <div className="text-[10px] uppercase tracking-witer font-bold text-destructive mb-1">
              Convergence
            </div>
            <p className="text-xs text-foreground">
              The right technical solution (DPPE) for the right demographic (medium-flock
              breeders) at the right time (climate urgency) = sustainable genetic rescue.
            </p>
          </div>
        </div>
        <div className="mt-4 flex items-center justify-center gap-2">
          <CheckCircle2 className="h-5 w-5 text-primary" />
          <span className="font-heading text-base font-bold text-primary">
            4/4 Hypotheses Supported → Triangulated Model Validated
          </span>
        </div>
      </Card>
    </div>
  );
}
