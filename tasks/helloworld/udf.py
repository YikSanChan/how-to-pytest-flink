from pyflink.table import DataTypes
from pyflink.table.udf import udf

@udf(input_types=[DataTypes.INT(), DataTypes.INT()], result_type=DataTypes.BIGINT())
def add(i, j):
    return i + j
