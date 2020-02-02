import marshal

from test import get_keywords
import functools

#file = open("data_set10.json", 'rb')
#dic = marshal.load(file)

dic = {}


def rankQuestions(set, question, query):
    # set is a set of tuples from the final intersection

    min_extra_words = 1000000
    best_question_index = 0

    secondbest = 0
    secondbest_index = 0
    """
    for i in range(len(tuples)):
        cur_max = 0
        for word in tuples[i]:
            if word in question:
                if word in query[0]:
                    cur_max += query[1][query[0].index(word)]
                    #cur_max += 3
                else:
                    cur_max += 1
        if cur_max == max_words_in_common:
            secondbest = cur_max
            secondbest_index = i
        elif cur_max > max_words_in_common:
            max_words_in_common = cur_max
            best_question_index = i

    if tuples[best_question_index] != tuples[secondbest_index]:
        return (tuples[best_question_index],tuples[secondbest_index])
    else:
        return tuples[best_question_index][1]
    """
    questions = list(set)

    for tup in questions:
        cur_extra_words = 0
        for strn in tup[0]:
            if strn not in query[0]:
                cur_extra_words += 1
        if secondbest == min_extra_words:
            secondbest = min_extra_words
            secondbest_index = i
        if cur_extra_words < min_extra_words:
            min_extra_words = cur_extra_words
            best_question_index = questions.index(tup)

    if questions[best_question_index] != questions[secondbest_index]:
        return (questions[best_question_index], questions[secondbest_index])
    else:
        return questions[best_question_index][1]
                

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









