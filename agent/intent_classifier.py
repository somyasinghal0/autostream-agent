def classify_intent(user_input):
    text = user_input.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(word in text for word in ["buy", "subscribe", "sign up", "try", "start", "interested"]):
        return "high_intent"

    elif any(word in text for word in ["offer", "offers", "feature", "features", "plans", "service"]):
        return "pricing"

    elif any(word in text for word in ["more", "detail", "details", "explain", "tell me more"]):
        return "follow_up"

    elif any(word in text for word in ["thanks", "thank you"]):
        return "thanks"

    return "unknown"