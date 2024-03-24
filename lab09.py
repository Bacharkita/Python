import sys
import math
import random
import zlib

def optask():
    txt = 'ABC abc'
    b = bytearray(txt,'ASCII')
    print(len(txt))        #7
    print(len(b))          #7
    print(b[0])            #A 65
    print(b[1])            #B 66
    print(b[2])            #C 67
    print(b[3])            #space 32
    print(b[4])            #a 97 
    print(b[5])            #b 98
    print(b[6])            #c 99


    txt2 ='ÅÄÖ'

    # b2 = bytearray(txt2,'utf-8')     #'ascii' codec can't encode characters in position 0-2: ordinal not in range(128)

    try:
        b2 = txt2.encode('LATIN-1')
        print(b2[0])            #Å 197
        print(b2[1])            #Ä 196
        print(b2[2])            #Ö 214
    except:
        print('(!Dec:) ' + str(txt2))

    try:
        b3 = txt2.encode('UTF-8')

        print(b3[0])            #Å 195
        print(b3[1])            #Ä 133
        print(b3[2])            #Ö 195
    except:
        print('(!Dec:) ' + str(txt2))
    print(b3.decode('UTF-8'))



def readSwe(swetextfile):
    byt= []

    swetextfile = open(swetextfile, 'r', encoding='LATIN-1').read()
    byteArr = bytearray(swetextfile, "LATIN-1")

    return byteArr


def task1(byteArr):
    str = []
    print("task1")

    x = byteArr.decode("LATIN-1")
    print(len(x))
    print(len(byteArr))




def makeHisto(byteArr):
    byt ={}
    for i in range(0,256):
        byt[i] = 0

    for i in byteArr:
        byt[i]+=1


    return byt
    

def makeProb(histo):
    histoSum = 0
    for i in histo:
        histoSum += histo[i]
    for i in histo:
        if histo[i] > 0:
            histo[i] =histo[i] / histoSum
    return histo


#def makeProbBit(histo):
#    histoSum = 0
#    for i in histo:
#        histoSum += histo[i]

#    return histoSum*8

def entropi(prob):
    h = 0
    for i in prob:
        if prob[i] == 0:
            continue
        else:
            l=math.log2(1/prob[i])
            h += prob[i] * l
    return h #ca 4,9 



def copy(theCopy):
    random.shuffle(theCopy)    
    return theCopy
    
    

# main

x = readSwe('exempeltext.txt')

optask()
task1(x)
#print(makeHisto(x))
print(makeProb(makeHisto(x)))

print(entropi(makeProb(makeHisto(x))))


copy(x[:])

code1 = zlib.compress(x)
code2 = zlib.compress(copy(x))

print((len(x)*8),'not compressed in bits') #232728 not compressed in bits
print((len(code1)*8),'compressed in bits') #100952 compressed in bits
print((len(code2)*8),'shuffled compressed in bits\n') #148800 shuffled compressed in bits


print(len(x),'not compressed') # 29091 not compressed
print(len(code1),'compressed') # 12619 compressed
print(len(code2),'shuffled compressed \n') # 18600 shuffled compressed

print(((len(code1)*8)/29000),'compressed') #3.4811034482758623 compressed is smallest
print(((len(code2)*8)/29000),'shuffled') # 5.137931034482759 shuffled compressed is biggest 
print(entropi(makeProb(makeHisto(x))),'not compressed\n\n') #ca 4,5 bit/symbol not compressed


t1 = """I hope this lab never ends because it is so incredubly thrilling!"""
t10 = 10*t1
print('len of symbols in t1 is{} and t10 is{}'.format(len(t1),len(t10))) #len of symbols in t1 is 64 and t10 is640


bt1 = bytearray(t1,'LATIN-1')
bt10 = bytearray(t10,'LATIN-1')

zt1= zlib.compress(bt1)
zt10=zlib.compress(bt10)

print('t1  not compressed bytes:{} , bytes:{}, {}: bits  '.format(len(bt1),len(zt1),len(zt1)*8)) # symbols 64 , bytes65, 520 bits
print('t10 not compressed bytes:{}, bytes:{}, {} :bits  '.format(len(bt10),len(zt10),len(zt10)*8)) # symbols 640, bytes75, 600 bits

et1= (len(zt1)*8)/ len(bt1)
et10= (len(zt10)*8) / len(bt10)
print(' t1 {} bites/symbol \nt10 {} bites/symbol'.format(et1,et10)) # t1 8.125 bites/symbol t2 0.9375 bites/symbol