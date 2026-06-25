"use client";

import Image from "next/image";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import {
  Quote,
  Users,
  Beaker,
  Globe2,
  Activity,
  Clock,
  TrendingUp,
  Target,
  Heart,
  Network,
} from "lucide-react";
import { motion } from "framer-motion";

const CONTRIBUTIONS = [
  {
    id: "field",
    title: "From Field Need",
    badge: "Experiments 1 + 4",
    icon: Users,
    color: "#8B6914",
    points: [
      "Surveyed 200 sheep keepers across 8 municipalities of El Oued",
      "Identified medium-flock vulnerability sweet spot (OR = 24.86)",
      "Documented 95% climate-fertility awareness + 41.5% adaptation gap",
      "Mapped trait preferences to conservation priorities",
    ],
  },
  {
    id: "tech",
    title: "To Technical Solution",
    badge: "Experiments 2 + 3",
    icon: Beaker,
    color: "#2D5016",
    points: [
      "Characterized Hamraia DPP — protein 37.94%, K 1140 mg/100g",
      "Validated DPPE-80: +9.2 pp total motility at 48h (η² = 0.76)",
      "Membrane integrity gain +8.8 pp — protects DHA-rich ram sperm",
      "Translated motility gain to +2–14 additional AI doses per ram",
    ],
  },
  {
    id: "framework",
    title: "To Conservation Framework",
    badge: "Triangulated model",
    icon: Network,
    color: "#9C4942",
    points: [
      "Proposed GHSI — weighted composite of 4 stewardship pillars",
      "Integrated biological, technical, socioeconomic, environmental axes",
      "Localized to arid agro-ecological context (El Oued, Algeria)",
      "Aligned with 7 SDGs and FAO Global Action Plan",
    ],
  },
];

const IMPACT_METRICS = [
  { value: "+9.2pp", label: "Motility gain (48h)", icon: Activity, color: "#2D5016" },
  { value: "48hr", label: "Genetic rescue window", icon: Clock, color: "#8B6914" },
  { value: "22–44×", label: "Cost reduction vs cryo", icon: TrendingUp, color: "#5C8A3E" },
  { value: "7", label: "SDGs aligned", icon: Target, color: "#9C4942" },
];

export default function ConclusionScene() {
  return (
    <div className="p-6 md:p-10 max-w-7xl mx-auto">
      <div className="mb-6">
        <div className="flex items-center gap-2 mb-2">
          <Badge variant="outline" className="text-accent border-accent/40 font-num">09 · CONCLUSION</Badge>
          <Badge variant="secondary" className="text-[10px] gap-1">
            <Heart className="h-3 w-3" /> Synthesis &amp; thanks
          </Badge>
        </div>
        <h2 className="font-heading text-3xl md:text-4xl font-bold text-primary mb-2">
          From Field Need to Conservation Framework
        </h2>
        <p className="text-muted-foreground text-sm">
          A bridge between the urgent need for ovine genetic conservation and the lack of accessible preservation
          technologies — grounded in the realities of the stakeholders it aims to serve.
        </p>
      </div>

      {/* ===== Closing quote ===== */}
      <Card className="p-6 md:p-8 mb-6 bg-primary/5 border-primary/20 relative overflow-hidden">
        <Quote className="absolute top-4 right-4 h-16 w-16 text-primary/10" />
        <div className="relative z-10">
          <div className="text-[10px] uppercase tracking-wider font-bold text-primary mb-3">
            Closing reflection
          </div>
          <p className="font-heading text-lg md:text-2xl text-foreground leading-relaxed italic">
            &ldquo;This thesis began by identifying a gap — the disconnect between urgent need for genetic
            conservation and lack of accessible preservation technologies. It ends by providing a bridge — a
            validated, low-cost, culturally acceptable protocol grounded in the realities of the stakeholders it
            aims to serve.&rdquo;
          </p>
        </div>
      </Card>

      {/* ===== Contribution cards ===== */}
      <div className="grid md:grid-cols-3 gap-4 mb-6">
        {CONTRIBUTIONS.map((c, i) => {
          const Icon = c.icon;
          return (
            <motion.div
              key={c.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.1 }}
            >
              <Card className="p-5 hover-lift h-full border-t-4" style={{ borderTopColor: c.color }}>
                <div className="flex items-center justify-between mb-3">
                  <div
                    className="w-10 h-10 rounded-md flex items-center justify-center"
                    style={{ backgroundColor: `${c.color}1A` }}
                  >
                    <Icon className="h-5 w-5" style={{ color: c.color }} />
                  </div>
                  <Badge variant="outline" className="text-[10px] font-num" style={{ color: c.color, borderColor: `${c.color}55` }}>
                    {c.badge}
                  </Badge>
                </div>
                <h3 className="font-heading text-lg font-bold mb-3" style={{ color: c.color }}>
                  {c.title}
                </h3>
                <ul className="space-y-2">
                  {c.points.map((p, j) => (
                    <li key={j} className="flex items-start gap-2 text-xs text-foreground leading-relaxed">
                      <span
                        className="w-1.5 h-1.5 rounded-full mt-1.5 flex-shrink-0"
                        style={{ backgroundColor: c.color }}
                      />
                      <span>{p}</span>
                    </li>
                  ))}
                </ul>
              </Card>
            </motion.div>
          );
        })}
      </div>

      {/* ===== Impact metrics ===== */}
      <Card className="p-5 mb-6">
        <div className="flex items-center gap-2 mb-4">
          <Target className="h-4 w-4 text-primary" />
          <h3 className="font-heading text-sm font-bold text-primary">Quantified Impact</h3>
        </div>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {IMPACT_METRICS.map((m, i) => {
            const Icon = m.icon;
            return (
              <motion.div
                key={m.label}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.08 }}
                className="text-center p-4 rounded-md border-l-4"
                style={{ borderLeftColor: m.color, backgroundColor: `${m.color}08` }}
              >
                <Icon className="h-5 w-5 mx-auto mb-2" style={{ color: m.color }} />
                <div className="font-num text-3xl font-bold" style={{ color: m.color }}>
                  {m.value}
                </div>
                <div className="text-[10px] uppercase tracking-wider text-muted-foreground mt-1">
                  {m.label}
                </div>
              </motion.div>
            );
          })}
        </div>
      </Card>

      {/* ===== Triangulated conservation model image ===== */}
      <Card className="p-5 mb-6">
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-2">
            <Globe2 className="h-4 w-4 text-primary" />
            <h3 className="font-heading text-sm font-bold text-primary">
              Triangulated Conservation Model
            </h3>
          </div>
          <Badge variant="outline" className="text-[10px] font-num text-accent border-accent/40">
            Figure 5.1
          </Badge>
        </div>
        <div className="relative w-full" style={{ aspectRatio: "16 / 9" }}>
          <Image
            src="/images/fig_5_1_conservation_model.png"
            alt="Triangulated conservation model integrating biological vulnerability, technical capacity, socioeconomic receptivity, and environmental urgency dimensions"
            fill
            sizes="(max-width: 768px) 100vw, 1200px"
            className="object-contain rounded-md"
          />
        </div>
        <p className="text-[10px] text-muted-foreground mt-2 italic leading-relaxed">
          The triangulated conservation model integrates biological vulnerability (DHA-rich membrane exposure,
          breed endangerment), technical capacity (DPPE protocol, lab infrastructure), socioeconomic receptivity
          (keeper awareness, cultural acceptance), and environmental urgency (climate stress, drought trajectory)
          into a single stewardship framework — operationalized through the GHSI calculator.
        </p>
      </Card>

      {/* ===== Final thank you card ===== */}
      <Card className="p-8 md:p-12 bg-primary text-primary-foreground border-primary">
        <div className="text-center">
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.6 }}
          >
            <div className="text-[10px] uppercase tracking-[0.3em] text-primary-foreground/70 mb-3">
              End of defense
            </div>
            <h3 className="font-heading text-5xl md:text-7xl font-bold mb-4 text-primary-foreground">
              Thank You
            </h3>
            <p className="font-heading text-2xl md:text-3xl italic text-primary-foreground/90 mb-2">
              Merci · شكراً · تشکر
            </p>
            <p className="text-sm text-primary-foreground/70 mb-8">
              For your attention, your questions, and your time.
            </p>

            <div className="h-px w-24 bg-primary-foreground/30 mx-auto mb-6" />

            <div className="space-y-1 text-primary-foreground/85">
              <p className="font-heading text-lg font-bold text-primary-foreground">
                [Candidate Full Name]
              </p>
              <p className="text-xs uppercase tracking-wider text-primary-foreground/70">
                PhD Candidate · Arid Lands Agriculture
              </p>
              <p className="text-xs text-primary-foreground/70 mt-3">
                Supervisor: Pr. [Supervisor Name] · Co-Supervisor: Dr. [Co-supervisor Name]
              </p>
              <p className="text-xs text-primary-foreground/70 mt-1">
                [University Name] · Faculty of Natural and Life Sciences · 2025–2026
              </p>
            </div>
          </motion.div>
        </div>
      </Card>
    </div>
  );
}
