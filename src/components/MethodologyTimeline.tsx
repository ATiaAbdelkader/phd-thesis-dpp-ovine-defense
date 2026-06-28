"use client";

import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import {
  ChevronRight, ChevronLeft, CheckCircle2, Circle, FlaskConical, Users, Beaker, Microscope, Cloud,
} from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

export interface MethodStep {
  num: number;
  title: string;
  detail: string;
  duration?: string;
  icon: string;
}

interface MethodologyTimelineProps {
  steps: MethodStep[];
  color: string;
  experimentTitle: string;
  onComplete?: () => void;
}

const iconMap: Record<string, React.ElementType> = {
  users: Users,
  beaker: Beaker,
  microscope: Microscope,
  cloud: Cloud,
  flask: FlaskConical,
  check: CheckCircle2,
};

export default function MethodologyTimeline({ steps, color, experimentTitle }: MethodologyTimelineProps) {
  const [currentStep, setCurrentStep] = useState(0);
  const [completed, setCompleted] = useState<Set<number>>(new Set());

  const step = steps[currentStep];
  const isLast = currentStep === steps.length - 1;
  const isFirst = currentStep === 0;
  const progress = ((currentStep + 1) / steps.length) * 100;

  const goNext = () => {
    setCompleted(prev => new Set(prev).add(currentStep));
    if (!isLast) setCurrentStep(currentStep + 1);
  };

  const goPrev = () => {
    if (!isFirst) setCurrentStep(currentStep - 1);
  };

  const goToStep = (idx: number) => {
    setCurrentStep(idx);
  };

  return (
    <div>
      {/* Progress bar */}
      <div className="flex items-center gap-2 mb-6">
        <div className="flex-1 h-2 bg-secondary rounded-full overflow-hidden">
          <motion.div
            className="h-full rounded-full"
            style={{ backgroundColor: color }}
            animate={{ width: `${progress}%` }}
            transition={{ duration: 0.3 }}
          />
        </div>
        <span className="font-num text-xs font-bold text-muted-foreground">
          Step {currentStep + 1} / {steps.length}
        </span>
      </div>

      {/* Step navigation circles */}
      <div className="flex items-center justify-center gap-2 mb-6 flex-wrap">
        {steps.map((s, i) => {
          const isCompleted = completed.has(i);
          const isCurrent = i === currentStep;
          const isPast = i < currentStep;
          return (
            <button
              key={i}
              onClick={() => goToStep(i)}
              className="flex items-center gap-1"
              title={s.title}
            >
              <div
                className={`w-9 h-9 rounded-full flex items-center justify-center text-xs font-bold transition-all border-2 ${
                  isCurrent ? "scale-110 shadow-md" : ""
                }`}
                style={{
                  backgroundColor: isCurrent ? color : isCompleted || isPast ? `${color}30` : "var(--secondary)",
                  borderColor: isCurrent ? color : isCompleted || isPast ? color : "var(--border)",
                  color: isCurrent ? "#FBFAF7" : isCompleted || isPast ? color : "var(--muted-foreground)",
                }}
              >
                {isCompleted || isPast ? (
                  <CheckCircle2 className="h-4 w-4" />
                ) : (
                  s.num
                )}
              </div>
              {i < steps.length - 1 && (
                <div
                  className="w-6 h-0.5"
                  style={{ backgroundColor: isPast || isCompleted ? color : "var(--border)" }}
                />
              )}
            </button>
          );
        })}
      </div>

      {/* Current step detail */}
      <AnimatePresence mode="wait">
        <motion.div
          key={currentStep}
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          exit={{ opacity: 0, x: -20 }}
          transition={{ duration: 0.3 }}
        >
          <Card className="p-6" style={{ borderLeft: `4px solid ${color}` }}>
            <div className="flex items-start gap-4">
              <div
                className="w-14 h-14 rounded-lg flex items-center justify-center flex-shrink-0"
                style={{ backgroundColor: `${color}20` }}
              >
                {(() => {
                  const Icon = iconMap[step.icon] || FlaskConical;
                  return <Icon className="h-7 w-7" style={{ color }} />;
                })()}
              </div>
              <div className="flex-1">
                <div className="flex items-baseline gap-2 mb-1">
                  <span className="font-num text-2xl font-bold" style={{ color }}>
                    Step {step.num}
                  </span>
                  {step.duration && (
                    <Badge variant="outline" className="text-[10px] font-num gap-1">
                      <ChevronLeft className="h-2.5 w-2.5 rotate-180" />
                      {step.duration}
                    </Badge>
                  )}
                </div>
                <h4 className="font-heading text-xl font-bold text-foreground mb-2">
                  {step.title}
                </h4>
                <p className="text-sm text-muted-foreground leading-relaxed">
                  {step.detail}
                </p>
              </div>
            </div>
          </Card>
        </motion.div>
      </AnimatePresence>

      {/* Navigation buttons */}
      <div className="flex items-center justify-between mt-6">
        <Button
          onClick={goPrev}
          disabled={isFirst}
          variant="outline"
          size="sm"
          className="gap-1"
        >
          <ChevronLeft className="h-4 w-4" />
          Previous Step
        </Button>

        <div className="text-xs text-muted-foreground">
          {completed.size === steps.length - 1 && isLast ? (
            <Badge className="bg-primary text-primary-foreground gap-1">
              <CheckCircle2 className="h-3 w-3" />
              Methodology complete
            </Badge>
          ) : (
            <span>Complete all steps to proceed to results</span>
          )}
        </div>

        <Button
          onClick={goNext}
          size="sm"
          className="gap-1"
          style={{ backgroundColor: color, color: "#FBFAF7" }}
        >
          {isLast ? "Finish" : "Next Step"}
          <ChevronRight className="h-4 w-4" />
        </Button>
      </div>
    </div>
  );
}
