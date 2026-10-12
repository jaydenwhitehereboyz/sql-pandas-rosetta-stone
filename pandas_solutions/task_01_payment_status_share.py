import pandas as pd


def payment_status_share(payments: pd.DataFrame) -> pd.DataFrame:
    status_count = payments['status'].value_counts()
    status_pct = payments['status'].value_counts(normalize=True).mul(100).round(1)

    return (
        pd.concat([status_count,status_pct],axis=1,keys=['status_count','share_pct']).reset_index()
    )

