import os
import pandas as pd
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")


def load_dataset() -> pd.DataFrame:
    """Load the verified BWF Badminton Q&A dataset from data/dataset.csv."""
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")
    return pd.read_csv(DATA_PATH)


def retrieve_relevant_qa(user_query: str, top_k: int = 3) -> str:
    """Find the top_k most relevant Q&A pairs using weighted keyword overlap."""
    df = load_dataset()
    stop_words = {"what", "is", "the", "a", "an", "to", "for", "in", "on", "of", "how", "can", "i", "do", "are"}
    query_words = {
        word.strip("?.,!").lower()
        for word in user_query.split()
        if word.strip("?.,!").lower() not in stop_words
    }

    scored_rows = []
    for _, row in df.iterrows():
        q_text = str(row["Question"]).lower()
        a_text = str(row["Answer"]).lower()
        # Give 2 points for matching words in Question and 1 point in Answer
        score = sum(2 for w in query_words if w in q_text) + sum(1 for w in query_words if w in a_text)
        scored_rows.append((score, row["Question"], row["Answer"]))

    scored_rows.sort(key=lambda x: x[0], reverse=True)
    top_matches = [item for item in scored_rows[:top_k] if item[0] > 0]

    if not top_matches:
        return "NO_RELEVANT_DATA_FOUND"

    context_blocks = []
    for _, q, a in top_matches:
        context_blocks.append(f"Q: {q}\nA: {a}")
    return "\n\n".join(context_blocks)


def ask_chatbot(user_query: str) -> tuple[str, str]:
    """Retrieve BWF rules context and generate a grounded reply using Gemini 2.5 Flash."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Missing GEMINI_API_KEY. Please set it in your .env file.")

    retrieved_context = retrieve_relevant_qa(user_query, top_k=3)
    client = genai.Client(api_key=api_key)

    prompt = f"""
You are a helpful, accurate Badminton Rules Assistant based on official BWF Laws of Badminton.
Answer the user's question using ONLY the verified Knowledge Base Context provided below.

Rules:
1. If the answer is in the Knowledge Base Context, explain the rule clearly, accurately, and concisely.
2. Keep your response friendly and easy for players and beginners to understand.
3. If the Knowledge Base Context is "NO_RELEVANT_DATA_FOUND" or does NOT contain the answer, politely say: "I'm sorry, I don't have verified information about that in my BWF badminton rules knowledge base. Please ask a question about court dimensions, scoring, serving, faults, lets, or match regulations." Do NOT guess or invent rules.

=== KNOWLEDGE BASE CONTEXT ===
{retrieved_context}

=== USER QUESTION ===
{user_query}
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.3),
        )
        return response.text, retrieved_context
    except Exception as e:
        return f"Sorry, I encountered a connection issue while contacting Gemini: {e}", retrieved_context
