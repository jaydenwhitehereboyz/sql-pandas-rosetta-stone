import pandas as pd


def failed_pct(payments: pd.DataFrame) -> pd.DataFrame:
    year = payments['created_at'].dt.year.rename('year')
    month = payments['created_at'].dt.month.rename('month')
    grouped =  payments.groupby([year,month]).agg(failed_count=('status', lambda s: (s == 'failed').sum()), payments_count=('status','count'),failed_pct=('status', lambda s: (s == 'failed').sum() * 100.0 / s.count())).reset_index()
    grouped =  grouped[grouped['failed_pct'] > 4]
    grouped['failed_pct'] = round(grouped['failed_pct'],1)
    grouped.index = range(0, len(grouped))
    return grouped



