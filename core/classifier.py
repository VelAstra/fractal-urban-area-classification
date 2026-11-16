"""
Urban Zone Classification Engine based on Fractal Morphology.
"""

from dataclasses import dataclass
from typing import Dict, Any
import numpy as np

from .fractal_analyzer import analyze_urban_tile


@dataclass
class UrbanClassificationResult:
    predicted_zone: str
    confidence: float
    features: Dict[str, float]
    morphology_summary: str


class UrbanMorphologyClassifier:
    """
    Classifies satellite tiles into:
    - dense_urban: High building concentration, continuous road grid (DF > 1.65, Density > 0.15)
    - suburban: Moderately spaced residential clusters (1.35 <= DF <= 1.65)
    - rural_agricultural: Open fields, natural topography, sparse settlements (DF < 1.35)
    """

    def classify(self, tile_rgb: np.ndarray) -> UrbanClassificationResult:
        feats = analyze_urban_tile(tile_rgb)
        df = feats["box_fractal_dimension"]
        density = feats["built_density"]

        if df >= 1.65 or (df >= 1.55 and density > 0.18):
            zone = "dense_urban"
            conf = min(0.98, 0.82 + (df - 1.65) * 0.5)
            desc = "Kawasan perkotaan padat (Dense Urban). Ditandai dengan kisi jalan rapat dan bangunan tinggi homogen."
        elif df >= 1.35:
            zone = "suburban"
            conf = min(0.95, 0.80 + (df - 1.35) * 0.4)
            desc = "Kawasan sub-urban / pemukiman teratur. Kepadatan bangunan menengah dengan ruang terbuka hijau."
        else:
            zone = "rural_agricultural"
            conf = min(0.97, 0.85 + (1.35 - df) * 0.4)
            desc = "Kawasan pedesaan / lahan pertanian terbuka. Struktur buatan manusia jarang dengan batas lanskap dominan."

        return UrbanClassificationResult(
            predicted_zone=zone,
            confidence=float(conf),
            features=feats,
            morphology_summary=desc,
        )
