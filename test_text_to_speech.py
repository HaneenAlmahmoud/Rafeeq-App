"""Real Google Cloud Text-to-Speech smoke test for Arabic output."""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from google.api_core import exceptions as google_exceptions
from google.cloud import texttospeech


SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = SCRIPT_DIR / "rafeeq_test.mp3"
DEFAULT_TEXT = "مرحبًا، أنا رفيق. يسعدني أن أساعدك اليوم."


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

    arabic_text = os.getenv("RAFEEQ_TTS_TEXT", DEFAULT_TEXT).strip()
    if not arabic_text:
        print("ERROR: RAFEEQ_TTS_TEXT is empty.")
        return 1

    try:
        response = texttospeech.TextToSpeechClient().synthesize_speech(
            input=texttospeech.SynthesisInput(text=arabic_text),
            voice=texttospeech.VoiceSelectionParams(
                language_code="ar-XA",
                ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
            ),
            audio_config=texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3,
                speaking_rate=0.85,
            ),
        )
        if not response.audio_content:
            print("ERROR: Text-to-Speech returned empty audio content.")
            return 1

        OUTPUT_FILE.write_bytes(response.audio_content)
        print("SUCCESS: Text-to-Speech smoke test passed.")
        print(f"Saved MP3 output to: {OUTPUT_FILE}")
        return 0
    except google_exceptions.GoogleAPICallError as exc:
        print(f"ERROR: Text-to-Speech API request failed: {exc}")
        return 1
    except Exception as exc:
        print(f"ERROR: Unexpected Text-to-Speech smoke-test failure: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
