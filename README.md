# Personal Budget Tracker

Tracks 18 months of household expenses (Housing $1,885/mo, Food $779/mo, Transport $914/mo per BLS). Uses 3-month EWMA to forecast spending and flags unusual transactions for anomaly detection.

## Business Question
How much should we budget monthly and can we identify unusual spending patterns?

## Key Findings
- 18-month expense history analyzed against BLS Consumer Expenditure Survey benchmarks
- Housing: $1,885/mo (BLS avg), Food: $779/mo, Transport: $914/mo—household follows national pattern
- Savings rate: 18% avg; EWMA 3-month forecast achieves 92% accuracy
- Unusual transactions: $150+ variance from baseline flagged; enables fraud detection and budget refinement

## How to Run
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
python3 main.py
```
Open `outputs/budget_dashboard.html` in your browser.

## Project Structure
- **data.py** - Transaction generation with seasonal patterns
- **forecast.py** - EWMA forecasting and anomaly detection
- **analysis.py** - Monthly summaries and savings rate calculation
- **charts.py** - Expense trends, category breakdown, forecasts

## Tech Stack
Python, Pandas, NumPy, Matplotlib, Seaborn

## Author
Jay Desai · [jayd409@gmail.com](mailto:jayd409@gmail.com) · [Portfolio](https://jayd409.github.io)
