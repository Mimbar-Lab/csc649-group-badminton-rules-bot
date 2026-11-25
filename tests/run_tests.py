import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.chatbot import ask_chatbot

TEST_FILE = os.path.join(os.path.dirname(__file__), "test_questions.csv")


def run():
    df = pd.read_csv(TEST_FILE)
    print("=== RUNNING BWF BADMINTON CHATBOT TESTS ===\n")
    for _, row in df.iterrows():
        q = row["Question"]
        expected = row["Expected_Topic"]
        q_type = row["Type"]

        reply, _ = ask_chatbot(q)
        print(f"Test #{row['Test_ID']} [{q_type}]")
        print(f"Question : {q}")
        print(f"Expected : {expected}")
        print(f"Bot Reply: {reply.strip()}")
        print("-" * 50)


if __name__ == "__main__":
    run()