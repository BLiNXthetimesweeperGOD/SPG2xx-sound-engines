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
currentTrack = 0
# Create a new MIDI file with one track
mid = mido.MidiFile(type=1)
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
    track = mido.MidiTrack()
    mid.tracks.append(track)
    with open(file_path, "rb") as sun:
        hits = 0
        track.append(mido.MetaMessage('set_tempo', tempo=150000))
        while True:
            data = sun.read(2)
            
            if data[1] == 0xB0:
                add_midi_message('program_change', currentTrack, data[0], None, 0) #Set program
                
            if data[1] == 0xF0 and data[0] == 0: #End of sequence
                break
                
            if data[1] in range(0x00, 0x7F): #Most likely note data. There can be multiple of these in a row, but they always eventually get followed up with a beat count value (the previous thing in this script)
                Duration = data[0]
                Note = data[1]
                add_midi_message('note_on', currentTrack, Note, 127, 0)
                add_midi_message('note_off', currentTrack, Note, 127, Duration*50) #Now end the note
    currentTrack+=1
    base, ext = os.path.splitext(file_path)
    output_path = f"{base}_converted.mid"
    mid.save(output_path)
    print(f"Conversion complete! MIDI file saved as {output_path}")
