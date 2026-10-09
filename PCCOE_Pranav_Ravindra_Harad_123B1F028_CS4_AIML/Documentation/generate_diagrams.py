#!/usr/bin/env python3
"""
System Architecture & Workflow Diagram Generator
Generates high-resolution publication-quality PNG diagrams for Technical Report & Synopsis.
Student: Pranav Ravindra Harad | PRN: 123B1F028 | PCCOE, Pune
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_architecture_diagram(output_path: str):
    fig, ax = plt.subplots(figsize=(12, 7), dpi=300)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')
    ax.axis('off')

    # Title
    ax.text(6, 6.6, "AUTOSAFE-REVIEW: SYSTEM ARCHITECTURE", ha='center', va='center',
            color='#38bdf8', fontsize=15, fontweight='bold')
    ax.text(6, 6.25, "100% Air-Gapped Hybrid Diagnostic & Automotive ECU Review Assistant", ha='center', va='center',
            color='#94a3b8', fontsize=11)

    # Layer 1: Ingestion Layer (Top)
    rect1 = patches.FancyBboxPatch((0.8, 4.4), 10.4, 1.4, boxstyle="round,pad=0.2",
                                  edgecolor='#38bdf8', facecolor='#1e293b', linewidth=1.5)
    ax.add_patch(rect1)
    ax.text(1.2, 5.5, "1. MULTI-MODAL DIAGNOSTIC INGESTION LAYER", color='#38bdf8', fontsize=11, fontweight='bold')
    
    # Sub-boxes in Ingestion
    sub_boxes1 = [
        ("C/C++ ECU Source Code\n(AST Function Chunker)", 1.5, 4.6),
        ("ARM/GCC Build Logs\n(Warning Stream Parser)", 5.0, 4.6),
        ("OASIS SARIF Reports\n(Static Analysis Reader)", 8.5, 4.6)
    ]
    for text, x, y in sub_boxes1:
        srect = patches.FancyBboxPatch((x, y), 2.8, 0.7, boxstyle="round,pad=0.1",
                                      edgecolor='#475569', facecolor='#0f172a')
        ax.add_patch(srect)
        ax.text(x + 1.4, y + 0.35, text, ha='center', va='center', color='#f8fafc', fontsize=9)

    # Layer 2: Hybrid Diagnostic & Retrieval Core (Middle)
    rect2 = patches.FancyBboxPatch((0.8, 2.3), 10.4, 1.7, boxstyle="round,pad=0.2",
                                  edgecolor='#10b981', facecolor='#1e293b', linewidth=1.5)
    ax.add_patch(rect2)
    ax.text(1.2, 3.7, "2. HYBRID TRIAGE & VECTOR RAG CORE (AIR-GAPPED)", color='#10b981', fontsize=11, fontweight='bold')

    sub_boxes2 = [
        ("Deterministic Checker\n(Cppcheck & AST Rules\n100% Precision Hits)", 1.5, 2.5),
        ("Automotive Vector RAG\n(MISRA / CERT / ISO 26262\nCosine Similarity Top-K)", 5.0, 2.5),
        ("Local LLM Service\n(Qwen2.5-Coder-7B / Fallback\nDiff Fix & Root-Cause Synth)", 8.5, 2.5)
    ]
    for text, x, y in sub_boxes2:
        srect = patches.FancyBboxPatch((x, y), 2.8, 1.0, boxstyle="round,pad=0.1",
                                      edgecolor='#475569', facecolor='#0f172a')
        ax.add_patch(srect)
        ax.text(x + 1.4, y + 0.5, text, ha='center', va='center', color='#f8fafc', fontsize=9)

    # Layer 3: Presentation & Automotive Workflow Layer (Bottom)
    rect3 = patches.FancyBboxPatch((0.8, 0.4), 10.4, 1.5, boxstyle="round,pad=0.2",
                                  edgecolor='#f59e0b', facecolor='#1e293b', linewidth=1.5)
    ax.add_patch(rect3)
    ax.text(1.2, 1.6, "3. COCKPIT UI & COMPLIANCE ARTIFACT WORKFLOW", color='#f59e0b', fontsize=11, fontweight='bold')

    sub_boxes3 = [
        ("Streamlit Cockpit\n(Severity Filter & Cards)", 1.5, 0.6),
        ("Interactive Diff Sandbox\n(Side-by-Side Review)", 4.3, 0.6),
        ("MISRA Deviation Generator\n(Signed Permit Form)", 6.9, 0.6),
        ("SARIF / PDF Exporters\n(CI/CD Pipeline Artifacts)", 9.3, 0.6)
    ]
    for text, x, y in sub_boxes3:
        w = 2.4 if x != 9.3 else 1.7
        srect = patches.FancyBboxPatch((x, y), w, 0.8, boxstyle="round,pad=0.1",
                                      edgecolor='#475569', facecolor='#0f172a')
        ax.add_patch(srect)
        ax.text(x + w/2.0, y + 0.4, text, ha='center', va='center', color='#f8fafc', fontsize=8.5)

    # Connecting Arrows
    ax.annotate('', xy=(6, 4.2), xytext=(6, 4.4),
                arrowprops=dict(facecolor='#38bdf8', edgecolor='#38bdf8', width=2, headwidth=7))
    ax.annotate('', xy=(6, 2.1), xytext=(6, 2.3),
                arrowprops=dict(facecolor='#10b981', edgecolor='#10b981', width=2, headwidth=7))

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

def generate_workflow_diagram(output_path: str):
    fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')
    ax.axis('off')

    ax.text(6, 5.6, "AUTOSAFE-REVIEW: WORKFLOW PIPELINE", ha='center', va='center',
            color='#38bdf8', fontsize=15, fontweight='bold')
    ax.text(6, 5.25, "End-to-End Automotive Code Ingestion to Human Disposition", ha='center', va='center',
            color='#94a3b8', fontsize=11)

    steps = [
        ("Step 1\nIngestion", "Ingest C Source,\nGCC Build Logs\n& SARIF Reports", 1.0, '#38bdf8'),
        ("Step 2\nAST Chunking", "Semantic Parse\nby Function, ISR\n& Call-Graph", 3.2, '#06b6d4'),
        ("Step 3\nDual Triage", "Deterministic Rule\nCheck + Semantic\nVector Retrieval", 5.4, '#10b981'),
        ("Step 4\nSynthesis", "Ground Findings\nwith ASIL Safety\nImpact & Fix Diff", 7.6, '#f59e0b'),
        ("Step 5\nDisposition", "Engineer Review:\nAccept / Reject /\nMISRA Deviation", 9.8, '#ec4899')
    ]

    for title, desc, x, color in steps:
        rect = patches.FancyBboxPatch((x - 0.9, 2.0), 1.8, 2.2, boxstyle="round,pad=0.15",
                                     edgecolor=color, facecolor='#1e293b', linewidth=1.5)
        ax.add_patch(rect)
        ax.text(x, 3.7, title, ha='center', va='center', color=color, fontsize=10, fontweight='bold')
        ax.text(x, 2.8, desc, ha='center', va='center', color='#f8fafc', fontsize=8.5)

    # Arrows between steps
    arrow_xs = [2.0, 4.2, 6.4, 8.6]
    for ax_pos in arrow_xs:
        ax.annotate('', xy=(ax_pos + 0.25, 3.1), xytext=(ax_pos - 0.15, 3.1),
                    arrowprops=dict(facecolor='#94a3b8', edgecolor='#94a3b8', width=2, headwidth=7))

    # Bottom output banner
    brect = patches.FancyBboxPatch((1.0, 0.4), 10.0, 0.9, boxstyle="round,pad=0.1",
                                  edgecolor='#64748b', facecolor='#1e293b')
    ax.add_patch(brect)
    ax.text(6.0, 0.85, "Outputs: Standard SARIF File (CI/CD) • CSV Compliance Matrix • MISRA Deviation Permit • Audit Report",
            ha='center', va='center', color='#e2e8f0', fontsize=9.5, fontweight='bold')

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

if __name__ == "__main__":
    doc_dir = os.path.dirname(os.path.abspath(__file__))
    arch_path = os.path.join(doc_dir, "Architecture_Diagram.png")
    wf_path = os.path.join(doc_dir, "Workflow_Diagram.png")
    
    print("[*] Generating Architecture Diagram...")
    generate_architecture_diagram(arch_path)
    print(f"  [+] Saved: {arch_path}")

    print("[*] Generating Workflow Diagram...")
    generate_workflow_diagram(wf_path)
    print(f"  [+] Saved: {wf_path}")
    print("[SUCCESS] Diagrams generated successfully!")
