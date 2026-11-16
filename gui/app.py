"""
Interactive GUI for Satellite Urban Morphology Classification.
"""

import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
from PIL import Image, ImageTk

from core.classifier import UrbanMorphologyClassifier


class UrbanClassificationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Satellite Urban Morphology & Fractal Sprawl Analyzer")
        self.geometry("920x620")
        self.configure(bg="#F1F5F9")

        self.classifier = UrbanMorphologyClassifier()
        self.current_img = None

        self._build_ui()
        sample = os.path.join(os.path.dirname(__file__), "..", "sample_data", "tile_dense_urban.png")
        if os.path.exists(sample):
            self.load_image(os.path.abspath(sample))

    def _build_ui(self):
        header = tk.Frame(self, bg="#1E3A8A", height=60, padx=20)
        header.pack(fill=tk.X)
        tk.Label(header, text="SATELLITE URBAN FRACTAL ANALYZER", font=("Segoe UI", 13, "bold"), fg="#FFFFFF", bg="#1E3A8A").pack(anchor="w", pady=(10, 0))
        tk.Label(header, text="Klasifikasi Zona Kepadatan Perkotaan Berbasis Dimensi Fraktal", font=("Segoe UI", 9), fg="#BFDBFE", bg="#1E3A8A").pack(anchor="w")

        tools = tk.Frame(self, bg="#FFFFFF", padx=15, pady=8, relief="groove", bd=1)
        tools.pack(fill=tk.X, padx=15, pady=10)
        ttk.Button(tools, text="Pilih Tile Satelit...", command=self.on_browse).pack(side=tk.LEFT, padx=5)
        ttk.Button(tools, text="Klasifikasi Zona Fraktal", command=self.on_classify).pack(side=tk.LEFT, padx=5)

        content = tk.Frame(self, bg="#F1F5F9", padx=15)
        content.pack(fill=tk.BOTH, expand=True)

        f_left = tk.Frame(content, bg="#FFFFFF", relief="groove", bd=1, width=320)
        f_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 8))
        tk.Label(f_left, text="CITRA SATELIT / TILE", font=("Segoe UI", 9, "bold"), bg="#FFFFFF", fg="#334155").pack(pady=4)
        self.lbl_img = tk.Label(f_left, bg="#E2E8F0")
        self.lbl_img.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        f_right = tk.Frame(content, bg="#FFFFFF", relief="groove", bd=1)
        f_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(8, 0))
        tk.Label(f_right, text="HASIL ANALISIS MORFOLOGI", font=("Segoe UI", 10, "bold"), bg="#FFFFFF", fg="#1E3A8A").pack(pady=8)

        self.lbl_zone = tk.Label(f_right, text="-", font=("Segoe UI", 14, "bold"), bg="#FFFFFF", fg="#0F172A")
        self.lbl_zone.pack(pady=4)

        self.lbl_conf = tk.Label(f_right, text="Tingkat Keyakinan: -", font=("Segoe UI", 10), bg="#FFFFFF", fg="#2563EB")
        self.lbl_conf.pack(pady=2)

        self.txt_desc = tk.Label(f_right, text="Pilih citra satelit dan jalankan analisis.", wraplength=340, font=("Segoe UI", 9), bg="#F8FAFC", fg="#334155", padx=10, pady=10)
        self.txt_desc.pack(fill=tk.X, padx=15, pady=12)

        self.lbl_feats = tk.Label(f_right, text="", justify=tk.LEFT, font=("Consolas", 9), bg="#FFFFFF", fg="#475569")
        self.lbl_feats.pack(anchor="w", padx=20, pady=5)

    def load_image(self, path):
        img = Image.open(path).convert("RGB")
        self.current_img = np.array(img)
        resized = img.resize((280, 280), Image.Resampling.NEAREST)
        tk_img = ImageTk.PhotoImage(resized)
        self.lbl_img.image = tk_img
        self.lbl_img.config(image=tk_img)

    def on_browse(self):
        f = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.tif")])
        if f:
            self.load_image(f)

    def on_classify(self):
        if self.current_img is None:
            return
        res = self.classifier.classify(self.current_img)
        self.lbl_zone.config(text=res.predicted_zone.upper())
        self.lbl_conf.config(text=f"Tingkat Keyakinan: {res.confidence * 100:.1f}%")
        self.txt_desc.config(text=res.morphology_summary)

        f_txt = (
            f"Dimensi Fraktal Box (DF) : {res.features['box_fractal_dimension']:.3f}\n"
            f"Dimensi Fraktal Radial   : {res.features['radial_fractal_dimension']:.3f}\n"
            f"Kepadatan Jejak Bangunan : {res.features['built_density']*100:.2f}%"
        )
        self.lbl_feats.config(text=f_txt)


def launch_gui():
    app = UrbanClassificationApp()
    app.mainloop()


if __name__ == "__main__":
    launch_gui()
