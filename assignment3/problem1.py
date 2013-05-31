import MapReduce
import sys

"""
Create an inverted index in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      print w
      mr.emit_intermediate(w,key)

def reducer(key, list_of_values):
    # key: word
    # value: list of document id
    list_of_doc_id = []
    for v in list_of_values:
      if not v in list_of_doc_id:
		    list_of_doc_id.append(v)	
    mr.emit((key, list_of_doc_id))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
