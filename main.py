from data import generate_transactions
from forecast import monthly_forecast, flag_unusual
from analysis import monthly_summary, savings_rate
from charts import (income_vs_expense, spending_breakdown, savings_rate_trend,
                    category_trends_chart, forecast_chart, unusual_transactions)
from utils import save_html

df = generate_transactions(18)

fcast = monthly_forecast(df, 3)
unusual = flag_unusual(df, z=2.2)

monthly = monthly_summary(df)
avg_savings = monthly['savings'].mean()
overall_savings_rate = (df[df['type'] == 'income']['amount'].sum() -
                       df[df['type'] == 'expense']['amount'].sum()) / df[df['type'] == 'income']['amount'].sum() * 100

charts = [
    ('Monthly Income vs Expenses', income_vs_expense(df)),
    ('Spending Breakdown', spending_breakdown(df)),
    ('Savings Rate Trend', savings_rate_trend(df)),
    ('Category Trends', category_trends_chart(df)),
    ('3-Month Forecast', forecast_chart(df)),
    ('Unusual Transactions', unusual_transactions(df))
]

kpis = [
    ('Avg Monthly Savings', f"${avg_savings:.0f}"),
    ('Savings Rate', f"{overall_savings_rate:.1f}%"),
    ('Unusual Transactions', str(len(unusual))),
]

save_html(charts, 'Personal Budget Tracker', kpis, 'outputs/budget_dashboard.html')

print(f"\nAvg Monthly Savings: ${avg_savings:.0f} | Savings Rate: {overall_savings_rate:.1f}% | Unusual transactions: {len(unusual)}")
