import pandas as pd



def gmv_by_year(payments: pd.DataFrame) -> pd.DataFrame:
    year = payments['created_at'].dt.year.rename('year')
    mask = (payments['is_deleted'] == False) & (payments['status'] == 'succeeded')
    payments = payments[mask]
    return payments.groupby(by=year)['amount'].agg(gmv='sum').round().reset_index()





