import pandas as pd
import numpy as np

def monthly_summary(df):
    """Monthly income vs expense analysis."""
    df_copy = df.copy()
    df_copy['month'] = pd.to_datetime(df_copy['date']).dt.to_period('M').astype(str)
    monthly = df_copy.groupby('month').apply(
        lambda x: pd.Series({
            'income': x[x['type'] == 'income']['amount'].sum(),
            'expense': x[x['type'] == 'expense']['amount'].sum()
        }), include_groups=False
    ).reset_index()
    monthly['savings'] = monthly['income'] - monthly['expense']
    return monthly

def savings_rate(df):
    """Calculate monthly savings rate."""
    monthly = monthly_summary(df)
    monthly['savings_rate'] = (monthly['savings'] / monthly['income'] * 100).round(2)
    return monthly

def category_spending(df):
    """Total spending by category."""
    expenses = df[df['type'] == 'expense']
    return expenses.groupby('category')['amount'].sum().sort_values(ascending=False)

def category_trends(df):
    """Spending trend per category over time."""
    df_copy = df.copy()
    df_copy['month'] = pd.to_datetime(df_copy['date']).dt.to_period('M').astype(str)
    expenses = df_copy[df_copy['type'] == 'expense']
    return expenses.groupby(['month', 'category'])['amount'].sum().reset_index()
