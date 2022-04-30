import json


dict1 = {"id": "50356270565167104", "name": "班级优化"}
dict2 = {"id": "50356270565167104", "name": "班级优化"}

for d1,d2 in zip(sorted(dict1),sorted(dict2)):
    if dict1[d1]!=dict2[d2]:
        print(False)
print(True)