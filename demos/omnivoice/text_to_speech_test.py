"""Smoke test for k2-fsa/OmniVoice: downloads the model into the local HF
cache and generates one audio file per example defined below.

Uses "voice design" mode (an `instruct` description of the voice) instead of
voice cloning, so no reference audio file is needed.

Valid instruct items (comma-separated, English or Chinese only, not mixed):
american accent, australian accent, british accent, canadian accent, child,
chinese accent, elderly, female, high pitch, indian accent, japanese accent,
korean accent, low pitch, male, middle-aged, moderate pitch, portuguese
accent, russian accent, teenager, very high pitch, very low pitch, whisper,
young adult

`language` is optional (a code like "sk"/"en" or a full name like "Slovak"/
"English", case-insensitive); the model is otherwise language-agnostic and
infers it from the text. Covers 600+ languages, including Slovak.

Usage (from the repo root):
    uv sync
    uv run demos/omnivoice/text_to_speech_test.py
"""

from pathlib import Path

import torch
import soundfile as sf
from omnivoice import OmniVoice

EXAMPLES = [
    {
        "name": "male_low_pitch",
        "text": "Hello NLP Summer School of 2026. Welcome in Kinit.",
        "instruct": "male, low pitch",
    },
    {
        "name": "female_british",
        "text": "Hello NLP Summer School of 2026. Welcome in Kinit.",
        "instruct": "female, british accent",
    },
    {
        "name": "child_high_pitch",
        "text": "Hello NLP Summer School of 2026. Welcome in Kinit.",
        "instruct": "child, high pitch",
    },
    {
        "name": "slovak_female",
        "text": "Ahoj, letná škola NLP 2026. Vitajte v Kinyte.",
        "instruct": "female, moderate pitch",
        "language": "sk",
    },
]

device = "cuda:0" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if device.startswith("cuda") else torch.float32

print(f"Loading k2-fsa/OmniVoice on {device} ({dtype})...")
model = OmniVoice.from_pretrained("k2-fsa/OmniVoice", device_map=device, dtype=dtype)

output_dir = Path(__file__).parent / "outputs"
output_dir.mkdir(exist_ok=True)

for example in EXAMPLES:
    print(f"Generating '{example['name']}'...")
    audio = model.generate(
        text=example["text"],
        instruct=example["instruct"],
        language=example.get("language"),
    )

    if isinstance(audio, list):
        audio = audio[0]

    output_path = output_dir / f"{example['name']}.wav"
    sf.write(output_path, audio, 24000)
    print(f"Wrote {output_path}")
