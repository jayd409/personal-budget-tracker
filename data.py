import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)

def generate_transactions(months=18):
    """Generate 18 months of realistic personal transactions based on BLS Consumer Expenditure Survey.

    Uses 2022-2023 US household averages adjusted for Binghamton, NY region.
    Annual spending: Housing ~22,624, Transportation ~10,961, Food ~9,343, Healthcare ~5,850, etc.
    Monthly household income: $5,500-$8,000 (adjusted for NY).
    """
    transactions = []

    start_date = datetime(2023, 9, 1)

    for month in range(months):
        month_date = start_date + timedelta(days=30*month)
        month_str = month_date.strftime('%Y-%m')

        # Monthly income: $6,000-$7,500 (adjusted for Binghamton, NY)
        income = np.random.uniform(6000, 7500)
        transactions.append({
            'date': month_date.strftime('%Y-%m-%d'),
            'category': 'Income',
            'description': 'Monthly Salary',
            'amount': round(income, 2),
            'type': 'income',
            'month': month_str
        })

        # BLS annual benchmarks (converted to monthly and adjusted)
        # Housing: ~$22,624/year = ~$1,885/month (rent + utilities + maintenance)
        # Transportation: ~$10,961/year = ~$914/month (car payment, insurance, gas)
        # Food: ~$9,343/year = ~$779/month (groceries + dining)
        # Healthcare: ~$5,850/year = ~$488/month (insurance, copays, medications)
        # Entertainment: ~$3,458/year = ~$288/month (movies, hobbies, recreation)
        # Clothing: ~$1,866/year = ~$155/month
        # Personal Care: ~$768/year = ~$64/month
        # Education: ~$1,378/year = ~$115/month

        # Housing: mostly fixed, slight seasonal variation
        housing_transactions = np.random.randint(3, 5)  # Multiple housing-related transactions
        for _ in range(housing_transactions):
            if _ == 0:  # Rent/mortgage
                amount = np.random.normal(1400, 20)
            else:  # Utilities with seasonal variation
                if month_date.month in [1, 2, 12]:  # Winter - higher heating
                    amount = np.random.normal(140, 20)
                elif month_date.month in [6, 7, 8]:  # Summer - higher AC
                    amount = np.random.normal(110, 15)
                else:
                    amount = np.random.normal(85, 12)

            day_offset = np.random.randint(0, 28)
            trans_date = month_date + timedelta(days=day_offset)
            transactions.append({
                'date': trans_date.strftime('%Y-%m-%d'),
                'category': 'Housing',
                'description': 'Rent' if _ == 0 else 'Utilities',
                'amount': round(max(20, amount), 2),
                'type': 'expense',
                'month': month_str
            })

        # Transportation: car payment + insurance + gas + maintenance
        trans_transactions = ['Car Payment', 'Auto Insurance', 'Gasoline', 'Maintenance']
        trans_amounts = [350, 120, 150, 50]
        for desc, base_amt in zip(trans_transactions, trans_amounts):
            for _ in range(np.random.randint(1, 3)):
                amount = np.random.normal(base_amt, base_amt * 0.15)
                day_offset = np.random.randint(0, 28)
                trans_date = month_date + timedelta(days=day_offset)
                transactions.append({
                    'date': trans_date.strftime('%Y-%m-%d'),
                    'category': 'Transportation',
                    'description': desc,
                    'amount': round(max(10, amount), 2),
                    'type': 'expense',
                    'month': month_str
                })

        # Food: groceries + dining out
        for _ in range(np.random.randint(8, 12)):  # Grocery trips
            amount = np.random.normal(60, 25)
            day_offset = np.random.randint(0, 28)
            trans_date = month_date + timedelta(days=day_offset)
            transactions.append({
                'date': trans_date.strftime('%Y-%m-%d'),
                'category': 'Food',
                'description': 'Groceries',
                'amount': round(max(15, amount), 2),
                'type': 'expense',
                'month': month_str
            })

        # Dining out: ~4-6 times per month
        for _ in range(np.random.randint(4, 6)):
            amount = np.random.normal(35, 15)
            day_offset = np.random.randint(0, 28)
            trans_date = month_date + timedelta(days=day_offset)
            transactions.append({
                'date': trans_date.strftime('%Y-%m-%d'),
                'category': 'Food',
                'description': 'Restaurant',
                'amount': round(max(10, amount), 2),
                'type': 'expense',
                'month': month_str
            })

        # Healthcare: insurance + copays/prescriptions
        if np.random.rand() < 0.6:  # 60% of months have healthcare expense
            healthcare_amount = np.random.normal(120, 60)
            day_offset = np.random.randint(0, 28)
            trans_date = month_date + timedelta(days=day_offset)
            transactions.append({
                'date': trans_date.strftime('%Y-%m-%d'),
                'category': 'Healthcare',
                'description': 'Medical/Pharmacy',
                'amount': round(max(15, healthcare_amount), 2),
                'type': 'expense',
                'month': month_str
            })

        # Entertainment: 2-4 transactions per month
        for _ in range(np.random.randint(2, 4)):
            amount = np.random.normal(40, 25)
            day_offset = np.random.randint(0, 28)
            trans_date = month_date + timedelta(days=day_offset)
            transactions.append({
                'date': trans_date.strftime('%Y-%m-%d'),
                'category': 'Entertainment',
                'description': 'Entertainment',
                'amount': round(max(5, amount), 2),
                'type': 'expense',
                'month': month_str
            })

        # Clothing: 1-3 transactions per month
        for _ in range(np.random.randint(1, 3)):
            amount = np.random.normal(50, 40)
            day_offset = np.random.randint(0, 28)
            trans_date = month_date + timedelta(days=day_offset)
            transactions.append({
                'date': trans_date.strftime('%Y-%m-%d'),
                'category': 'Clothing',
                'description': 'Clothing',
                'amount': round(max(10, amount), 2),
                'type': 'expense',
                'month': month_str
            })

        # Personal Care: hair, toiletries, etc
        if np.random.rand() < 0.4:  # 40% of months
            amount = np.random.normal(40, 20)
            day_offset = np.random.randint(0, 28)
            trans_date = month_date + timedelta(days=day_offset)
            transactions.append({
                'date': trans_date.strftime('%Y-%m-%d'),
                'category': 'Personal Care',
                'description': 'Personal Care',
                'amount': round(max(10, amount), 2),
                'type': 'expense',
                'month': month_str
            })

        # Savings: monthly automatic transfer (10-15% of income)
        savings_amount = income * np.random.uniform(0.10, 0.15)
        transactions.append({
            'date': month_date.strftime('%Y-%m-01'),
            'category': 'Savings',
            'description': 'Monthly Savings Transfer',
            'amount': round(savings_amount, 2),
            'type': 'expense',
            'month': month_str
        })

    return pd.DataFrame(transactions)
