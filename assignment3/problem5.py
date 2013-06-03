import MapReduce
import sys

"""
Implement a friend count as a MapReduce query in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: user
    # value: friend
    key = record[0]
    value = record[1]
    mr.emit_intermediate(value[:-10],key)
      

def reducer(key, list_of_values):
    # key: word
    # value: list of document id
    mr.emit(key)
  

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
