"""
Unit and Integration Tests for Fractal Urban Area Classification Suite.
"""

import unittest
import numpy as np
from PIL import Image

from core.fractal_analyzer import analyze_urban_tile, compute_box_dimension
from core.classifier import UrbanMorphologyClassifier
from core.evaluation import evaluate_urban_classification


class TestUrbanClassification(unittest.TestCase):

    def test_box_dimension(self):
        # Empty map vs filled grid
        empty = np.zeros((32, 32), dtype=np.uint8)
        self.assertEqual(compute_box_dimension(empty), 1.0)

        grid = np.zeros((32, 32), dtype=np.uint8)
        grid[::4, :] = 1
        grid[:, ::4] = 1
        df = compute_box_dimension(grid)
        self.assertGreater(df, 1.4)

    def test_classifier(self):
        clf = UrbanMorphologyClassifier()
        # High density urban tile
        tile = np.random.uniform(50, 200, (64, 64, 3)).astype(np.uint8)
        res = clf.classify(tile)
        self.assertIn(res.predicted_zone, ["dense_urban", "suburban", "rural_agricultural"])
        self.assertGreater(res.confidence, 0.5)

    def test_evaluation(self):
        y_t = ["dense_urban", "suburban", "rural_agricultural"]
        y_p = ["dense_urban", "suburban", "rural_agricultural"]
        metrics = evaluate_urban_classification(y_t, y_p)
        self.assertEqual(metrics["overall_accuracy"], 1.0)


if __name__ == "__main__":
    unittest.main()
