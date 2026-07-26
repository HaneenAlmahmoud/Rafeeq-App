# Rafeeq API Smoke Tests

These scripts exercise the Rafeeq voice pipeline with real API requests:

1. `test_speech_to_text.py` reads `test_audio.wav` and requests Arabic (`ar-SA`) transcription.
2. `test_gemini.py` sends a Saudi-Arabic reminder request to Gemini and prints the response.
3. `test_text_to_speech.py` synthesizes Arabic speech at a slower pace and saves `rafeeq_test.mp3`.

## Setup

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, then provide your own local credentials. Never commit `.env` or a service-account JSON key.

Place a 16-bit PCM WAV file named `test_audio.wav` beside the scripts, then run:

```bash
python test_gemini.py
python test_speech_to_text.py
python test_text_to_speech.py
```

## Verification status

- All scripts pass Python syntax validation.
- Google Cloud authentication was accepted by the live STT and TTS requests.
- Live STT and TTS execution is deferred because Google Cloud requires billing before those APIs can be activated.
- Gemini requires a local free-tier API key from Google AI Studio.
