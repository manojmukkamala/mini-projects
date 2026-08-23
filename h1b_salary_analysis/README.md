# h1b_salary_analysis

Salary survey for data-engineer roles, built from the U.S. Department of
Labor's public **H-1B LCA (Labor Condition Application) disclosure
data** — quarterly Excel files of every filed LCA (job title,
employer, worksite, wage rate). The notebook surveys Lead and Staff
Data Engineer wages overall and at specific employers (Shipt,
Instacart, Uber, DoorDash, Grubhub), plus application volume over
time. Written in early 2024, mostly on Databricks.

`H1B_Sal_Analysis.ipynb` (63 cells) has two halves:

- **Spark** — `findspark` + PySpark session, `spark-excel` reader for
  the raw `.xlsx` files, xlsx→csv conversion, Delta table
  (`test_db.lca_2022_csv`), then SQL: application counts by
  received-date, employer counts, and wage pulls for
  lead/staff data-engineer titles (with `director`/`test` titles
  filtered out) at the employers above.
- **Pandas** — `openpyxl`-based fallback: read the FY2023 Q1 xlsx,
  filter to Lead / Staff Data Engineer rows, fill `WAGE_RATE_OF_PAY_TO`
  from `_FROM`, and produce `describe()` + histograms.

## How to run

Built for a Databricks workspace and not directly runnable as
committed: the data cells point at stale workspace paths (see Notes)
and the cells ran in a non-linear order (the Pandas half produces the
CSVs the Spark half reads). To run locally:

1. Download the quarterly files below into two local folders
   (`2021_salaries/`, `2022_salaries/`).
2. Point the data cells at those folders, plus the relative
   `lca_Q1_2023.xlsx` reference in the Pandas half.

```sh
pip install pandas openpyxl matplotlib findspark pyspark delta-spark
jupyter notebook H1B_Sal_Analysis.ipynb
```

## Data

DOL H-1B LCA disclosure data, public and re-downloadable (three of the
URLs spot-checked live on 2026-08-23; the rest follow the same
pattern). Index page:
<https://www.dol.gov/agencies/eta/foreign-labor/performance>

```
https://www.dol.gov/sites/dolgov/files/ETA/oflc/pdfs/LCA_Disclosure_Data_FY2021_Q1.xlsx
https://www.dol.gov/sites/dolgov/files/ETA/oflc/pdfs/LCA_Disclosure_Data_FY2021_Q2.xlsx
https://www.dol.gov/sites/dolgov/files/ETA/oflc/pdfs/LCA_Disclosure_Data_FY2021_Q3.xlsx
https://www.dol.gov/sites/dolgov/files/ETA/oflc/pdfs/LCA_Disclosure_Data_FY2021_Q4.xlsx
https://www.dol.gov/sites/dolgov/files/ETA/oflc/pdfs/LCA_Disclosure_Data_FY2022_Q1.xlsx
https://www.dol.gov/sites/dolgov/files/ETA/oflc/pdfs/LCA_Disclosure_Data_FY2022_Q2.xlsx
https://www.dol.gov/sites/dolgov/files/ETA/oflc/pdfs/LCA_Disclosure_Data_FY2022_Q3.xlsx
https://www.dol.gov/sites/dolgov/files/ETA/oflc/pdfs/LCA_Disclosure_Data_FY2022_Q4.xlsx
https://www.dol.gov/sites/dolgov/files/ETA/oflc/pdfs/LCA_Disclosure_Data_FY2023_Q1.xlsx
```

## Notes

- **Stale Databricks paths:** all data references point into an old
  workspace (`/opt/spark/work-dir/manoj_repo/shipt/storage/spark/…`)
  that no longer exists — nothing in the repo depends on it; the data
  comes from the DOL URLs above.
- No data files are committed (the xlsx/CSV downloads were never
  copied into this folder); the notebook is self-describing with the
  URLs above.
