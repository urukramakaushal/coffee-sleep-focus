# ☕ Coffee, Sleep & Focus

A small data science project exploring how coffee and sleep relate to focus, using synthetic data.

## Run it
```bash
pip install -r requirements.txt
python src/generate_data.py
python src/analyze.py
```

## What it does
- `generate_data.py` creates 200 days of synthetic data in `data/habits.csv`
- `analyze.py` prints summary stats, correlations, fits a simple linear regression, and saves `focus_plot.png`

## Ideas to extend (one per day!)
- Day 2: add a train/test split and report R²
- Day 3: try a random forest and compare
- Day 4: add a Jupyter notebook with EDA
- Day 5: swap in real personal data
