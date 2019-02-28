#!/usr/bin/env python3

import sys
from collections import OrderedDict

if len(sys.argv) == 2:
    fd = open(sys.argv[1], "r")
else:
    fd  = open("Input", "r")

FileLines = fd.read().split('\n')
print(FileLines)
Dic = OrderedDict()

def AddToDict(Tag):
    print("Tag: "+str(Tag))
    if Tag in list(Dic.keys()):
        print("Tag already exists, ID: "+str(Dic[Tag]))
        return Dic[Tag]
    else:
        if len(list(Dic.keys())):
            print("Is not empty, adding as "+str(Dic[list(Dic.keys())[-1]]+1))
            Dic[Tag] = Dic[list(Dic.keys())[-1]]+1
            return Dic[Tag]
        else:
            print("IS empty, adding as 0")
            Dic[Tag] = 0
            return 0

FotoAmmount = int(FileLines[0])

AllSlides = list(map(lambda x: x.split(" "), FileLines[1:(len(FileLines)-1)]))

#print(AllSlides)

ParsedSlides = list()

ParsedTags = list()

for Slide in AllSlides:
    #print([Slide[x+1] for x in range(int(Slide[1])-1)])
    templ = list()
    # H == 0  V == 1
    templ.append(1 if Slide[0] == "V" else 0)
    templ.append(int(Slide[1]))
    ParsedSlides.append(templ+[AddToDict(Slide[x+2]) for x in range(int(Slide[1]))])
#print(Dic)
print(ParsedSlides)
