import struct
import tkinter as tk
from tkinter import filedialog
import mido
import os

# Set up the tkinter file dialog
root = tk.Tk()
root.withdraw()
files = filedialog.askopenfilenames()
root.destroy()

# Create a new MIDI file with one track
mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)
current_time = 0
# Function to add MIDI messages to the track
def add_midi_message(message_type, channel, data1, data2, delta_time):
    global current_time
    if message_type == 'program_change':
        track.append(mido.Message('program_change', program=data1, channel=channel, time=delta_time))
    elif message_type == 'note_on':
        track.append(mido.Message('note_on', note=data1, velocity=data2, channel=channel, time=delta_time))
    elif message_type == 'note_off':
        track.append(mido.Message('note_off', note=data1, velocity=0, channel=channel, time=delta_time))
    # Update the current time
    current_time += delta_time
    # Add other message types as needed
for file_path in files:
    # Create a new MIDI file with one track
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)
    current_time = 0
    # Read the custom format and convert to MIDI
    with open(file_path, "rb") as sun:
        prevnotes = []
        prevdelay = 0 #For testing something
        hits = 0
        while True:
            data = sun.read(2)
            if not data:
                break  # End of file
            if data[1] in range(0x27, 0x2F): #Set tempo
                #print(f"Tempo: {data[0]}")
                tempo = data[0]
                if data[1] >= 0x29:
                    try:
                        tempobytemain = str(hex(data[0]))[2:4]
                        #print(tempobytemain)
                    except:
                        tempobytemain = "0"+str(hex(data[0]))[2:3]
                        #print(tempobytemain)
                    tempoconverted = int(str(hex(int("0x"+str(hex(data[1]))[-1], 16)-8))+tempobytemain, 16)
                    #print(tempoconverted, data[1], data[0])
                    tempo = tempoconverted
                #track.append(mido.MetaMessage('set_tempo', tempo=tempo*20))
                track.append(mido.MetaMessage('set_tempo', tempo=5000))
            if data[1] in range(0, 16): #Program change
                channel = data[1]
                add_midi_message('program_change', channel, data[0], None, 0)
            if data[1] == 0x10: #Pitchwheel (and others?)
                sun.read(2)
                add_midi_message('note_off', note[1], note[0], 0, delay)
            if data[1] == 0x40: #Beat count value (might be how long the notes are all held for?)
                #print(f"Beat Count Value: {data[0]}")
                #current_time += data[0]
                var = 0 #The current channel
                hits += 1
                #if hits == 2:
                delay = data[0]*len(prevnotes)*tempo
                for note in prevnotes:
                    add_midi_message('note_off', note[1], note[0], 0, delay)
                    if delay!= 0:
                        prevdelay=delay
                    delay = 0
                    var += 1
                delta_time = -prevdelay
                hits = 0
                prevnotes = [] #Clear the previous notes
                
            if data[1] in range(0x80, 0x8F): #Most likely note data. There can be multiple of these in a row, but they always eventually get followed up with a beat count value (the previous thing in this script)
                channel = int(str("0x"+str(hex(data[0]))[2]), 16) #The channel ID
                data2 = sun.read(2) #Should hold the pitch info. Byte 2 (1 in Python) is always 0x40.
                data3 = sun.read(2) #Should hold the volume info
                volume = data3[0]
                pitch = data2[0]
                delta_time = 0
                note = pitch, channel
                prevnotes.append(note)
                #add_midi_message('note_on', channel, data2[0], data3[0])
                add_midi_message('note_on', channel, data2[0], data3[0], delta_time)
                
            
                

    base, ext = os.path.splitext(file_path)
    output_path = f"{base}_converted.mid"
    mid.save(output_path)
    print(f"Conversion complete! MIDI file saved as {output_path}")
