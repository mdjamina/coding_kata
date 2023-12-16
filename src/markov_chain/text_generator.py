from collections import defaultdict, Counter
import random

"""premeire partie du programme
"""

def tokenize( text):
    """tokenisation du texte"""
    return [ token.lower() for token in text.split() ]


def make_bigrams( text):
    """ creation des bigrams à partir de text"""
    
    tokens = tokenize(text)    
    bigram = [(t1, t2) for t1, t2 in zip(tokens, tokens[1:])]
    
    # ajouter le dernier token avec une chaîne vide si tokens n'est pas vide
    if tokens:
        bigram.append((tokens[-1], ''))
    return bigram
        

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


def affiche_stats( stats):
    """affiche les statistiques du modèle de Markov"""

    for key,values in stats.items():
        print( f'"{key}" est suivi par ', end='')
        print( " et ".join([f'"{k}" à {p*100}%' for k,p in values.items()]))
    print()



"""deuxieme partie du programme
"""

def pick_next_word( distrib):
    """choisit un mot suivant les statistiques

    choisit le mot suivant en fonction du mot donné et des probabilités du modèle.
    """
    
    probabilities = distrib    
    # Si le mot n'est pas dans le modèle, retourner une chaîne vide
    if not probabilities:
        return ''    
    words, probs = zip(*probabilities.items())
    return random.choices(words, weights=probs, k=1)[0]

def generate_text( stats, start_word=None, max_length=5):
    """génère un texte à partir des statistiques """
    
    # Choisir un mot aléatoire si aucun mot n'est donné
    if start_word is None:
        start_word = random.choice(list(stats.keys()))
    
    text = [start_word]
    current_word = start_word
    
    while len(text) < max_length:        
        next_word = pick_next_word(stats[current_word])
        # Si le mot suivant est une chaîne vide, choisir un mot aléatoire
        if next_word == '':
            next_word = random.choice(list(stats.keys()))
        text.append(next_word)
        current_word = next_word
        
    return ' '.join(text)


def main():
    test_text = "les hommes Libres peuvent rester libres ou bien vendre leur liberté"
    
    stats = calcul_stats(test_text)
    
    affiche_stats(stats)
    
    generated_text = generate_text(stats, start_word='hommes', max_length=10)
    
    print("Generated text:",generated_text)
    


if __name__ == "__main__":
    main()