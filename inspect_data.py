from pathlib import Path

import yaml

source_path = Path("data/source_music_theory/music_data/Scales.yaml")

with source_path.open("r", encoding="utf-8") as file:
    scales_data = yaml.safe_load(file)

print(f"Loaded {len(scales_data)} scales from {source_path}")

for scale in scales_data[:3]:
    print(scale)