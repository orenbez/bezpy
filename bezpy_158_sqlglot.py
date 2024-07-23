# pip install sqlglot==23.11.2,  SQL Parsing Tool
# https://medium.com/@anupkumarray/sql-parsing-using-sqlglot-ad8a3c7fac59
# https://sqlglot.com/sqlglot.html


from sqlglot import parse_one, exp
query = """SELECT col1,col2,col3 FROM db1.table1"""


# Extracting table name(s), db name(s) from any given SQL
for table in parse_one(query).find_all(exp.Table):
    print(f"Table => {table.name} | DB => {table.db}")


# Extract column names from given SQL
for column in parse_one(query).find_all(exp.Column):
  print(f"Column => {column.name}")

# Find CTE to Table relation (can be useful in building lineage / Query DAG)

query = """
            with tab1 as
            (
              select a,b from db1.table1
            )
            ,tab2 as
            (
              select a from tab1
            )
            ,tab3 as
            (
              select
              t1.a
              ,t2.b
              from tab1 t1
              join tab2 t2
              on t1.a = t2.a
            )
            select
            *
            from tab3
        """

dependencies = {}

for cte in parse_one(query).find_all(exp.CTE):
  dependencies[cte.alias_or_name] = []

  cte_query = cte.this.sql()
  for table in parse_one(cte_query).find_all(exp.Table):
    dependencies[cte.alias_or_name].append(table.name)
print(dependencies)

# -- Output: {'tab1': ['table1'], 'tab2': ['tab1'], 'tab3': ['tab1', 'tab2']}


