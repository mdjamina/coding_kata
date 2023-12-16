

"""premeire partie du programme
"""

def tokenize( text):
    """tokenisation du texte"""
    return [ token.lower() for token in text.split() ]


def make_bigrams( text):
    """ creation des bigrams à partir de text"""
    
    tokens = tokenize(text)
    
    return [(t1, t2) for t1, t2 in zip(tokens, tokens[1:])]
        


def main():
    test_text = "les hommes Libres peuvent rester libres ou bien vendre leur liberté"
    
    print(make_bigrams(test_text))


if __name__ == "__main__":
    main()