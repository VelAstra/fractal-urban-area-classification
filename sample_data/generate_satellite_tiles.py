"""
Synthetic Satellite Image Tile Generator.
Generates realistic land-use scenes: Dense Urban, Suburban, and Rural Agricultural.
"""

import os
from typing import List, Tuple
import numpy as np
from PIL import Image, ImageDraw


def generate_satellite_samples(output_dir: str = "sample_data", size: int = 160) -> List[Tuple[str, str]]:
    os.makedirs(output_dir, exist_ok=True)
    samples = []

    # 1. Dense Urban Tile
    img_u = Image.new("RGB", (size, size), color=(140, 140, 145))
    draw_u = ImageDraw.Draw(img_u)
    # Dense street grid
    for x in range(15, size, 25):
        draw_u.line([x, 0, x, size], fill=(50, 50, 50), width=3)
    for y in range(15, size, 25):
        draw_u.line([0, y, size, y], fill=(50, 50, 50), width=3)
    # Compact buildings
    for x in range(20, size - 20, 25):
        for y in range(20, size - 20, 25):
            draw_u.rectangle([x, y, x + 16, y + 16], fill=(190, 80, 70), outline=(20, 20, 20))
    p_u = os.path.join(output_dir, "tile_dense_urban.png")
    img_u.save(p_u)
    samples.append((p_u, "dense_urban"))

    # 2. Suburban Tile
    img_s = Image.new("RGB", (size, size), color=(110, 160, 110))
    draw_s = ImageDraw.Draw(img_s)
    # Curved road
    draw_s.line([0, 40, 80, 80], fill=(60, 60, 60), width=4)
    draw_s.line([80, 80, size, 120], fill=(60, 60, 60), width=4)
    # Spaced houses
    for x, y in [(30, 20), (70, 30), (110, 50), (40, 110), (100, 130)]:
        draw_s.rectangle([x, y, x + 20, y + 18], fill=(210, 120, 90), outline=(30, 30, 30))
    p_s = os.path.join(output_dir, "tile_suburban.png")
    img_s.save(p_s)
    samples.append((p_s, "suburban"))

    # 3. Rural Agricultural Tile
    img_r = Image.new("RGB", (size, size), color=(90, 145, 80))
    draw_r = ImageDraw.Draw(img_r)
    # Farmland parcels
    draw_r.polygon([(10, 10), (140, 15), (130, 80), (15, 75)], fill=(150, 175, 70), outline=(40, 90, 30), width=2)
    draw_r.polygon([(20, 90), (150, 95), (140, 150), (25, 145)], fill=(130, 115, 60), outline=(40, 90, 30), width=2)
    p_r = os.path.join(output_dir, "tile_rural.png")
    img_r.save(p_r)
    samples.append((p_r, "rural_agricultural"))

    return samples


if __name__ == "__main__":
    res = generate_satellite_samples()
    print(f"Generated {len(res)} satellite tiles.")
