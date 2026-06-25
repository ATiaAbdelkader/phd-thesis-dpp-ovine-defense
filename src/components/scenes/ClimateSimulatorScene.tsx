"use client";

import { useMemo, useState } from "react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Slider } from "@/components/ui/slider";
import { Button } from "@/components/ui/button";
import { Sun, CloudRain, RotateCcw, TrendingDown, Gauge } from "lucide-react";
import { motion } from "framer-motion";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
  Cell,
  LabelList,
} from "recharts";

/* ============================================================
   Baseline climate (El Oued today) & flock-size vulnerabilities
   ============================================================ */
const BASELINE_HEAT = 60; // days/year
const BASELINE_RAIN = 50; // mm deficit
const BASE_MEDIUM_OR = 24.86;

type FlockId = "small" | "medium" | "large" | "commercial";

const FLOCKS: { id: FlockId; label: string; baselineProb: number; color: string }[] = [
  { id: "small", label: "Small (<20)", baselineProb: 0.65, color: "#8B6914" },
  { id: "medium", label: "Medium (20–50)", baselineProb: 0.785, color: "#2D5016" },
  { id: "large", label: "Large (50–100)", baselineProb: 0.55, color: "#5C8A3E" },
  { id: "commercial", label: "Commercial (>100)", baselineProb: 0.35, color: "#9C4942" },
];

const SCENARIOS: {
  name: string;
  heat: number;
  rain: number;
  color: string;
  desc: string;
}[] = [
  { name: "Current El Oued", heat: 60, rain: 50, color: "#2D5016", desc: "Baseline 2024 conditions" },
  { name: "+2°C warming", heat: 85, rain: 80, color: "#8B6914", desc: "Mid-century projection" },
  { name: "Severe drought", heat: 100, rain: 120, color: "#9C4942", desc: "Worst-case 2050" },
  { name: "Optimistic 2030", heat: 50, rain: 30, color: "#5C8A3E", desc: "Aggressive adaptation" },
];

function cap99(v: number): number {
  return Math.min(99, Math.max(0, v));
}

export default function ClimateSimulatorScene() {
  const [heat, setHeat] = useState(60);
  const [rain, setRain] = useState(50);

  // Multipliers — baseline = 1.0
  const heatMultiplier = heat / BASELINE_HEAT;
  const rainMultiplier = rain / BASELINE_RAIN;

  // Medium-flock OR
  const mediumOR = BASE_MEDIUM_OR * heatMultiplier * rainMultiplier;

  // Per-flock projected fertility decline (%)
  // Climate factor = average of the two ratios; sublinear scaling to avoid trivial saturation
  const climateFactor = (heatMultiplier + rainMultiplier) / 2;
  const declineScale = 0.5 + 0.5 * climateFactor;

  const chartData = useMemo(
    () =>
      FLOCKS.map((f) => {
        const baselinePct = f.baselineProb * 100;
        const projectedPct = cap99(baselinePct * declineScale);
        return {
          flock: f.label,
          baseline: Number(baselinePct.toFixed(1)),
          projected: Number(projectedPct.toFixed(1)),
          color: f.color,
          delta: Number((projectedPct - baselinePct).toFixed(1)),
        };
      }),
    [declineScale],
  );

  const reset = () => {
    setHeat(60);
    setRain(50);
  };

  const matchedScenario = SCENARIOS.find((s) => s.heat === heat && s.rain === rain);

  return (
    <div className="p-6 md:p-10 max-w-7xl mx-auto">
      <div className="mb-6">
        <div className="flex items-center gap-2 mb-2">
          <Badge variant="outline" className="text-accent border-accent/40 font-num">08 · CLIMATE SIMULATOR</Badge>
          <Badge variant="secondary" className="text-[10px] gap-1">
            <TrendingDown className="h-3 w-3" /> Logistic model · Exp 4 baseline
          </Badge>
        </div>
        <h2 className="font-heading text-3xl md:text-4xl font-bold text-primary mb-2">
          Climate Stress × Fertility Decline Predictor
        </h2>
        <p className="text-muted-foreground text-sm">
          Adjust heat-stress days and rainfall deficit to project climate-driven fertility decline across flock
          categories. The medium-flock vulnerability sweet spot (OR = 24.86 at baseline) scales multiplicatively
          with both climate axes.
        </p>
      </div>

      {/* ===== Sliders + scenarios ===== */}
      <Card className="p-5 mb-6">
        <div className="grid md:grid-cols-2 gap-6 mb-4">
          <div>
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-2">
                <Sun className="h-4 w-4 text-destructive" />
                <span className="font-heading text-sm font-bold text-primary">Heat-stress days / year</span>
              </div>
              <Badge className="bg-destructive text-white font-num text-xs">{heat} days</Badge>
            </div>
            <Slider value={[heat]} min={20} max={150} step={1} onValueChange={(v) => setHeat(v[0])} aria-label="Heat days" />
            <div className="flex justify-between mt-2 text-[10px] text-muted-foreground font-num">
              <span>20</span><span>60 (baseline)</span><span>150</span>
            </div>
            <div className="mt-1 text-[11px] text-muted-foreground">
              Multiplier vs baseline:{" "}
              <span className="font-num font-bold text-destructive">×{heatMultiplier.toFixed(2)}</span>
            </div>
          </div>

          <div>
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-2">
                <CloudRain className="h-4 w-4 text-accent" />
                <span className="font-heading text-sm font-bold text-primary">Rainfall deficit (mm)</span>
              </div>
              <Badge className="bg-accent text-accent-foreground font-num text-xs">{rain} mm</Badge>
            </div>
            <Slider value={[rain]} min={0} max={150} step={1} onValueChange={(v) => setRain(v[0])} aria-label="Rainfall deficit" />
            <div className="flex justify-between mt-2 text-[10px] text-muted-foreground font-num">
              <span>0</span><span>50 (baseline)</span><span>150</span>
            </div>
            <div className="mt-1 text-[11px] text-muted-foreground">
              Multiplier vs baseline:{" "}
              <span className="font-num font-bold text-accent">×{rainMultiplier.toFixed(2)}</span>
            </div>
          </div>
        </div>

        <div className="border-t border-border pt-4">
          <div className="text-[10px] uppercase tracking-wider font-bold text-muted-foreground mb-2">
            Quick scenarios
          </div>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-2">
            {SCENARIOS.map((s) => {
              const active = matchedScenario?.name === s.name;
              return (
                <button
                  key={s.name}
                  onClick={() => {
                    setHeat(s.heat);
                    setRain(s.rain);
                  }}
                  className={`text-left p-3 rounded-md border transition-all ${active ? "shadow-sm" : "hover:bg-secondary/40"}`}
                  style={active ? { borderColor: s.color, backgroundColor: `${s.color}0D` } : { borderColor: "var(--border)" }}
                >
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-bold" style={{ color: s.color }}>{s.name}</span>
                    {active && <span className="w-2 h-2 rounded-full" style={{ backgroundColor: s.color }} />}
                  </div>
                  <div className="text-[10px] text-muted-foreground mt-1 font-num">
                    {s.heat} days · {s.rain} mm
                  </div>
                  <div className="text-[9px] text-muted-foreground mt-0.5">{s.desc}</div>
                </button>
              );
            })}
          </div>
        </div>

        <div className="flex justify-end mt-4">
          <Button variant="outline" size="sm" onClick={reset} className="gap-1.5">
            <RotateCcw className="h-3.5 w-3.5" /> Reset to baseline
          </Button>
        </div>
      </Card>

      {/* ===== Medium-flock OR highlight ===== */}
      <Card className="p-5 mb-6 border-l-4 border-l-primary">
        <div className="flex flex-col md:flex-row items-start md:items-center gap-4">
          <div className="w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center flex-shrink-0">
            <Gauge className="h-6 w-6 text-primary" />
          </div>
          <div className="flex-1">
            <div className="text-[10px] uppercase tracking-wider font-bold text-primary mb-1">
              Medium-flock odds ratio for perceived fertility decline
            </div>
            <div className="text-xs text-muted-foreground mb-2">
              Logistic model: <span className="font-num font-bold text-foreground">OR = 24.86 × heatMult × rainMult</span>
            </div>
            <div className="font-num text-xs text-muted-foreground">
              = 24.86 × {heatMultiplier.toFixed(2)} × {rainMultiplier.toFixed(2)}{" "}
              <span className="text-foreground">=</span>{" "}
              <span className="font-num text-3xl font-bold text-primary ml-1">{mediumOR.toFixed(1)}</span>
            </div>
          </div>
          <div className="text-right">
            <div className="text-[10px] uppercase tracking-wider text-muted-foreground">vs baseline</div>
            <div
              className={`font-num text-lg font-bold ${mediumOR >= BASE_MEDIUM_OR ? "text-destructive" : "text-primary"}`}
            >
              {mediumOR >= BASE_MEDIUM_OR ? "+" : ""}
              {((mediumOR - BASE_MEDIUM_OR) / BASE_MEDIUM_OR * 100).toFixed(0)}%
            </div>
          </div>
        </div>
      </Card>

      {/* ===== Bar chart ===== */}
      <Card className="p-5 mb-6">
        <div className="flex items-center justify-between mb-3">
          <div>
            <h3 className="font-heading text-sm font-bold text-primary">
              Fertility Decline by Flock Size — Baseline vs Projected
            </h3>
            <p className="text-[11px] text-muted-foreground">
              % of keepers in each flock category reporting perceived fertility decline
            </p>
          </div>
          <div className="flex gap-2">
            <Badge variant="outline" className="text-[10px] font-num text-muted-foreground border-border">
              Climate factor ×{climateFactor.toFixed(2)}
            </Badge>
          </div>
        </div>

        <div style={{ height: "340px" }}>
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={chartData} margin={{ top: 20, right: 20, left: 0, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#D2CEC0" />
              <XAxis dataKey="flock" stroke="#6B6B6B" fontSize={11} />
              <YAxis
                stroke="#6B6B6B"
                fontSize={11}
                domain={[0, 100]}
                unit="%"
                label={{ value: "% reporting decline", angle: -90, position: "insideLeft", style: { fontSize: 11, fill: "#6B6B6B" } }}
              />
              <Tooltip
                contentStyle={{ backgroundColor: "#FBFAF7", border: "1px solid #D2CEC0", borderRadius: "8px", fontSize: "11px" }}
                formatter={(value: number, name: string) => [`${value}%`, name]}
              />
              <Legend wrapperStyle={{ fontSize: 11 }} />
              <Bar dataKey="baseline" name="Baseline (current climate)" radius={[3, 3, 0, 0]} fill="#A89F88">
                <LabelList dataKey="baseline" position="top" style={{ fontSize: 10, fill: "#6B6B6B", fontWeight: 600 }} formatter={(v: number) => `${v}%`} />
              </Bar>
              <Bar dataKey="projected" name="Projected (selected climate)" radius={[3, 3, 0, 0]}>
                {chartData.map((entry, i) => (
                  <Cell key={i} fill={entry.color} />
                ))}
                <LabelList dataKey="projected" position="top" style={{ fontSize: 10, fontWeight: 700 }} formatter={(v: number) => `${v}%`} />
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-2 mt-3">
          {chartData.map((d) => {
            const positive = d.delta >= 0;
            return (
              <div key={d.flock} className="p-2 rounded-md border-l-4" style={{ borderLeftColor: d.color, backgroundColor: `${d.color}08` }}>
                <div className="font-bold text-xs" style={{ color: d.color }}>{d.flock}</div>
                <div className="text-[10px] text-muted-foreground font-num">
                  {d.baseline}% → {d.projected}%
                </div>
                <div className={`text-[10px] font-num font-bold ${positive ? "text-destructive" : "text-primary"}`}>
                  {positive ? "+" : ""}{d.delta} pp
                </div>
              </div>
            );
          })}
        </div>
      </Card>

      {/* ===== Interpretation ===== */}
      <Card className="p-5 bg-destructive/5 border-destructive/20">
        <div className="flex items-start gap-3">
          <TrendingDown className="h-5 w-5 text-destructive flex-shrink-0 mt-0.5" />
          <div>
            <div className="text-[10px] uppercase tracking-wider font-bold text-destructive mb-1">Interpretation</div>
            <p className="text-sm text-foreground leading-relaxed">
              At <span className="font-num font-bold">{heat}</span> heat-stress days and{" "}
              <span className="font-num font-bold">{rain}</span> mm rainfall deficit, the medium-flock odds ratio
              reaches <span className="font-num font-bold text-destructive">{mediumOR.toFixed(1)}</span> —{" "}
              {mediumOR > BASE_MEDIUM_OR ? "amplifying" : "attenuating"} the baseline vulnerability by{" "}
              <span className="font-num font-bold">{Math.abs(((mediumOR - BASE_MEDIUM_OR) / BASE_MEDIUM_OR * 100)).toFixed(0)}%</span>.
              {mediumOR > 50
                ? " At this level, virtually every medium-flock keeper would report perceived fertility decline — the threshold for systemic collapse of smallholder livelihoods."
                : mediumOR > BASE_MEDIUM_OR
                  ? " Medium flocks (20–50 head) remain the vulnerability sweet spot — large enough to exhibit systematic patterns, small enough to lack institutional buffering."
                  : " Climate conditions improve relative to baseline — but structural vulnerability of medium flocks persists."}
            </p>
          </div>
        </div>
      </Card>
    </div>
  );
}
