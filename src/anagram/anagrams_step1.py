def is_anagram(w1, w2):
    return sorted(w1) == sorted(w2)


WORD_LIST_FILE_PATH = 'wordlist.txt'

word = 'documenting'

with open(WORD_LIST_FILE_PATH, 'r') as f:
    word_list = set(f.read().split())
    for word1 in word_list:
        for word2 in word_list:
            if is_anagram(word, word1 + word2) and word1 != word2:
                print(f'{word1} {word2}')
