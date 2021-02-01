import random

res = set(sorted(random.sample(range(10),5)))
for element in res:
    res.remove(element)
print(res)
