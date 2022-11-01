import re

s = str(input())
stopword = str(input())


def removing_stopwords(with_stopwords: str, stopword: str):
    indexes_start_stop = []
    with_stopwords += " "
    without_stopwords = ""
    final = ""

    indexes = [m.start() for m in re.finditer(stopword, with_stopwords)]
    for elem in indexes:  # finding all the occurrences
        start = str(elem)
        end = str(int(elem) + len(stopword))
        result = start + ' ' + end
        if with_stopwords[elem - 1:elem + len(stopword) + 1] == " " + stopword + " ":       # finding only separate
            # stop-words
            without_stopwords += without_stopwords[elem:len(stopword)]
            indexes_start_stop.append(result)

    without_stopwords = with_stopwords.replace(" " + stopword + " ", " ") # removing the stop-word from the string
    without_stopwords = without_stopwords[:-1]

    for index in indexes_start_stop:
        final += index + '\n'

    final += without_stopwords

    return final


print(removing_stopwords(s, stopword))

# output: 20 24
        # 35 39
        # here is my stopword it please
