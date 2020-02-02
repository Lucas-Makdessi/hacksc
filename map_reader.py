import marshal

from test import get_keywords
import functools

file = open("data_set10.json", 'rb')
dic = marshal.load(file)

def rankQuestions(set, query):
    return set

for i in range(0,200):
    dic2 = marshal.load(file)
    for key in dic2:
        if key in dic:
            dic[key] += dic2[key]
        else:
            dic[key] = dic2[key]


file.close()

file=open("data_set.json", 'rb')

for i in range(2030):
    print(i)
    dic2 = marshal.load(file)
    for key in dic2:
        if key in dic:
            dic[key] += dic2[key]
        else:
            dic[key] = dic2[key]

file.close()

print(len(dic))

def getSetIntsersection(question):
    # for key, value in dic.items() :
    #     print (key)
    query = get_keywords(question)
    print(query)
    if len(query) == 1:
        if query[0] in dic:
            return rankQuestions(dic[query[0]], query)
        else:
            return("no useful queries were found")
    elif len(query) == 0:
        return("no queries were found")
    else:
        finalSet = {}
        prevSet = {}
        setList = []
        for val in query:
            if val in dic:
                setList.append(set(dic[val]))
        if len(setList) == 0:
            return("no matching records were found")
        elif len(setList) == 1:
            return rankQuestions(setList[0], query)
        else:
            prevSet = setList[0]
            for i in range(1,len(setList)):
                finalSet = set.intersection(prevSet, setList[i])
                if (len(finalSet)) == 0:
                    return rankQuestions(prevSet, query)
                prevSet = finalSet
            return rankQuestions(finalSet, query)


if __name__ == "__main__":
    print(getSetIntsersection(input("q: ")))
=======

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







