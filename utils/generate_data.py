import pandas as pd
import random

def generate_data(rows=500000):
    """Generate synthetic data with the specified number of rows."""
    data = {
        "user_id": [random.randint(1, 1000) for _ in range(rows)],
        "event_id": [random.randint(1, 500) for _ in range(rows)],
        "created_at_user": pd.date_range(start="2023-01-01", periods=rows, freq="T").strftime('%Y-%m-%d %H:%M:%S'),
        "created_at_event": pd.date_range(start="2023-01-01", periods=rows, freq="T").strftime('%Y-%m-%d %H:%M:%S'),
    }
    df = pd.DataFrame(data)
    output_path = "data/raw_data.csv"
    df.to_csv(output_path, index=False)
    return output_path
