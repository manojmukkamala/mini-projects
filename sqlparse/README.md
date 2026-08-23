# SQLparse

Tiny stdlib-only experiment: extract the table names referenced in a
SQL query.

`get_tables.py` defines `get_tables(query)`, which splits the query
into whitespace tokens, finds every `FROM` and `JOIN`, and collects
the token that follows each one. It filters out false positives:
subqueries (`FROM (` / `FROM SELECT`) and date functions
(`DAY(...)` / `MONTH(...)` / `YEAR(...)`) are skipped, and double
quotes are stripped from table names.

## How to run

No dependencies (pure stdlib), no install needed:

```sh
python3 -c "
from get_tables import get_tables
q = 'SELECT * FROM orders JOIN customers ON orders.cid = customers.id WHERE DAY(created) > 0'
print(get_tables(q))   # ['orders', 'customers']
"
```

## Limitations

This is a tokenizing sketch, not a real SQL parser — it mis-handles
e.g. quoted identifiers containing whitespace, `FROM(SELECT` written
without a space, schema-qualified names (`db.table` keeps the dot),
and keywords used as column names. (The real `sqlparse` PyPI
package parses SQL properly, if you ever need one.)
