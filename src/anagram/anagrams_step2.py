
WORD_LIST_FILE_PATH = 'src/anagram/word_list.txt'

word = 'documenting'


with open(WORD_LIST_FILE_PATH, 'r') as f:
    word_list = list(set(f.read().split()))

for i, word1 in enumerate(word_list):
    for word2 in word_list[i+1:]:
        if set(word) == set(word1 + word2):
            print(f'{word1} {word2}')