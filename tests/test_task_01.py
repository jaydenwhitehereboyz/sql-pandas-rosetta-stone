import pandas as pd

from pandas_solutions.task_01_payment_status_share import payment_status_share


def test_task_01_payment_status_share(payments, run_sql):
    expected = run_sql("sql/01_payment_status_share.sql")
    result = payment_status_share(payments)
    pd.testing.assert_frame_equal(result, expected, check_dtype=False, atol=0.1)
    print("\nSQL:\n", expected)
    print("\npandas:\n", result)