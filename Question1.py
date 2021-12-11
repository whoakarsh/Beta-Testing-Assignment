def freqChar(string,char):
    char.lower()
    string.lower()
    count = 0
    for i in range(0,len(string)):
        if string[i] == char:
            count += 1 
    return count

string = input()
char = input()
countChar = freqChar(string,char)
print(countChar)