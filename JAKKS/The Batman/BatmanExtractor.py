import struct
import tkinter as tk
from tkinter import filedialog
import os
seqStart = 0x1D85D8 #The start of the sequence table
#Set up the tkinter file dialog
root = tk.Tk()
root.withdraw()
files = filedialog.askopenfilenames()
root.destroy()
currentDir = os.getcwd()
for file in files:
    romSize = os.path.getsize(file)
    with open(file, 'rb') as rom:
        rom.seek(seqStart)
        for song in range(10):
            songOffset = struct.unpack("<I", rom.read(4))[0]*2
            print(hex(songOffset))
            lastSongOffset = rom.tell()
            rom.seek(songOffset)
            ch_count = struct.unpack("<H", rom.read(2))[0]
            unknown_data = rom.read(2)
            try:
                for sequence in range(ch_count):
                    dataCheck = 0
                    offset = struct.unpack("<I", rom.read(4))[0]*2
                    last = rom.tell()
                    rom.seek(offset)
                    #print(hex(offset))
                    with open(f"{currentDir}/Batman_{song}_{sequence}.bin", "w+b") as output:
                        while dataCheck != 0xF000:
                            data = rom.read(2)
                            output.write(data)
                            dataCheck = struct.unpack("<H", data)[0]
                    if sequence != 3:
                        rom.seek(last)
                    else:
                        rom.seek(4, 1)
                rom.seek(lastSongOffset)
            except:
                rom.seek(lastSongOffset)
                    
