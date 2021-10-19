def play():
    print("************************")
    print("* BEM-VINDE AO GALLOWS *")
    print("*  NÃO SEJA ENFORCADO  *")
    print("************************")

    word = "arroz"
    guesses = []
    letters = ['_', '_', '_', '_', '_']
    user_word = "".join(letters)

    hanged = False
    hit = False
    tries = len(letters) + 3

    print("Você tem {} tentativas".format(tries))
    print("Boa sorte!\n")      
    
    while(not hanged and not hit):

        print(user_word)

        guess = input("chute uma letra:".strip())
        print("\n")

        if (guess in guesses):
            print("Você já chutou essa letra! Tente outra")
            tries -= 1
            print('Você tem {} tentativas\n'. format(tries))
        elif (guess == ""):
            print("Chute vazio :P escreva uma letra na próxima")
            tries -= 1
            print('Você tem {} tentativas\n'. format(tries))
        else:
            guesses.append(guess)

            index = 0

            for letter in word:
                if (letter.lower() == guess.lower()):
                    letters[index] = guess
                    user_word = "".join(letters)    

                index += 1
            
            tries -= 1
            print('Você tem {} tentativas\n'. format(tries))

        hanged = tries == 0
        hit = word == user_word

    if (hanged == True):
        print("VOCÊ FOI ENFORCADO X_X")
        print("MAIS SORTE NA PRÓXIMA VEZ")

    if (hit == True):
        print("CONSEGUIU SALVAR SEU PESCOÇO, MAS FOI PURA SORTE")
        print("TE ESPERO DE NOVO")

if(__name__ == "__main__"):
    play()