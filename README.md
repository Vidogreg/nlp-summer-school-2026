# NLP Summer School 2026 — Demos

Demos for the [Kinit NLP Summer School](https://kinit.sk/event/nlp-school/).

## Setup

One shared environment for all demos, managed with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

## Demos

- [demos/omnivoice](demos/omnivoice) — TTS with [k2-fsa/OmniVoice](https://huggingface.co/k2-fsa/OmniVoice)
- [demos/whisper](demos/whisper) — STT & translation with [Whisper turbo](https://huggingface.co/openai/whisper-large-v3-turbo) and [NLLB-200](https://huggingface.co/facebook/nllb-200-distilled-600M)
