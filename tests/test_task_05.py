import pandas as pd
from pandas_solutions.task_05_failed_pct import failed_pct


def test_task_05_failed_pct(payments, run_sql):
    expected = run_sql("sql/05_failed_pct.sql")
    result = failed_pct(payments)
    pd.testing.assert_frame_equal(result, expected, check_dtype=False, atol=0.1)
    print("\nSQL:\n", expected)
    print("\npandas:\n", result)