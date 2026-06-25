"use client";

import { useMemo, useState } from "react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Slider } from "@/components/ui/slider";
import { Button } from "@/components/ui/button";
import { RotateCcw, Scale, Microscope, Wrench, Users, CloudRain } from "lucide-react";
import { motion } from "framer-motion";
import {
  RadialBarChart,
  RadialBar,
  Legend,
  Tooltip,
  ResponsiveContainer,
  PolarAngleAxis,
} from "recharts";

interface Pillar {
  id: string;
  name: string;
  short: string;
  weight: number;
  default: number;
  color: string;
  icon: typeof Scale;
  desc: string;
}

const PILLARS: Pillar[] = [
  {
    id: "bio",
    name: "Biological Vulnerability",
    short: "V_bio",
    weight: 0.30,
    default: 55,
    color: "#9C4942",
    icon: Microscope,
    desc: "Genetic uniqueness, DHA-rich membrane exposure, breed endangerment status, post-mortem recoverability.",
  },
  {
    id: "tech",
    name: "Technical Capacity",
    short: "C_tech",
    weight: 0.25,
    default: 35,
    color: "#2D5016",
    icon: Wrench,
    desc: "Availability of preservation protocols, trained personnel, lab infrastructure, AI delivery systems.",
  },
  {
    id: "soc",
    name: "Socioeconomic Receptivity",
    short: "R_soc",
    weight: 0.25,
    default: 62,
    color: "#8B6914",
    icon: Users,
    desc: "Keeper awareness, cultural acceptance of AI, willingness to adopt new preservation tools.",
  },
  {
    id: "env",
    name: "Environmental Urgency",
    short: "U_env",
    weight: 0.20,
    default: 78,
    color: "#C4A858",
    icon: CloudRain,
    desc: "Climate stress exposure, drought frequency, heat-stress days, fertility decline trajectory.",
  },
];

interface Category {
  label: string;
  color: string;
  range: string;
}

function getCategory(score: number): Category {
  if (score >= 80) return { label: "Optimal", color: "#5C8A3E", range: "80–100" };
  if (score >= 60) return { label: "Active", color: "#8FB36B", range: "60–79" };
  if (score >= 40) return { label: "Emerging", color: "#C4A858", range: "40–59" };
  if (score >= 20) return { label: "Critical", color: "#8B6914", range: "20–39" };
  return { label: "Absent", color: "#9C4942", range: "0–19" };
}

const ALL_CATEGORIES = [
  { label: "Optimal", color: "#5C8A3E", range: "80–100" },
  { label: "Active", color: "#8FB36B", range: "60–79" },
  { label: "Emerging", color: "#C4A858", range: "40–59" },
  { label: "Critical", color: "#8B6914", range: "20–39" },
  { label: "Absent", color: "#9C4942", range: "0–19" },
];

export default function GHSICalculatorScene() {
  const [scores, setScores] = useState<Record<string, number>>(() =>
    Object.fromEntries(PILLARS.map((p) => [p.id, p.default])),
  );

  const ghsi = useMemo(
    () => PILLARS.reduce((sum, p) => sum + p.weight * scores[p.id], 0),
    [scores],
  );

  const category = getCategory(ghsi);

  const chartData = PILLARS.map((p) => ({
    name: p.short,
    fullName: p.name,
    value: scores[p.id],
    fill: p.color,
  }));

  const reset = () =>
    setScores(Object.fromEntries(PILLARS.map((p) => [p.id, p.default])));

  return (
    <div className="p-6 md:p-10 max-w-7xl mx-auto">
      <div className="mb-6">
        <div className="flex items-center gap-2 mb-2">
          <Badge variant="outline" className="text-accent border-accent/40 font-num">06 · GHSI CALCULATOR</Badge>
          <Badge variant="secondary" className="text-[10px] gap-1">
            <Scale className="h-3 w-3" /> Weighted composite index · 0–100
          </Badge>
        </div>
        <h2 className="font-heading text-3xl md:text-4xl font-bold text-primary mb-2">
          Genetic Heritage Stewardship Index
        </h2>
        <p className="text-muted-foreground text-sm">
          A composite index that triangulates biological, technical, socioeconomic and environmental dimensions
          of ovine genetic-heritage stewardship. Adjust each pillar to explore policy scenarios.
        </p>
      </div>

      <div className="grid lg:grid-cols-[1fr_1.2fr] gap-6 mb-6">
        {/* ===== Big GHSI score + chart ===== */}
        <Card className="p-6 flex flex-col items-center justify-center text-center">
          <div className="text-[10px] uppercase tracking-wider font-bold text-muted-foreground mb-2">
            Composite GHSI Score
          </div>
          <motion.div
            key={Math.round(ghsi)}
            initial={{ scale: 0.92, opacity: 0.5 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ type: "spring", stiffness: 220, damping: 20 }}
            className="font-num text-7xl md:text-8xl font-bold leading-none"
            style={{ color: category.color }}
          >
            {ghsi.toFixed(1)}
          </motion.div>
          <div className="text-[10px] text-muted-foreground font-num mt-1">out of 100</div>

          <motion.div
            key={category.label}
            initial={{ opacity: 0, y: 6 }}
            animate={{ opacity: 1, y: 0 }}
            className="mt-4 px-4 py-2 rounded-full font-bold text-sm"
            style={{ backgroundColor: `${category.color}1A`, color: category.color, border: `1px solid ${category.color}55` }}
          >
            {category.label} stewardship · {category.range}
          </motion.div>

          <div style={{ height: "240px", width: "100%" }} className="mt-4">
            <ResponsiveContainer width="100%" height="100%">
              <RadialBarChart
                cx="50%"
                cy="50%"
                innerRadius="25%"
                outerRadius="100%"
                barSize={11}
                data={chartData}
                startAngle={90}
                endAngle={-270}
              >
                <PolarAngleAxis type="number" domain={[0, 100]} tick={false} />
                <RadialBar background={{ fill: "#EFECE3" }} dataKey="value" cornerRadius={6} />
                <Legend
                  iconSize={10}
                  layout="vertical"
                  verticalAlign="middle"
                  align="right"
                  wrapperStyle={{ fontSize: 11, lineHeight: "20px" }}
                />
                <Tooltip
                  contentStyle={{ backgroundColor: "#FBFAF7", border: "1px solid #D2CEC0", borderRadius: "8px", fontSize: "11px" }}
                  formatter={(value: number, _name: string, props: { payload?: { fullName?: string } }) => [
                    `${value}/100`,
                    props?.payload?.fullName ?? "",
                  ]}
                />
              </RadialBarChart>
            </ResponsiveContainer>
          </div>
        </Card>

        {/* ===== Pillar sliders ===== */}
        <Card className="p-5">
          <div className="flex items-center justify-between mb-4">
            <h3 className="font-heading text-sm font-bold text-primary">Pillar Scores</h3>
            <Button variant="outline" size="sm" onClick={reset} className="gap-1.5">
              <RotateCcw className="h-3.5 w-3.5" /> Reset
            </Button>
          </div>

          <div className="space-y-5">
            {PILLARS.map((p) => {
              const Icon = p.icon;
              const v = scores[p.id];
              const contribution = (p.weight * v).toFixed(2);
              return (
                <div key={p.id}>
                  <div className="flex items-center justify-between mb-2">
                    <div className="flex items-center gap-2">
                      <div
                        className="w-7 h-7 rounded-md flex items-center justify-center"
                        style={{ backgroundColor: `${p.color}1A` }}
                      >
                        <Icon className="h-4 w-4" style={{ color: p.color }} />
                      </div>
                      <div>
                        <div className="text-xs font-bold text-foreground">{p.name}</div>
                        <div className="text-[10px] text-muted-foreground font-num">
                          weight {p.weight.toFixed(2)} · {p.short}
                        </div>
                      </div>
                    </div>
                    <div className="text-right">
                      <div className="font-num text-lg font-bold" style={{ color: p.color }}>{v}</div>
                      <div className="text-[10px] text-muted-foreground font-num">→ {contribution}</div>
                    </div>
                  </div>
                  <Slider
                    value={[v]}
                    min={0}
                    max={100}
                    step={1}
                    onValueChange={(val) => setScores((prev) => ({ ...prev, [p.id]: val[0] }))}
                    aria-label={p.name}
                  />
                  <p className="text-[10px] text-muted-foreground mt-1 leading-relaxed">{p.desc}</p>
                </div>
              );
            })}
          </div>
        </Card>
      </div>

      {/* ===== Formula display ===== */}
      <Card className="p-5 mb-6 bg-primary/5 border-primary/20">
        <div className="text-[10px] uppercase tracking-wider font-bold text-primary mb-2">Composite formula</div>
        <div className="font-num text-sm md:text-base text-foreground overflow-x-auto whitespace-nowrap">
          <span className="font-bold text-primary">GHSI</span> ={" "}
          <span className="text-[#9C4942]">0.30 × V_bio</span> +{" "}
          <span className="text-[#2D5016]">0.25 × C_tech</span> +{" "}
          <span className="text-[#8B6914]">0.25 × R_soc</span> +{" "}
          <span className="text-[#C4A858]">0.20 × U_env</span>
        </div>
        <div className="font-num text-xs md:text-sm text-muted-foreground mt-2">
          = 0.30 × {scores.bio} + 0.25 × {scores.tech} + 0.25 × {scores.soc} + 0.20 × {scores.env}
          {"  =  "}
          <span className="font-bold" style={{ color: category.color }}>{ghsi.toFixed(2)}</span>
          {"  →  "}
          <span className="font-bold" style={{ color: category.color }}>{category.label}</span>
        </div>
      </Card>

      {/* ===== Category scale ===== */}
      <Card className="p-5">
        <div className="text-[10px] uppercase tracking-wider font-bold text-muted-foreground mb-3">
          Stewardship category scale
        </div>
        <div className="grid grid-cols-2 md:grid-cols-5 gap-2">
          {ALL_CATEGORIES.map((c) => {
            const isActive = c.label === category.label;
            return (
              <motion.div
                key={c.label}
                animate={{ scale: isActive ? 1.04 : 1 }}
                className="p-3 rounded-md text-center border"
                style={{
                  backgroundColor: isActive ? `${c.color}1A` : "transparent",
                  borderColor: isActive ? c.color : "var(--border)",
                }}
              >
                <div className="font-num text-xs font-bold" style={{ color: c.color }}>{c.range}</div>
                <div className="text-xs font-bold text-foreground mt-1">{c.label}</div>
                {isActive && (
                  <div className="text-[9px] mt-1 font-bold" style={{ color: c.color }}>● current</div>
                )}
              </motion.div>
            );
          })}
        </div>
        <p className="text-[10px] text-muted-foreground mt-3 leading-relaxed">
          The El Oued baseline (default sliders) places the system in the <strong className="text-accent">Emerging</strong> band —
          high environmental urgency and socioeconomic receptivity are offset by low technical capacity.
          The DPPE protocol is designed to lift C_tech, pushing the composite into the <strong className="text-primary">Active</strong> band.
        </p>
      </Card>
    </div>
  );
}
