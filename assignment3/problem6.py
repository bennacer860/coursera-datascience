import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

MAX = 5

def mapper(record):
    # key: document identifier
    # value: document contents
    if record[0] == 'a':
        key = record[1]
        for i in range(MAX):
            mr.emit_intermediate((key,i), record)
    else:
        key = record[2]
        for i in range(MAX):
            mr.emit_intermediate((i,key), record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    a = {}
    b = {}
    for record in list_of_values:
        if record[0] == 'a':
            a[record[2]] = record[3]
        else:
            b[record[1]] = record[3]
    sum = 0
    for i in a:
        if i in b:
            sum += a[i]*b[i]
    mr.emit((key[0], key[1], sum))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)