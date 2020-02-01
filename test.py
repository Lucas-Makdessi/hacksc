from google.cloud import language_v1
from google.cloud.language_v1 import enums


def analyze_entities(text_content):
    client = language_v1.LanguageServiceClient()

    type_ = enums.Document.Type.PLAIN_TEXT

    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_entities(document, encoding_type=encoding_type)

    for entity in response.entities:
        print(u"Representative name for the entity: {}".format(entity.name))

        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))

        # Get the salience score associated with the entity in the [0, 1.0] range
        # print(u"Salience score: {}".format(entity.salience))

        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        # """
        for metadata_name, metadata_value in entity.metadata.items():
            print(u"{}: {}".format(metadata_name, metadata_value))
        # """

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.

        # """
        for mention in entity.mentions:
            print(u"Mention text: {}".format(mention.text.content))
            # Get the mention type, e.g. PROPER for proper noun
            print(
                u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name)
            )
        # """

    return response

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    # print(u"Language of the text: {}".format(response.language))


def analyze_syntax(text_content):

    client = language_v1.LanguageServiceClient()
    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_syntax(document, encoding_type=encoding_type)

    # return response

    # Loop through tokens returned from the API
    for token in response.tokens:
        # Get the text content of this token. Usually a word or punctuation.
        text = token.text
        print(u"Token text: {}".format(text.content))
        # print(u"Location of this token in overall document: {}".format(text.begin_offset))
        part_of_speech = token.part_of_speech
        print(u"Lemma: {}".format(token.lemma))

        print(
            u"Part of Speech tag: {}".format(
                enums.PartOfSpeech.Tag(part_of_speech.tag).name
            )
        )

        # Get the dependency tree parse information for this token.
        # For more information on dependency labels:
        # http://www.aclweb.org/anthology/P13-2017

        # """
        dependency_edge = token.dependency_edge
        print(u"Head token index: {}".format(dependency_edge.head_token_index))
        print(
            u"Label: {}".format(enums.DependencyEdge.Label(dependency_edge.label).name)
        )
        # """
    return response

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.

    # print(u"Language of the text: {}".format(response.language))



question = input("What is your medical question? ")

syntax_list = analyze_syntax(question)
entity_list = analyze_entities(question)

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
    x = 1


for item in query:
    print(item)

