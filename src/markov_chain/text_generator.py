from collections import defaultdict, Counter

"""premeire partie du programme
"""

def tokenize( text):
    """tokenisation du texte"""
    return [ token.lower() for token in text.split() ]


def make_bigrams( text):
    """ creation des bigrams à partir de text"""
    
    tokens = tokenize(text)
    
    return [(t1, t2) for t1, t2 in zip(tokens, tokens[1:])]
        

def calcul_stats( text):
    """
    calcule les statistiques du modèle de Markov à partir du texte donné.
    """
    
    # Créer des bigrammes à partir du texte
    bigrams = make_bigrams(text)
    
    # Compter les bigrammes
    bigram_counts = Counter(bigrams)
    
    stats = {}

    for (first_word, second_word), count in bigram_counts.items():
        if first_word not in stats:
            stats[first_word] = defaultdict(int)
        stats[first_word][second_word] += count

    # normaliser les probabilités
    for first_word, second_word_counts in stats.items():
        total_count = sum(second_word_counts.values())
        for second_word in second_word_counts:
            second_word_counts[second_word] /= total_count
            
    return stats

def main():
    test_text = "les hommes Libres peuvent rester libres ou bien vendre leur liberté"
    
    print(calcul_stats(test_text))


if __name__ == "__main__":
    main()