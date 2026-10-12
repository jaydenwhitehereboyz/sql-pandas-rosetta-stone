import pandas as pd

from pandas_solutions.task_02_gmv_by_year import gmv_by_year


def test_task_02_gmv_by_year(payments, run_sql):
    expected = run_sql("sql/02_gmv_by_year.sql")
    result = gmv_by_year(payments)
    pd.testing.assert_frame_equal(result, expected, check_dtype=False, atol=0.1)
    print("\nSQL:\n", expected)
    print("\npandas:\n", result)