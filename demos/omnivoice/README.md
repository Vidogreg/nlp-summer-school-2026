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

## Colab version

`text_to_speech_colab.ipynb` is a Colab-ready variant for the workshop: it
mounts Google Drive and caches the model weights there (via `HF_HOME`) so
attendees don't re-download a few GB every session, falling back to a normal
download if the Drive cache isn't available.

It also has a **voice cloning** section, in two parts:
1. Clones a public sample voice (one clip from `hf-internal-testing/librispeech_asr_dummy`) to say new text.
2. Records the attendee's own voice from the browser mic (reading a printed
   prompt sentence), saves it to their Drive cache folder, then clones it to
   say something new.

The mic-recording cell uses a JS `MediaRecorder` snippet + `pydub`/ffmpeg to
decode the browser's recording — this is the least-tested part (no way to
exercise real browser mic access outside Colab itself), so try it early
rather than right before presenting.
