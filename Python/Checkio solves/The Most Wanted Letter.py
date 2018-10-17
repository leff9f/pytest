import operator


def checkio(text: str):
    text = sorted([a for a in text.lower() if a.isalpha()])
    alph_dict = {text[0]: text.count(text[0])}
    for i in range(0, len(text)-1):
        if text[i] != text[i+1]:
            alph_dict.update({text[i+1]: text.count(text[i+1])})

    return max(alph_dict.items(), key=operator.itemgetter(1))[0]


checkio('da!!!!')
checkio('a'*10000+'b'*9000)