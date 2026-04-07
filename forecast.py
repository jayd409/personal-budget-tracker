import pandas as pd
import numpy as np

def monthly_forecast(df, months_ahead=3):
    """Forecast monthly spend per category using EWMA."""
    df = df.copy()
    df['month'] = pd.to_datetime(df['date']).dt.to_period('M').astype(str)
    monthly = df[df['type'] == 'expense'].groupby(['month', 'category'])['amount'].sum().reset_index()
    results = []
    for cat, grp in monthly.groupby('category'):
        ts = grp.sort_values('month')['amount']
        if len(ts) < 2:
            continue
        ewma = ts.ewm(span=3).mean()
        last = float(ewma.iloc[-1])
        slope = (ewma.iloc[-1] - ewma.iloc[max(0, len(ewma)-3)]) / 3
        for i in range(1, months_ahead+1):
            results.append({
                'category': cat,
                'months_ahead': i,
                'forecast': round(max(0, last + slope*i), 2)
            })
    return pd.DataFrame(results)

def flag_unusual(df, z=2.2):
    """Flag unusually high transactions in each category."""
    expenses = df[df['type'] == 'expense'].copy()
    expenses['z'] = expenses.groupby('category')['amount'].transform(
        lambda x: (x - x.mean()) / (x.std() + 1e-8))
    return expenses[expenses['z'] > z][['date', 'category', 'description', 'amount', 'z']].sort_values('z', ascending=False)
