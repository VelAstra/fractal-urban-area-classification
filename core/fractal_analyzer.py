"""
Urban Morphology Fractal Analyzer Module.
Quantifies urban sprawl, building density, and road connectivity
via Multi-Scale Box-Counting and Radial Dimension analysis on satellite imagery.
"""

from typing import Tuple, Dict, Any
import numpy as np


def compute_box_dimension(binary_edge_map: np.ndarray) -> float:
    h, w = binary_edge_map.shape
    p = min(h, w)
    if p < 8 or np.sum(binary_edge_map) == 0:
        return 1.0

    scales = [2, 4, 8, 16, 32]
    counts = []

    for s in scales:
        ny = h // s
        nx = w // s
        if ny == 0 or nx == 0:
            continue
        trimmed = binary_edge_map[: ny * s, : nx * s]
        boxes = trimmed.reshape(ny, s, nx, s)
        counts.append(max(1, int(np.sum(np.any(boxes > 0, axis=(1, 3))))))

    if len(counts) < 2:
        return 1.0

    log_inv = np.log(1.0 / np.array(scales[:len(counts)], dtype=np.float64))
    log_c = np.log(counts)
    poly = np.polyfit(log_inv, log_c, 1)
    df = float(poly[0])
    return max(1.0, min(2.0, df))


def compute_radial_dimension(binary_map: np.ndarray) -> float:
    """
    Computes Radial Dimension D_rad from urban core outwards:
    N(R) ~ R^{D_rad}
    """
    h, w = binary_map.shape
    cy, cx = h // 2, w // 2
    y, x = np.mgrid[0:h, 0:w]
    radii = np.sqrt((x - cx)**2 + (y - cy)**2)

    r_steps = [10, 20, 30, 40, 50]
    counts = []
    for r in r_steps:
        mask = (radii <= r) & (binary_map > 0)
        counts.append(max(1, int(np.sum(mask))))

    log_r = np.log(r_steps)
    log_n = np.log(counts)
    poly = np.polyfit(log_r, log_n, 1)
    return float(max(0.5, min(2.0, poly[0])))


def analyze_urban_tile(tile_rgb: np.ndarray) -> Dict[str, float]:
    """
    Extracts structural building footprint and road network features:
    """
    gray = (0.299 * tile_rgb[:, :, 0] + 0.587 * tile_rgb[:, :, 1] + 0.114 * tile_rgb[:, :, 2]).astype(np.float32)

    # Edge extraction for built structures
    gy, gx = np.gradient(gray)
    edge_mag = np.sqrt(gx**2 + gy**2)
    built_edges = (edge_mag > (np.mean(edge_mag) + 0.8 * np.std(edge_mag))).astype(np.uint8)

    df_box = compute_box_dimension(built_edges)
    df_rad = compute_radial_dimension(built_edges)
    built_density = float(np.mean(built_edges))

    return {
        "box_fractal_dimension": df_box,
        "radial_fractal_dimension": df_rad,
        "built_density": built_density,
    }
