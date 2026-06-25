"use client";

import { Suspense, useState } from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Html } from "@react-three/drei";
import { Card } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Microscope, Shield, Atom, Zap, Activity, Layers } from "lucide-react";
import type { LucideIcon } from "lucide-react";
import { motion } from "framer-motion";

type Vec3 = [number, number, number];

interface Hotspot {
  id: string;
  position: Vec3;
  title: string;
  desc: string;
  mechanism: string;
  icon: LucideIcon;
  color: string;
}

const HOTSPOTS: Hotspot[] = [
  {
    id: "acrosome",
    position: [4.4, 0, 0],
    title: "Acrosome Cap",
    desc: "Apical vesicle containing hydrolytic enzymes (hyaluronidase, acrosin) required for zona pellucida binding and penetration.",
    mechanism:
      "DPP polyphenols (caffeic & ferulic acid) stabilize the outer acrosomal membrane, preventing premature acrosome reaction during chilled storage. Fewer sperm arrive at the oocyte already acrosome-reacted — and therefore infertile.",
    icon: Shield,
    color: "#9C4942",
  },
  {
    id: "nucleus",
    position: [3, 0.5, 0.5],
    title: "Haploid Nucleus",
    desc: "Densely compacted chromatin (protamine-bound) carrying the paternal haploid genome.",
    mechanism:
      "Zinc (8.4 mg/100g) and selenium (0.038 mg/100g) in DPP serve as cofactors for protamine disulfide cross-linking and DNA repair enzymes. Reduces the DNA fragmentation index during 48h chilled storage.",
    icon: Atom,
    color: "#2D5016",
  },
  {
    id: "midpiece",
    position: [-0.5, 0.6, 0],
    title: "Mitochondrial Sheath",
    desc: "~70–80 helical mitochondria wrapped around the midpiece, generating ATP via oxidative phosphorylation for flagellar beat.",
    mechanism:
      "Amphiphilic flavonoids from DPP integrate into the mitochondrial outer membrane, quenching ROS at the source (Complex I/III electron leak). Preserves mitochondrial membrane potential (ΔΨm) and ATP synthesis — measurable as higher progressive motility.",
    icon: Zap,
    color: "#8B6914",
  },
  {
    id: "tail",
    position: [-3.5, 0, 0],
    title: "Flagellum (9+2 axoneme)",
    desc: "Microtubule axoneme with dynein arms — the propulsive organelle generating progressive motility.",
    mechanism:
      "Selenium-dependent GPx and zinc-dependent SOD (both supported by DPP cofactors) prevent dynein ATPase oxidation. Maintains beat frequency and amplitude — the physical basis of progressive motility.",
    icon: Activity,
    color: "#5C8A3E",
  },
  {
    id: "membrane",
    position: [3.5, -0.8, 0.3],
    title: "Plasma Membrane (DHA-rich)",
    desc: "30–40% of ram sperm phospholipids are DHA — exceptional fluidity, exceptional peroxidation vulnerability.",
    mechanism:
      "Vitamin E (tocopherols) and amphiphilic polyphenols from DPP intercalate into the bilayer, intercepting lipid peroxyl radicals (LOO•) at the propagation step. Vitamin C then regenerates tocopherol — the synergistic cycle that the DPPH assay cannot capture.",
    icon: Layers,
    color: "#C4A858",
  },
];

/* ============================================================
   3D sperm model — head (+X), midpiece (~0), tail (-X)
   ============================================================ */
function SpermModel() {
  return (
    <group>
      {/* Head body — capsule */}
      <mesh position={[3, 0, 0]} rotation={[0, 0, Math.PI / 2]}>
        <capsuleGeometry args={[0.6, 1.2, 8, 20]} />
        <meshStandardMaterial color="#F5E8C8" roughness={0.45} />
      </mesh>

      {/* Acrosome cap — cone */}
      <mesh position={[4.4, 0, 0]} rotation={[0, 0, -Math.PI / 2]}>
        <coneGeometry args={[0.6, 0.9, 20]} />
        <meshStandardMaterial color="#E8D7A8" roughness={0.4} />
      </mesh>

      {/* Neck */}
      <mesh position={[2.0, 0, 0]} rotation={[0, 0, Math.PI / 2]}>
        <cylinderGeometry args={[0.22, 0.35, 0.5, 16]} />
        <meshStandardMaterial color="#D4C293" roughness={0.5} />
      </mesh>

      {/* Midpiece */}
      <mesh position={[0.4, 0, 0]} rotation={[0, 0, Math.PI / 2]}>
        <cylinderGeometry args={[0.30, 0.25, 1.8, 16]} />
        <meshStandardMaterial color="#C9B677" roughness={0.5} />
      </mesh>

      {/* Mitochondrial rings around midpiece */}
      {[1.2, 0.8, 0.4, 0.0, -0.4].map((x, i) => (
        <mesh key={i} position={[x, 0, 0]} rotation={[0, Math.PI / 2, 0]}>
          <torusGeometry args={[0.34, 0.06, 8, 24]} />
          <meshStandardMaterial color="#8B6914" roughness={0.4} metalness={0.15} />
        </mesh>
      ))}

      {/* Flagellum — tapering */}
      <mesh position={[-1.5, 0, 0]} rotation={[0, 0, Math.PI / 2]}>
        <cylinderGeometry args={[0.16, 0.10, 1.6, 12]} />
        <meshStandardMaterial color="#A89366" roughness={0.6} />
      </mesh>
      <mesh position={[-2.7, 0, 0]} rotation={[0, 0, Math.PI / 2]}>
        <cylinderGeometry args={[0.08, 0.04, 1.4, 12]} />
        <meshStandardMaterial color="#A89366" roughness={0.6} />
      </mesh>
      <mesh position={[-3.6, 0, 0]} rotation={[0, 0, Math.PI / 2]}>
        <cylinderGeometry args={[0.04, 0.02, 0.8, 8]} />
        <meshStandardMaterial color="#A89366" roughness={0.6} />
      </mesh>
    </group>
  );
}

interface HotspotProps {
  hotspot: Hotspot;
  isActive: boolean;
  isHovered: boolean;
  onSelect: (id: string) => void;
  onHover: (id: string | null) => void;
}

function Hotspot({ hotspot, isActive, isHovered, onSelect, onHover }: HotspotProps) {
  const showLabel = isHovered || isActive;
  return (
    <group position={hotspot.position}>
      <mesh
        onClick={(e) => {
          e.stopPropagation();
          onSelect(hotspot.id);
        }}
        onPointerOver={(e) => {
          e.stopPropagation();
          onHover(hotspot.id);
          document.body.style.cursor = "pointer";
        }}
        onPointerOut={() => {
          onHover(null);
          document.body.style.cursor = "auto";
        }}
      >
        <sphereGeometry args={[0.22, 16, 16]} />
        <meshStandardMaterial
          color={hotspot.color}
          emissive={hotspot.color}
          emissiveIntensity={isActive ? 0.7 : isHovered ? 0.5 : 0.25}
          roughness={0.35}
        />
      </mesh>

      {isActive && (
        <mesh>
          <sphereGeometry args={[0.34, 16, 16]} />
          <meshBasicMaterial color={hotspot.color} transparent opacity={0.22} />
        </mesh>
      )}

      {showLabel && (
        <Html distanceFactor={9} position={[0, 0.45, 0]} center>
          <div
            className="px-2 py-1 rounded-md text-[10px] font-bold whitespace-nowrap select-none"
            style={{
              backgroundColor: hotspot.color,
              color: "#FBFAF7",
              boxShadow: "0 4px 12px rgba(0,0,0,0.25)",
            }}
          >
            {hotspot.title}
          </div>
        </Html>
      )}
    </group>
  );
}

export default function Sperm3DScene() {
  const [activeId, setActiveId] = useState<string>("acrosome");
  const [hoveredId, setHoveredId] = useState<string | null>(null);

  const active = HOTSPOTS.find((h) => h.id === activeId) ?? HOTSPOTS[0];
  const ActiveIcon = active.icon;

  return (
    <div className="p-6 md:p-10 max-w-7xl mx-auto">
      <div className="mb-6">
        <div className="flex items-center gap-2 mb-2">
          <Badge variant="outline" className="text-accent border-accent/40 font-num">05 · 3D SPERM MODEL</Badge>
          <Badge variant="secondary" className="text-[10px] gap-1">
            <Microscope className="h-3 w-3" /> Click hotspots · drag to orbit
          </Badge>
        </div>
        <h2 className="font-heading text-3xl md:text-4xl font-bold text-primary mb-2">
          Where DPP Acts — Interactive 3D Model
        </h2>
        <p className="text-muted-foreground text-sm">
          Each sphere marks a sperm compartment where DPP constituents exert a protective mechanism. Click a
          hotspot — or use the buttons on the right — to explore the underlying biology.
        </p>
      </div>

      <div className="grid lg:grid-cols-[1fr_360px] gap-6">
        {/* ===== 3D canvas ===== */}
        <Card className="p-0 overflow-hidden">
          <div
            style={{
              height: "560px",
              background:
                "radial-gradient(circle at 50% 30%, #FFFFFF 0%, #FBFAF7 45%, #F1EFE8 100%)",
            }}
          >
            <Canvas camera={{ position: [0, 1.5, 13], fov: 45 }}>
              <Suspense fallback={null}>
                <ambientLight intensity={0.7} />
                <directionalLight position={[6, 8, 5]} intensity={1.1} />
                <directionalLight position={[-6, -3, -4]} intensity={0.4} color="#8B6914" />
                <SpermModel />
                {HOTSPOTS.map((h) => (
                  <Hotspot
                    key={h.id}
                    hotspot={h}
                    isActive={activeId === h.id}
                    isHovered={hoveredId === h.id}
                    onSelect={setActiveId}
                    onHover={setHoveredId}
                  />
                ))}
                <OrbitControls enablePan={false} minDistance={6} maxDistance={22} />
              </Suspense>
            </Canvas>
          </div>
          <div className="px-4 py-2 bg-secondary/40 text-[10px] text-muted-foreground flex items-center justify-between">
            <span>Drag to rotate · scroll to zoom · click spheres to inspect</span>
            <span className="font-num">{HOTSPOTS.length} hotspots</span>
          </div>
        </Card>

        {/* ===== Right panel ===== */}
        <div className="space-y-4">
          <Card className="p-4">
            <div className="text-[10px] uppercase tracking-wider font-bold text-muted-foreground mb-3">
              Select compartment
            </div>
            <div className="grid grid-cols-1 gap-2">
              {HOTSPOTS.map((h) => {
                const Icon = h.icon;
                const isActive = activeId === h.id;
                return (
                  <button
                    key={h.id}
                    onClick={() => setActiveId(h.id)}
                    className={`flex items-center gap-3 p-3 rounded-md border text-left transition-all ${isActive ? "shadow-sm" : "hover:bg-secondary"}`}
                    style={
                      isActive
                        ? { borderColor: h.color, backgroundColor: `${h.color}10` }
                        : { borderColor: "var(--border)" }
                    }
                  >
                    <div
                      className="w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0"
                      style={{ backgroundColor: `${h.color}20` }}
                    >
                      <Icon className="h-4 w-4" style={{ color: h.color }} />
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="text-xs font-bold text-foreground truncate">{h.title}</div>
                      <div className="text-[10px] text-muted-foreground truncate">{h.id}</div>
                    </div>
                    {isActive && (
                      <div className="w-2 h-2 rounded-full" style={{ backgroundColor: h.color }} />
                    )}
                  </button>
                );
              })}
            </div>
          </Card>

          <motion.div key={active.id} initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }}>
            <Card className="p-5 border-l-4" style={{ borderLeftColor: active.color }}>
              <div className="flex items-center gap-2 mb-2">
                <ActiveIcon className="h-4 w-4" style={{ color: active.color }} />
                <span
                  className="text-[10px] uppercase tracking-wider font-bold"
                  style={{ color: active.color }}
                >
                  {active.id}
                </span>
              </div>
              <h3 className="font-heading text-lg font-bold text-foreground mb-2">{active.title}</h3>
              <p className="text-xs text-muted-foreground leading-relaxed mb-3">{active.desc}</p>
              <div
                className="rounded-md p-3"
                style={{ backgroundColor: `${active.color}0D`, border: `1px solid ${active.color}33` }}
              >
                <div
                  className="text-[10px] uppercase tracking-wider font-bold mb-1"
                  style={{ color: active.color }}
                >
                  DPP mechanism
                </div>
                <p className="text-xs text-foreground leading-relaxed">{active.mechanism}</p>
              </div>
            </Card>
          </motion.div>
        </div>
      </div>
    </div>
  );
}
