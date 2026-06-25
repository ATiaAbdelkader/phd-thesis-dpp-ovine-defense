"use client";

import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Progress } from "@/components/ui/progress";
import { motion, AnimatePresence } from "framer-motion";
import {
  AlertTriangle,
  Truck,
  Beaker,
  Clock,
  Trophy,
  RotateCcw,
  CheckCircle2,
  ArrowRight,
  Heart,
  Activity,
  ShieldCheck,
} from "lucide-react";

type Transport = "fast" | "slow";
type Dose = 0 | 40 | 80;
type Storage = 0 | 24 | 48;
type Step = 0 | 1 | 2 | 3 | 4;

interface Outcome {
  motility: number;
  aiDoses: number;
  survivalProb: number;
  title: string;
  color: string;
}

const RESULTS: Record<string, Outcome> = {
  "fast-80-48h": { motility: 67.5, aiDoses: 11, survivalProb: 92, title: "Optimal Rescue", color: "#2D5016" },
  "fast-80-24h": { motility: 74.8, aiDoses: 12, survivalProb: 95, title: "Strong Early Rescue", color: "#5C8A3E" },
  "fast-80-0h": { motility: 80.2, aiDoses: 13, survivalProb: 97, title: "Emergency Use Only", color: "#5C8A3E" },
  "fast-40-48h": { motility: 63.1, aiDoses: 10, survivalProb: 78, title: "Suboptimal Dose", color: "#8B6914" },
  "fast-0-48h": { motility: 58.3, aiDoses: 9, survivalProb: 62, title: "Genetic Loss Risk", color: "#9C4942" },
  "slow-80-48h": { motility: 52.0, aiDoses: 8, survivalProb: 55, title: "Compromised Recovery", color: "#9C4942" },
  "slow-0-48h": { motility: 38.0, aiDoses: 5, survivalProb: 25, title: "Genetic Loss", color: "#9C4942" },
};

const DEFAULT_OUTCOME: Outcome = {
  motility: 55,
  aiDoses: 8,
  survivalProb: 60,
  title: "Intermediate Outcome",
  color: "#8B6914",
};

const TRANSPORT_OPTIONS: {
  id: Transport;
  label: string;
  detail: string;
  icon: typeof Truck;
  color: string;
}[] = [
  {
    id: "fast",
    label: "Rapid Transport",
    detail: "≤ 2h to lab · maintained at 4°C in cool box · cauda kept moist in saline",
    icon: Truck,
    color: "#2D5016",
  },
  {
    id: "slow",
    label: "Delayed Transport",
    detail: "> 4h to lab · ambient temperature exposure · tissue desiccation risk",
    icon: Truck,
    color: "#9C4942",
  },
];

const DOSE_OPTIONS: {
  id: Dose;
  label: string;
  detail: string;
  color: string;
  recommended?: boolean;
}[] = [
  { id: 0, label: "Control", detail: "No DPPE · standard saline extender only", color: "#9C4942" },
  { id: 40, label: "DPPE-40", detail: "40 mg/mL · partial protection", color: "#8B6914" },
  { id: 80, label: "DPPE-80", detail: "80 mg/mL · validated optimal dose", color: "#2D5016", recommended: true },
];

const STORAGE_OPTIONS: {
  id: Storage;
  label: string;
  detail: string;
  color: string;
}[] = [
  { id: 0, label: "0 hours", detail: "Immediate AI · minimal quality loss", color: "#5C8A3E" },
  { id: 24, label: "24 hours", detail: "Next-day AI · modest decline", color: "#8B6914" },
  { id: 48, label: "48 hours", detail: "Maximum window · significant decline without protectant", color: "#9C4942" },
];

const STEP_LABELS = ["Intro", "Transport", "Dose", "Storage", "Outcome"];

export default function RescueSimulatorScene() {
  const [step, setStep] = useState<Step>(0);
  const [transport, setTransport] = useState<Transport | null>(null);
  const [dose, setDose] = useState<Dose | null>(null);
  const [storage, setStorage] = useState<Storage | null>(null);

  const progressPct = (step / 4) * 100;

  const outcome: Outcome | null =
    step === 4 && transport && dose !== null && storage !== null
      ? RESULTS[`${transport}-${dose}-${storage}h`] ?? DEFAULT_OUTCOME
      : null;

  const reset = () => {
    setStep(0);
    setTransport(null);
    setDose(null);
    setStorage(null);
  };

  return (
    <div className="p-6 md:p-10 max-w-7xl mx-auto">
      <div className="mb-6">
        <div className="flex items-center gap-2 mb-2">
          <Badge variant="outline" className="text-accent border-accent/40 font-num">07 · RESCUE SIMULATOR</Badge>
          <Badge variant="secondary" className="text-[10px] gap-1"><Clock className="h-3 w-3" /> 48-hour decision game</Badge>
        </div>
        <h2 className="font-heading text-3xl md:text-4xl font-bold text-primary mb-2">The 48-Hour Genetic Rescue Game</h2>
        <p className="text-muted-foreground text-sm">
          A genetically elite ram has died. You have 48 hours to salvage his genome. Make the right calls at each
          step to maximize motility, AI doses, and the survival probability of his lineage.
        </p>
      </div>

      {/* ===== Progress bar ===== */}
      <Card className="p-4 mb-6">
        <div className="flex items-center justify-between mb-2">
          <div className="flex items-center gap-2">
            <span className="text-[10px] uppercase tracking-wider font-bold text-muted-foreground">Progress</span>
            <Badge variant="outline" className="text-[10px] font-num">
              Step {step + 1} / 5 · {STEP_LABELS[step]}
            </Badge>
          </div>
          <span className="font-num text-xs text-muted-foreground">{Math.round(progressPct)}%</span>
        </div>
        <Progress value={progressPct} />
        <div className="grid grid-cols-5 gap-1 mt-2">
          {STEP_LABELS.map((label, i) => (
            <div key={label} className="text-center">
              <div
                className={`h-1 rounded-full transition-all ${i <= step ? "bg-primary" : "bg-secondary"}`}
              />
              <div
                className={`text-[9px] uppercase tracking-wider mt-1 font-bold ${
                  i === step ? "text-primary" : i < step ? "text-foreground" : "text-muted-foreground"
                }`}
              >
                {label}
              </div>
            </div>
          ))}
        </div>
      </Card>

      {/* ===== Step content ===== */}
      <AnimatePresence mode="wait">
        {step === 0 && (
          <motion.div
            key="intro"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            transition={{ duration: 0.3 }}
          >
            <Card className="p-8 border-l-4 border-l-destructive">
              <div className="flex flex-col md:flex-row items-start gap-6">
                <div className="w-14 h-14 rounded-full bg-destructive/10 flex items-center justify-center flex-shrink-0">
                  <AlertTriangle className="h-7 w-7 text-destructive" />
                </div>
                <div className="flex-1">
                  <div className="text-[10px] uppercase tracking-wider font-bold text-destructive mb-1">
                    Mortality Event Detected
                  </div>
                  <h3 className="font-heading text-2xl font-bold text-foreground mb-3">
                    An elite Ouled Djellal ram has died of pneumonia in Djelfa.
                  </h3>
                  <p className="text-sm text-muted-foreground leading-relaxed mb-4">
                    You are the field veterinarian. Live semen collection is no longer possible — but the cauda
                    epididymides still contain 5–15 billion sperm within the 48-hour post-mortem viability window.
                    Every decision you make in the next 48 hours will determine how much of this ram&apos;s genome
                    reaches the next generation.
                  </p>
                  <div className="grid grid-cols-3 gap-3 mb-4">
                    <div className="bg-secondary/50 rounded-md p-3">
                      <div className="font-num text-xl font-bold text-primary">5–15B</div>
                      <div className="text-[10px] uppercase tracking-wider text-muted-foreground">sperm recoverable</div>
                    </div>
                    <div className="bg-secondary/50 rounded-md p-3">
                      <div className="font-num text-xl font-bold text-accent">48h</div>
                      <div className="text-[10px] uppercase tracking-wider text-muted-foreground">rescue window</div>
                    </div>
                    <div className="bg-secondary/50 rounded-md p-3">
                      <div className="font-num text-xl font-bold text-destructive">87.5%</div>
                      <div className="text-[10px] uppercase tracking-wider text-muted-foreground">published pregnancy rate</div>
                    </div>
                  </div>
                  <Button size="lg" onClick={() => setStep(1)} className="gap-2">
                    Begin the rescue <ArrowRight className="h-4 w-4" />
                  </Button>
                </div>
              </div>
            </Card>
          </motion.div>
        )}

        {step === 1 && (
          <motion.div
            key="transport"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            transition={{ duration: 0.3 }}
          >
            <Card className="p-6">
              <div className="flex items-center gap-2 mb-4">
                <Truck className="h-5 w-5 text-primary" />
                <h3 className="font-heading text-xl font-bold text-primary">Step 1 · Transport Decision</h3>
              </div>
              <p className="text-sm text-muted-foreground mb-4">
                How will you move the epididymides from the field to the lab?
              </p>
              <div className="grid md:grid-cols-2 gap-4 mb-4">
                {TRANSPORT_OPTIONS.map((opt) => {
                  const selected = transport === opt.id;
                  return (
                    <button
                      key={opt.id}
                      onClick={() => setTransport(opt.id)}
                      className={`text-left p-5 rounded-lg border-2 transition-all ${
                        selected ? "shadow-md" : "hover:border-primary/40 hover:bg-secondary/40"
                      }`}
                      style={selected ? { borderColor: opt.color, backgroundColor: `${opt.color}0D` } : { borderColor: "var(--border)" }}
                    >
                      <div className="flex items-center justify-between mb-2">
                        <div className="flex items-center gap-2">
                          <opt.icon className="h-5 w-5" style={{ color: opt.color }} />
                          <span className="font-heading text-base font-bold" style={{ color: opt.color }}>{opt.label}</span>
                        </div>
                        {selected && <CheckCircle2 className="h-5 w-5" style={{ color: opt.color }} />}
                      </div>
                      <p className="text-xs text-muted-foreground leading-relaxed">{opt.detail}</p>
                    </button>
                  );
                })}
              </div>
              <div className="flex justify-end">
                <Button disabled={!transport} onClick={() => setStep(2)} className="gap-2">
                  Continue <ArrowRight className="h-4 w-4" />
                </Button>
              </div>
            </Card>
          </motion.div>
        )}

        {step === 2 && (
          <motion.div
            key="dose"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            transition={{ duration: 0.3 }}
          >
            <Card className="p-6">
              <div className="flex items-center gap-2 mb-4">
                <Beaker className="h-5 w-5 text-primary" />
                <h3 className="font-heading text-xl font-bold text-primary">Step 2 · DPPE Dose Selection</h3>
              </div>
              <p className="text-sm text-muted-foreground mb-4">
                Choose the DPPE concentration to add to the extender.
              </p>
              <div className="grid md:grid-cols-3 gap-4 mb-4">
                {DOSE_OPTIONS.map((opt) => {
                  const selected = dose === opt.id;
                  return (
                    <button
                      key={opt.id}
                      onClick={() => setDose(opt.id)}
                      className={`text-left p-5 rounded-lg border-2 transition-all relative ${selected ? "shadow-md" : "hover:border-primary/40 hover:bg-secondary/40"}`}
                      style={selected ? { borderColor: opt.color, backgroundColor: `${opt.color}0D` } : { borderColor: "var(--border)" }}
                    >
                      {opt.recommended && (
                        <Badge className="absolute -top-2 right-3 text-[9px] bg-primary text-primary-foreground">
                          Recommended
                        </Badge>
                      )}
                      <div className="flex items-center justify-between mb-2">
                        <span className="font-heading text-base font-bold" style={{ color: opt.color }}>{opt.label}</span>
                        {selected && <CheckCircle2 className="h-5 w-5" style={{ color: opt.color }} />}
                      </div>
                      <p className="text-xs text-muted-foreground leading-relaxed">{opt.detail}</p>
                    </button>
                  );
                })}
              </div>
              <div className="flex justify-between">
                <Button variant="outline" onClick={() => setStep(1)}>Back</Button>
                <Button disabled={dose === null} onClick={() => setStep(3)} className="gap-2">
                  Continue <ArrowRight className="h-4 w-4" />
                </Button>
              </div>
            </Card>
          </motion.div>
        )}

        {step === 3 && (
          <motion.div
            key="storage"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            transition={{ duration: 0.3 }}
          >
            <Card className="p-6">
              <div className="flex items-center gap-2 mb-4">
                <Clock className="h-5 w-5 text-primary" />
                <h3 className="font-heading text-xl font-bold text-primary">Step 3 · Storage Duration</h3>
              </div>
              <p className="text-sm text-muted-foreground mb-4">
                How long will the extended semen be stored at 4°C before AI deployment?
              </p>
              <div className="grid md:grid-cols-3 gap-4 mb-4">
                {STORAGE_OPTIONS.map((opt) => {
                  const selected = storage === opt.id;
                  return (
                    <button
                      key={opt.id}
                      onClick={() => setStorage(opt.id)}
                      className={`text-left p-5 rounded-lg border-2 transition-all ${selected ? "shadow-md" : "hover:border-primary/40 hover:bg-secondary/40"}`}
                      style={selected ? { borderColor: opt.color, backgroundColor: `${opt.color}0D` } : { borderColor: "var(--border)" }}
                    >
                      <div className="flex items-center justify-between mb-2">
                        <span className="font-heading text-base font-bold" style={{ color: opt.color }}>{opt.label}</span>
                        {selected && <CheckCircle2 className="h-5 w-5" style={{ color: opt.color }} />}
                      </div>
                      <p className="text-xs text-muted-foreground leading-relaxed">{opt.detail}</p>
                    </button>
                  );
                })}
              </div>
              <div className="flex justify-between">
                <Button variant="outline" onClick={() => setStep(2)}>Back</Button>
                <Button disabled={storage === null} onClick={() => setStep(4)} className="gap-2">
                  Reveal outcome <Trophy className="h-4 w-4" />
                </Button>
              </div>
            </Card>
          </motion.div>
        )}

        {step === 4 && outcome && (
          <motion.div
            key="outcome"
            initial={{ opacity: 0, scale: 0.96 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.96 }}
            transition={{ duration: 0.35 }}
          >
            <Card className="p-6 border-l-4" style={{ borderLeftColor: outcome.color }}>
              <div className="flex flex-col md:flex-row items-start gap-6 mb-6">
                <div
                  className="w-14 h-14 rounded-full flex items-center justify-center flex-shrink-0"
                  style={{ backgroundColor: `${outcome.color}1A` }}
                >
                  <Trophy className="h-7 w-7" style={{ color: outcome.color }} />
                </div>
                <div className="flex-1">
                  <div className="text-[10px] uppercase tracking-wider font-bold mb-1" style={{ color: outcome.color }}>
                    Rescue outcome
                  </div>
                  <h3 className="font-heading text-2xl md:text-3xl font-bold mb-2" style={{ color: outcome.color }}>
                    {outcome.title}
                  </h3>
                  <div className="text-sm text-muted-foreground font-num">
                    {transport}-{dose}-{storage}h configuration
                  </div>
                </div>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                <motion.div
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.05 }}
                  className="rounded-lg p-5 border"
                  style={{ backgroundColor: `${outcome.color}08`, borderColor: `${outcome.color}33` }}
                >
                  <div className="flex items-center gap-2 mb-2">
                    <Activity className="h-4 w-4" style={{ color: outcome.color }} />
                    <span className="text-[10px] uppercase tracking-wider font-bold text-muted-foreground">Total Motility</span>
                  </div>
                  <div className="font-num text-4xl font-bold" style={{ color: outcome.color }}>
                    {outcome.motility.toFixed(1)}%
                  </div>
                  <div className="text-[10px] text-muted-foreground mt-1">predicted at storage end</div>
                </motion.div>

                <motion.div
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.15 }}
                  className="rounded-lg p-5 border"
                  style={{ backgroundColor: `${outcome.color}08`, borderColor: `${outcome.color}33` }}
                >
                  <div className="flex items-center gap-2 mb-2">
                    <Beaker className="h-4 w-4" style={{ color: outcome.color }} />
                    <span className="text-[10px] uppercase tracking-wider font-bold text-muted-foreground">AI Doses</span>
                  </div>
                  <div className="font-num text-4xl font-bold" style={{ color: outcome.color }}>
                    {outcome.aiDoses}
                  </div>
                  <div className="text-[10px] text-muted-foreground mt-1">@ 100–200M motile per dose</div>
                </motion.div>

                <motion.div
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.25 }}
                  className="rounded-lg p-5 border"
                  style={{ backgroundColor: `${outcome.color}08`, borderColor: `${outcome.color}33` }}
                >
                  <div className="flex items-center gap-2 mb-2">
                    <ShieldCheck className="h-4 w-4" style={{ color: outcome.color }} />
                    <span className="text-[10px] uppercase tracking-wider font-bold text-muted-foreground">Survival Probability</span>
                  </div>
                  <div className="font-num text-4xl font-bold" style={{ color: outcome.color }}>
                    {outcome.survivalProb}%
                  </div>
                  <div className="text-[10px] text-muted-foreground mt-1">genetic lineage preserved</div>
                </motion.div>
              </div>

              <Card className="p-4 bg-secondary/40 mb-4">
                <div className="text-[10px] uppercase tracking-wider font-bold text-muted-foreground mb-2">Decision recap</div>
                <div className="grid grid-cols-3 gap-2 text-xs">
                  <div>
                    <div className="text-muted-foreground">Transport</div>
                    <div className="font-bold text-foreground capitalize">{transport}</div>
                  </div>
                  <div>
                    <div className="text-muted-foreground">DPPE dose</div>
                    <div className="font-bold text-foreground">{dose} mg/mL</div>
                  </div>
                  <div>
                    <div className="text-muted-foreground">Storage</div>
                    <div className="font-bold text-foreground">{storage}h at 4°C</div>
                  </div>
                </div>
              </Card>

              <div className="flex gap-2 justify-end">
                <Button variant="outline" onClick={() => setStep(3)}>Back</Button>
                <Button onClick={reset} className="gap-2">
                  <RotateCcw className="h-4 w-4" /> Play again
                </Button>
              </div>
            </Card>
          </motion.div>
        )}
      </AnimatePresence>

      {/* ===== Outcomes legend (always visible) ===== */}
      <Card className="p-4 mt-6">
        <div className="flex items-center gap-2 mb-3">
          <Heart className="h-4 w-4 text-accent" />
          <span className="text-[10px] uppercase tracking-wider font-bold text-muted-foreground">
            All possible outcomes · try to find them all
          </span>
        </div>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-2">
          {Object.entries(RESULTS).map(([key, o]) => (
            <div
              key={key}
              className="p-2 rounded-md border-l-4 text-[10px]"
              style={{ borderLeftColor: o.color, backgroundColor: `${o.color}08` }}
            >
              <div className="font-bold text-foreground">{o.title}</div>
              <div className="text-muted-foreground font-num">{key}</div>
              <div className="text-muted-foreground font-num">motility {o.motility}% · {o.aiDoses} doses · {o.survivalProb}% survival</div>
            </div>
          ))}
          <div
            className="p-2 rounded-md border-l-4 text-[10px]"
            style={{ borderLeftColor: DEFAULT_OUTCOME.color, backgroundColor: `${DEFAULT_OUTCOME.color}08` }}
          >
            <div className="font-bold text-foreground">{DEFAULT_OUTCOME.title}</div>
            <div className="text-muted-foreground font-num">default (other combos)</div>
            <div className="text-muted-foreground font-num">motility {DEFAULT_OUTCOME.motility}% · {DEFAULT_OUTCOME.aiDoses} doses · {DEFAULT_OUTCOME.survivalProb}% survival</div>
          </div>
        </div>
      </Card>
    </div>
  );
}
