#!/usr/bin/env python3
"""
Verify all wiki files are exported and properly categorized
"""

import os
from pathlib import Path

WIKI_DIR = Path(r"C:\Users\hi\Desktop\SystemsEM\wiki")

# All files from export script
EXPORTED_FILES = {
    # Book 1
    "_indexes/root.md", "concepts/00-model-identity.md", "concepts/02-master-equation.md",
    "entities/master-equation.md", "legacy/master-equation.md", "sources/6-canonical-v2-1.md",
    "sources/canonical-v2-consolidated-model.md", "concepts/06-time-constants.md",
    "legacy/nyquist-constraint.md", "concepts/transfer-functions.md", "concepts/order-parameter.md",
    "concepts/hysteresis.md", "concepts/self-organized-criticality.md", "concepts/condition-decay.md",
    "concepts/littles-law.md", "concepts/utilization-curve.md", "concepts/measurement-theory.md",
    "concepts/ethical-measurement.md", "concepts/goodharts-law.md", "concepts/falsifiability-criteria.md",
    "concepts/boundary-conditions.md", "concepts/open-research-questions.md", "concepts/digital-twin.md",
    "concepts/discrete-event-simulation.md", "concepts/telemetry-engine-schema.md", "concepts/53-literature-map.md",
    
    # Book 2
    "concepts/20-diagnostic-sequence.md", "concepts/21-zero-override.md", "legacy/zero-override-rule.md",
    "entities/table-2-diagnostics.md", "legacy/fix-order.md", "concepts/structure-vs-development-rule.md",
    "concepts/lever-access-rule.md", "concepts/41-metrics-by-block.md", "legacy/metrics-framework.md",
    "concepts/51-anti-patterns.md", "legacy/anti-patterns.md", "concepts/practitioners-checklist.md",
    "concepts/temporal-integration-loop.md", "concepts/resource-allocation-game.md",
    "concepts/cynical-equilibrium.md", "concepts/incentive-mechanism-design.md",
    "syntheses/review-2026-04-09-findings.md", "syntheses/historical-evolution.md", "log/2026-04.md",
    
    # Book 3
    "concepts/p1-crisis.md", "concepts/p2-stabilizing.md", "concepts/p3-functional.md",
    "concepts/p4-thriving.md", "concepts/p5-scaling.md", "concepts/p6-mixed-state.md",
    "concepts/v2-extended-states.md", "concepts/losing-loop.md", "concepts/winning-loop.md",
    "concepts/incentive-death-spiral.md", "concepts/fear-amplification-loop.md",
    "concepts/sustainability-drain-loop.md", "concepts/strategic-drift-loop.md",
    "concepts/hero-culture-trap.md", "concepts/rushing-trap.md", "concepts/conways-law.md",
    
    # Book 4
    "concepts/10-block-V.md", "legacy/value-alignment.md", "concepts/11-block-P.md",
    "legacy/people-system.md", "concepts/12-block-E.md", "legacy/execution-system.md",
    "legacy/clarity.md", "legacy/focus.md", "legacy/skill.md", "legacy/coordination.md",
    "legacy/quality.md", "concepts/feedback-speed.md", "concepts/13-block-A.md",
    "legacy/org-alignment.md", "concepts/14-block-L.md", "legacy/learning-adaptation.md",
    "sources/diagram-set-1.md", "sources/diagram-set-2.md", "sources/3-extended-framework.md",
    "sources/4-visual-architecture.md",
    
    # Book 5
    "concepts/fractal-scaling.md", "concepts/multi-scale-dynamics.md",
    "concepts/cross-domain-extensions.md", "_indexes/concepts.md", "_indexes/entities.md",
    "_indexes/sources.md", "_indexes/syntheses.md",
}

def get_all_wiki_files():
    """Get all .md files in wiki directory"""
    all_files = set()
    for root, dirs, files in os.walk(WIKI_DIR):
        for file in files:
            if file.endswith('.md'):
                rel_path = os.path.relpath(os.path.join(root, file), WIKI_DIR)
                rel_path = rel_path.replace('\\', '/')
                all_files.add(rel_path)
    return all_files

def verify_export():
    """Verify all files are accounted for"""
    
    wiki_files = get_all_wiki_files()
    
    print("=" * 80)
    print("WIKI EXPORT VERIFICATION")
    print("=" * 80)
    print()
    
    print(f"Total files in wiki: {len(wiki_files)}")
    print(f"Total files in export mapping: {len(EXPORTED_FILES)}")
    print()
    
    # Find missing files
    missing = wiki_files - EXPORTED_FILES
    if missing:
        print(f"[WARNING] FILES IN WIKI BUT NOT EXPORTED ({len(missing)}):")
        for f in sorted(missing):
            print(f"   - {f}")
        print()
    
    # Find extra files
    extra = EXPORTED_FILES - wiki_files
    if extra:
        print(f"[WARNING] FILES IN EXPORT BUT NOT IN WIKI ({len(extra)}):")
        for f in sorted(extra):
            print(f"   - {f}")
        print()
    
    if not missing and not extra:
        print("[SUCCESS] PERFECT MATCH! All wiki files are exported.")
        print()
    
    # Show distribution
    print("=" * 80)
    print("FILE DISTRIBUTION BY DIRECTORY")
    print("=" * 80)
    
    dirs = {}
    for f in wiki_files:
        dir_name = f.split('/')[0]
        dirs[dir_name] = dirs.get(dir_name, 0) + 1
    
    for dir_name in sorted(dirs.keys()):
        print(f"   {dir_name:20s}: {dirs[dir_name]:3d} files")
    
    print()
    print(f"   {'TOTAL':20s}: {len(wiki_files):3d} files")
    print()

if __name__ == "__main__":
    verify_export()
