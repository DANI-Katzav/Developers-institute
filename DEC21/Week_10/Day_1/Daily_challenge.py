import translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

for el in french_words:
    print(f"{el}, {translator.translator_dict[el]}")