"""Real Gemini API smoke test for the Rafeeq project."""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import errors


def load_environment() -> None:
    """Load the existing project .env without overriding shell variables."""
    explicit_env = os.getenv("RAFEEQ_ENV_FILE")
    if explicit_env:
        load_dotenv(explicit_env, override=False)
        return
    load_dotenv(Path.cwd() / ".env", override=False)
    load_dotenv(Path(__file__).resolve().parent / ".env", override=False)


def main() -> int:
    load_environment()
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: Set GEMINI_API_KEY (or GOOGLE_API_KEY) in the existing .env file.")
        return 1

    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    prompt = os.getenv(
        "GEMINI_SMOKE_TEST_PROMPT",
        (
            "حلّل طلب المستخدم باللهجة السعودية وأعد JSON فقط يحتوي intent وtime: "
            "ذكّرني آخذ الدواء الساعة ثمانية مساءً"
        ),
    )

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(model=model, contents=prompt)
        response_text = (response.text or "").strip()
        if not response_text:
            print("ERROR: Gemini returned an empty response.")
            return 1
        print(f"SUCCESS: Gemini smoke test passed using {model}.")
        print("AI response:")
        print(response_text)
        return 0
    except errors.APIError as exc:
        print(f"ERROR: Gemini API request failed ({exc.code}): {exc.message}")
        return 1
    except Exception as exc:
        print(f"ERROR: Unexpected Gemini smoke-test failure: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
