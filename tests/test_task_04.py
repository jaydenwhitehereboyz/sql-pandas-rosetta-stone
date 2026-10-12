import pandas as pd
from pandas_solutions.task_04_top_10_gmv import top_10_gmv


def test_task_04_top_10_gmv(payments, run_sql):
    expected = run_sql("sql/04_top_10_gmv.sql")
    result = top_10_gmv(payments)
    pd.testing.assert_frame_equal(result, expected, check_dtype=False, atol=0.1)
    print("\nSQL:\n", expected)
    print("\npandas:\n", result)