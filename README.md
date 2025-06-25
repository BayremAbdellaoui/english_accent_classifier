# English Accent Detector from Video URLs

This project is a lightweight CLI tool that detects the English accent (e.g., American, British, Indian, Australian, etc.) from the audio of a video URL (YouTube, Loom, etc.).

## Features
- Accepts a video URL as input
- Downloads and extracts audio automatically
- Detects the English accent using a state-of-the-art open-source model
- Outputs the detected accent, confidence score, and model label

## Supported Accents
- American English
- British English
- Australian English
- Indian English
- Irish English
- Canadian English
- Scottish English
- Welsh English
- South Atlantic English
- Hong Kong English
- Singaporean English
- Malaysian English
- Philippine English
- Bermuda English
- African English
- New Zealand English

## Requirements
- Python 3.8+
- [ffmpeg](https://ffmpeg.org/) installed and available in your PATH

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/BayremAbdellaoui/english_accent_classifier.git
   cd accent_detector
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Edit `app.py` and set your desired video URL in the `VIDEO_URL` variable.
2. Run the CLI tool:
   ```bash
   python app.py
   ```
3. The tool will download the video, extract the audio, and print the detected English accent and confidence score.

## Notes
- The accent classifier model is open-source and provided by [Jzuluaga/accent-id-commonaccent_ecapa](https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa).
- The model works best with clear, single-speaker English audio. Results may be less accurate for noisy, multi-speaker, or short clips.
- All downloaded models and audio files are stored locally and ignored by git.

## License
MIT License

## Acknowledgements
- [SpeechBrain](https://speechbrain.github.io/)
- [HuggingFace Model: Jzuluaga/accent-id-commonaccent_ecapa](https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for video downloading 