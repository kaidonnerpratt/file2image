

#make room
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

#imports
import os
import pathlib
import math
from PIL import Image
import numpy as np
#functions
def binaryToPxlData(binary):

    print(len(binary))
    print("before: ", binary)
    if not (int(len(binary))/8) % 3 == 0:
        binary ='00000000'+binary
        print(math.floor(int(len(binary))/3)==int(len(binary)), len(binary)/8)


    print("after: ", binary)

    byteAmount = int(int(len(binary))/8/3)

    print(int(len(binary))/8/3)

    arraySize = closestDivisors(byteAmount)

    pxlArrayData=[]

    tempbin=[]
    for x in range(0,len(binary),8):
        tempbin.append(binary[x:x+8])
    binary=tempbin

    print(arraySize)

    for i in range(arraySize[0]):

        pxlRow=[]

        for o in range(arraySize[1]):

            pxl=[]

            for p in range(3):
                index = (o*3)+(i*arraySize[1]*3)+p
                print('(',i,',',o,',',p,')',' ',index," = ",int(binary[index],2))
                pxl.append(int(binary[index],2))

            pxlRow.append(tuple(pxl))        

        
        pxlArrayData.append(pxlRow)


    print(pxlArrayData)
    return(pxlArrayData)
    

def closestDivisors(n):
    a = round(math.sqrt(n))
    while n%a > 0: a -= 1
    return a,n//a

def pxlDataToImage(pxlArrayData, name):

    pxlArrayData = np.array(pxlArrayData, dtype=np.uint8)

    print(list(pxlArrayData.flatten()))

    image = Image.fromarray(pxlArrayData)
    image.save('output/'+name+'.png')


#actual code
path = str(pathlib.Path().resolve()) +'/input' #get path

print('path: ', path)

filesInPath = os.listdir(path) #get files in path

print('\nfiles in path : ', filesInPath)

print('\n')

for i in filesInPath: #loop over eavry file in path

    file = open('input/'+i,'rb') #read the file as binary
    f=file.read().hex()
    file.close()
    print(f)

    
    f = "".join(f"{ord(x):08b}" for x in f) #turn the file into real binary(1's and 0's)

    
    pxlDataToImage(binaryToPxlData(f),i) #turn the binary into pixle data, turn the pixle data into and image.
    print('\n') #make more room




#make even more room
print('\n')