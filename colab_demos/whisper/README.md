# Whisper speech-to-text & translation demo

Colab notebook for [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo)
(transcription, English/Slovak) and [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M)
(translation into several languages).

## Run

Open `speech_to_text_colab.ipynb` in Colab (via the badge cell at the top, or
[this link](https://colab.research.google.com/github/Vidogreg/nlp-summer-school-2026/blob/main/demos/whisper/speech_to_text_colab.ipynb)).

Structure, same pattern as the [omnivoice demo](../omnivoice):
1. Mounts Google Drive and caches both models there (via `HF_HOME`) so you
   don't re-download them every session, falling back to a normal download
   if the Drive cache isn't available.
2. Sanity-checks the ASR model against one public sample clip with a known
   transcript.
3. Records your voice from the browser mic and transcribes it — once in
   English, once in Slovak.
4. Records your voice again and translates the transcript into German,
   French, Spanish, Czech, and Ukrainian via NLLB-200.
5. A markdown section discussing common ASR failure modes (named entities,
   numbers/dates, code-switching, low-resource languages, hallucination on
   silence, etc.) — useful as workshop discussion material.

The mic-recording cell reuses the same JS `MediaRecorder` + `pydub`/ffmpeg
approach as the OmniVoice notebook — least-tested part, try it early.
