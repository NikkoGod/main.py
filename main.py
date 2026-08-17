
meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "VDD": "abreviação da palavra verdade " ,
            "BISCOITAR": "postar algo apenas para chamar a atenção" 
            }
for i in range(5):
  word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")
if word in meme_dict.keys():
    print (meme_dict[word])
else:
    print ("Nao consta na minha base de dados!")
