#!/usr/bin/env python3
"""
FINAL Comprehensive Wiki Export - All 87 Files Properly Categorized
Some files appear in multiple books for context where appropriate
"""

import os
from pathlib import Path

WIKI_DIR = Path(r"C:\Users\hi\Desktop\SystemsEM\wiki")
EXPORT_DIR = Path(r"C:\Users\hi\Desktop\SystemsEM\text_export")

# Final Book Mappings - All 87 Actual Wiki Files
# Some files appear in multiple books for context
BOOK_MAPPINGS = {
    
    # ========================================================================
    # BOOK 1: FOUNDATIONS - Theory, Mathematics, Physics (27 files)
    # ========================================================================
    "Book1_Foundations": [
        # Core Identity & Architecture
        "_indexes/root.md",
        "concepts/00-model-identity.md",
        "concepts/02-master-equation.md",
        "entities/master-equation.md",
        "legacy/master-equation.md",
        
        # Canonical Sources
        "sources/6-canonical-v2-1.md",
        "sources/canonical-v2-consolidated-model.md",
        
        # Time & Control Theory
        "concepts/06-time-constants.md",
        "legacy/nyquist-constraint.md",
        "concepts/transfer-functions.md",
        
        # Theorems & Mathematical Foundations
        "concepts/hysteresis.md",
        "concepts/self-organized-criticality.md",
        "concepts/condition-decay.md",
        
        # Queuing Physics & Flow
        "concepts/littles-law.md",
        "concepts/utilization-curve.md",
        
        # Measurement Science
        "concepts/measurement-theory.md",
        "concepts/ethical-measurement.md",
        "concepts/goodharts-law.md",
        
        # Validation & Research
        "concepts/falsifiability-criteria.md",
        "concepts/boundary-conditions.md",
        "concepts/open-research-questions.md",
        
        # Computational Models
        "concepts/digital-twin.md",
        "concepts/discrete-event-simulation.md",
        "concepts/telemetry-engine-schema.md",
        
        # Literature
        "concepts/53-literature-map.md",
        
        # Cross-reference: Conway's Law (foundational constraint)
        "concepts/conways-law.md",
    ],
    
    # ========================================================================
    # BOOK 2: DIAGNOSTICS - Practical Diagnosis & Intervention (22 files)
    # ========================================================================
    "Book2_Diagnostics": [
        # Core Diagnostic Framework
        "concepts/20-diagnostic-sequence.md",
        "concepts/21-zero-override.md",
        "legacy/zero-override-rule.md",
        "entities/table-2-diagnostics.md",
        "legacy/fix-order.md",
        
        # Diagnostic Rules
        "concepts/structure-vs-development-rule.md",
        "concepts/lever-access-rule.md",
        
        # Metrics & Measurement
        "concepts/41-metrics-by-block.md",
        "legacy/metrics-framework.md",
        
        # Anti-Patterns
        "concepts/51-anti-patterns.md",
        "legacy/anti-patterns.md",
        
        # Implementation
        "concepts/practitioners-checklist.md",
        "concepts/temporal-integration-loop.md",
        
        # Political Economy & Constraints
        "concepts/resource-allocation-game.md",
        "concepts/cynical-equilibrium.md",
        "concepts/incentive-mechanism-design.md",
        
        # Syntheses
        "syntheses/review-2026-04-09-findings.md",
        "syntheses/historical-evolution.md",
        
        # Operations Log
        "log/2026-04.md",
        
        # Cross-reference: Time constants (for intervention timing)
        "concepts/06-time-constants.md",
        
        # Cross-reference: Measurement theory (for metrics)
        "concepts/measurement-theory.md",
        "concepts/ethical-measurement.md",
    ],
    
    # ========================================================================
    # BOOK 3: TEAM STATES & DYNAMICS - States, Loops, Patterns (18 files)
    # ========================================================================
    "Book3_TeamStates": [
        # Team States P1-P6
        "concepts/p1-crisis.md",
        "concepts/p2-stabilizing.md",
        "concepts/p3-functional.md",
        "concepts/p4-thriving.md",
        "concepts/p5-scaling.md",
        "concepts/p6-mixed-state.md",
        "concepts/v2-extended-states.md",
        
        # Core Dynamics
        "concepts/losing-loop.md",
        "concepts/winning-loop.md",
        
        # Cross-Layer Loops
        "concepts/incentive-death-spiral.md",
        "concepts/fear-amplification-loop.md",
        "concepts/sustainability-drain-loop.md",
        "concepts/strategic-drift-loop.md",
        
        # Pathological States
        "concepts/hero-culture-trap.md",
        "concepts/rushing-trap.md",
        
        # Structural Dynamics
        "concepts/conways-law.md",
        
        # Cross-reference: Hysteresis (explains state transitions)
        "concepts/hysteresis.md",
        
        # Cross-reference: Condition decay (explains why states regress)
        "concepts/condition-decay.md",
    ],
    
    # ========================================================================
    # BOOK 4: THE FIVE BLOCKS - Deep Dives into V, P, E, A, L (26 files)
    # ========================================================================
    "Book4_FiveBlocks": [
        # Block V - Value Alignment
        "concepts/10-block-V.md",
        "legacy/value-alignment.md",
        
        # Block P - People System
        "concepts/11-block-P.md",
        "legacy/people-system.md",
        
        # Block E - Execution System
        "concepts/12-block-E.md",
        "legacy/execution-system.md",
        "legacy/clarity.md",
        "legacy/focus.md",
        "legacy/skill.md",
        "legacy/coordination.md",
        "legacy/quality.md",
        "concepts/feedback-speed.md",
        
        # Block A - Org Alignment
        "concepts/13-block-A.md",
        "legacy/org-alignment.md",
        
        # Block L - Learning & Adaptation
        "concepts/14-block-L.md",
        "legacy/learning-adaptation.md",
        
        # Source Diagrams (detailed block explanations)
        "sources/diagram-set-1.md",
        "sources/diagram-set-2.md",
        "sources/3-extended-framework.md",
        "sources/4-visual-architecture.md",
        
        # Cross-reference: Master equation (shows how blocks multiply)
        "concepts/02-master-equation.md",
        "entities/master-equation.md",
        
        # Cross-reference: Queuing physics (for Block E)
        "concepts/littles-law.md",
        "concepts/utilization-curve.md",
        
        # Cross-reference: Conway's Law (for Block A)
        "concepts/conways-law.md",
    ],
    
    # ========================================================================
    # BOOK 5: SCALING & CROSS-DOMAIN - Multi-Scale, Extensions (11 files)
    # ========================================================================
    "Book5_Scaling": [
        # Scaling Concepts
        "concepts/fractal-scaling.md",
        "concepts/multi-scale-dynamics.md",
        
        # Cross-Domain Applications
        "concepts/cross-domain-extensions.md",
        
        # Indexes (navigation & overview)
        "_indexes/concepts.md",
        "_indexes/entities.md",
        "_indexes/sources.md",
        "_indexes/syntheses.md",
        
        # Cross-reference: All 5 canonical blocks (for scaling context)
        "concepts/10-block-V.md",
        "concepts/11-block-P.md",
        "concepts/12-block-E.md",
        "concepts/13-block-A.md",
        "concepts/14-block-L.md",
    ],
}


def export_files():
    """Export all wiki markdown files to text files organized by book."""
    
    total_unique_files = set()
    total_exports = 0
    exported_files = 0
    missing_files = []
    
    print("=" * 80)
    print("FINAL COMPREHENSIVE WIKI EXPORT - 5 BOOK STRUCTURE")
    print("All 87 Wiki Files Properly Categorized")
    print("Some files appear in multiple books for context")
    print("=" * 80)
    print()
    
    for book_name, file_list in BOOK_MAPPINGS.items():
        book_dir = EXPORT_DIR / book_name
        print(f"\n[BOOK] Processing {book_name}...")
        print(f"   Target: {book_dir}")
        print(f"   Files to export: {len(file_list)}")
        print("-" * 80)
        
        book_exported = 0
        
        for md_file in file_list:
            total_exports += 1
            total_unique_files.add(md_file)
            source_path = WIKI_DIR / md_file
            
            # Create output filename
            txt_filename = md_file.replace("/", "__").replace(".md", ".txt")
            dest_path = book_dir / txt_filename
            
            if source_path.exists():
                try:
                    with open(source_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    with open(dest_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    exported_files += 1
                    book_exported += 1
                    print(f"   [OK] {md_file}")
                    
                except Exception as e:
                    print(f"   [ERROR] exporting {md_file}: {e}")
                    missing_files.append((md_file, str(e)))
            else:
                print(f"   [MISSING] {md_file}")
                missing_files.append((md_file, "File not found"))
        
        print(f"\n   {book_name}: {book_exported}/{len(file_list)} files exported")
    
    # Summary
    print("\n" + "=" * 80)
    print("EXPORT SUMMARY")
    print("=" * 80)
    print(f"Unique wiki files: {len(total_unique_files)}")
    print(f"Total exports (with duplicates): {total_exports}")
    print(f"Successfully exported: {exported_files}")
    print(f"Missing/Failed: {len(missing_files)}")
    
    if missing_files:
        print("\n[WARNING] Missing or Failed Files:")
        for file, reason in missing_files:
            print(f"   - {file}: {reason}")
    else:
        print("\n[SUCCESS] All files exported successfully!")
    
    print(f"\n[OUTPUT] Directory: {EXPORT_DIR}")
    
    # Create book manifests
    print("\n" + "=" * 80)
    print("CREATING BOOK MANIFESTS")
    print("=" * 80)
    
    for book_name in BOOK_MAPPINGS.keys():
        book_dir = EXPORT_DIR / book_name
        manifest_path = book_dir / "MANIFEST.txt"
        
        txt_files = sorted([f.name for f in book_dir.glob("*.txt")])
        
        with open(manifest_path, 'w', encoding='utf-8') as f:
            f.write(f"{book_name} - File Manifest\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Total files: {len(txt_files)}\n\n")
            f.write("Files:\n")
            f.write("-" * 60 + "\n")
            for i, filename in enumerate(txt_files, 1):
                f.write(f"{i:3d}. {filename}\n")
        
        print(f"   [OK] Created {book_name}/MANIFEST.txt ({len(txt_files)} files)")
    
    print("\n[SUCCESS] Export complete!")
    print()


if __name__ == "__main__":
    export_files()
