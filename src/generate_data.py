import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 200
coffee = rng.integers(0, 6, n)
sleep = np.clip(rng.normal(7, 1.2, n), 3, 10)
focus = np.clip(3 + 0.9 * sleep + 0.5 * coffee - 0.12 * coffee**2 + rng.normal(0, 0.8, n), 0, 10)

df = pd.DataFrame({"coffee_cups": coffee, "sleep_hours": sleep.round(1), "focus_score": focus.round(2)})
df.to_csv("data/habits.csv", index=False)
print("Saved data/habits.csv", df.shape)
