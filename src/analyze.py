import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data/habits.csv")
print(df.describe().round(2), "\n")
print("Correlations:\n", df.corr().round(2), "\n")

X, y = df[["coffee_cups", "sleep_hours"]], df["focus_score"]
model = LinearRegression().fit(X, y)
print("Coefficients:", dict(zip(X.columns, model.coef_.round(3))))
print("R^2:", round(model.score(X, y), 3))

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].scatter(df.sleep_hours, df.focus_score, alpha=0.5)
ax[0].set(xlabel="Sleep (hours)", ylabel="Focus", title="Sleep vs Focus")
df.groupby("coffee_cups").focus_score.mean().plot(kind="bar", ax=ax[1])
ax[1].set(xlabel="Cups of coffee", ylabel="Mean focus", title="Coffee vs Focus")
plt.tight_layout()
plt.savefig("focus_plot.png", dpi=120)
