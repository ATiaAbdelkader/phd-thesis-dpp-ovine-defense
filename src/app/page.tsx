"use client";

import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { ChevronRight, ChevronLeft, Sparkles, Clock, Leaf, Microscope, Users, Beaker, Cloud, Activity, Atom, Calculator, Timer, BookOpen } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import HeroScene from "@/components/scenes/HeroScene";
import BackgroundScene from "@/components/scenes/BackgroundScene";
import ResearchDesignScene from "@/components/scenes/ResearchDesignScene";
import Experiment1Scene from "@/components/scenes/Experiment1Scene";
import Experiment2Scene from "@/components/scenes/Experiment2Scene";
import Experiment3Scene from "@/components/scenes/Experiment3Scene";
import Experiment4Scene from "@/components/scenes/Experiment4Scene";
import DoseResponseScene from "@/components/scenes/DoseResponseScene";
import Sperm3DScene from "@/components/scenes/Sperm3DScene";
import GHSICalculatorScene from "@/components/scenes/GHSICalculatorScene";
import RescueSimulatorScene from "@/components/scenes/RescueSimulatorScene";
import ClimateSimulatorScene from "@/components/scenes/ClimateSimulatorScene";
import ConclusionScene from "@/components/scenes/ConclusionScene";
import InterconnectionScene from "@/components/scenes/InterconnectionScene";
import PresentationAssistant from "@/components/PresentationAssistant";
import { Network } from "lucide-react";

export type Scene =
  | "hero"
  | "background"
  | "design"
  | "exp1"
  | "exp2"
  | "exp3"
  | "exp4"
  | "interconnection"
  | "dose-response"
  | "sperm-3d"
  | "ghsi"
  | "rescue-simulator"
  | "climate-simulator"
  | "conclusion";

const SCENES: { id: Scene; title: string; icon: React.ElementType; section: string; group: string }[] = [
  { id: "hero", title: "Cover", icon: Sparkles, section: "00", group: "intro" },
  { id: "background", title: "Background", icon: Leaf, section: "01", group: "intro" },
  { id: "design", title: "Design", icon: BookOpen, section: "02", group: "intro" },
  { id: "exp1", title: "Exp 1: Survey", icon: Users, section: "03", group: "experiments" },
  { id: "exp2", title: "Exp 2: DPP Bio", icon: Beaker, section: "04", group: "experiments" },
  { id: "exp3", title: "Exp 3: Sperm", icon: Microscope, section: "05", group: "experiments" },
  { id: "exp4", title: "Exp 4: Climate", icon: Cloud, section: "06", group: "experiments" },
  { id: "interconnection", title: "Links", icon: Network, section: "07", group: "experiments" },
  { id: "dose-response", title: "Dose Mixer", icon: Activity, section: "08", group: "interactive" },
  { id: "sperm-3d", title: "3D Sperm", icon: Atom, section: "09", group: "interactive" },
  { id: "ghsi", title: "GHSI Calc", icon: Calculator, section: "10", group: "interactive" },
  { id: "rescue-simulator", title: "Rescue Game", icon: Timer, section: "11", group: "interactive" },
  { id: "climate-simulator", title: "Climate Sim", icon: Cloud, section: "12", group: "interactive" },
  { id: "conclusion", title: "Conclusion", icon: ChevronRight, section: "13", group: "outro" },
];

const GROUP_LABELS: Record<string, string> = {
  intro: "Introduction",
  experiments: "Experiments & Results",
  interactive: "Interactive Tools",
  outro: "Conclusion",
};

export default function Home() {
  const [currentScene, setCurrentScene] = useState<Scene>("hero");
  const [countdown, setCountdown] = useState(48 * 60);
  const [isFullscreen, setIsFullscreen] = useState(false);

  useEffect(() => {
    const interval = setInterval(() => {
      setCountdown((prev) => (prev > 0 ? prev - 1 : 48 * 60));
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  const formatTime = (mins: number) => {
    const h = Math.floor(mins / 60);
    const m = mins % 60;
    return `${h.toString().padStart(2, "0")}:${m.toString().padStart(2, "0")}`;
  };

  const goToScene = (scene: Scene) => setCurrentScene(scene);
  const nextScene = () => {
    const idx = SCENES.findIndex((s) => s.id === currentScene);
    if (idx < SCENES.length - 1) setCurrentScene(SCENES[idx + 1].id);
  };
  const prevScene = () => {
    const idx = SCENES.findIndex((s) => s.id === currentScene);
    if (idx > 0) setCurrentScene(SCENES[idx - 1].id);
  };

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen();
      setIsFullscreen(true);
    } else {
      document.exitFullscreen();
      setIsFullscreen(false);
    }
  };

  const groupedScenes = SCENES.reduce((acc, scene) => {
    if (!acc[scene.group]) acc[scene.group] = [];
    acc[scene.group].push(scene);
    return acc;
  }, {} as Record<string, typeof SCENES>);

  return (
    <div className="min-h-screen flex flex-col palm-pattern bg-background">
      <header className="sticky top-0 z-50 border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/80">
        <div className="flex h-14 items-center px-4 gap-4">
          <div className="flex items-center gap-2 flex-shrink-0">
            <Leaf className="h-5 w-5 text-primary" />
            <span className="font-heading text-base font-bold text-primary hidden sm:inline">DPP · PhD Defense</span>
          </div>

          <div className="flex-1 overflow-x-auto">
            <div className="flex items-center gap-3 justify-center">
              {Object.entries(groupedScenes).map(([group, scenes]) => (
                <div key={group} className="flex items-center gap-1">
                  <span className="text-[9px] uppercase tracking-wider text-muted-foreground font-bold hidden lg:inline mr-1">{GROUP_LABELS[group]}</span>
                  {scenes.map((scene) => {
                    const Icon = scene.icon;
                    const isActive = currentScene === scene.id;
                    return (
                      <button
                        key={scene.id}
                        onClick={() => goToScene(scene.id)}
                        className={`flex items-center gap-1.5 px-2.5 py-1.5 rounded-md text-xs font-medium transition-all whitespace-nowrap ${
                          isActive ? "bg-primary text-primary-foreground shadow-sm" : "text-muted-foreground hover:bg-secondary hover:text-foreground"
                        }`}
                        title={scene.title}
                      >
                        <span className="font-num opacity-70">{scene.section}</span>
                        <Icon className="h-3.5 w-3.5" />
                        <span className="hidden xl:inline">{scene.title}</span>
                      </button>
                    );
                  })}
                  <div className="w-px h-6 bg-border last:hidden" />
                </div>
              ))}
            </div>
          </div>

          <div className="flex items-center gap-3 flex-shrink-0">
            <div className="flex items-center gap-1.5 px-2.5 py-1 bg-accent/10 border border-accent/30 rounded-md">
              <Clock className="h-3.5 w-3.5 text-accent" />
              <span className="font-num text-xs font-bold text-accent">{formatTime(countdown)}</span>
              <span className="text-[10px] text-accent/70 hidden sm:inline">/ 48:00</span>
            </div>
            <Button variant="ghost" size="sm" onClick={toggleFullscreen} className="hidden sm:inline-flex">{isFullscreen ? "Exit" : "Fullscreen"}</Button>
          </div>
        </div>
      </header>

      <main className="flex-1 flex flex-col">
        <AnimatePresence mode="wait">
          <motion.div
            key={currentScene}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            transition={{ duration: 0.3 }}
            className="flex-1"
          >
            {currentScene === "hero" && <HeroScene onNext={nextScene} />}
            {currentScene === "background" && <BackgroundScene />}
            {currentScene === "design" && <ResearchDesignScene />}
            {currentScene === "exp1" && <Experiment1Scene />}
            {currentScene === "exp2" && <Experiment2Scene />}
            {currentScene === "exp3" && <Experiment3Scene />}
            {currentScene === "exp4" && <Experiment4Scene />}
            {currentScene === "interconnection" && <InterconnectionScene />}
            {currentScene === "dose-response" && <DoseResponseScene />}
            {currentScene === "sperm-3d" && <Sperm3DScene />}
            {currentScene === "ghsi" && <GHSICalculatorScene />}
            {currentScene === "rescue-simulator" && <RescueSimulatorScene />}
            {currentScene === "climate-simulator" && <ClimateSimulatorScene />}
            {currentScene === "conclusion" && <ConclusionScene />}
          </motion.div>
        </AnimatePresence>
      </main>

      <footer className="border-t border-border bg-background/95 backdrop-blur">
        <div className="flex h-12 items-center px-4 gap-2 justify-between">
          <Button variant="ghost" size="sm" onClick={prevScene} disabled={currentScene === "hero"} className="gap-1">
            <ChevronLeft className="h-4 w-4" /> Previous
          </Button>
          <div className="text-xs text-muted-foreground font-num hidden sm:block">
            Scene {SCENES.findIndex((s) => s.id === currentScene) + 1} of {SCENES.length} · {SCENES.find((s) => s.id === currentScene)?.title}
          </div>
          <Button variant="default" size="sm" onClick={nextScene} disabled={currentScene === "conclusion"} className="gap-1 bg-primary hover:bg-primary/90">
            Next <ChevronRight className="h-4 w-4" />
          </Button>
        </div>
      </footer>

      {/* Presentation Assistant — floating panel with timer, teleprompter, and Q&A */}
      <PresentationAssistant currentScene={currentScene} />
    </div>
  );
}
