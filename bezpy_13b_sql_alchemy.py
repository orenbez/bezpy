from datetime import datetime
import itertools
from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import PrimaryKeyConstraint, UniqueConstraint

from sqlalchemy.exc import IntegrityError, StatementError
from sqlalchemy.sql.sqltypes import Float, Integer, TIMESTAMP, Boolean, String, UnicodeText
# from sqlalchemy import Float, Integer, TIMESTAMP, Boolean, String, UnicodeText  < - - - this would be same as above

# Note: PrimaryKeyConstraint = UniqueConstraint with no NULLs allowed

# Create a SQLAlchemy engine
engine = create_engine('sqlite:///example.db')

# Create a SQLAlchemy session
Session = sessionmaker(bind=engine)
session = Session()

# Define a SQLAlchemy model
Base = declarative_base()


class Example1(Base):
    __tablename__ = 'EXAMPLE_1_TBL'
    __table_args__ = (UniqueConstraint('str_val', 'ts_val', name='STR_TS_UNIQ'),)  # sets Uniqueness constraint on combinded pair
    id = Column(Integer, primary_key=True, nullable=False, comment='id column')
    str_val = Column(String(50), nullable=False, comment='str_val max length is 500')
    ts_val = Column(TIMESTAMP(), nullable=False, default=datetime.utcnow())
    unicode_val = Column(UnicodeText(), nullable=True, comment='Configuration Details')
    float_val = Column(Float)

class Example2(Base):
    __tablename__ = 'EXAMPLE_2_TBL'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='this auto increments')
    fk_val = Column(String(50), ForeignKey("EXAMPLE_1_TBL.str_val"), nullable=False)
    bool_val = Column(Boolean, nullable=False, default=False, comment='Flag to indicate user_input')

# Create the example table
Base.metadata.create_all(engine)

example_1_rows_deleted = session.query(Example1).delete()   # purge all rows
example_2_rows_deleted = session.query(Example2).delete()   # purge all rows
session.commit()  # this

# Insert some data into the example1 table, will not fail at this stage for integrity error, only on commit. but will fail for erroneous  keywords i.e. column names
session.add(Example1(id=1, str_val='one', ts_val=datetime(1974, 2, 20, 12, 0, 0), unicode_val='😀😃😄', float_val=3.14))
session.add(Example1(id=1, str_val='one', ts_val=datetime(1974, 2, 20, 12, 0, 0), unicode_val='😀😃😄', float_val=3.14))

try:
    session.commit()
except IntegrityError as e:
    print(f'IntegrityError Occured {e}, rolling back')
    session.rollback()

session.add(Example1(id=1, str_val='one', ts_val=datetime(1974, 2, 20, 12, 0, 0), unicode_val='😀😃😄', float_val=3.14))
session.add(Example1(id=2, str_val='two', float_val=10.28))
session.add(Example1(id=3, str_val='three', float_val=10.28))
session.commit()

results = session.query(Example1).all()             # returns list of instances of class Example1
results = session.query(Example1).limit(2).all()    # returns only first two instances e.g. [<__main__.Example1 object at 0x0000023B74654760>, <__main__.Example1 object at 0x0000023B746547C0>]
[(x.id, x.str_val, x.float_val) for x in results]   # [(1, 'one', 3.14), (2, 'two', 10.28)]

result = session.query(Example1.id).all()     # returns list of tuples [(1,), (3,), (2,)]
tuple(itertools.chain.from_iterable(result))  # (1, 3, 2)


# Use a mathematical equation as a filter in a query
query = session.query(Example1).filter(Example1.float_val * 2 > 4)    # type: sqlalchemy.orm.query.Query
x = query.statement.compile()   # Compile query to SQL
print(x)
# SELECT "EXAMPLE_1_TBL".id, "EXAMPLE_1_TBL".str_val, "EXAMPLE_1_TBL".ts_val, "EXAMPLE_1_TBL".unicode_val, "EXAMPLE_1_TBL".float_val
# FROM "EXAMPLE_1_TBL"
# WHERE "EXAMPLE_1_TBL".float_val * :float_val_1 > :param_1
x.bind_names   # {BindParameter('%(2574610877360 float_val)s', 2, type_=Integer()): 'float_val_1', BindParameter('%(2574610875632 param)s', 4, type_=Integer()): 'param_1'}

session.add_all([Example2(fk_val='one'), Example2(fk_val='two', bool_val=True)])
session.commit()
results = session.query(Example2).all()
[(r.id, r.fk_val, r.bool_val) for r in results]   #  [(1, 'one', False), (2, 'two', True)]

session.query(Example2.id, Example2.bool_val).all()  #  returns list of tuples, not instances of Example2 [(1, False), (2, True)]

# results = session.query(Example).filter(Example.value * 2 > 3).all()
# Print the results
# for result in results:
#     print(result.value)
    # Output: 2, 3

    # Study how these work
    # session.query(module.TableClass.table_column1)
    # .func.max(module.TableClass.table_column2)
    # .label(‘label_name’)
    # .groupby(module.TableClass.table_column1)
    # .subquery(‘subquery_name’)
    # .join().filter().and_().status.in_()
    # update(table).where(table.c.col_name == 'xxx').values('')

    # https://stackoverflow.com/questions/34322471/sqlalchemy-engine-connection-and-session-difference
    # https://www.youtube.com/watch?v=T_cgZsmAuM4
    # https://www.youtube.com/watch?v=9X64KuKMyMc
    # https://www.youtube.com/watch?v=9X64KuKMyMc



