load_dotenv()

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")


def load_dataset() -> pd.DataFrame:
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")
    return pd.read_csv(DATA_PATH)


def retrieve_relevant_qa(user_query: str, top_k: int = 3) -> str:
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
