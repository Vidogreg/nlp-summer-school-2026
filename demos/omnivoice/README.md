# OmniVoice demo

Minimal smoke test for [k2-fsa/OmniVoice](https://huggingface.co/k2-fsa/OmniVoice),
a zero-shot multilingual TTS model.

## Setup

From the repo root (shared env for all demos):

```bash
uv sync
```

## Run

From the repo root:

```bash
uv run demos/omnivoice/text_to_speech_test.py
```

Downloads the model into the local HF cache (`~/.cache/huggingface`, first run
only), then generates one `.wav` per entry in the `EXAMPLES` list at the top
of `text_to_speech_test.py` into `outputs/`, using voice-design mode (no
reference audio needed — just an `instruct` description of the voice).

Edit `EXAMPLES` to try different text/voice combinations. `instruct` must be
built only from the model's fixed vocabulary (see the comment in the script
for the full list, e.g. `"female, british accent"` or `"child, high pitch"`).
Each example can also set `language` (a code like `"sk"` or a full name like
`"Slovak"`) — the model covers 600+ languages and is otherwise language-
agnostic, inferring it from the text.
