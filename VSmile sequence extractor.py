#A super simple script that aims to extract all of the audio-related assets from V.Smile ROMs
import struct
import tkinter as tk #Used to kill the extra tkinter window
import os
from tkinter import filedialog
import random
root = tk.Tk()#Create a root window
root.withdraw()#Hide the root window
file = filedialog.askopenfilename()
root.destroy()#Destroy the root window
def offsetScan(file, instring): #Scans for a byte string and returns the offset of what it hits
    hits = 0
    with open(file, "rb") as f:
        
        FINDS = [instring,
                 ]
        CHECK = False
        for FIND in FINDS:
            hits2 = 0
            i = 0
            CHECK = False
            complete = 0
            for B in range(os.path.getsize(file)):
                A = f.read(1)
                try:
                    if A[0] == FIND[i]:
                        i+=1
                        CHECK = True
                except:
                    i = 0
                    try:
                        if A[0] == FIND[i]:
                            i+=1
                            CHECK = True
                    except:
                        print("End of file reached.")
                        return 0
                try:
                    if A[0] != FIND[i] and CHECK == False:
                        i = 0
                except:
                    i = 0
                CHECK = False
                if i == len(FIND)-1:
                    f.seek(-3,1)
                    offset = f.tell()
                    return offset
                    
                    hits2+=1
                    
def stringScan(file, instring, amount): #Scans for a byte string and returns the offset of what it hits
    hits = 0
    with open(file, "rb") as f:
        
        FINDS = [instring,
                 ]
        CHECK = False
        for FIND in FINDS:
            hits2 = 0
            i = 0
            CHECK = False
            complete = 0
            for B in range(os.path.getsize(file)):
                A = f.read(1)
                try:
                    if A[0] == FIND[i]:
                        i+=1
                        CHECK = True
                except:
                    i = 0
                    try:
                        if A[0] == FIND[i]:
                            i+=1
                            CHECK = True
                    except:
                        print("End of file reached.")
                        return 0
                try:
                    if A[0] != FIND[i] and CHECK == False:
                        i = 0
                except:
                    i = 0
                CHECK = False
                if i == len(FIND)-1:
                    f.seek(-amount,1)
                    offset = f.tell()
                    if hits2 >= 1: #Done this way to avoid really common values in place of the offset
                        return offset
                    
                    hits2+=1
                    
def offsetConvert(offset): #Converts the true offset to a ROM offset
    newOffset = struct.pack("<I", int(offset/2))
    return newOffset

def getSoundTableLength(file, offset): #Reads the entire table until it hits a decreased value
    lastTable = 0
    newTable = 0
    index = 0
    with open(file, "rb") as f:
        f.seek(offset)
        while lastTable <= newTable:
            newTable = struct.unpack("<I", f.read(4))[0]
            if newTable > lastTable:
                lastTable = newTable
            if newTable < lastTable:
                f.seek(-4,1)
                songListOffset = struct.unpack("<I", f.read(4))[0]
                voiceListOffset = struct.unpack("<I", f.read(4))[0]
                voiceListOffset2 = struct.unpack("<I", f.read(4))[0]
                return index, songListOffset, voiceListOffset
            index+=1

def extractSounds(file, offset, count):
    "" #To be implemented

def extractSequences(file, offset, count): #Extract sequences to output/(game name)/sequences/
    NAME = os.path.basename(file).split(".")[0]
    output = os.getcwd()+"/output/"+NAME+"/sequences/"
    if os.path.exists(output) == False:
        os.makedirs(output)
    seqstring = "Track "
    with open(file, "rb") as f:
        f.seek(offset)
        pointers = []
        for i in range(count):
            pointer = struct.unpack("<I", f.read(4))[0]*2
            pointers.append(pointer)
        i = 0
        ID = 0
        for pointer in pointers:
            i+=1
            f.seek(pointer)
            try:
                song = f.read(pointers[i]-pointer)
            except: #End of song list has been hit. Stop the loop.
                break
            with open(output+seqstring+str(ID)+".bin", "w+b") as o:
                o.write(song)
            ID+=1

#Start of the actual script stuff
toneMaker = stringScan(file, b"SP_T", 3) #SP_ToneMaker
soundClip = stringScan(file, b"SunplusTe", 8) #SunplusTech/Sunplus Tech
print(hex(toneMaker), hex(soundClip))
toneMaker_Table = offsetScan(file, offsetConvert(toneMaker))-4 #This is as far as we'll go with the ToneMaker stuff for now
soundClip_Table = offsetScan(file, offsetConvert(soundClip))-4
print(hex(toneMaker_Table))
print(hex(soundClip_Table))
sounds = getSoundTableLength(file, soundClip_Table)
print(sounds[0], hex(sounds[1]*2), hex(sounds[2]*2))
soundTableCount = sounds[0]
songTableOffset = sounds[1]*2
songTableCount = int((sounds[2]*2-sounds[1]*2)/4)+1
print(songTableCount)
extractSequences(file, songTableOffset, songTableCount)
