import random
import time


words = []
counter = 0
answ = "y"
word = 0

nome = "WORDLIST"
print(25*"=-")
print(nome.center(50, " "))
print(25*"=-")


while answ == "y":
    answ = str.lower(input("Você quer gerar uma WordList? (Y/N): "))
    if answ != "y":
        print("Você optou por não criar uma WordList...")
        time.sleep(2)
        print("Encerrando script...")
        time.sleep(2)
        print("SCRIPT ENCERRADO COM SUCESSO!")
        p = "\n"
        for j in range(2):
            if j < 2:
                print(p)
        break
    print("Para parar entrada de palavras, digite 5")
    while word != "5":
        counter += 1
        word = input("Digite uma palavra: ")
        if word == "5":
            print("Inserção de palavras finalizado")
            break
        else:
            words.append(word)
    senhas = int(input("Quantas palavras personalizadas você quer gerar? "))
    dig = int(input("Quantos caracteres as palavras devem conter? "))
    wordlist = []
    list1 = []
    list2 = []
    list1 = words
    list2 = words
    words.sort
    list1.sort(reverse=True)
    list2.reverse
    for i in range(senhas):
        word = random.choice(words)+random.choice(list1)
        while len(word) < dig:
            word += random.choice(list2)
        wordlist.append(word)
    file = open("wordlist.txt", "w")
    for y in wordlist:
        file.write(y)
        file.write("\n")
        file.close
