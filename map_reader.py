import marshal

dic = dict()

for i in range(2030):
    dic.update(marshal.load(open("data_set.json", 'rb')))
    print(i)

print(len(dic))

if "penis" in dic:
    print(dic["penis"])







