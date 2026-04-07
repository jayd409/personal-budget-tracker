import matplotlib.pyplot as plt
import pandas as pd
from analysis import monthly_summary, savings_rate, category_spending, category_trends
from forecast import monthly_forecast, flag_unusual

def income_vs_expense(df):
    """Chart 1: Monthly income vs expenses."""
    monthly = monthly_summary(df)
    fig, ax = plt.subplots(figsize=(10, 5))
    x = range(len(monthly))
    width = 0.35
    ax.bar([i - width/2 for i in x], monthly['income'], width, label='Income', color='green')
    ax.bar([i + width/2 for i in x], monthly['expense'], width, label='Expense', color='red')
    ax.set_title('Monthly Income vs Expenses', fontsize=12, fontweight='bold')
    ax.set_xlabel('Month')
    ax.set_ylabel('Amount ($)')
    ax.legend()
    ax.set_xticks(x)
    ax.set_xticklabels(monthly['month'], rotation=45, fontsize=8)
    return fig

def spending_breakdown(df):
    """Chart 2: Spending breakdown by category."""
    cat_spend = category_spending(df)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.pie(cat_spend.values, labels=cat_spend.index, autopct='%1.1f%%')
    ax.set_title('Spending Breakdown by Category', fontsize=12, fontweight='bold')
    return fig

def savings_rate_trend(df):
    """Chart 3: Savings rate by month."""
    monthly = savings_rate(df)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(monthly['month'], monthly['savings_rate'], marker='o', color='blue', linewidth=2)
    ax.axhline(y=monthly['savings_rate'].mean(), color='green', linestyle='--', label='Average')
    ax.set_title('Monthly Savings Rate', fontsize=12, fontweight='bold')
    ax.set_xlabel('Month')
    ax.set_ylabel('Savings Rate (%)')
    ax.legend()
    ax.tick_params(axis='x', rotation=45)
    return fig

def category_trends_chart(df):
    """Chart 4: Top 4 category spending trends."""
    trends = category_trends(df)
    top_cats = category_spending(df).nlargest(4).index
    fig, ax = plt.subplots(figsize=(10, 5))
    for cat in top_cats:
        cat_data = trends[trends['category'] == cat]
        ax.plot(cat_data['month'], cat_data['amount'], marker='o', label=cat)
    ax.set_title('Spending Trends (Top 4 Categories)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Month')
    ax.set_ylabel('Amount ($)')
    ax.legend()
    ax.tick_params(axis='x', rotation=45)
    return fig

def forecast_chart(df):
    """Chart 5: 3-month forecast by category."""
    fcast = monthly_forecast(df, months_ahead=3)
    fig, ax = plt.subplots(figsize=(10, 5))
    for cat in fcast['category'].unique()[:5]:
        cat_fcast = fcast[fcast['category'] == cat]
        ax.plot(cat_fcast['months_ahead'], cat_fcast['forecast'], marker='o', label=cat)
    ax.set_title('3-Month Spending Forecast', fontsize=12, fontweight='bold')
    ax.set_xlabel('Months Ahead')
    ax.set_ylabel('Forecast Amount ($)')
    ax.legend(fontsize=8)
    return fig

def unusual_transactions(df):
    """Chart 6: Unusual transactions (high z-score)."""
    unusual = flag_unusual(df, z=2.2)
    fig, ax = plt.subplots(figsize=(10, 5))
    if len(unusual) > 0:
        colors = ['red' if z > 3 else 'orange' for z in unusual['z'].head(15)]
        ax.barh(range(min(15, len(unusual))), unusual['amount'].head(15), color=colors)
        ax.set_yticks(range(min(15, len(unusual))))
        ax.set_yticklabels([f"{c[:15]}" for c in unusual['category'].head(15)], fontsize=8)
    ax.set_title('Unusual Transactions (Top 15)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Amount ($)')
    return fig
