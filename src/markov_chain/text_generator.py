

"""premeire partie du programme
"""

def tokenize( text):
    """tokenisation du texte"""
    return [ token.lower() for token in text.split() ]



def main():
    test_text = "les hommes Libres peuvent rester libres ou bien vendre leur liberté"
    
    print(tokenize(test_text))


if __name__ == "__main__":
    main()