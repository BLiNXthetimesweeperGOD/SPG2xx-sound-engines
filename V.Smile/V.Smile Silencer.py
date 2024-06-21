#A script that disables all voice clips in a V.Smile ROM by setting values in their headers to really low numbers
import struct
import tkinter as tk #Used to kill the extra tkinter window
import os
from tkinter import filedialog
import random
root = tk.Tk()#Create a root window
root.withdraw()#Hide the root window
dats = filedialog.askopenfilenames()
root.destroy()#Destroy the root window
for dat in dats:
    NAME = os.path.basename(dat).split(".")[0]
    out = os.getcwd()+"/output/"+NAME+"/"
    try:
        os.makedirs(out)
    except:
        ""
    hits = 0
    f = open(dat,"r+b")
    print(dat)
    FINDS = ["SunplusT".encode('utf-8'),
             ]
    CHECK = False
    for FIND in FINDS:
        i = 0
        CHECK = False
        complete = 0
        for B in range(os.path.getsize(dat)):
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
                    quit()
            try:
                if A[0] != FIND[i] and CHECK == False:
                    i = 0
            except:
                i = 0
            CHECK = False
            if i == len(FIND)-1:
                f.seek(-7,1)
                header = f.read(0x10)
                print(header.decode("UTF-8"))
                if header[7] == 0x20:
                    mode = "instruments/"
                    ext = ".ST2I" #Unsigned 8-Bit PCM
                if header[7] == 0x54:
                    mode = "voices/"
                    ext = ".ST2V" #IMA encoded audio
                if complete == 0:
                    #Read the data first to make it writable into the output file
                    #R = f.read(4)
                    if mode == "voices/":
                        f.write(b'\x01\x10\x00\x00')
                        f.write(b'\x01\x00\x00\x00')
                        f.write(b'\x01\x00\x00\x00')
                        f.write(b'\x01\x00\x00\x00')
                        f.write(b'\x01\x00\x00\x00')
                        f.write(b'\x55\x00\x00\x00')
                        f.write(b'\xFF\xFF\x7F\x7F')
                    else:
                        f.read(4*7)
                    #rate = struct.unpack("<I", R)[0]

