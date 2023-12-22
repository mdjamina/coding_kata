import timeit


def is_anagram(w1, w2):
    return sorted(w1) == sorted(w2)


def find_anagrams(word, words_list):
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            w1 = words_list[i]
            w2 = words_list[j]
            if is_anagram(word, w1 + w2):
                print(f'{w1} {w2}')


WORD_LIST_FILE_PATH = 'wordlist.10000.txt'

word = 'documenting'

with open(WORD_LIST_FILE_PATH, 'r') as f:
    word_list = f.read().split()
    print(f'pool: {len(word_list)}')
    find_anagrams(word, word_list)
    #time = timeit.timeit('find_anagrams(word, word_list)', number=1, globals=globals())
    #print(f'time: {time}')
