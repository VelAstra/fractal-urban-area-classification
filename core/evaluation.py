"""
Evaluation Metrics for Satellite Urban Area Classification.
"""

from typing import List, Dict, Any
import numpy as np


def evaluate_urban_classification(
    y_true: List[str],
    y_pred: List[str],
    classes: List[str] = None
) -> Dict[str, Any]:
    if classes is None:
        classes = ["dense_urban", "suburban", "rural_agricultural"]

    n_cls = len(classes)
    cls_map = {c: i for i, c in enumerate(classes)}
    conf_matrix = np.zeros((n_cls, n_cls), dtype=np.int32)

    for yt, yp in zip(y_true, y_pred):
        if yt in cls_map and yp in cls_map:
            conf_matrix[cls_map[yt], cls_map[yp]] += 1

    total = len(y_true)
    correct = np.trace(conf_matrix)
    accuracy = correct / float(total) if total > 0 else 0.0

    per_class = {}
    for i, c in enumerate(classes):
        tp = conf_matrix[i, i]
        fp = np.sum(conf_matrix[:, i]) - tp
        fn = np.sum(conf_matrix[i, :]) - tp

        prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = (2 * prec * rec) / (prec + rec) if (prec + rec) > 0 else 0.0

        per_class[c] = {
            "precision": float(prec),
            "recall": float(rec),
            "f1_score": float(f1),
            "support": int(np.sum(conf_matrix[i, :])),
        }

    return {
        "classes": classes,
        "confusion_matrix": conf_matrix.tolist(),
        "overall_accuracy": float(accuracy),
        "per_class": per_class,
    }
