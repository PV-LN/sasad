import nltk


def extract_entity_names(query):
    """
    Returns extracted entities
    :param t: nltk tree
    :return: entity list
    """
    entity_names = []

    words = nltk.word_tokenize(query.lower())
    tags = nltk.pos_tag(words)
    tags = tags
    # print(tags)
    for tag in tags:
        if tag[1] in ["JJ", "NN", "NNS", "NNP"]:
            entity_names.append(tag[0])
    print(entity_names)
    return entity_names;
