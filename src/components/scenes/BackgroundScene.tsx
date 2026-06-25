"use client";

import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Leaf, AlertTriangle, Microscope } from "lucide-react";
import { motion } from "framer-motion";
import InteractiveROSCascade from "@/components/InteractiveROSCascade";

export default function BackgroundScene() {
  return (
    <div className="p-6 md:p-10 max-w-7xl mx-auto">
      <div className="mb-8">
        <Badge variant="outline" className="text-accent border-accent/40 mb-2 font-num">01 · BACKGROUND</Badge>
        <h2 className="font-heading text-3xl md:text-4xl font-bold text-primary mb-2">The Crisis & The Opportunity</h2>
        <p className="text-muted-foreground text-sm">Ovine genetic diversity under threat — and a botanical solution from the Algerian Sahara</p>
      </div>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
        {[
          { value: "1,300+", label: "Sheep breeds globally", color: "text-primary" },
          { value: "27%", label: "Endangered (FAO)", color: "text-destructive" },
          { value: "1/month", label: "Breed extinction rate", color: "text-destructive" },
          { value: "25M+", label: "Algerian sheep population", color: "text-accent" },
        ].map((stat, i) => (
          <motion.div key={i} initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: i * 0.1 }}>
            <Card className="p-5 hover-lift">
              <div className={`font-num text-3xl md:text-4xl font-bold ${stat.color}`}>{stat.value}</div>
              <div className="text-xs text-muted-foreground uppercase tracking-wider mt-1">{stat.label}</div>
            </Card>
          </motion.div>
        ))}
      </div>

      <div className="grid md:grid-cols-2 gap-6 mb-8">
        <Card className="p-6 border-l-4 border-l-destructive">
          <div className="flex items-center gap-2 mb-3">
            <AlertTriangle className="h-5 w-5 text-destructive" />
            <h3 className="font-heading text-xl font-bold text-foreground">The Genetic Emergency</h3>
          </div>
          <p className="text-sm text-muted-foreground mb-4 leading-relaxed">A genetically elite Ouled Djellal ram dies unexpectedly of pneumonia in Djelfa, Algeria. With live semen collection impossible, what genetic material can be salvaged?</p>
          <div className="space-y-2 text-sm">
            <div className="flex justify-between border-b border-border pb-2"><span className="text-muted-foreground">Sperm recoverable from cauda</span><span className="font-num font-bold text-foreground">5–15 billion</span></div>
            <div className="flex justify-between border-b border-border pb-2"><span className="text-muted-foreground">Post-mortem window</span><span className="font-num font-bold text-foreground">24–48 hours</span></div>
            <div className="flex justify-between"><span className="text-muted-foreground">Published pregnancy rate</span><span className="font-num font-bold text-foreground">87.5%</span></div>
          </div>
        </Card>

        <Card className="p-6 border-l-4 border-l-primary">
          <div className="flex items-center gap-2 mb-3">
            <Leaf className="h-5 w-5 text-primary" />
            <h3 className="font-heading text-xl font-bold text-foreground">The Botanical Solution</h3>
          </div>
          <p className="text-sm text-muted-foreground mb-4 leading-relaxed">Date Palm Pollen (<em>Phoenix dactylifera</em> L.) — a multi-target botanical matrix co-occurring geographically with sheep production in arid Algeria.</p>
          <div className="grid grid-cols-2 gap-2 text-xs">
            <div className="bg-secondary p-2 rounded"><div className="font-bold text-primary">Polyphenols</div><div className="text-muted-foreground">Multi-target ROS scavenging</div></div>
            <div className="bg-secondary p-2 rounded"><div className="font-bold text-primary">Minerals</div><div className="text-muted-foreground">Zn, Se — enzyme cofactors</div></div>
            <div className="bg-secondary p-2 rounded"><div className="font-bold text-primary">Vitamins</div><div className="text-muted-foreground">E + C synergistic pair</div></div>
            <div className="bg-secondary p-2 rounded"><div className="font-bold text-primary">Amino acids</div><div className="text-muted-foreground">Arginine → NO synthesis</div></div>
          </div>
        </Card>
      </div>

      <Card className="p-6 mb-6">
        <InteractiveROSCascade />
      </Card>

      <Card className="p-6 bg-primary/5 border-primary/20">
        <div className="flex items-center gap-2 mb-3">
          <Microscope className="h-5 w-5 text-primary" />
          <h3 className="font-heading text-xl font-bold text-primary">Ovine-Specific Vulnerability: DHA-Rich Membranes</h3>
        </div>
        <div className="grid md:grid-cols-3 gap-4">
          <div>
            <div className="font-num text-5xl font-bold text-primary">30–40%</div>
            <div className="text-xs text-muted-foreground uppercase tracking-wider mt-1">of ram sperm membrane phospholipids = DHA</div>
            <p className="text-xs text-muted-foreground mt-2">Highest among domestic livestock — essential for membrane fluidity but exceptionally vulnerable to peroxidation.</p>
          </div>
          <div>
            <div className="font-num text-5xl font-bold text-destructive">6</div>
            <div className="text-xs text-muted-foreground uppercase tracking-wider mt-1">double bonds in DHA molecule</div>
            <p className="text-xs text-muted-foreground mt-2">Five bis-allylic carbons = prime targets for radical attack. ~75 kJ/mol lower bond dissociation energy than mono-allylic.</p>
          </div>
          <div>
            <div className="font-num text-5xl font-bold text-accent">70–80</div>
            <div className="text-xs text-muted-foreground uppercase tracking-wider mt-1">mitochondria in sperm midpiece</div>
            <p className="text-xs text-muted-foreground mt-2">PUFA-rich mitochondrial membranes near electron transport chain = compounded oxidative vulnerability.</p>
          </div>
        </div>
      </Card>
    </div>
  );
}
