"use client";

import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { StickyNote, ChevronDown, ChevronUp, Lightbulb, MessageSquare, Clock } from "lucide-react";

export interface SpeakerNote {
  type: "key" | "transition" | "qa" | "timing";
  text: string;
}

export interface SpeakerNotesProps {
  notes: SpeakerNote[];
  defaultOpen?: boolean;
}

const typeConfig = {
  key: { icon: Lightbulb, color: "text-primary", bg: "bg-primary/5", border: "border-primary/20", label: "Key point" },
  transition: { icon: ChevronRight, color: "text-accent", bg: "bg-accent/5", border: "border-accent/20", label: "Transition" },
  qa: { icon: MessageSquare, color: "text-destructive", bg: "bg-destructive/5", border: "border-destructive/20", label: "Anticipated Q&A" },
  timing: { icon: Clock, color: "text-muted-foreground", bg: "bg-secondary", border: "border-border", label: "Timing" },
};

function ChevronRight(props: { className?: string }) {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={props.className}>
      <path d="m9 18 6-6-6-6" />
    </svg>
  );
}

export default function SpeakerNotes({ notes, defaultOpen = false }: SpeakerNotesProps) {
  const [isOpen, setIsOpen] = useState(defaultOpen);

  return (
    <Card className={`overflow-hidden transition-all ${isOpen ? "border-accent/40" : ""}`}>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="w-full flex items-center gap-2 p-3 bg-accent/10 hover:bg-accent/15 transition-colors"
      >
        <StickyNote className="h-4 w-4 text-accent" />
        <span className="text-sm font-bold text-accent uppercase tracking-wider">Speaker Notes</span>
        <Badge variant="outline" className="text-[10px] font-num border-accent/40 text-accent">{notes.length} cues</Badge>
        <span className="ml-auto text-xs text-muted-foreground">{isOpen ? "Hide" : "Show for presentation"}</span>
        {isOpen ? <ChevronUp className="h-4 w-4 text-accent" /> : <ChevronDown className="h-4 w-4 text-accent" />}
      </button>
      {isOpen && (
        <div className="p-4 space-y-2 max-h-[400px] overflow-y-auto">
          {notes.map((note, i) => {
            const cfg = typeConfig[note.type];
            const Icon = cfg.icon;
            return (
              <div key={i} className={`flex items-start gap-3 p-3 rounded-md ${cfg.bg} ${cfg.border} border`}>
                <div className="flex-shrink-0 mt-0.5">
                  <Icon className={`h-4 w-4 ${cfg.color}`} />
                </div>
                <div className="flex-1 min-w-0">
                  <div className={`text-[10px] uppercase tracking-wider font-bold ${cfg.color} mb-0.5`}>{cfg.label}</div>
                  <p className="text-sm text-foreground leading-relaxed">{note.text}</p>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </Card>
  );
}
