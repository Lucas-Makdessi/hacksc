from google.cloud import language_v1
from google.cloud.language_v1 import enums


def get_keywords(question):
    client = language_v1.LanguageServiceClient()

    type_ = enums.Document.Type.PLAIN_TEXT

    language = "en"

    # question = input("What is your medical question? ")

    document = {"gcs_content_uri": "gs://staging.medicalnlp-1580537107836.appspot.com/questions/questions.txt.{}".format(question), "type": type_, "language": language}

    encoding_type = enums.EncodingType.UTF8

    entity_list = client.analyze_entities(document, encoding_type=encoding_type)
    syntax_list = client.analyze_syntax(document, encoding_type=encoding_type)

    query = []

    for entity in entity_list.entities:
        if format(enums.Entity.Type(entity.type).name).lower() == "number":
            query.append(format(entity.name))
        elif format(enums.Entity.Type(entity.type).name).lower() == "other":
            query.append(format(entity.name))
        elif format(enums.Entity.Type(entity.type).name).lower() == "person":
            for mention in entity.mentions:
                if format(enums.EntityMention.Type(mention.type).name).lower != "proper":
                    query.append(format(entity.name))

    for token in syntax_list.tokens:
        text = token.text

        if format(token.lemma).lower() == "be" or format(token.lemma).lower() == "do" or format(token.lemma).lower() == "have":
            negative = ""

            for other_token in syntax_list.tokens:
                if format(enums.DependencyEdge.Label(other_token.dependency_edge.label).name).lower() == "neg":
                    negative = " " + format(other_token.text.content)

            if negative == "":
                query.append(format(text.content))
            else:
                query.append(format(text.content) + negative)

        elif format(enums.PartOfSpeech.Tag(token.part_of_speech.tag).name).lower() == "adj" or format(enums.PartOfSpeech.Tag(token.part_of_speech.tag).name).lower() == "verb":
            query.append(format(token.text.content))

    return query


def answer_question():
    question = input("What is your medical question? ")

    query = get_keywords(question)

    answer_sets = []

    dic = {"toe": [("my toe is bent", "it is probably broken"), ("my toe is purple", "put some ice on it")],
           "bent": [("my toe is bent", "it is probably broken")],
           "my": [("my toe is bent", "it is probably broken"), ("my toe is purple", "put some ice on it")],
           "is": [("my toe is bent", "it is probably broken"), ("my toe is purple", "put some ice on it")],
           "purple": [("my toe is purple", "put some ice on it")],
           }

    final_answer = set()
    index = 0

    for i in range(len(query)):
        answer_sets.append({""})

    for keyword in query:
        answer_sets[index].clear()
        if keyword in dic:
            for answer in dic[keyword]:
                (answer_sets[index]).add(answer[1])
                final_answer.add(answer[1])

        index += 1

    bad_keys = []

    for index in range(len(answer_sets)):

        if len(final_answer & answer_sets[index]) == 0:
                bad_keys.append(query[index])
        else:
            final_answer = final_answer & answer_sets[index]

    print("These keywords were unhelpful: ", end="")
    for bad in bad_keys:
        print(bad, end=" ")
    print()

    if len(final_answer) == 0:
        print("I could not find any information on this")
    else:
        for item in final_answer:
            print("The doctor says: ", item)

textthing = "bb"
result = get_keywords(textthing)
with open("question{}Key.txt".format(textthing), 'w') as f:
    f.write(result)

