"""Real Google Cloud Speech-to-Text smoke test for Arabic audio."""

import os
import sys
import wave
from pathlib import Path

from dotenv import load_dotenv
from google.api_core import exceptions as google_exceptions
from google.cloud import speech


SCRIPT_DIR = Path(__file__).resolve().parent
AUDIO_FILE = SCRIPT_DIR / "test_audio.wav"


def load_environment() -> None:
    """Load the existing project .env without overriding shell variables."""
    explicit_env = os.getenv("RAFEEQ_ENV_FILE")
    if explicit_env:
        load_dotenv(explicit_env, override=False)
        return
    load_dotenv(Path.cwd() / ".env", override=False)
    load_dotenv(SCRIPT_DIR / ".env", override=False)


def validate_credentials() -> bool:
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not credentials_path:
        print("ERROR: GOOGLE_APPLICATION_CREDENTIALS is missing from the existing .env file.")
        return False
    if not Path(credentials_path).expanduser().is_file():
        print(f"ERROR: Google Cloud credential file does not exist: {credentials_path}")
        return False
    return True


def main() -> int:
    load_environment()
    if not validate_credentials():
        return 1
    if not AUDIO_FILE.is_file():
        print(f"ERROR: WAV input file was not found: {AUDIO_FILE}")
        return 1

    try:
        with wave.open(str(AUDIO_FILE), "rb") as wav_file:
            channels = wav_file.getnchannels()
            sample_width = wav_file.getsampwidth()
            sample_rate = wav_file.getframerate()

        if sample_width != 2:
            print("ERROR: test_audio.wav must be 16-bit PCM (LINEAR16).")
            return 1

        audio = speech.RecognitionAudio(content=AUDIO_FILE.read_bytes())
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=sample_rate,
            language_code="ar-SA",
            audio_channel_count=channels,
            enable_separate_recognition_per_channel=channels > 1,
            enable_automatic_punctuation=True,
        )
        response = speech.SpeechClient().recognize(config=config, audio=audio)
        transcripts = [
            result.alternatives[0].transcript.strip()
            for result in response.results
            if result.alternatives and result.alternatives[0].transcript.strip()
        ]
        if not transcripts:
            print("ERROR: Speech-to-Text returned no recognized speech.")
            return 1

        print("SUCCESS: Speech-to-Text smoke test passed (ar-SA).")
        print("Recognized Arabic text:")
        print(" ".join(transcripts))
        return 0
    except wave.Error as exc:
        print(f"ERROR: test_audio.wav is not a valid PCM WAV file: {exc}")
        return 1
    except google_exceptions.GoogleAPICallError as exc:
        print(f"ERROR: Speech-to-Text API request failed: {exc}")
        return 1
    except Exception as exc:
        print(f"ERROR: Unexpected Speech-to-Text smoke-test failure: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
