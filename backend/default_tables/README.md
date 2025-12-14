# Default tables

Default tables provide accident_type and injury_type based on HSE classification.

HSE Stats: https://www.hse.gov.uk/statistics/tables/index.htm

**RIDNAT - RIDDOR reported fatal and non-fatal injuries in Great Britain by nature of injury**

- https://www.hse.gov.uk/statistics/assets/docs/ridnat.xlsx

> injury_types is based on "nature of injury"

**RIDKIND - RIDDOR reported fatal and non-fatal injuries in Great Britain by kind of accident and broad industry group (.xlsx)**

- https://www.hse.gov.uk/statistics/assets/docs/ridkind.xlsx

> accident_type is based on "kind of accident"

**The default accident and injury types are bulk inserted as part of the initial alembic revision:**

```python
accident_types = sa.table(
    "accident_types",
    sa.column("id", sa.Integer),
    sa.column("name", sa.String),
)
op.bulk_insert(
    accident_types,
    pd.read_csv("backend/default_tables/accident.csv").to_dict("records"),
)

injury_types = sa.table(
    "injury_types",
    sa.column("id", sa.Integer),
    sa.column("name", sa.String),
)
op.bulk_insert(
    injury_types,
    pd.read_csv("backend/default_tables/injury.csv").to_dict("records"),
)
```
