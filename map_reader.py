import marshal

from test import get_keywords
import functools

#file = open("data_set10.json", 'rb')
#dic = marshal.load(file)

dic = {}


def rankQuestions(set, question, query):
    # set is a set of tuples from the final intersection

    tuples = list(set)

    max_words_in_common = 0
    best_question_index = 0

    for i in range(len(tuples)):
        cur_max = 0
        for word in tuples[i]:
            if word in question:
                if word in query[0]:
                    cur_max += query[1][query[0].index(word)]
                else:
                    cur_max += 1

        if cur_max > max_words_in_common:
            max_words_in_common = cur_max
            best_question_index = i

    return tuples[best_question_index][1]


# for i in range(0,200):
#     dic2 = marshal.load(file)
#     for key in dic2:
#         if key in dic:
#             dic[key] += dic2[key]
#         else:
#             dic[key] = dic2[key]
#
#
# file.close()

file = open("data_set.json", 'rb')

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
    query1 = query[0]
    print(query1)
    if len(query1) == 1:
        if query1 in dic:
            return rankQuestions(dic[query1[0]], question, query)
        else:
            return("no useful queries were found")
    elif len(query1) == 0:
        return("no queries were found")
    else:
        finalSet = {}
        prevSet = {}
        setList = []
        for val in query1:
            if val in dic:
                setList.append(set(dic[val]))
        if len(setList) == 0:
            return("no matching records were found")
        elif len(setList) == 1:
            return rankQuestions(setList[0], question, query)
        else:
            prevSet = setList[0]
            for i in range(1,len(setList)):
                finalSet = set.intersection(prevSet, setList[i])
                if (len(finalSet)) == 0:
                    return rankQuestions(prevSet, question, query)
                prevSet = finalSet
            return rankQuestions(finalSet, question, query)


if __name__ == "__main__":
    print(getSetIntsersection(input("q: ")))









