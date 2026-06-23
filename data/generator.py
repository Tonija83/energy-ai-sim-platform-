import numpy as np
import pandas as pd

def generate_smart_meter_data(n=500):
    time = pd.date_range("2024-01-01", periods=n, freq="H")

    base = np.sin(np.linspace(0, 30, n))
    noise = np.random.normal(0, 0.3, n)

    consumption = base + noise + 2

    return pd.DataFrame({
        "timestamp": time,
        "consumption": consumption
    })
