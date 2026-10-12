import pandas as pd



def platform_fee(payments: pd.DataFrame) -> pd.DataFrame:
    month = payments['created_at'].dt.month
    mask = (payments['is_deleted'] == False) & (payments['status'] == 'succeeded') & (payments['created_at'] > '2025-01-01') & (payments['created_at'] < '2026-01-01')
    return payments[mask].groupby(month).agg(platform_revenue=('platform_fee_amount','sum'),payments_count=('payment_id','count'),avg_amount=('amount','mean')).round().reset_index().rename(columns={"created_at":"month"})



