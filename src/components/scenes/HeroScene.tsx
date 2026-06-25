"use client";

import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Sparkles, ArrowRight, Atom, Clock, Activity, AlertTriangle, TrendingUp, Calculator, Timer, Cloud, Leaf } from "lucide-react";
import { motion } from "framer-motion";

export default function HeroScene({ onNext }: { onNext: () => void }) {
  return (
    <div className="min-h-[calc(100vh-104px)] flex items-center justify-center p-8 relative overflow-hidden">
      <div className="absolute inset-0 palm-pattern pointer-events-none" />
      <div className="absolute top-20 right-20 w-96 h-96 rounded-full bg-primary/5 blur-3xl float" />
      <div className="absolute bottom-20 left-20 w-72 h-72 rounded-full bg-accent/5 blur-3xl float" style={{ animationDelay: "1s" }} />

      <div className="relative z-10 max-w-6xl w-full">
        <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} className="text-center">
          <div className="flex items-center justify-center gap-2 mb-6">
            <div className="h-px w-12 bg-accent" />
            <Badge variant="outline" className="text-accent border-accent/40 font-num text-[10px] tracking-[0.2em] uppercase">Interactive PhD Defense · 2025–2026</Badge>
            <div className="h-px w-12 bg-accent" />
          </div>

          <p className="font-body text-xs text-muted-foreground uppercase tracking-[0.15em] mb-2">People's Democratic Republic of Algeria</p>
          <p className="font-body text-sm text-foreground/80 mb-8">[University Name] · Faculty of [Natural and Life Sciences]</p>

          <h1 className="font-heading text-4xl md:text-6xl lg:text-7xl font-bold text-primary leading-[1.05] mb-6 max-w-5xl mx-auto">
            Date Palm Pollen
            <span className="block text-accent text-2xl md:text-3xl lg:text-4xl font-normal italic mt-2">(Phoenix dactylifera L.)</span>
            <span className="block mt-3">as a Natural Cryoprotective Agent</span>
          </h1>

          <p className="font-heading text-lg md:text-xl text-foreground/80 italic max-w-3xl mx-auto mb-4 leading-relaxed">for Post-Slaughter Ovine Epididymal Sperm Preservation</p>
          <p className="font-body text-sm md:text-base text-muted-foreground max-w-2xl mx-auto mb-10">An Integrated Socio-Technical-Environmental Approach in Arid Algeria</p>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-3 max-w-4xl mx-auto mb-10">
            {[
              { value: "+9.2pp", label: "Motility gain", icon: Activity },
              { value: "OR 24.86", label: "Vulnerability", icon: AlertTriangle },
              { value: "48hr", label: "Rescue window", icon: Clock },
              { value: "22-44×", label: "Cost reduction", icon: TrendingUp },
            ].map((stat, i) => {
              const Icon = stat.icon;
              return (
                <motion.div key={i} initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.3 + i * 0.1 }}>
                  <Card className="p-4 hover-lift">
                    <Icon className="h-4 w-4 text-accent mx-auto mb-2" />
                    <div className="font-num text-2xl font-bold text-primary">{stat.value}</div>
                    <div className="text-[10px] text-muted-foreground uppercase tracking-wider mt-1">{stat.label}</div>
                  </Card>
                </motion.div>
              );
            })}
          </div>

          <div className="flex flex-wrap items-center justify-center gap-2 mb-10">
            <Badge variant="secondary" className="gap-1"><Sparkles className="h-3 w-3" /> Live Dose Mixer</Badge>
            <Badge variant="secondary" className="gap-1"><Atom className="h-3 w-3" /> 3D Sperm Model</Badge>
            <Badge variant="secondary" className="gap-1"><Calculator className="h-3 w-3" /> GHSI Calculator</Badge>
            <Badge variant="secondary" className="gap-1"><Timer className="h-3 w-3" /> Rescue Simulator</Badge>
            <Badge variant="secondary" className="gap-1"><Cloud className="h-3 w-3" /> Climate Sim</Badge>
          </div>

          <Button onClick={onNext} size="lg" className="bg-primary hover:bg-primary/90 text-primary-foreground gap-2 px-8 py-6 text-base font-num">
            Begin Defense
            <ArrowRight className="h-5 w-5" />
          </Button>

          <p className="font-body text-xs text-muted-foreground mt-6">Candidate: [Candidate Full Name] · Supervisor: Pr. [Supervisor Name] · Co-Supervisor: Dr. [Co-supervisor Name]</p>
        </motion.div>
      </div>
    </div>
  );
}
