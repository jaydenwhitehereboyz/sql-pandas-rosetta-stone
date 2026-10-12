import pandas as pd


def top_10_gmv(payments: pd.DataFrame) -> pd.DataFrame:
    success = (payments['is_deleted'] == False) & (payments['status'] == 'succeeded')
    return payments[success].groupby('account_id')['amount'].sum().sort_values(ascending=False).round().reset_index().rename(columns={"amount":"gmv"}).iloc[:10]


