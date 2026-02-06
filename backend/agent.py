# backend/agent.py

import json
from backend.llm import generate_response
from backend.core.logger import logger


# ---------------------------
# EMAIL CLASSIFICATION
# ---------------------------
def classify_email(subject: str, body: str) -> dict:
    """
    Classifies email into Spam, Complaint, Job, or Inquiry.
    Returns structured JSON output.
    """

    prompt = f"""
You are an AI email classification system.

Classify the following email into ONE of these categories:
- Spam
- Complaint
- Job
- Inquiry

Return ONLY valid JSON in this exact format:

{{
    "category": "Spam | Complaint | Job | Inquiry",
    "confidence": 0.0,
    "reason": "Short explanation"
}}

Email:
Subject: {subject}
Body: {body}
"""

    try:
        result = generate_response(prompt)

        # Parse JSON safely
        parsed = json.loads(result)

        logger.info(f"Classification result: {parsed}")
        return parsed

    except json.JSONDecodeError:
        logger.error("Failed to parse classification response as JSON.")
        return {
            "category": "Unknown",
            "confidence": 0.0,
            "reason": "Model returned invalid JSON."
        }

    except Exception as e:
        logger.error(f"Classification error: {e}")
        return {
            "category": "Error",
            "confidence": 0.0,
            "reason": str(e)
        }


# ---------------------------
# REPLY GENERATION
# ---------------------------
def generate_reply(subject: str, body: str) -> str:
    """
    Generates a professional email reply.
    """

    prompt = f"""
You are a professional AI email assistant.

Write a polite, concise, and professional email reply.

Rules:
- Use formal tone
- Keep it under 200 words
- Do NOT hallucinate details
- If email is spam, warn the user politely
- Sign the email as: Support Team

Email:
Subject: {subject}
Body: {body}
"""

    try:
        reply = generate_response(prompt)
        logger.info("Reply generated successfully.")
        return reply

    except Exception as e:
        logger.error(f"Reply generation failed: {e}")
        return "Unable to generate reply at the moment."


# ---------------------------
# AGENT BUILDER
# ---------------------------
def build_agent():
    class Agent:
        def invoke(self, data: dict):
            subject = data.get("subject", "")
            body = data.get("body", "")

            logger.info("Starting agent pipeline...")

            # Step 1: Classification
            logger.info("Classifying email...")
            classification = classify_email(subject, body)

            # Step 2: Reply generation
            logger.info("Generating reply...")
            reply = generate_reply(subject, body)

            logger.info("Agent pipeline completed.")

            return {
                "subject": subject,
                "body": body,
                "category": classification["category"],
                "confidence": classification["confidence"],
                "reason": classification["reason"],
                "reply": reply
            }

    return Agent()
