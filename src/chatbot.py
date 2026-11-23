import os
import pandas as pd

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")


def load_dataset() -> pd.DataFrame:
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")
    return pd.read_csv(DATA_PATH)
