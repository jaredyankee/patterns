import pandas as pd
from flatten_rows import flatten_dataframe

def test_collapses_orders_and_sums_price():
    df = pd.DataFrame({
        "order_id": [1, 1, 2, 3, 3, 3, 4],
        "item":     ["a", "b", "a", "a", "c", "a", "b"],
        "qty":      [2, 1, 5, 1, 3, 2, 4],
        "price":    [10.00, 25.50, 10.00, 10.00, 7.25, 10.00, 25.50],
        "customer": ["Acme", "Acme", "Beta", "Cato", "Cato", "Cato", "Dune"],
    })
    result = flatten_dataframe(df, "order_id", "price")

    assert len(result) == 4
    assert list(result["price"]) == [35.50, 10.00, 27.25, 25.50]
    assert "item" not in result.columns
