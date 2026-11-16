"""
CLI for Fractal Urban Area Classification Suite.
"""

import argparse
import sys
import numpy as np
from PIL import Image

from core.classifier import UrbanMorphologyClassifier
from core.evaluation import evaluate_urban_classification


def cmd_classify(args):
    img = Image.open(args.input).convert("RGB")
    arr = np.array(img)
    print(f"[Satellite Analysis] Mengklasifikasi tile satelit: {args.input}")

    clf = UrbanMorphologyClassifier()
    res = clf.classify(arr)

    print("\n" + "=" * 55)
    print("HASIL KLASIFIKASI MORFOLOGI WILAYAH PERKOTAAN")
    print("=" * 55)
    print(f"Zona Morfologi       : {res.predicted_zone.upper()}")
    print(f"Tingkat Kepercayaan  : {res.confidence * 100:.1f}%")
    print(f"Karakteristik Wilayah: {res.morphology_summary}")
    print("\nFitur Fraktal Spasial:")
    print(f"- Dimensi Fraktal Box-Counting (DF) : {res.features['box_fractal_dimension']:.3f}")
    print(f"- Dimensi Fraktal Radial (D_rad)    : {res.features['radial_fractal_dimension']:.3f}")
    print(f"- Kepadatan Jejak Bangunan/Jalan    : {res.features['built_density']*100:.2f}%")
    print("=" * 55 + "\n")


def cmd_gui(args):
    from gui.app import launch_gui
    launch_gui()


def main():
    p = argparse.ArgumentParser(description="Fractal Urban Area Classification")
    sub = p.add_subparsers(dest="command")

    p_cls = sub.add_parser("classify", help="Classify an aerial or satellite tile")
    p_cls.add_argument("input", help="Input satellite image file")

    sub.add_parser("gui", help="Launch interactive satellite zone classification GUI")

    args = p.parse_args()
    if args.command == "classify":
        cmd_classify(args)
    elif args.command == "gui":
        cmd_gui(args)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
