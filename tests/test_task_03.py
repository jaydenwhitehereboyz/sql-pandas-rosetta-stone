import pandas as pd

from pandas_solutions.task_03_platform_fee import platform_fee


def test_task_03_platform_fee(payments, run_sql):
    expected = run_sql("sql/03_platform_fee.sql")
    result = platform_fee(payments)
    pd.testing.assert_frame_equal(result, expected, check_dtype=False, atol=0.1)
    print("\nSQL:\n", expected)
    print("\npandas:\n", result)