# SPG2xx-sound-engines
A repository for documentation and tools for the various sound engines and formats used on SPG2xx-based devices.


Currently completed stuff:
- Scripts for extracting instruments, sound effects, voices and sequences from V.Smile games


Work-in-progress stuff:
- Detection of the type of instrument in V.Smile games to make the output txth file work better/play everything properly
- Extracting sounds and instruments from non-V.Smile games (such as the JAKKS Pacific Plug 'N Plays and the LeapFrog ClickStart)
- Automating the extraction of sequences (and documenting the commands within the said sequences) (mainly just JAKKS, the V.Smile and all SunMidi stuff is mostly figured out already)
- Listing every sound engine and how they work (there's more than 1)
- Listing every codec used by each system individually
- A genuinely full list of systems using SPG2xx hardware (including each JAKKS PACIFIC Plug 'N Play)

# V.Smile (and all variants that are also SPG2xx-based)
V.Smile has a few formats (and all but the sequences have headers!). Here's a list of them:
- SP_Tonemaker (not fully documented yet, but it's being worked on. Seems to be some sort of configuration data for the sound.)
- Sunplus Tech.02. (Instruments. Not all can be played back yet, but they're being worked on. Can be IMA ADPCM, Unsigned 8-Bit PCM or 16-Bit PCM.)
- SunplusTech.02. (Voices and sound effects. IMA ADPCM.)
- Sequences (these are in a SunPlus format known as SunMidi/SunMidiAr. I've documented everything I know about it so far.)
- The sequence and sound effect/voice tables are in the same area of the ROM

# LeapFrog ClickStart: My First Computer
- Uses a newer sound engine, but the said engine still uses parts of the engine used on the V.Smile (such as the SP_ToneMaker and sequence data)
- MAME doesn't emulate the voices yet. They might be in the same format as the original LeapPad and the Leapster, as I haven't found what codec they use yet.
- Instruments and sound effects are stored in an unknown codec (which is emulated in MAME, but I have yet to find the name or decode these outside of emulation)
- Some games (such as Finding Nemo: Sea of Keys) store some audio as unsigned 8-Bit PCM.
- Sequences (same format as the V.Smile)

# Sports Vii
This uses a lot of the same formats as the V.Smile and ClickStart. Still needs research when it comes to finding the tables with this stuff though.

# JAKKS PACIFIC Plug it in and Play TV Games
As the name suggests, these are Plug 'N Plays. Several were made and they all work in mostly the same way.
- Instruments all use unsigned 8-Bit PCM and are stored at the end of the ROMs in most cases
- Sequences (custom, completely different to how the SunPlus SunMidi/SunMidiAr format works)
- These systems have test modes that can be accessed at the boot screens. These can be used to more easily figure out the format.
- The sequence table seems to be spread across the ROMs. Each channel is loaded individually and played as a separate sequence.



# Other important information
My conversion script makes use of the Python Mido library. Be sure to run "pip install mido" if you want it to work!

Some games may not have their sequences or sounds get extracted properly with the VRipper script. That's likely due to differences in the sound engine or programming of the said games. Please make an issue for the said games (V.Smile only for now) so I can eventually look into them.

I am primarily focused on the V.Smile and JAKKS Pacific stuff for now since they have the most games with unique sound engines.
