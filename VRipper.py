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
    FINDS = ["Sunplus".encode('utf-8'),
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
                f.seek(-6,1)
                header = f.read(0x10)
                print(header.decode("UTF-8"))
                if header[7] == 0x20:
                    mode = "instruments/"
                    ext = ".ST2I" #Unsigned 8-Bit PCM
                    #Automatically place the TXTH file in the folder to make ripping more automated
                    if os.path.exists(out+mode) == False:
                        os.makedirs(out+mode)
                    if os.path.exists(out+mode+".ST2I.txth") == False:
                        with open(out+mode+".ST2I.txth", "w+") as t:
                            t.write("""codec = PCM8_U                
sample_rate = @0x10$4
channels = 1
start_offset = 0x20
num_samples = @0x14""")
                if header[7] == 0x54:
                    mode = "voices/"
                    ext = ".ST2V" #IMA encoded audio
                    if os.path.exists(out+mode) == False:
                        os.makedirs(out+mode)
                    #Automatically place the TXTH file in the folder to make ripping more automated
                    if os.path.exists(out+mode+".ST2V.txth") == False:
                        with open(out+mode+".ST2V.txth", "w+") as t:
                            t.write("""codec = IMA                 
sample_rate = @0x10$4
channels = 1
start_offset = 0x28
num_samples = @0x14*2""")
                if complete == 0:
                    #Read the data first to make it writable into the output file
                    R = f.read(4)
                    S = f.read(4)
                    rate = struct.unpack("<I", R)[0]
                    size = struct.unpack("<I", S)[0]
                    #Unknown variables
                    U1 = f.read(4)
                    U2 = f.read(4)
                    U3 = f.read(4)
                    U4 = f.read(4)
                    DATA = f.read(size-2)
                    with open(out+mode+str(hits)+ext, "w+b") as o: #Open the output file
                        output = b''
                        output = output+header+R+S+U1+U2+U3+U4+DATA
                        o.write(output)
                    hits += 1



