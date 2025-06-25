import os
import sys
from download import download_and_extract_audio
from classify_accent import classify_accent

VIDEO_URL = "https://www.youtube.com/shorts/jJdHKN6LWWk"

def main():
    print(f"[1/2] Downloading and extracting audio from: {VIDEO_URL}")
    try:
        audio_path = download_and_extract_audio(VIDEO_URL)
    except Exception as e:
        print(f"Error downloading or extracting audio: {e}")
        sys.exit(1)

    print(f"[2/2] Classifying English accent...")
    try:
        accent_result = classify_accent(audio_path)
    except Exception as e:
        print(f"Error during accent classification: {e}")
        sys.exit(1)

    accent = accent_result["accent"]
    confidence = accent_result["confidence"]
    raw_label = accent_result["raw_label"]

    print(f"\nResult:")
    print(f"Detected English Accent: {accent}")
    print(f"Confidence Score: {confidence}%")
    print(f"(Model label: {raw_label})")

if __name__ == "__main__":
    main()
