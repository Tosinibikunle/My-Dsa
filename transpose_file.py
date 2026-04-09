python3 -c '
from collections import defaultdict
data = defaultdict(list)
with open("file.txt") as f:
   for line in f:
       for i, word in enumerate(line.split()):
           data[i].append(word)
for line in data.values():
    print(" ".join(line))
'
