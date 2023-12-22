from itertools import combinations


def is_anagram(w1, w2):
    return sorted(w1) == sorted(w2)


def find_anagrams(word, words_list):
    return {(w1, w2) for w1, w2 in combinations(words_list, 2) if is_anagram(word, w1 + w2)}


def test_is_anagram():
    print('test_is_anagram')
    assert is_anagram('abc', 'cba'), 'abc cba should be anagrams'
    assert is_anagram('abc', 'abc'), 'abc abc should be anagrams'
    assert is_anagram('abc', 'bac'), 'abc bac should be anagrams'
    assert is_anagram('abc', 'bca'), 'abc bca should be anagrams'
    assert not is_anagram('abc', 'ab'), 'abc ab should not be anagrams'
    assert not is_anagram('abc', 'abcd'), 'abc abcd should not be anagrams'


def test_find_anagrams():
    print('test_find_anagrams')

    assert len(find_anagrams('abc', ['abc', 'bac', 'cba', 'bca', 'ab', 'abcd', 'ab', 'c', 'ba', 'd',
                                     'a'])) == 2, 'abc should have 2 anagrams'
    assert len(find_anagrams('abcd', ['abc', 'bac', 'cba', 'bca', 'ab', 'abcd', 'ab', 'c', 'ba', 'd',
                                      'a'])) == 4, 'abcd should have 4 anagrams'


if __name__ == '__main__':
    test_is_anagram()
    test_find_anagrams()
