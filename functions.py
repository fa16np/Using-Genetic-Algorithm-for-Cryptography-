import re

#decrypting text using the given key
def decrypt(k,c):

    #Sanitize the ciphr and the key
    cipher = c.lower()
    cipher = re.sub('[^a-z]'," ",cipher)
    cipher = cipher.replace(" ","")

    ke = k.lower()
    ke = re.sub('[^a-z]'," ",ke)
    ke = ke.replace(" ","")

    key = list(ke)
    for i in range(len(ke)):
        key[i] = chr(ord(key[i])-97)

    #run decryption
    plain = ""
    keyptr = 0
    for i in range(len(cipher)):
        keyChar= chr(0)
        if len(key) > 0:
            while ord(key[keyptr]) > 25 or ord(key[keyptr]) < 0:
                keyptr = (keyptr+1)%len(key)
            keyChar = key[keyptr]
            keyptr = (keyptr+1)%len(key)

        plain= plain + chr((((ord(cipher[i])-97+26-ord(keyChar))%26)+97))

    return plain


#encrypting text using the given key
def encrypt(k,p):

    plain = p.lower()
    plain = re.sub('[^a-z]'," ",plain)
    plain = plain.replace(" ","")
    cipher=""

    ke = k.lower();
    ke = re.sub('[^a-z]'," ",ke)
    ke = ke.replace(" ","")

    #Encrypt text
    key = list(ke)
    for i in range(len(key)):
        key[i] = chr(ord(key[i])-97)

    keyPtr = 0
    for i in range(len(plain)):
        keyChar = chr(0)
        if len(key)>0:
            #Ignore any value not in the expected range
            while ord(key[keyPtr])>25 or ord(key[keyPtr]) < 0:
                keyPtr = (keyPtr+1)%len(key)
            keyChar = key[keyPtr]
            keyPtr = (keyPtr+1)%len(key)

        cipher = cipher + chr((((ord(plain[i])-97+ord(keyChar))%26)+97))

    return cipher

#This is a very simple fitness function based on the expected frequency of each letter in english
#There is lots of room for improvement in this function.
def fitness(k,c):
    expectedFrequencies = [float]*26
    expectedFrequencies[0] = 0.085;    #Expected frequency of a
    expectedFrequencies[1] = 0.016;    #Expected frequency of b
    expectedFrequencies[2] = 0.0316;   #Expected frequency of c
    expectedFrequencies[3] = 0.0387;   #Expected frequency of d
    expectedFrequencies[4] = 0.121;    #Expected frequency of e
    expectedFrequencies[5] = 0.0218;   #Expected frequency of f
    expectedFrequencies[6] = 0.0209;   #Expected frequency of g
    expectedFrequencies[7] = 0.0496;   #Expected frequency of h
    expectedFrequencies[8] = 0.0733;   #Expected frequency of i
    expectedFrequencies[9] = 0.0022;   #Expected frequency of j
    expectedFrequencies[10] = 0.0081;  #Expected frequency of k
    expectedFrequencies[11] = 0.0421;  #Expected frequency of l
    expectedFrequencies[12] = 0.0253;  #Expected frequency of m
    expectedFrequencies[13] = 0.0717;  #Expected frequency of n
    expectedFrequencies[14] = 0.0747;  #Expected frequency of o
    expectedFrequencies[15] = 0.0207;  #Expected frequency of p
    expectedFrequencies[16] = 0.001;   #Expected frequency of q
    expectedFrequencies[17] = 0.0633;  #Expected frequency of r
    expectedFrequencies[18] = 0.0673;  #Expected frequency of s
    expectedFrequencies[19] = 0.0894;  #Expected frequency of t
    expectedFrequencies[20] = 0.0268;  #Expected frequency of u
    expectedFrequencies[21] = 0.0106;  #Expected frequency of v
    expectedFrequencies[22] = 0.0183;  #Expected frequency of w
    expectedFrequencies[23] = 0.0019;  #Expected frequency of x
    expectedFrequencies[24] = 0.0172;  #Expected frequency of y
    expectedFrequencies[25] = 0.0011;  #Expected frequency of z


    #sanitize cipher text
    d = c.lower()
    d = re.sub('[^a-z]'," ",d)
    d = d.replace(" ","")

    cipher = list(c)
    for i in range(len(c)):
        cipher[i] = int(ord(d[i])-97)

    ke = k.lower()
    ke = re.sub('[^a-z]'," ",ke)
    ke = ke.replace(" ","")

    key = list(ke)
    for i in range(len(key)):
        key[i] = chr(ord(key[i])-97)


    charCounts = [int]*26

    for i in range(26): charCounts[i]=0

    plain = [int]*len(cipher)

    #decrypt each character
    keyPtr=0
    for i in range(len(cipher)):
        keyChar = chr(0)
        if len(key) > 0:

            #ignore any value not in the range
            while ord(key[keyPtr]) > 25 or ord(key[keyPtr]) < 0:
                keyPtr = (keyPtr+1)%len(key)
            keyChar = key[keyPtr]
            keyPtr = (keyPtr+1)%len(key)

        plain[i] = ((26+cipher[i]-ord(keyChar))%26)

    for x in plain :
        charCounts[x] = charCounts[x]+1

    score = 0
    for i in range(len(charCounts)):
        score = score + abs(((float(charCounts[i])/len(plain))-expectedFrequencies[i]))

    return score

#
# #
# p = "This is some text to decrypt"
# k = "pas-sw-o-rd-"
#
# print(k)
# c = encrypt(k,p)
# fit = fitness(k,c)
# d = decrypt(k,c)
# print(c)
# print(d)
# print(fit)
#

