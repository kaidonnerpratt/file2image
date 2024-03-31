#make room
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

#imports
import os
import pathlib
import math
from PIL import Image
import numpy as np
import re
import ast
from itertools import chain

#functions
def binToHex(binary):

    hex=''

    print(len(binary)/8)


    for i in range(int(len(binary)/8)):

        byte = ''

        for o in range(8):
            byte = byte + binary[(i*8)+o]

        hex = hex + chr(int(byte,2))
    
    return hex

    


def decToBin(n):
    return bin(n).replace('0b','')

def pxlDataToBinary(pxlArrayData):

    binary=''

    for i in range(len(pxlArrayData)):
        byte=pxlArrayData[i]
        tempBin = str(decToBin(byte))

        while len(tempBin) < 8:

            tempBin = '0'+tempBin

        binary = binary + tempBin

    print(binary)
    #assert binary == '001101110011011100110110001110000011011001100110001101110011011100110010001100000011011000111001001101110011001100110010001100000011011100110100001101100011100000110110001110010011011100110011001100100011000000110110001100010011011001100101001100100011000000110110001110010011011001100100001101100011000100110110001101110011011000110101001100100011000000110110011001010011011001100110001101110011011100110011011001100011001101100110001100110110011000110011011001100011000001100001'
    return binary

def imageToPxlData(im):
    
    width, height = im.size

    pxlArrayData = list(im.getdata())

    pxlArrayData = list(chain.from_iterable(pxlArrayData))

    print(pxlArrayData)
    return pxlArrayData

    


#actual code

path = str(pathlib.Path().resolve()) +'/input' #get path

print('path: ', path)

filesInPath = os.listdir(path) #get files in path

pngFilesInPath = [filesInPath[i] for i in range(len(filesInPath)) if filesInPath[i].endswith('.png') and '.' in filesInPath[i][:filesInPath[i].rindex('.png')] ]


print('\npng files in path : ', pngFilesInPath)

print('\n')

for i in pngFilesInPath: #loop over eavry file in path

    file = Image.open('input/'+i) #read the image file
    im=file
    

    hex = binToHex(pxlDataToBinary(imageToPxlData(im))) #turn it into hex

    print(hex)

    st=bytes.fromhex(hex) #turn the hex into ascii

    print(st)

    #assert(hex == '77686f77206973207468697320616e20696d616765206e6f773f3f3f3f0a')

    

    file.close()
    
    file = open('output/'+i[:-4], 'wb') #create new file to put the data in

    file.write(st)
    
    file.close()

    '''
    f = "".join(f"{ord(x):08b}" for x in f) #turn the file into binary(1's and 0's)


    pxlDataToImage(binaryToPxlData(f),i) #turn the binary into pixle data, turn the pixle data into and image.
    '''
    print('\n') #make more room

    

    