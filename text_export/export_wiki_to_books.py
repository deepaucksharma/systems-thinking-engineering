#!/usr/bin/env python3
"""
Export Wiki Markdown Files to Text Files Organized by Book Structure
"""

import os
import shutil
from pathlib import Path

# Base paths
WIKI_DIR = Path(r"C:\Users\hi\Desktop\SystemsEM\wiki")
EXPORT_DIR = Path(r"C:\Users\hi\Desktop\SystemsEM\text_export")

# Book structure mapping
BOOK_MAPPINGS = {
    "Book1_Foundations": [
        "_indexes/root.md",
        "sources/6-canonical-v2-1.md",
        "sources/canonical-v2-consolidated-model.md",
        "concepts/00-model-identity.md",
        "concepts/02-master-equation.md",
        "entities/master-equation.md",
        "concepts/06-time-constants.md",
        "concepts/v2-theorems.md",
        "concepts/order-parameter.md",
        "concepts/hysteresis.md",
        "concepts/self-organized-criticality.md",
        "concepts/littles-law.md",
        "concepts/utilization-curve.md",
        "concepts/nyquist-constraint.md",
        "concepts/condition-decay.md",
        "concepts/measurement-theory.md",
        "concepts/falsifiability-criteria.md",
        "concepts/boundary-conditions.md",
        "concepts/discrete-event-simulation.md",
        "concepts/digital-twin.md",
        "concepts/53-literature-map.md",
    ],
    "Book2_Diagnostics": [
        "concepts/20-diagnostic-sequence.md",
        "concepts/21-zero-override.md",
        "entities/table-2-diagnostics.md",
        "concepts/fix-order.md",
        "concepts/zero-override-rule.md",
        "concepts/structure-vs-development-rule.md",
        "concepts/lever-access-rule.md",
        "concepts/41-metrics-by-block.md",
        "concepts/metrics-framework.md",
        "concepts/51-anti-patterns.md",
        "concepts/anti-patterns.md",
        "concepts/practitioners-checklist.md",
        "concepts/temporal-integration-loop.md",
        "concepts/ethical-measurement.md",
        "concepts/goodharts-law.md",
    ],
    "Book3_TeamStates": [
        "concepts/p1-crisis.md",
        "concepts/p2-stabilizing.md",
        "concepts/p3-functional.md",
        "concepts/p4-thriving.md",
        "concepts/p5-scaling.md",
        "concepts/p6-mixed-state.md",
        "concepts/v2-extended-states.md",
        "concepts/losing-loop.md",
        "concepts/winning-loop.md",
        "concepts/incentive-death-spiral.md",
        "concepts/fear-amplification-loop.md",
        "concepts/sustainability-drain-loop.md",
        "concepts/strategic-drift-loop.md",
        "concepts/hero-culture-trap.md",
        "concepts/rushing-trap.md",
        "concepts/cynical-equilibrium.md",
    ],
    "Book4_FiveBlocks": [
        "concepts/10-block-V.md",
        "concepts/value-alignment.md",
        "concepts/11-block-P.md",
        "concepts/people-system.md",
        "concepts/12-block-E.md",
        "concepts/execution-system.md",
        "concepts/clarity.md",
        "concepts/focus.md",
        "concepts/skill.md",
        "concepts/coordination.md",
        "concepts/quality.md",
        "concepts/feedback-speed.md",
        "concepts/13-block-A.md",
        "concepts/org-alignment.md",
        "concepts/conways-law.md",
        "concepts/resource-allocation-game.md",
        "concepts/14-block-L.md",
        "concepts/learning-adaptation.md",
    ],
    "Book5_Scaling": [
        "concepts/fractal-scaling.md",
        "concepts/multi-scale-dynamics.md",
        "concepts/cross-domain-extensions.md",
        "concepts/open-research-questions.md",
        "sources/3-extended-framework.md",
        "sources/4-visual-architecture.md",
        "sources/diagram-set-1.md",
        "sources/diagram-set-2.md",
        "log/2026-04.md",
        "_indexes/concepts.md",
        "_indexes/entities.md",
        "_indexes/sources.md",
        "_indexes/syntheses.md",
    ],
}


def export_files():
    """Export all wiki markdown files to text files organized by book."""
    
    total_files = 0
    exported_files = 0
    missing_files = []
    
    print("=" * 80)
    print("WIKI TO TEXT EXPORT - 5 BOOK STRUCTURE")
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
            total_files += 1
            source_path = WIKI_DIR / md_file
            
            # Create output filename (replace .md with .txt, keep directory structure in name)
            # e.g., "concepts/00-model-identity.md" -> "concepts__00-model-identity.txt"
            txt_filename = md_file.replace("/", "__").replace(".md", ".txt")
            dest_path = book_dir / txt_filename
            
            if source_path.exists():
                try:
                    # Read markdown content
                    with open(source_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Write as text file
                    with open(dest_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    exported_files += 1
                    book_exported += 1
                    print(f"   [OK] {md_file} -> {txt_filename}")
                    
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
    print(f"Total files mapped: {total_files}")
    print(f"Successfully exported: {exported_files}")
    print(f"Missing/Failed: {len(missing_files)}")
    
    if missing_files:
        print("\n[WARNING] Missing or Failed Files:")
        for file, reason in missing_files:
            print(f"   - {file}: {reason}")
    
    print("\n[SUCCESS] Export complete!")
    print(f"[OUTPUT] Directory: {EXPORT_DIR}")
    print()


if __name__ == "__main__":
    export_files()
