import torch
from speechbrain.pretrained import EncoderClassifier

# Load the English accent classifier model
classifier = EncoderClassifier.from_hparams(
    source="Jzuluaga/accent-id-commonaccent_ecapa",
    savedir="pretrained_models/accent-id-commonaccent_ecapa",
    run_opts={"device": "cpu"},  # change to "cuda" if GPU available
)

# Mapping of accent labels to human-readable names
ACCENT_LABELS = {
    "african": "African English",
    "australia": "Australian English",
    "bermuda": "Bermuda English",
    "canada": "Canadian English",
    "england": "British English",
    "hongkong": "Hong Kong English",
    "indian": "Indian English",
    "ireland": "Irish English",
    "malaysia": "Malaysian English",
    "newzealand": "New Zealand English",
    "philippines": "Philippine English",
    "scotland": "Scottish English",
    "singapore": "Singaporean English",
    "southatlandtic": "South Atlantic English",
    "us": "American English",
    "wales": "Welsh English",
}

def classify_accent(audio_path):
    signal = classifier.load_audio(audio_path)
    out_prob, score, index, text_lab = classifier.classify_batch(signal)
    confidence = torch.softmax(out_prob, dim=1)[0, index[0]].item()
    predicted_label = text_lab[0] if text_lab else "unknown"
    accent = ACCENT_LABELS.get(predicted_label, "Unknown English Accent")
    return {
        "accent": accent,
        "confidence": round(confidence * 100, 2),
        "raw_label": predicted_label,
    }
