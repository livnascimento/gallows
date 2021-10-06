def play():
    print("************************")
    print("* BEM-VINDE AO GALLOWS *")
    print("*  NÃO SEJA ENFORCADO  *")
    print("************************")

    word = "arroz"

    hanged = False
    hit = False

    while(not hanged and not hit):      

        guess = input("chute uma letra:".strip())
        
        index = 0

        for letter in word:
            if (letter.lower() == guess.lower()):
                print(letter)

        index += 1
    
if(__name__ == "__main__"):
    play()