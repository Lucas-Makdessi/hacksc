import marshal

dic = dict()

for i in range(2031):
    dic_temp = marshal.load(open("data_set.json", 'rb'))

    for key in dic_temp:
        if key in dic:
            dic[key] += dic_temp[key]
        else:
            dic[key] = dic_temp[key]

    print(i)

print(len(dic))

if "penis" in dic:
    print(dic["penis"])







