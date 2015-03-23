    longword="a"
    for word in words_set:
        if len(longword) < len(word):
            longword = word
    for word in words_set:
        if longword != word:
            if word.endswith(word):
                W = True
                break
            else:
                W = False
        else:
            W = False

    return W
