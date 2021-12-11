key = "Realize that excellent marks qualify everybody for jumps in wages"
key = key.split(" ")
encodedString = input()
encodedString = encodedString.split("@")
decodedWords = []
for wordEnc in encodedString:
    word = []
    wordEnc = wordEnc.split(",")
    for charEnc in wordEnc:
        charEnc = charEnc.split("-")
        wordInd = int(charEnc[0])-1
        charInd = int(charEnc[1])-1
        word.append(key[wordInd][charInd])
    word = "".join(word)
    decodedWords.append(word)
decodedWords = " ".join(decodedWords)
print(decodedWords)