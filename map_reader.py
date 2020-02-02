import csv
from test import get_keywords
from test import answer_question
import ast
import pickle
import time


medical_map = {"": [""]}
medical_map.clear()

file = open("questions2.txt", "w")

answer_dict = dict()

with open("data.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)

    count = 0

    for row in csvReader:
        if count > 800000:
            file.write("{} ".format(row[3]))

            # keywords = get_keywords(row[3])

            #answer_list = ast.literal_eval(row[1])

            # for dic in answer_list:
            #
            #     answer = "{} says {}".format(dic["doctor_name"], dic["answer"])
            #
            #     for keyword in keywords:
            #         if keyword in medical_map:
            #             medical_map[keyword].append(answer)
            #         else:
            #             answers = [answer]
            #             medical_map.update({keyword: answers})

        count += 1


file.close()

# f = open("data_set.pkl", "wb")
# pickle.dump(medical_map, f)
# f.close()

# answer_question(medical_map)

