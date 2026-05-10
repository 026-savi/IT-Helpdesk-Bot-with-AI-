def detect_priority(text):
    text = text.lower()

    if "urgent" in text or "not working" in text or "down" in text:
        return "high"
    elif "slow" in text or "issue" in text:
        return "medium"
    else:
        return "low"