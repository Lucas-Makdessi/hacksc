import csv
import ast
import marshal
import spacy

medical_map = {"": [("", ""), ("", "")]}
medical_map.clear()

spacy.prefer_gpu()
nlp = spacy.load("en_core_web_sm")

f = open("data_set.json", "wb")

answer_dict = dict()

with open("data.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)

    count = 0

    for row in csvReader:
        if count % 500 == 0 and count != 0:
            marshal.dump(medical_map, f)
            medical_map.clear()
            print(count)

        if count != 0:

            question = row[3]

            doc = nlp(question)

            keywords = []
            keywords.append(row[2])

            for token in doc:
                keywords.append(token.lemma_)

            answer_list = ast.literal_eval(row[1])

            for dic in answer_list:
                answer = "{} says {}".format(dic["doctor_name"], dic["answer"])

                for keyword in keywords:
                    if keyword in medical_map:
                        medical_map[keyword].append((question, answer))
                    else:
                        qa = [(question, answer)]
                        medical_map.update({keyword: qa})
        count += 1

f.close()

