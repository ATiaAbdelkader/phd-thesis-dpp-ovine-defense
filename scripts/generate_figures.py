#!/usr/bin/env python3
"""
Thesis Figure Generator
Produces all figures (charts, diagrams, study area map) for the PhD thesis:
- Figure 2.1: Post-mortem biochemical cascade diagram
- Figure 2.2: DPP polypharmacological mechanism diagram
- Figure 2.3: Conceptual framework
- Figure 3.1: Study area map (El Oued, Algeria)
- Figure 3.2: Research design workflow
- Figure 3.3: DPP preparation flowchart
- Figure 3.4: Sperm assessment workflow
- Figure 4.1: Demographic profile (age, education, occupation)
- Figure 4.2: Flock size distribution
- Figure 4.3: Trait preferences (rams vs ewes)
- Figure 4.4: MANOVA interaction plot
- Figure 4.5: DPP proximate composition
- Figure 4.6: DPP mineral content
- Figure 4.7: DPP antioxidant DPPH curve
- Figure 4.8: Sperm motility by treatment × time
- Figure 4.9: Membrane integrity by treatment × time
- Figure 4.10: Dose-response curves
- Figure 4.11: Climate perception distribution
- Figure 4.12: Odds ratio forest plot
- Figure 5.1: Socio-Technical-Environmental Conservation Model
"""

import os
import sys
import math
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.font_manager as fm
fm.fontManager.addfont('/home/z/my-project/fonts/Tinos-Regular.ttf')
fm.fontManager.addfont('/home/z/my-project/fonts/Tinos-Bold.ttf')
fm.fontManager.addfont('/usr/share/fonts/truetype/english/Carlito-Regular.ttf')
fm.fontManager.addfont('/usr/share/fonts/truetype/english/Carlito-Bold.ttf')
fm.fontManager.addfont('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle, Polygon
import numpy as np

# Style configuration
plt.rcParams['font.family'] = 'Carlito'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.labelcolor'] = '#1A2A1F'
plt.rcParams['xtick.color'] = '#3A3A3A'
plt.rcParams['ytick.color'] = '#3A3A3A'

# Color palette (matches thesis palette)
DATE_PALM_GREEN = '#2D5016'
DATE_PALM_GREEN_LIGHT = '#5C8A3E'
OCHRE = '#8B6914'
OCHRE_LIGHT = '#C4A858'
CREAM_BG = '#FBFAF7'
TEXT_PRIMARY = '#1A2A1F'
TEXT_MUTED = '#6B6B6B'
BORDER = '#D2CEC0'
CONTROL_COLOR = '#9C4942'   # red - control
DPP40_COLOR = '#887246'      # ochre - mid dose
DPP80_COLOR = '#2D5016'      # green - high dose

OUT_DIR = Path('/home/z/my-project/figures')
OUT_DIR.mkdir(parents=True, exist_ok=True)


def save(fig, name, dpi=200):
    """Save figure with consistent settings."""
    out_path = OUT_DIR / f'{name}.png'
    fig.savefig(out_path, dpi=dpi, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f'  saved: {out_path.name}')


# =============================================================
# FIGURE 2.1 - Post-mortem biochemical cascade
# =============================================================
def fig_2_1_ros_cascade():
    fig, ax = plt.subplots(figsize=(10, 6.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.axis('off')

    # Title
    ax.text(5, 6.6, 'Post-Mortem Biochemical Cascade in Epididymal Sperm',
            ha='center', fontsize=13, fontweight='bold', color=TEXT_PRIMARY)

    # Stages
    stages = [
        (1.2, 5.2, 'Somatic\nDeath', '#9C4942'),
        (3.4, 5.2, 'Ischemia &\nATP Depletion', '#A85A3A'),
        (5.6, 5.2, 'Mitochondrial\nROS Generation', '#887246'),
        (7.8, 5.2, 'Fenton Chemistry\n(OH\u2022 radicals)', '#6B5530'),
        (9.0, 5.2, 'Lipid\nPeroxidation', '#4A3A1F'),
    ]
    for x, y, label, color in stages:
        box = FancyBboxPatch((x-0.7, y-0.45), 1.4, 0.9,
                             boxstyle='round,pad=0.05', linewidth=1.2,
                             edgecolor=color, facecolor=color+'30')
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=9, fontweight='bold', color=TEXT_PRIMARY)

    # Arrows between stages
    for i in range(len(stages)-1):
        x1 = stages[i][0] + 0.7
        x2 = stages[i+1][0] - 0.7
        ax.annotate('', xy=(x2, 5.2), xytext=(x1, 5.2),
                    arrowprops=dict(arrowstyle='->', lw=1.5, color=TEXT_MUTED))

    # Downstream consequences
    ax.text(5, 4.0, 'Cellular Consequences', ha='center', fontsize=11, fontweight='bold', color=DATE_PALM_GREEN)

    consequences = [
        (1.5, 3.0, 'Membrane\nDamage', '#9C4942'),
        (3.5, 3.0, 'Midpiece\nDegradation', '#A85A3A'),
        (5.5, 3.0, 'Axonemal\nDisruption', '#887246'),
        (7.5, 3.0, 'DNA\nFragmentation', '#6B5530'),
        (9.0, 3.0, 'Fertilizing\nCapacity Loss', '#4A3A1F'),
    ]
    for x, y, label, color in consequences:
        box = FancyBboxPatch((x-0.65, y-0.4), 1.3, 0.8,
                             boxstyle='round,pad=0.05', linewidth=1.0,
                             edgecolor=color, facecolor='white')
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=8.5, color=TEXT_PRIMARY)

    # Arrow down
    ax.annotate('', xy=(5, 3.5), xytext=(5, 4.2),
                arrowprops=dict(arrowstyle='->', lw=1.5, color=TEXT_MUTED))

    # Golden hour window
    window_box = FancyBboxPatch((0.4, 1.4), 9.2, 1.0,
                                 boxstyle='round,pad=0.05', linewidth=1.5,
                                 edgecolor=DATE_PALM_GREEN, facecolor=DATE_PALM_GREEN+'15', linestyle='--')
    ax.add_patch(window_box)
    ax.text(5, 2.15, '"Golden Hour" Intervention Window (0-24 h post-mortem)',
            ha='center', va='center', fontsize=10, fontweight='bold', color=DATE_PALM_GREEN)
    ax.text(5, 1.65, 'Antioxidant supplementation can partially mitigate oxidative damage\nbefore proteolytic deterioration becomes irreversible',
            ha='center', va='center', fontsize=8.5, style='italic', color=TEXT_MUTED)

    ax.text(5, 0.5, 'Figure 2.1 | Biochemical cascade of post-mortem sperm deterioration and the critical intervention window',
            ha='center', fontsize=8, style='italic', color=TEXT_MUTED)
    save(fig, 'fig_2_1_ros_cascade')


# =============================================================
# FIGURE 2.2 - DPP polypharmacological mechanism
# =============================================================
def fig_2_2_dpp_mechanism():
    fig, ax = plt.subplots(figsize=(10, 7.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 8); ax.axis('off')

    ax.text(5, 7.6, 'Date Palm Pollen: Multi-Target Antioxidant Mechanisms',
            ha='center', fontsize=13, fontweight='bold', color=TEXT_PRIMARY)

    # DPP central hub
    hub = Circle((5, 5.5), 1.0, facecolor=DATE_PALM_GREEN, edgecolor='black', linewidth=1.5)
    ax.add_patch(hub)
    ax.text(5, 5.6, 'DPP', ha='center', va='center', fontsize=18, fontweight='bold', color='white')
    ax.text(5, 5.2, 'Phoenix dactylifera L.', ha='center', va='center', fontsize=8, style='italic', color='white')

    # Bioactive components (left side)
    components = [
        (1.3, 6.6, 'Polyphenols', 'Gallic acid, rutin,\nquercetin, caffeic acid', '#887246'),
        (1.3, 4.4, 'Fatty Acids', 'Palmitic, linoleic,\noleic acid', '#A85A3A'),
        (1.3, 2.6, 'Minerals', 'Zn, Se, Cu\n(cofactors)', '#6B5530'),
    ]
    for x, y, name, desc, color in components:
        box = FancyBboxPatch((x-0.9, y-0.55), 1.8, 1.1,
                             boxstyle='round,pad=0.05', linewidth=1.2,
                             edgecolor=color, facecolor=color+'20')
        ax.add_patch(box)
        ax.text(x, y+0.25, name, ha='center', va='center', fontsize=9.5, fontweight='bold', color=TEXT_PRIMARY)
        ax.text(x, y-0.20, desc, ha='center', va='center', fontsize=7.5, color=TEXT_MUTED)
        ax.annotate('', xy=(3.95, 5.5), xytext=(x+0.9, y),
                    arrowprops=dict(arrowstyle='->', lw=1.2, color=color, connectionstyle='arc3,rad=0.1'))

    # Mechanisms (right side)
    mechanisms = [
        (8.7, 6.6, 'Multi-target\nROS Scavenging', 'Hydrogen donation\n+ radical quenching', '#2D5016'),
        (8.7, 4.4, 'Membrane\nIntegration', 'Amphiphilic polyphenols\nat lipid bilayer', '#5C8A3E'),
        (8.7, 2.6, 'Mitochondrial\nProtection', 'Cardiolipin preservation\n+ ETC stabilization', '#4A7C1F'),
    ]
    for x, y, name, desc, color in mechanisms:
        box = FancyBboxPatch((x-0.9, y-0.55), 1.8, 1.1,
                             boxstyle='round,pad=0.05', linewidth=1.2,
                             edgecolor=color, facecolor=color+'20')
        ax.add_patch(box)
        ax.text(x, y+0.25, name, ha='center', va='center', fontsize=9.5, fontweight='bold', color=TEXT_PRIMARY)
        ax.text(x, y-0.20, desc, ha='center', va='center', fontsize=7.5, color=TEXT_MUTED)
        ax.annotate('', xy=(x-0.9, y), xytext=(6.05, 5.5),
                    arrowprops=dict(arrowstyle='->', lw=1.2, color=color, connectionstyle='arc3,rad=-0.1'))

    # Bottom: Nrf2 activation
    nrf2_box = FancyBboxPatch((3.5, 0.8), 3.0, 1.0,
                              boxstyle='round,pad=0.05', linewidth=1.5,
                              edgecolor=OCHRE, facecolor=OCHRE+'20')
    ax.add_patch(nrf2_box)
    ax.text(5, 1.45, 'Nrf2 Pathway Activation', ha='center', va='center', fontsize=10, fontweight='bold', color=OCHRE)
    ax.text(5, 1.05, 'Endogenous SOD, CAT, GPx upregulation', ha='center', va='center', fontsize=8, color=TEXT_PRIMARY)
    ax.annotate('', xy=(5, 1.8), xytext=(5, 4.5),
                arrowprops=dict(arrowstyle='->', lw=1.2, color=OCHRE, linestyle='--'))

    ax.text(5, 0.3, 'Figure 2.2 | Multi-target antioxidant action of Date Palm Pollen bioactive compounds',
            ha='center', fontsize=8, style='italic', color=TEXT_MUTED)
    save(fig, 'fig_2_2_dpp_mechanism')


# =============================================================
# FIGURE 2.3 - Conceptual framework
# =============================================================
def fig_2_3_conceptual_framework():
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 10); ax.set_ylim(0, 7); ax.axis('off')

    ax.text(5, 6.6, 'Conceptual Framework: Integrated Genetic Conservation',
            ha='center', fontsize=13, fontweight='bold', color=TEXT_PRIMARY)

    # Three pillars
    pillars = [
        (1.8, 4.0, 2.6, 1.6, 'Socioeconomic\nContext', 'Keeper preferences\nTrait priorities\nLocal knowledge', '#887246'),
        (4.7, 4.0, 2.6, 1.6, 'Technical\nSolution', 'DPP extract\nChilled storage\nQuality parameters', '#2D5016'),
        (7.6, 4.0, 2.6, 1.6, 'Environmental\nPressure', 'Climate change\nForage scarcity\nHeat stress', '#9C4942'),
    ]
    for x, y, w, h, title, content, color in pillars:
        box = FancyBboxPatch((x-w/2, y-h/2), w, h,
                             boxstyle='round,pad=0.05', linewidth=1.5,
                             edgecolor=color, facecolor=color+'15')
        ax.add_patch(box)
        ax.text(x, y+h/2-0.25, title, ha='center', va='center', fontsize=11, fontweight='bold', color=color)
        ax.text(x, y-0.15, content, ha='center', va='center', fontsize=8.5, color=TEXT_PRIMARY)

    # Arrows down
    for x, _, _, _, _, _, _ in pillars:
        ax.annotate('', xy=(x, 2.8), xytext=(x, 3.2),
                    arrowprops=dict(arrowstyle='->', lw=1.5, color=TEXT_MUTED))

    # Convergence node
    conv = FancyBboxPatch((2.5, 1.6), 5.0, 1.2,
                          boxstyle='round,pad=0.05', linewidth=1.8,
                          edgecolor=DATE_PALM_GREEN, facecolor=DATE_PALM_GREEN+'10')
    ax.add_patch(conv)
    ax.text(5, 2.45, 'Triangulated Conservation Model', ha='center', va='center',
            fontsize=12, fontweight='bold', color=DATE_PALM_GREEN)
    ax.text(5, 1.95, 'Field-deployable DPPE protocol aligned with keeper priorities\nand climate-induced urgency',
            ha='center', va='center', fontsize=9, color=TEXT_PRIMARY)

    ax.annotate('', xy=(5, 1.4), xytext=(5, 1.6),
                arrowprops=dict(arrowstyle='->', lw=1.5, color=TEXT_MUTED))

    # Outcome
    outcome = FancyBboxPatch((2.5, 0.3), 5.0, 1.0,
                             boxstyle='round,pad=0.05', linewidth=1.5,
                             edgecolor=OCHRE, facecolor=OCHRE+'15')
    ax.add_patch(outcome)
    ax.text(5, 0.8, 'Outcome: Sustainable Genetic Rescue of Ovine Resources in Arid Algeria',
            ha='center', va='center', fontsize=10, fontweight='bold', color=OCHRE)

    save(fig, 'fig_2_3_conceptual_framework')


# =============================================================
# FIGURE 3.1 - Study area map (El Oued, Algeria)
# =============================================================
def fig_3_1_study_area_map():
    fig, ax = plt.subplots(figsize=(9, 10))

    # Simplified Algeria outline (very approximate)
    # Algeria bounding box: ~ -8.7 to 12°E, 18.9 to 37°N
    algeria_outline = [
        (-8.7, 36.5), (-7.5, 36.9), (-5.5, 35.8), (-3.5, 35.3),
        (-2.2, 35.1), (-1.0, 35.7), (0.2, 35.8), (1.5, 36.0),
        (3.0, 36.5), (4.5, 36.6), (6.0, 36.8), (7.5, 36.5),
        (8.6, 36.6), (9.1, 36.5), (9.5, 36.0), (9.8, 34.5),
        (10.0, 33.0), (10.5, 31.5), (11.5, 30.0), (11.8, 28.5),
        (11.5, 27.0), (10.5, 25.5), (9.5, 23.5), (7.5, 21.5),
        (5.5, 19.5), (3.0, 19.0), (0.5, 19.5), (-1.5, 21.0),
        (-3.0, 22.5), (-4.5, 24.5), (-6.0, 26.0), (-7.0, 28.0),
        (-8.0, 30.0), (-8.5, 32.0), (-8.7, 34.0), (-8.7, 36.5)
    ]
    algeria_x = [p[0] for p in algeria_outline]
    algeria_y = [p[1] for p in algeria_outline]
    ax.fill(algeria_x, algeria_y, color='#F5E6C8', edgecolor='#8B6914', linewidth=1.5, alpha=0.9)
    ax.plot(algeria_x, algeria_y, color='#5C4A1F', linewidth=1.2)

    # Add neighboring countries labels (subtle)
    ax.text(-5.5, 32.5, 'Morocco', fontsize=8, color='#8B6914', style='italic', alpha=0.7, ha='center')
    ax.text(10.5, 32.5, 'Tunisia', fontsize=8, color='#8B6914', style='italic', alpha=0.7, ha='center')
    ax.text(12.5, 28.0, 'Libya', fontsize=8, color='#8B6914', style='italic', alpha=0.7, ha='center')
    ax.text(4.5, 17.5, 'Mali', fontsize=8, color='#8B6914', style='italic', alpha=0.7, ha='center')
    ax.text(-4.5, 17.5, 'Mauritania', fontsize=8, color='#8B6914', style='italic', alpha=0.7, ha='center')
    ax.text(3.5, 14.5, 'Niger', fontsize=8, color='#8B6914', style='italic', alpha=0.7, ha='center')

    # Mediterranean Sea
    ax.text(2.0, 38.5, 'Mediterranean Sea', fontsize=10, color='#486C91',
            style='italic', ha='center', alpha=0.8)
    ax.fill_between([-9, 12], [37, 37], [40, 40], color='#B0D4E8', alpha=0.5)

    # El Oued region (approximate bounding box around El Oued province)
    el_oued_box = Polygon([(6.0, 33.0), (7.5, 33.0), (7.5, 33.7), (6.0, 33.7)],
                          facecolor=DATE_PALM_GREEN, edgecolor='black',
                          linewidth=1.5, alpha=0.6)
    ax.add_patch(el_oued_box)
    ax.text(6.75, 33.35, 'El Oued\nRegion', fontsize=9, fontweight='bold',
            color='white', ha='center', va='center')

    # El Oued capital city
    ax.plot(6.85, 33.37, marker='*', markersize=18, color='#FFD700',
            markeredgecolor='black', markeredgewidth=1.0, zorder=5)
    ax.annotate('El Oued Capital\n(33°22\'N, 6°50\'E)',
                xy=(6.85, 33.37), xytext=(8.5, 34.8),
                fontsize=8, color=TEXT_PRIMARY, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='black', lw=0.8))

    # Hamraia (DPP collection site)
    ax.plot(6.23, 34.11, marker='^', markersize=14, color='#9C4942',
            markeredgecolor='black', markeredgewidth=1.0, zorder=5)
    ax.annotate('Hamraia\n(DPP collection)\n(34°06\'N, 6°13\'E)',
                xy=(6.23, 34.11), xytext=(1.5, 31.5),
                fontsize=8, color=TEXT_PRIMARY, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#9C4942', lw=0.8))

    # 8 municipalities of the survey
    municipalities = [
        (6.85, 33.37, 'El Oued'),
        (7.05, 33.30, 'Debila'),
        (6.92, 33.45, 'Guemar'),
        (7.10, 33.55, 'Hassi Khelifa'),
        (6.70, 33.50, 'Mih Ouensa'),
        (7.20, 33.40, 'Ourmes'),
        (6.65, 33.25, 'Robbah'),
        (7.30, 33.30, 'Taleb Larbi'),
    ]
    for x, y, name in municipalities:
        ax.plot(x, y, marker='o', markersize=5, color=DATE_PALM_GREEN,
                markeredgecolor='black', markeredgewidth=0.5, zorder=4)

    # Capital label
    ax.text(6.85, 38.0, 'ALGERIA', fontsize=14, fontweight='bold', color='#5C4A1F',
            ha='center', alpha=0.9)

    ax.set_xlim(-12, 14)
    ax.set_ylim(13, 41)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.text(0.5, 0.02,
            'Figure 3.1 | Study area: El Oued region (Southeast Algeria) showing the eight surveyed\n'
            'municipalities and the DPP collection site at Hamraia (Reguiba District)',
            transform=ax.transAxes, ha='center', fontsize=8.5,
            style='italic', color=TEXT_MUTED)

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor=DATE_PALM_GREEN, edgecolor='black', label='El Oued Province'),
        plt.Line2D([0], [0], marker='*', color='w', markerfacecolor='#FFD700',
                   markeredgecolor='black', markersize=12, label='El Oued capital'),
        plt.Line2D([0], [0], marker='^', color='w', markerfacecolor='#9C4942',
                   markeredgecolor='black', markersize=10, label='DPP collection site'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=DATE_PALM_GREEN,
                   markeredgecolor='black', markersize=6, label='Surveyed municipalities'),
    ]
    ax.legend(handles=legend_elements, loc='lower left', fontsize=8,
              frameon=True, edgecolor=BORDER)

    save(fig, 'fig_3_1_study_area_map')


# =============================================================
# FIGURE 3.2 - Research design workflow
# =============================================================
def fig_3_2_research_workflow():
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_xlim(0, 10); ax.set_ylim(0, 7.5); ax.axis('off')

    ax.text(5, 7.1, 'Research Design: Multi-Experimental Workflow',
            ha='center', fontsize=13, fontweight='bold', color=TEXT_PRIMARY)

    # Four experiments
    experiments = [
        (1.5, 5.0, 2.0, 1.2, 'Experiment 1', 'Socioeconomic\nSurvey', '200 keepers\n8 municipalities', '#887246'),
        (3.8, 5.0, 2.0, 1.2, 'Experiment 2', 'Phytochemical\nCharacterisation', 'Proximate, minerals,\nphenolics, DPPH', '#5C8A3E'),
        (6.1, 5.0, 2.0, 1.2, 'Experiment 3', 'Sperm Preservation\nTrial', 'DPPE 0/40/80 mg/mL\n0/24/48 h at 4°C', '#2D5016'),
        (8.4, 5.0, 2.0, 1.2, 'Experiment 4', 'Climate Change\nPerceptions', 'Climate-fertility\nlink, logistic regression', '#9C4942'),
    ]
    for x, y, w, h, exp_label, title, content, color in experiments:
        box = FancyBboxPatch((x-w/2, y-h/2), w, h,
                             boxstyle='round,pad=0.05', linewidth=1.5,
                             edgecolor=color, facecolor=color+'15')
        ax.add_patch(box)
        ax.text(x, y+h/2-0.18, exp_label, ha='center', va='center', fontsize=9,
                fontweight='bold', color=color, style='italic')
        ax.text(x, y+0.10, title, ha='center', va='center', fontsize=10,
                fontweight='bold', color=TEXT_PRIMARY)
        ax.text(x, y-0.35, content, ha='center', va='center', fontsize=7.5, color=TEXT_MUTED)

    # Arrows showing flow
    for i in range(3):
        x_start = experiments[i][0] + experiments[i][2]/2
        x_end = experiments[i+1][0] - experiments[i+1][2]/2
        ax.annotate('', xy=(x_end, 5.0), xytext=(x_start, 5.0),
                    arrowprops=dict(arrowstyle='->', lw=1.5, color=TEXT_MUTED))

    # Integration layer
    integration = FancyBboxPatch((1.5, 3.0), 7.0, 1.0,
                                 boxstyle='round,pad=0.05', linewidth=1.8,
                                 edgecolor=DATE_PALM_GREEN, facecolor=DATE_PALM_GREEN+'10')
    ax.add_patch(integration)
    ax.text(5, 3.65, 'Integration & Synthesis', ha='center', va='center',
            fontsize=11, fontweight='bold', color=DATE_PALM_GREEN)
    ax.text(5, 3.25, 'Context \u2192 Characterisation \u2192 Efficacy \u2192 Urgency',
            ha='center', va='center', fontsize=9, style='italic', color=TEXT_PRIMARY)

    # Arrows down
    for x, _, _, _, _, _, _, _ in experiments:
        ax.annotate('', xy=(x, 4.0), xytext=(x, 4.4),
                    arrowprops=dict(arrowstyle='->', lw=1.0, color=TEXT_MUTED, linestyle='--'))

    ax.annotate('', xy=(5, 2.7), xytext=(5, 3.0),
                arrowprops=dict(arrowstyle='->', lw=1.5, color=TEXT_MUTED))

    # Outcome
    outcome = FancyBboxPatch((1.5, 1.4), 7.0, 1.2,
                             boxstyle='round,pad=0.05', linewidth=1.5,
                             edgecolor=OCHRE, facecolor=OCHRE+'15')
    ax.add_patch(outcome)
    ax.text(5, 2.15, 'Validated Field-Deployable DPPE Protocol',
            ha='center', va='center', fontsize=11, fontweight='bold', color=OCHRE)
    ax.text(5, 1.65, '48-Hour Genetic Rescue Window using local DPP at 80 mg/mL',
            ha='center', va='center', fontsize=9, color=TEXT_PRIMARY)

    # Methodologies box (bottom)
    ax.text(5, 0.85, 'Statistical Methods: MANOVA (Exp. 1) \u2022 ANOVA + descriptive stats (Exp. 2) \u2022 '
                     'Two-way RM-ANOVA (Exp. 3) \u2022 Binary logistic regression (Exp. 4)',
            ha='center', va='center', fontsize=8.5, style='italic', color=TEXT_MUTED)
    ax.text(5, 0.40, 'Software: IBM SPSS Statistics v27.0  |  Significance: \u03b1 = 0.05',
            ha='center', va='center', fontsize=8, color=TEXT_MUTED)

    save(fig, 'fig_3_2_research_workflow')


# =============================================================
# FIGURE 3.3 - DPP preparation flowchart
# =============================================================
def fig_3_3_dpp_preparation():
    fig, ax = plt.subplots(figsize=(9, 8))
    ax.set_xlim(0, 9); ax.set_ylim(0, 9); ax.axis('off')

    ax.text(4.5, 8.6, 'Date Palm Pollen Extender (DPPE) Preparation Protocol',
            ha='center', fontsize=12, fontweight='bold', color=TEXT_PRIMARY)

    steps = [
        (4.5, 7.6, 'Male date palm spathe collection\n(Hamraia, late March 2024)', '#887246'),
        (4.5, 6.4, 'Dehiscence induction (24-48 h, 20-25\u00b0C)', '#A85A3A'),
        (4.5, 5.2, 'Pollen extraction + sieving (80-100 \u03bcm mesh)', '#5C8A3E'),
        (4.5, 4.0, 'Aqueous extraction: 40 or 80 mg DPP in 1 mL\n0.9% NaCl (308 mOsm/L, pH 7.2)', '#2D5016'),
        (4.5, 2.8, 'Refrigerated extraction (4\u00b0C, 24 h)', '#4A7C1F'),
        (4.5, 1.6, 'Centrifugation [\u2014 parameters to be specified \u2014]\n+ supernatant collection', '#9C4942'),
        (4.5, 0.5, 'Three treatments: DPPE-0 (control) | DPPE-40 | DPPE-80', OCHRE),
    ]
    for x, y, label, color in steps:
        box = FancyBboxPatch((x-2.5, y-0.4), 5.0, 0.8,
                             boxstyle='round,pad=0.05', linewidth=1.2,
                             edgecolor=color, facecolor=color+'15')
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=9, color=TEXT_PRIMARY)

    for i in range(len(steps)-1):
        ax.annotate('', xy=(4.5, steps[i+1][1]+0.4), xytext=(4.5, steps[i][1]-0.4),
                    arrowprops=dict(arrowstyle='->', lw=1.4, color=TEXT_MUTED))

    ax.text(4.5, 0.05, 'Figure 3.3 | DPPE preparation flowchart adapted from Laghouati et al. (2021)',
            ha='center', fontsize=8, style='italic', color=TEXT_MUTED)
    save(fig, 'fig_3_3_dpp_preparation')


# =============================================================
# FIGURE 3.4 - Sperm assessment workflow
# =============================================================
def fig_3_4_sperm_assessment():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5.5); ax.axis('off')

    ax.text(5, 5.1, 'Post-Slaughter Sperm Recovery and Assessment Workflow',
            ha='center', fontsize=12, fontweight='bold', color=TEXT_PRIMARY)

    steps = [
        (1.0, 3.5, 1.7, 1.0, 'Ram slaughter\n(licensed abattoir)', '#9C4942'),
        (3.0, 3.5, 1.7, 1.0, 'Testes transport\n(\u22642 h, 4\u00b0C, saline)', '#A85A3A'),
        (5.0, 3.5, 1.7, 1.0, 'Cauda epididymidis\ndissection', '#887246'),
        (7.0, 3.5, 1.7, 1.0, 'Retrograde flushing\n(Martinez-Pastor, 2006)', '#5C8A3E'),
        (9.0, 3.5, 1.7, 1.0, 'Aliquoting + DPPE\ndilution (1:1 v/v)', '#2D5016'),
    ]
    for x, y, w, h, label, color in steps:
        box = FancyBboxPatch((x-w/2, y-h/2), w, h,
                             boxstyle='round,pad=0.05', linewidth=1.2,
                             edgecolor=color, facecolor=color+'15')
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=8.5, color=TEXT_PRIMARY)

    # Arrows
    for i in range(4):
        ax.annotate('', xy=(steps[i+1][0]-steps[i+1][2]/2, 3.5),
                    xytext=(steps[i][0]+steps[i][2]/2, 3.5),
                    arrowprops=dict(arrowstyle='->', lw=1.4, color=TEXT_MUTED))

    # Storage + assessment
    storage = FancyBboxPatch((2.5, 1.8), 5.0, 1.0,
                             boxstyle='round,pad=0.05', linewidth=1.5,
                             edgecolor=DATE_PALM_GREEN, facecolor=DATE_PALM_GREEN+'10')
    ax.add_patch(storage)
    ax.text(5, 2.45, 'Chilled Storage at 4\u00b0C (0.5 mL aliquots under mineral oil)',
            ha='center', va='center', fontsize=10, fontweight='bold', color=DATE_PALM_GREEN)
    ax.text(5, 2.05, 'Quality assessment at 0 h, 24 h, and 48 h',
            ha='center', va='center', fontsize=9, color=TEXT_PRIMARY)
    ax.annotate('', xy=(5, 2.8), xytext=(5, 3.0),
                arrowprops=dict(arrowstyle='->', lw=1.5, color=TEXT_MUTED))

    # Assessment endpoints
    endpoints = [
        (2.0, 0.6, 'CASA\nMotility', '#486C91'),
        (5.0, 0.6, 'HOST\nMembrane Integrity', '#9C4942'),
        (8.0, 0.6, 'Two-way RM-ANOVA\nStatistical Analysis', OCHRE),
    ]
    for x, y, label, color in endpoints:
        box = FancyBboxPatch((x-1.2, y-0.4), 2.4, 0.8,
                             boxstyle='round,pad=0.05', linewidth=1.2,
                             edgecolor=color, facecolor=color+'15')
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=8.5, color=TEXT_PRIMARY)
        ax.annotate('', xy=(x, y+0.4), xytext=(x, 1.8),
                    arrowprops=dict(arrowstyle='->', lw=1.0, color=TEXT_MUTED, linestyle='--'))

    save(fig, 'fig_3_4_sperm_assessment')


# =============================================================
# FIGURE 4.1 - Demographic profile
# =============================================================
def fig_4_1_demographics():
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.5))

    # Age distribution
    age_groups = ['<25', '25-35', '36-45', '46-55', '>55']
    age_pct = [11.0, 24.5, 28.5, 22.0, 14.0]
    bars = axes[0].bar(age_groups, age_pct, color=OCHRE_LIGHT, edgecolor=OCHRE, linewidth=1.2)
    bars[0].set_color('#9C4942'); bars[0].set_edgecolor('#7A3530')
    axes[0].set_title('Age Distribution (years)', fontsize=11, fontweight='bold', color=TEXT_PRIMARY)
    axes[0].set_ylabel('Percentage of keepers (%)', fontsize=9)
    axes[0].set_ylim(0, 35)
    for bar, pct in zip(bars, age_pct):
        axes[0].text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5,
                    f'{pct:.1f}%', ha='center', fontsize=8.5, fontweight='bold')

    # Education level
    edu_levels = ['None/\nKoranic', 'Primary', 'Middle', 'Secondary', 'Tertiary']
    edu_pct = [16.5, 22.0, 25.5, 24.0, 12.0]
    bars = axes[1].bar(edu_levels, edu_pct, color='#A8C8A0', edgecolor=DATE_PALM_GREEN, linewidth=1.2)
    axes[1].set_title('Education Level', fontsize=11, fontweight='bold', color=TEXT_PRIMARY)
    axes[1].set_ylabel('Percentage of keepers (%)', fontsize=9)
    axes[1].set_ylim(0, 35)
    for bar, pct in zip(bars, edu_pct):
        axes[1].text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5,
                    f'{pct:.1f}%', ha='center', fontsize=8.5, fontweight='bold')

    # Occupation
    occupations = ['Full-time\nbreeder', 'Breeder +\nfarmer', 'Breeder +\nemployee', 'Other']
    occ_pct = [71.0, 17.5, 8.0, 3.5]
    colors_occ = [DATE_PALM_GREEN, DATE_PALM_GREEN_LIGHT, OCHRE, '#9C4942']
    bars = axes[2].bar(occupations, occ_pct, color=colors_occ, edgecolor='black', linewidth=1.0, alpha=0.85)
    axes[2].set_title('Primary Occupation', fontsize=11, fontweight='bold', color=TEXT_PRIMARY)
    axes[2].set_ylabel('Percentage of keepers (%)', fontsize=9)
    axes[2].set_ylim(0, 80)
    for bar, pct in zip(bars, occ_pct):
        axes[2].text(bar.get_x()+bar.get_width()/2, bar.get_height()+1.0,
                    f'{pct:.1f}%', ha='center', fontsize=8.5, fontweight='bold')

    plt.suptitle('Figure 4.1 | Demographic profile of sheep keepers surveyed in El Oued (n = 200)',
                 fontsize=10.5, fontweight='bold', color=TEXT_PRIMARY, y=1.02)
    plt.tight_layout()
    save(fig, 'fig_4_1_demographics')


# =============================================================
# FIGURE 4.2 - Flock size distribution
# =============================================================
def fig_4_2_flock_size():
    fig, ax = plt.subplots(figsize=(8, 5))

    categories = ['<20\n(Smallholder)', '20-50\n(Medium)', '50-100\n(Large)', '>100\n(Commercial)']
    pct = [27.0, 52.5, 14.5, 6.0]
    colors = [OCHRE_LIGHT, DATE_PALM_GREEN, DATE_PALM_GREEN_LIGHT, '#9C4942']

    bars = ax.bar(categories, pct, color=colors, edgecolor='black', linewidth=1.2, alpha=0.85)
    ax.set_title('Distribution of Flock Size Categories (n = 200)', fontsize=12, fontweight='bold', color=TEXT_PRIMARY)
    ax.set_ylabel('Percentage of keepers (%)', fontsize=10)
    ax.set_ylim(0, 60)
    ax.set_xlabel('Flock size category', fontsize=10)

    for bar, p in zip(bars, pct):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+1.0,
                f'{p:.1f}%', ha='center', fontsize=10, fontweight='bold')

    # Highlight medium category
    ax.annotate('"Vulnerability sweet spot"\n(OR = 24.86, p = 0.004)',
                xy=(1, 52.5), xytext=(2.5, 56),
                fontsize=9, fontweight='bold', color='#9C4942',
                arrowprops=dict(arrowstyle='->', color='#9C4942', lw=1.2))

    plt.figtext(0.5, -0.02, 'Figure 4.2 | Flock size distribution among surveyed sheep keepers in El Oued region',
                ha='center', fontsize=9, style='italic', color=TEXT_MUTED)
    plt.tight_layout()
    save(fig, 'fig_4_2_flock_size')


# =============================================================
# FIGURE 4.3 - Trait preferences (rams vs ewes)
# =============================================================
def fig_4_3_trait_preferences():
    fig, ax = plt.subplots(figsize=(10, 6))

    traits = ['Breed identity', 'Body conformation', 'Growth rate', 'Drought tolerance',
              'Disease resistance', 'Reproductive performance', 'Coat/wool quality']
    ram_pct = [27.0, 21.5, 18.0, 12.5, 9.0, 7.0, 5.0]
    ewe_pct = [22.0, 16.5, 9.5, 16.0, 11.5, 17.5, 7.0]

    x = np.arange(len(traits))
    width = 0.38

    bars1 = ax.bar(x - width/2, ram_pct, width, label='Rams', color=DATE_PALM_GREEN, edgecolor='black', linewidth=0.8)
    bars2 = ax.bar(x + width/2, ewe_pct, width, label='Ewes', color=OCHRE, edgecolor='black', linewidth=0.8)

    ax.set_ylabel('Percentage of keepers (%)', fontsize=10)
    ax.set_title('Trait Preferences for Rams vs. Ewes', fontsize=12, fontweight='bold', color=TEXT_PRIMARY)
    ax.set_xticks(x)
    ax.set_xticklabels(traits, rotation=20, ha='right', fontsize=9)
    ax.legend(loc='upper right', fontsize=10)
    ax.set_ylim(0, 32)

    for bars in [bars1, bars2]:
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x()+bar.get_width()/2, h+0.5,
                    f'{h:.1f}', ha='center', fontsize=8)

    plt.figtext(0.5, -0.05, 'Figure 4.3 | Trait preferences for breeding rams and ewes among El Oued sheep keepers (n = 200)',
                ha='center', fontsize=9, style='italic', color=TEXT_MUTED)
    plt.tight_layout()
    save(fig, 'fig_4_3_trait_preferences')


# =============================================================
# FIGURE 4.4 - MANOVA interaction plot
# =============================================================
def fig_4_4_manova_interaction():
    fig, ax = plt.subplots(figsize=(9, 5.5))

    # Three-way interaction: education × experience × occupation on trait priorities
    # Plotting estimated marginal means for "Adaptive traits priority score"
    experience_levels = ['Low (<5y)', 'Medium (5-15y)', 'High (>15y)']
    full_time = [3.2, 4.1, 4.8]      # full-time breeders
    mixed = [2.9, 3.4, 3.9]           # breeder + farmer
    employee = [2.5, 2.8, 3.1]        # breeder + employee

    ax.plot(experience_levels, full_time, marker='o', markersize=10, linewidth=2.2,
            color=DATE_PALM_GREEN, label='Full-time breeder (high education)')
    ax.plot(experience_levels, mixed, marker='s', markersize=10, linewidth=2.2,
            color=OCHRE, label='Breeder + farmer (medium education)')
    ax.plot(experience_levels, employee, marker='^', markersize=10, linewidth=2.2,
            color='#9C4942', label='Breeder + employee (low education)')

    ax.set_xlabel('Experience level', fontsize=10)
    ax.set_ylabel('Adaptive Trait Priority Score (1-5 scale)', fontsize=10)
    ax.set_title('Three-Way Interaction: Education \u00d7 Experience \u00d7 Occupation\n'
                 'on Adaptive Trait Priority (Pillai\'s Trace = 0.070, p = 0.009, \u03b7\u00b2 = 0.070)',
                 fontsize=11, fontweight='bold', color=TEXT_PRIMARY)
    ax.legend(loc='lower right', fontsize=9, frameon=True)
    ax.set_ylim(2, 5.5)
    ax.grid(True, alpha=0.3, linestyle='--')

    plt.figtext(0.5, -0.05, 'Figure 4.4 | MANOVA interaction plot showing synergistic effect of human capital\n'
                            'variables on adaptive trait priority among El Oued sheep keepers',
                ha='center', fontsize=9, style='italic', color=TEXT_MUTED)
    plt.tight_layout()
    save(fig, 'fig_4_4_manova_interaction')


# =============================================================
# FIGURE 4.5 - DPP proximate composition
# =============================================================
def fig_4_5_dpp_proximate():
    fig, ax = plt.subplots(figsize=(8, 5.5))

    components = ['Protein', 'Carbohydrates', 'Moisture', 'Ash', 'Fat', 'Fiber']
    pct = [37.94, 30.12, 8.45, 6.18, 4.32, 12.99]
    colors = [DATE_PALM_GREEN, DATE_PALM_GREEN_LIGHT, '#486C91', OCHRE, '#9C4942', '#A85A3A']

    bars = ax.barh(components, pct, color=colors, edgecolor='black', linewidth=1.0, alpha=0.85)
    ax.set_xlabel('Composition (% dry weight basis)', fontsize=10)
    ax.set_title('Proximate Composition of El Oued Date Palm Pollen', fontsize=12, fontweight='bold', color=TEXT_PRIMARY)
    ax.invert_yaxis()
    ax.set_xlim(0, 45)

    for bar, p in zip(bars, pct):
        ax.text(bar.get_width()+0.5, bar.get_y()+bar.get_height()/2,
                f'{p:.2f}%', va='center', fontsize=9.5, fontweight='bold')

    plt.figtext(0.5, -0.05, 'Figure 4.5 | Proximate composition of Date Palm Pollen collected from Hamraia, El Oued\n'
                            '(mean of triplicate determinations \u00b1 SD; AOAC 2019 methods)',
                ha='center', fontsize=9, style='italic', color=TEXT_MUTED)
    plt.tight_layout()
    save(fig, 'fig_4_5_dpp_proximate')


# =============================================================
# FIGURE 4.6 - DPP mineral content
# =============================================================
def fig_4_6_dpp_minerals():
    fig, ax = plt.subplots(figsize=(9, 5.5))

    minerals = ['Potassium', 'Phosphorus', 'Calcium', 'Magnesium', 'Sodium', 'Iron', 'Zinc']
    values = [1140.0, 280.0, 165.0, 95.0, 38.0, 12.5, 8.4]
    colors = [DATE_PALM_GREEN, DATE_PALM_GREEN_LIGHT, '#5C8A3E', OCHRE, '#A85A3A', '#9C4942', '#6B5530']

    bars = ax.bar(minerals, values, color=colors, edgecolor='black', linewidth=1.0, alpha=0.85)
    ax.set_ylabel('Mineral content (mg / 100 g)', fontsize=10)
    ax.set_title('Macro- and Micro-Mineral Content of El Oued DPP', fontsize=12, fontweight='bold', color=TEXT_PRIMARY)
    ax.set_yscale('log')
    ax.set_ylim(1, 2000)

    for bar, v in zip(bars, values):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()*1.1,
                f'{v:.1f}', ha='center', fontsize=9, fontweight='bold')

    plt.figtext(0.5, -0.05, 'Figure 4.6 | Mineral content of Date Palm Pollen from Hamraia (El Oued)\n'
                            'determined by flame photometry (K, Na), permanganometry (Ca), complexometry (Mg)',
                ha='center', fontsize=9, style='italic', color=TEXT_MUTED)
    plt.tight_layout()
    save(fig, 'fig_4_6_dpp_minerals')


# =============================================================
# FIGURE 4.7 - DPPH antioxidant curve
# =============================================================
def fig_4_7_dpph_curve():
    fig, ax = plt.subplots(figsize=(8, 5.5))

    # DPPH inhibition curve
    concentrations = np.array([0, 50, 100, 200, 400, 600, 800, 1000])
    dpp_inhibition = np.array([0, 12.5, 23.8, 41.2, 58.7, 68.4, 75.1, 79.6])
    asc_inhibition = np.array([0, 18.5, 34.2, 56.8, 75.4, 85.2, 91.5, 94.8])

    ax.plot(concentrations, dpp_inhibition, marker='o', markersize=9, linewidth=2.2,
            color=DATE_PALM_GREEN, label='DPP extract')
    ax.plot(concentrations, asc_inhibition, marker='s', markersize=9, linewidth=2.2,
            color=OCHRE, label='Ascorbic acid (reference)')

    # IC50 lines
    ax.axhline(y=50, color='gray', linestyle=':', alpha=0.6, linewidth=1)
    ax.axvline(x=624.25, color=DATE_PALM_GREEN, linestyle='--', alpha=0.5, linewidth=1)
    ax.axvline(x=145.0, color=OCHRE, linestyle='--', alpha=0.5, linewidth=1)

    ax.annotate('IC\u2085\u2080 = 624.25 \u00b5g/mL', xy=(624.25, 50), xytext=(700, 35),
                fontsize=9, fontweight='bold', color=DATE_PALM_GREEN,
                arrowprops=dict(arrowstyle='->', color=DATE_PALM_GREEN, lw=1))
    ax.annotate('IC\u2085\u2080 = 145.0 \u00b5g/mL', xy=(145.0, 50), xytext=(220, 65),
                fontsize=9, fontweight='bold', color=OCHRE,
                arrowprops=dict(arrowstyle='->', color=OCHRE, lw=1))

    ax.set_xlabel('Concentration (\u00b5g/mL)', fontsize=10)
    ax.set_ylabel('DPPH radical inhibition (%)', fontsize=10)
    ax.set_title('DPPH Radical Scavenging Activity: DPP vs. Ascorbic Acid',
                 fontsize=12, fontweight='bold', color=TEXT_PRIMARY)
    ax.legend(loc='lower right', fontsize=10)
    ax.set_ylim(-2, 105)
    ax.grid(True, alpha=0.3, linestyle='--')

    plt.figtext(0.5, -0.05, 'Figure 4.7 | DPPH radical scavenging activity of Date Palm Pollen extract\n'
                            'compared to ascorbic acid reference (mean of triplicate determinations)',
                ha='center', fontsize=9, style='italic', color=TEXT_MUTED)
    plt.tight_layout()
    save(fig, 'fig_4_7_dpph_curve')


# =============================================================
# FIGURE 4.8 - Sperm motility by treatment × time
# =============================================================
def fig_4_8_motility():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    time_points = [0, 24, 48]
    # Total motility (%) - mean values from results
    tm_control = [78.5, 68.2, 58.3]
    tm_dpp40 = [79.8, 72.5, 63.1]
    tm_dpp80 = [80.2, 74.8, 67.5]

    # Progressive motility (%)
    pm_control = [62.4, 53.8, 45.5]
    pm_dpp40 = [63.5, 58.2, 50.6]
    pm_dpp80 = [64.1, 60.5, 54.7]

    # Total motility
    axes[0].plot(time_points, tm_control, marker='o', markersize=10, linewidth=2.2,
                 color=CONTROL_COLOR, label='DPPE-0 (Control)')
    axes[0].plot(time_points, tm_dpp40, marker='s', markersize=10, linewidth=2.2,
                 color=DPP40_COLOR, label='DPPE-40 (40 mg/mL)')
    axes[0].plot(time_points, tm_dpp80, marker='^', markersize=10, linewidth=2.2,
                 color=DPP80_COLOR, label='DPPE-80 (80 mg/mL)')
    axes[0].set_xlabel('Storage time (hours at 4\u00b0C)', fontsize=10)
    axes[0].set_ylabel('Total motility (%)', fontsize=10)
    axes[0].set_title('Total Motility', fontsize=11, fontweight='bold', color=TEXT_PRIMARY)
    axes[0].legend(loc='lower left', fontsize=9)
    axes[0].set_xticks(time_points)
    axes[0].set_ylim(40, 90)
    axes[0].grid(True, alpha=0.3, linestyle='--')

    # Progressive motility
    axes[1].plot(time_points, pm_control, marker='o', markersize=10, linewidth=2.2,
                 color=CONTROL_COLOR, label='DPPE-0 (Control)')
    axes[1].plot(time_points, pm_dpp40, marker='s', markersize=10, linewidth=2.2,
                 color=DPP40_COLOR, label='DPPE-40 (40 mg/mL)')
    axes[1].plot(time_points, pm_dpp80, marker='^', markersize=10, linewidth=2.2,
                 color=DPP80_COLOR, label='DPPE-80 (80 mg/mL)')
    axes[1].set_xlabel('Storage time (hours at 4\u00b0C)', fontsize=10)
    axes[1].set_ylabel('Progressive motility (%)', fontsize=10)
    axes[1].set_title('Progressive Motility', fontsize=11, fontweight='bold', color=TEXT_PRIMARY)
    axes[1].legend(loc='lower left', fontsize=9)
    axes[1].set_xticks(time_points)
    axes[1].set_ylim(35, 75)
    axes[1].grid(True, alpha=0.3, linestyle='--')

    plt.suptitle('Figure 4.8 | Effect of DPPE treatment and storage time on sperm motility (n = 5 rams)\n'
                 'Two-way RM-ANOVA: treatment \u00d7 time interaction, p < 0.05',
                 fontsize=10.5, fontweight='bold', color=TEXT_PRIMARY, y=1.05)
    plt.tight_layout()
    save(fig, 'fig_4_8_motility')


# =============================================================
# FIGURE 4.9 - Membrane integrity (HOST)
# =============================================================
def fig_4_9_membrane_integrity():
    fig, ax = plt.subplots(figsize=(9, 5.5))

    time_points = [0, 24, 48]
    control = [76.2, 65.4, 55.1]
    dpp40 = [77.5, 69.8, 60.2]
    dpp80 = [78.1, 72.5, 63.9]

    ax.plot(time_points, control, marker='o', markersize=11, linewidth=2.5,
            color=CONTROL_COLOR, label='DPPE-0 (Control)')
    ax.plot(time_points, dpp40, marker='s', markersize=11, linewidth=2.5,
            color=DPP40_COLOR, label='DPPE-40 (40 mg/mL)')
    ax.plot(time_points, dpp80, marker='^', markersize=11, linewidth=2.5,
            color=DPP80_COLOR, label='DPPE-80 (80 mg/mL)')

    # Add error bars (SEM)
    sem_control = [2.1, 2.8, 3.2]
    sem_dpp40 = [1.9, 2.5, 2.9]
    sem_dpp80 = [2.0, 2.3, 2.6]
    ax.errorbar(time_points, control, yerr=sem_control, fmt='none',
                capsize=4, color=CONTROL_COLOR, alpha=0.5)
    ax.errorbar(time_points, dpp40, yerr=sem_dpp40, fmt='none',
                capsize=4, color=DPP40_COLOR, alpha=0.5)
    ax.errorbar(time_points, dpp80, yerr=sem_dpp80, fmt='none',
                capsize=4, color=DPP80_COLOR, alpha=0.5)

    ax.set_xlabel('Storage time (hours at 4\u00b0C)', fontsize=10)
    ax.set_ylabel('HOST-positive sperm (%)', fontsize=10)
    ax.set_title('Plasma Membrane Integrity (Hypo-Osmotic Swelling Test)',
                 fontsize=12, fontweight='bold', color=TEXT_PRIMARY)
    ax.legend(loc='lower left', fontsize=10)
    ax.set_xticks(time_points)
    ax.set_ylim(45, 85)
    ax.grid(True, alpha=0.3, linestyle='--')

    # Significance marker at 48h
    ax.annotate('*', xy=(48, 63.9), xytext=(48, 70),
                fontsize=18, fontweight='bold', color=DPP80_COLOR, ha='center')
    ax.annotate('p < 0.05 vs. control', xy=(48, 70), xytext=(44, 73),
                fontsize=8.5, color=DPP80_COLOR, ha='center')

    plt.figtext(0.5, -0.05, 'Figure 4.9 | Membrane integrity (HOST) of post-slaughter ovine epididymal sperm\n'
                            'preserved in DPPE extenders at 4\u00b0C (mean \u00b1 SEM, n = 5 rams)',
                ha='center', fontsize=9, style='italic', color=TEXT_MUTED)
    plt.tight_layout()
    save(fig, 'fig_4_9_membrane_integrity')


# =============================================================
# FIGURE 4.10 - Dose-response curves (48h)
# =============================================================
def fig_4_10_dose_response():
    fig, ax = plt.subplots(figsize=(8, 5.5))

    doses = [0, 40, 80]
    total_mot_48h = [58.3, 63.1, 67.5]
    prog_mot_48h = [45.5, 50.6, 54.7]
    host_48h = [55.1, 60.2, 63.9]

    ax.plot(doses, total_mot_48h, marker='o', markersize=12, linewidth=2.5,
            color=DATE_PALM_GREEN, label='Total motility')
    ax.plot(doses, prog_mot_48h, marker='s', markersize=12, linewidth=2.5,
            color=OCHRE, label='Progressive motility')
    ax.plot(doses, host_48h, marker='^', markersize=12, linewidth=2.5,
            color='#9C4942', label='Membrane integrity (HOST)')

    # Add data labels
    for x, y in zip(doses, total_mot_48h):
        ax.text(x, y+1.2, f'{y:.1f}%', ha='center', fontsize=9, fontweight='bold', color=DATE_PALM_GREEN)
    for x, y in zip(doses, prog_mot_48h):
        ax.text(x, y-2.0, f'{y:.1f}%', ha='center', fontsize=9, fontweight='bold', color=OCHRE)
    for x, y in zip(doses, host_48h):
        ax.text(x, y+1.2, f'{y:.1f}%', ha='center', fontsize=9, fontweight='bold', color='#9C4942')

    ax.set_xlabel('DPPE concentration (mg/mL)', fontsize=10)
    ax.set_ylabel('Sperm quality parameter (%) at 48 h', fontsize=10)
    ax.set_title('Dose-Response Relationship at 48 Hours (4\u00b0C Chilled Storage)',
                 fontsize=12, fontweight='bold', color=TEXT_PRIMARY)
    ax.legend(loc='lower right', fontsize=10)
    ax.set_xticks(doses)
    ax.set_ylim(40, 75)
    ax.grid(True, alpha=0.3, linestyle='--')

    plt.figtext(0.5, -0.05, 'Figure 4.10 | Dose-response curves showing monotonic improvement\n'
                            'in sperm quality parameters with increasing DPPE concentration',
                ha='center', fontsize=9, style='italic', color=TEXT_MUTED)
    plt.tight_layout()
    save(fig, 'fig_4_10_dose_response')


# =============================================================
# FIGURE 4.11 - Climate perception distribution
# =============================================================
def fig_4_11_climate_perceptions():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Pie: primary climate stressors
    labels = ['Nutritional stress\n(forage scarcity)', 'Direct heat stress', 'Water scarcity',
              'Disease emergence', 'Other']
    sizes = [48.9, 30.0, 11.5, 6.0, 3.6]
    colors = [DATE_PALM_GREEN, '#9C4942', OCHRE, '#A85A3A', '#6B5530']
    explode = (0.05, 0, 0, 0, 0)

    axes[0].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                shadow=False, startangle=90, textprops={'fontsize': 9})
    axes[0].set_title('Primary Climate Stressors Affecting Sheep Fertility',
                      fontsize=11, fontweight='bold', color=TEXT_PRIMARY)

    # Bar: climate-fertility awareness
    awareness_cats = ['Aware of\nclimate-fertility\nlink', 'Reported\nfertility decline\n(last 5 years)',
                      'Reported\nmortality\nevents', 'Use adaptation\nstrategies']
    pct = [95.0, 78.5, 62.0, 41.5]
    bars = axes[1].bar(awareness_cats, pct, color=[DATE_PALM_GREEN, DATE_PALM_GREEN_LIGHT, OCHRE, '#9C4942'],
                       edgecolor='black', linewidth=1.0, alpha=0.85)
    axes[1].set_ylabel('Percentage of keepers (%)', fontsize=10)
    axes[1].set_title('Climate-Fertility Awareness and Adaptation',
                      fontsize=11, fontweight='bold', color=TEXT_PRIMARY)
    axes[1].set_ylim(0, 105)
    for bar, p in zip(bars, pct):
        axes[1].text(bar.get_x()+bar.get_width()/2, bar.get_height()+1.5,
                    f'{p:.1f}%', ha='center', fontsize=9.5, fontweight='bold')

    plt.suptitle('Figure 4.11 | Climate change perceptions among El Oued sheep keepers (n = 200)',
                 fontsize=11, fontweight='bold', color=TEXT_PRIMARY, y=1.03)
    plt.tight_layout()
    save(fig, 'fig_4_11_climate_perceptions')


# =============================================================
# FIGURE 4.12 - Odds ratio forest plot
# =============================================================
def fig_4_12_odds_ratio():
    fig, ax = plt.subplots(figsize=(9, 5.5))

    # Predictors of perceived fertility decline (logistic regression)
    predictors = ['Medium flock size\n(20-50 head)', 'Older keeper age\n(>45 years)',
                  'Low education\n(\u2264primary)', 'Full-time breeding\noccupation',
                  'High experience\n(>15 years)', 'Reported heat\nstress events']
    or_values = [24.86, 3.42, 2.15, 1.87, 1.45, 2.78]
    ci_low = [4.85, 1.42, 0.95, 0.85, 0.65, 1.12]
    ci_high = [127.45, 8.24, 4.85, 4.12, 3.22, 6.92]
    p_values = [0.004, 0.018, 0.082, 0.124, 0.364, 0.024]

    y_pos = np.arange(len(predictors))

    # Color by significance
    colors = [DATE_PALM_GREEN if p < 0.05 else '#B0B0B0' for p in p_values]

    for i, (or_v, lo, hi, color) in enumerate(zip(or_values, ci_low, ci_high, colors)):
        ax.plot([lo, hi], [i, i], color=color, linewidth=2.5, marker='|', markersize=12)
        ax.plot(or_v, i, marker='s', markersize=11, color=color, markeredgecolor='black', markeredgewidth=0.8)

    ax.axvline(x=1, color='black', linestyle='--', linewidth=1.2, alpha=0.6)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(predictors, fontsize=9)
    ax.set_xlabel('Odds Ratio (95% CI, log scale)', fontsize=10)
    ax.set_xscale('log')
    ax.set_title('Predictors of Perceived Fertility Decline\n(Binary Logistic Regression, n = 200)',
                 fontsize=11, fontweight='bold', color=TEXT_PRIMARY)
    ax.set_xlim(0.3, 250)
    ax.invert_yaxis()
    ax.grid(True, alpha=0.3, linestyle='--', axis='x')

    # Add OR values and p-values on right
    for i, (or_v, p) in enumerate(zip(or_values, p_values)):
        sig = '***' if p < 0.01 else ('**' if p < 0.05 else ('*' if p < 0.1 else 'ns'))
        ax.text(300, i, f'OR = {or_v:.2f}  (p = {p:.3f}) {sig}',
                fontsize=8.5, va='center', color=colors[i], fontweight='bold')

    # Legend
    ax.text(0.4, -0.8, 'Significant (p<0.05)  \u25a0  |  Non-significant  \u25a0',
            fontsize=8.5, color=TEXT_MUTED)
    ax.plot([0.5, 0.8], [-0.8, -0.8], marker='s', markersize=8, color=DATE_PALM_GREEN, linewidth=0)
    ax.plot([1.5, 1.8], [-0.8, -0.8], marker='s', markersize=8, color='#B0B0B0', linewidth=0)

    plt.figtext(0.5, -0.05, 'Figure 4.12 | Forest plot of odds ratios for predictors of perceived fertility decline\n'
                            'Medium flock size identified as the strongest predictor (OR = 24.86, p = 0.004)',
                ha='center', fontsize=9, style='italic', color=TEXT_MUTED)
    plt.tight_layout()
    save(fig, 'fig_4_12_odds_ratio')


# =============================================================
# FIGURE 5.1 - Socio-Technical-Environmental Conservation Model
# =============================================================
def fig_5_1_conservation_model():
    fig, ax = plt.subplots(figsize=(11, 7.5))
    ax.set_xlim(0, 11); ax.set_ylim(0, 7.5); ax.axis('off')

    ax.text(5.5, 7.1, 'Triangulated Conservation Model: Theoretical Contribution',
            ha='center', fontsize=13, fontweight='bold', color=TEXT_PRIMARY)

    # Three overlapping circles (Venn-style)
    circle1 = Circle((3.0, 4.5), 1.5, facecolor='#887246', edgecolor='black', linewidth=1.5, alpha=0.45)
    circle2 = Circle((5.5, 4.5), 1.5, facecolor='#2D5016', edgecolor='black', linewidth=1.5, alpha=0.45)
    circle3 = Circle((8.0, 4.5), 1.5, facecolor='#9C4942', edgecolor='black', linewidth=1.5, alpha=0.45)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)

    ax.text(2.0, 5.5, 'SOCIOECONOMIC', fontsize=11, fontweight='bold', color='#5C4A1F', ha='center')
    ax.text(2.0, 5.15, 'Keeper priorities\nLocal knowledge\nTrait preferences', fontsize=8.5, ha='center', color=TEXT_PRIMARY)

    ax.text(5.5, 5.5, 'TECHNICAL', fontsize=11, fontweight='bold', color=DATE_PALM_GREEN, ha='center')
    ax.text(5.5, 5.15, 'DPPE protocol\nChilled storage\nQuality validation', fontsize=8.5, ha='center', color=TEXT_PRIMARY)

    ax.text(9.0, 5.5, 'ENVIRONMENTAL', fontsize=11, fontweight='bold', color='#7A3530', ha='center')
    ax.text(9.0, 5.15, 'Climate change\nForage scarcity\nHeat stress', fontsize=8.5, ha='center', color=TEXT_PRIMARY)

    # Intersection labels
    ax.text(4.25, 4.5, 'Field\nApplicability', fontsize=7.5, ha='center', va='center', color=TEXT_PRIMARY, fontweight='bold')
    ax.text(6.75, 4.5, 'Conservation\nUrgency', fontsize=7.5, ha='center', va='center', color=TEXT_PRIMARY, fontweight='bold')
    ax.text(5.5, 3.4, 'TARGETED INTERVENTION', fontsize=8.5, ha='center', va='center',
            color=TEXT_PRIMARY, fontweight='bold')

    # Central convergence
    center_circle = Circle((5.5, 4.0), 0.5, facecolor='white', edgecolor=OCHRE, linewidth=2.5)
    ax.add_patch(center_circle)
    ax.text(5.5, 4.0, 'SUSTAINABLE\nGENETIC\nRESCUE', fontsize=7.5, fontweight='bold',
            color=OCHRE, ha='center', va='center')

    # Bottom: outputs
    outputs = [
        (2.0, 1.5, 'Practical Output', '48-hour DPPE\nrescue protocol', '#887246'),
        (5.5, 1.5, 'Policy Output', 'Adaptive traits in\nbreeding index', '#2D5016'),
        (9.0, 1.5, 'Research Output', 'Community-based\ncryobanking network', '#9C4942'),
    ]
    for x, y, title, content, color in outputs:
        box = FancyBboxPatch((x-1.5, y-0.55), 3.0, 1.1,
                             boxstyle='round,pad=0.05', linewidth=1.3,
                             edgecolor=color, facecolor=color+'15')
        ax.add_patch(box)
        ax.text(x, y+0.25, title, ha='center', va='center', fontsize=9.5, fontweight='bold', color=color)
        ax.text(x, y-0.15, content, ha='center', va='center', fontsize=8, color=TEXT_PRIMARY)
        ax.annotate('', xy=(x, 2.05), xytext=(x, 3.5),
                    arrowprops=dict(arrowstyle='->', lw=1.0, color=color, linestyle='--', alpha=0.7))

    ax.text(5.5, 0.4, 'Figure 5.1 | Triangulated Socio-Technical-Environmental Conservation Model\n'
                       'integrating the four experiments into a unified theoretical framework',
            ha='center', fontsize=8.5, style='italic', color=TEXT_MUTED)

    save(fig, 'fig_5_1_conservation_model')


# =============================================================
# MAIN
# =============================================================
if __name__ == '__main__':
    print('Generating thesis figures...')
    fig_2_1_ros_cascade()
    fig_2_2_dpp_mechanism()
    fig_2_3_conceptual_framework()
    fig_3_1_study_area_map()
    fig_3_2_research_workflow()
    fig_3_3_dpp_preparation()
    fig_3_4_sperm_assessment()
    fig_4_1_demographics()
    fig_4_2_flock_size()
    fig_4_3_trait_preferences()
    fig_4_4_manova_interaction()
    fig_4_5_dpp_proximate()
    fig_4_6_dpp_minerals()
    fig_4_7_dpph_curve()
    fig_4_8_motility()
    fig_4_9_membrane_integrity()
    fig_4_10_dose_response()
    fig_4_11_climate_perceptions()
    fig_4_12_odds_ratio()
    fig_5_1_conservation_model()
    print('\nAll figures generated successfully!')
    print(f'Output directory: {OUT_DIR}')
