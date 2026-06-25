"use client";

import { useMemo, useState } from "react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Slider } from "@/components/ui/slider";
import { Button } from "@/components/ui/button";
import { Activity, Zap, Heart, Beaker, Clock, RotateCcw, FlaskConical } from "lucide-react";
import { motion } from "framer-motion";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
  ReferenceDot,
  ReferenceLine,
} from "recharts";

/* ============================================================
   Source data — measured at three doses × three storage times
   ============================================================ */
type Timepoint = 0 | 24 | 48;

const RAW = {
  total: {
    0: { 0: 78.5, 40: 79.8, 80: 80.2 },
    24: { 0: 68.2, 40: 72.5, 80: 74.8 },
    48: { 0: 58.3, 40: 63.1, 80: 67.5 },
  } as Record<Timepoint, Record<0 | 40 | 80, number>>,
  progressive: {
    0: { 0: 62.4, 40: 63.5, 80: 64.1 },
    24: { 0: 53.8, 40: 58.2, 80: 60.5 },
    48: { 0: 45.5, 40: 50.6, 80: 54.7 },
  } as Record<Timepoint, Record<0 | 40 | 80, number>>,
  host: {
    0: { 0: 76.2, 40: 77.5, 80: 78.1 },
    24: { 0: 65.4, 40: 69.8, 80: 72.5 },
    48: { 0: 55.1, 40: 60.2, 80: 63.9 },
  } as Record<Timepoint, Record<0 | 40 | 80, number>>,
};

/**
 * Predict a quality endpoint at an arbitrary dose for a given timepoint.
 *  - 0–40 mg/mL: linear interpolation
 *  - 40–80 mg/mL: linear interpolation
 *  - >80 mg/mL: logistic extrapolation toward a modest plateau
 */
function predictValue(dose: number, t: Timepoint, series: keyof typeof RAW): number {
  const points = RAW[series][t];
  const v0 = points[0];
  const v40 = points[40];
  const v80 = points[80];

  if (dose <= 0) return v0;
  if (dose <= 40) return v0 + ((v40 - v0) * dose) / 40;
  if (dose <= 80) return v40 + ((v80 - v40) * (dose - 40)) / 40;

  // Logistic plateau above 80 mg/mL
  const plateau = v80 + Math.min(2.5, (v80 - v0) * 0.3);
  const k = 0.04;
  return plateau - (plateau - v80) * Math.exp(-k * (dose - 80));
}

const DOSE_TICKS = [0, 20, 40, 60, 80, 100, 120, 140, 150];
const DOSE_CURVE = [0, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150];

const SERIES_META = {
  total: { key: "total" as const, label: "Total Motility", color: "#2D5016", icon: Activity },
  progressive: { key: "progressive" as const, label: "Progressive Motility", color: "#8B6914", icon: Zap },
  host: { key: "host" as const, label: "Membrane Integrity (HOST)", color: "#9C4942", icon: Heart },
};

export default function DoseResponseScene() {
  const [dose, setDose] = useState(80);
  const [hours, setHours] = useState<Timepoint>(48);

  // Build the chart dataset for the currently-selected storage time
  const chartData = useMemo(() => {
    return DOSE_CURVE.map((d) => ({
      dose: d,
      total: Number(predictValue(d, hours, "total").toFixed(2)),
      progressive: Number(predictValue(d, hours, "progressive").toFixed(2)),
      host: Number(predictValue(d, hours, "host").toFixed(2)),
    }));
  }, [hours]);

  const predicted = {
    total: predictValue(dose, hours, "total"),
    progressive: predictValue(dose, hours, "progressive"),
    host: predictValue(dose, hours, "host"),
  };

  // Dose band classification
  const doseBand =
    dose === 0
      ? { label: "Control (no DPPE)", color: "#9C4942" }
      : dose <= 40
        ? { label: "DPPE-40 band", color: "#8B6914" }
        : dose <= 80
          ? { label: "DPPE-80 band (validated)", color: "#2D5016" }
          : { label: "Extrapolated > 80 mg/mL (logistic plateau)", color: "#5C8A3E" };

  const reset = () => {
    setDose(80);
    setHours(48);
  };

  return (
    <div className="p-6 md:p-10 max-w-7xl mx-auto">
      <div className="mb-6">
        <div className="flex items-center gap-2 mb-2">
          <Badge variant="outline" className="text-accent border-accent/40 font-num">04 · LIVE DOSE MIXER</Badge>
          <Badge variant="secondary" className="text-[10px] gap-1"><FlaskConical className="h-3 w-3" /> Interpolated model · Exp 3 data</Badge>
        </div>
        <h2 className="font-heading text-3xl md:text-4xl font-bold text-primary mb-2">Dose-Response Interactive Simulator</h2>
        <p className="text-muted-foreground text-sm">
          Drag the sliders to predict motility &amp; membrane integrity at any DPPE concentration and storage time.
          Linear interpolation is used between 0 / 40 / 80 mg/mL; above 80 mg/mL a logistic plateau is assumed.
        </p>
      </div>

      {/* ===== Mixer controls ===== */}
      <Card className="p-5 mb-6">
        <div className="grid md:grid-cols-2 gap-6">
          <div>
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-2">
                <Beaker className="h-4 w-4 text-primary" />
                <span className="font-heading text-sm font-bold text-primary">DPPE Concentration</span>
              </div>
              <Badge className="font-num text-xs" style={{ backgroundColor: doseBand.color, color: "#FBFAF7" }}>
                {dose} mg/mL
              </Badge>
            </div>
            <Slider
              value={[dose]}
              min={0}
              max={150}
              step={5}
              onValueChange={(v) => setDose(v[0])}
              aria-label="DPPE concentration"
            />
            <div className="flex justify-between mt-2 text-[10px] text-muted-foreground font-num">
              {DOSE_TICKS.map((t) => (
                <span key={t}>{t}</span>
              ))}
            </div>
            <div className="mt-2 text-[11px] font-bold" style={{ color: doseBand.color }}>
              {doseBand.label}
            </div>
          </div>

          <div>
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-2">
                <Clock className="h-4 w-4 text-accent" />
                <span className="font-heading text-sm font-bold text-primary">Storage Time (4°C)</span>
              </div>
              <Badge className="bg-accent text-accent-foreground font-num text-xs">{hours}h</Badge>
            </div>
            <Slider
              value={[hours]}
              min={0}
              max={48}
              step={24}
              onValueChange={(v) => setHours(v[0] as Timepoint)}
              aria-label="Storage time"
            />
            <div className="flex justify-between mt-2 text-[10px] text-muted-foreground font-num">
              <span>0h</span>
              <span>24h</span>
              <span>48h</span>
            </div>
            <div className="mt-2 text-[11px] text-muted-foreground">
              Validated endpoints · 4°C chilled storage
            </div>
          </div>
        </div>

        <div className="flex justify-end mt-4">
          <Button variant="outline" size="sm" onClick={reset} className="gap-1.5">
            <RotateCcw className="h-3.5 w-3.5" /> Reset to DPPE-80 · 48h
          </Button>
        </div>
      </Card>

      {/* ===== Predicted stat cards ===== */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        {(Object.keys(SERIES_META) as (keyof typeof SERIES_META)[]).map((key, i) => {
          const meta = SERIES_META[key];
          const Icon = meta.icon;
          const value = predicted[key];
          const control = predictValue(0, hours, key);
          const gain = value - control;
          return (
            <motion.div
              key={key}
              initial={{ opacity: 0, y: 16 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: i * 0.08 }}
            >
              <Card className="p-5 hover-lift border-l-4" style={{ borderLeftColor: meta.color }}>
                <div className="flex items-center justify-between mb-2">
                  <div className="flex items-center gap-2">
                    <Icon className="h-4 w-4" style={{ color: meta.color }} />
                    <span className="text-[10px] uppercase tracking-wider font-bold text-muted-foreground">{meta.label}</span>
                  </div>
                  <Badge variant="outline" className="text-[9px] font-num" style={{ color: meta.color, borderColor: `${meta.color}55` }}>
                    @ {dose} mg/mL
                  </Badge>
                </div>
                <div className="font-num text-4xl font-bold" style={{ color: meta.color }}>
                  {value.toFixed(1)}%
                </div>
                <div className="text-[11px] text-muted-foreground mt-1">
                  vs control {control.toFixed(1)}% ·{" "}
                  <span className="font-num font-bold" style={{ color: gain >= 0 ? meta.color : "#9C4942" }}>
                    {gain >= 0 ? "+" : ""}{gain.toFixed(1)} pp
                  </span>
                </div>
              </Card>
            </motion.div>
          );
        })}
      </div>

      {/* ===== Dose-response chart ===== */}
      <Card className="p-5 mb-6">
        <div className="flex items-center justify-between mb-3">
          <div>
            <h3 className="font-heading text-sm font-bold text-primary">Dose-Response Curves · {hours}h storage</h3>
            <p className="text-[11px] text-muted-foreground">
              Predicted endpoint (%) vs DPPE dose (mg/mL). Dots mark your current slider position.
            </p>
          </div>
          <div className="flex gap-2">
            <Badge variant="outline" className="text-[10px] font-num text-primary border-primary/40">Linear 0–80</Badge>
            <Badge variant="outline" className="text-[10px] font-num text-accent border-accent/40">Logistic &gt;80</Badge>
          </div>
        </div>

        <div style={{ height: "380px" }}>
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={chartData} margin={{ top: 10, right: 30, left: 0, bottom: 20 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#D2CEC0" />
              <XAxis
                dataKey="dose"
                stroke="#6B6B6B"
                fontSize={11}
                ticks={DOSE_TICKS}
                domain={[0, 150]}
                label={{ value: "DPPE concentration (mg/mL)", position: "insideBottom", offset: -10, style: { fontSize: 11, fill: "#6B6B6B" } }}
              />
              <YAxis
                stroke="#6B6B6B"
                fontSize={11}
                domain={[40, 90]}
                label={{ value: "Predicted endpoint (%)", angle: -90, position: "insideLeft", style: { fontSize: 11, fill: "#6B6B6B" } }}
              />
              <Tooltip
                contentStyle={{ backgroundColor: "#FBFAF7", border: "1px solid #D2CEC0", borderRadius: "8px", fontSize: "11px" }}
                labelStyle={{ color: "#2D5016", fontWeight: 700 }}
                labelFormatter={(v) => `${v} mg/mL`}
              />
              <Legend wrapperStyle={{ fontSize: 11 }} />
              <ReferenceLine x={80} stroke="#8B6914" strokeDasharray="4 4" label={{ value: "Validated max", position: "top", style: { fontSize: 10, fill: "#8B6914" } }} />
              <Line type="monotone" dataKey="total" name="Total Motility" stroke={SERIES_META.total.color} strokeWidth={2.5} dot={false} />
              <Line type="monotone" dataKey="progressive" name="Progressive Motility" stroke={SERIES_META.progressive.color} strokeWidth={2.5} dot={false} />
              <Line type="monotone" dataKey="host" name="Membrane Integrity" stroke={SERIES_META.host.color} strokeWidth={2.5} dot={false} />
              <ReferenceDot x={dose} y={predicted.total} r={7} fill={SERIES_META.total.color} stroke="#FBFAF7" strokeWidth={2} />
              <ReferenceDot x={dose} y={predicted.progressive} r={7} fill={SERIES_META.progressive.color} stroke="#FBFAF7" strokeWidth={2} />
              <ReferenceDot x={dose} y={predicted.host} r={7} fill={SERIES_META.host.color} stroke="#FBFAF7" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div className="mt-3 grid md:grid-cols-3 gap-2">
          {(Object.keys(SERIES_META) as (keyof typeof SERIES_META)[]).map((key) => {
            const meta = SERIES_META[key];
            return (
              <div key={key} className="p-2 rounded-md border-l-4" style={{ borderLeftColor: meta.color, backgroundColor: `${meta.color}08` }}>
                <div className="font-bold text-xs" style={{ color: meta.color }}>{meta.label}</div>
                <div className="text-[10px] text-muted-foreground font-num">
                  @ {dose} mg/mL · {hours}h → <span className="font-bold text-foreground">{predicted[key].toFixed(1)}%</span>
                </div>
              </div>
            );
          })}
        </div>
      </Card>

      {/* ===== Interpretation footer ===== */}
      <Card className="p-5 bg-primary/5 border-primary/20">
        <div className="flex items-start gap-3">
          <Beaker className="h-5 w-5 text-primary flex-shrink-0 mt-0.5" />
          <div>
            <div className="text-[10px] uppercase tracking-wider font-bold text-primary mb-1">Interpretation</div>
            <p className="text-sm text-foreground leading-relaxed">
              At <span className="font-num font-bold text-primary">{dose} mg/mL</span> DPPE and{" "}
              <span className="font-num font-bold text-primary">{hours}h</span> of chilled storage, the model predicts{" "}
              <span className="font-num font-bold text-primary">{predicted.total.toFixed(1)}%</span> total motility —{" "}
              <span className="font-num font-bold" style={{ color: predicted.total - predictValue(0, hours, "total") >= 0 ? "#2D5016" : "#9C4942" }}>
                {predicted.total - predictValue(0, hours, "total") >= 0 ? "+" : ""}
                {(predicted.total - predictValue(0, hours, "total")).toFixed(1)} pp
              </span>{" "}
              vs control. {dose > 80
                ? "Doses above 80 mg/mL lie beyond the experimentally-validated range and follow a logistic plateau — additional benefit is expected to be marginal."
                : dose === 80
                  ? "This is the experimentally-validated optimal dose (DPPE-80)."
                  : "Lower doses provide measurable but submaximal protection."}
            </p>
          </div>
        </div>
      </Card>
    </div>
  );
}
