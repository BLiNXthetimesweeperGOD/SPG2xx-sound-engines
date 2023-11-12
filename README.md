# SPG2xx-sound-engines
A repository for documentation and tools for the various sound engines and formats used on SPG2xx-based devices.


Currently completed stuff:
- A script for extracting instruments, sound effects and voices from V.Smile (and maybe Sports Vii) games


Work-in-progress stuff:
- Detection of the type of instrument in V.Smile games to make the output txth file work better/play everything properly
- Extracting sounds and instruments from non-V.Smile games (such as the JAKKS Pacific Plug 'N Plays and the LeapFrog ClickStart)
- Automating the extraction of sequences (and documenting the commands within the said sequences)
- Listing every sound engine and how they work (there's more than 1)
- Listing every codec used by each system individually
- A genuinely full list of systems using SPG2xx hardware (including each JAKKS PACIFIC Plug 'N Play)


# V.Smile
V.Smile has a few formats (and all but the sequences have headers!). Here's a list of them:
- SP_Tonemaker (not fully documented yet, but it's being worked on. Seems to be some sort of configuration data for the sound.)
- Sunplus Tech.02. (Instruments. Not all can be played back yet, but they're being worked on. Can be IMA ADPCM, Unsigned 8-Bit PCM or 16-Bit PCM.)
- SunplusTech.02. (Voices and sound effects. IMA ADPCM.)
- Sequences (unknown, the actual data for them still needs to be found)

Some other stuff:

- Sequence table (the pointer format still needs to be figured out)

# Sports Vii
This uses a lot of the same formats as the V.Smile.

# JAKKS PACIFIC Plug it in and Play TV Games
As the name suggests, these are Plug 'N Plays. Several were made and they all work in mostly the same way.
- Instruments all use unsigned 8-Bit PCM and are stored at the end of the ROMs in most cases
- Sequences (unknown, the actual data for them still needs to be found)
- These systems have test modes that can be accessed at the boot screens. These can be used to more easily figure out the format.

Some other stuff:
- Sequence table seems to be spread across the ROMs. Each channel is loaded individually in a lot of cases.

# LeapFrog ClickStart
- Uses a newer sound engine, but the said engine still uses parts of the engine used on the V.Smile/Sports Vii (such as the SP_ToneMaker data)
- MAME doesn't emulate the voices yet. They might be in the same format as the original LeapPad and the Leapster, as I haven't found what codec they use yet.
- Modifying (what I believe are) the sequences in any way tends to crash MAME with an invalid instruction error.
- Some games (such as Finding Nemo: Sea of Keys) store some audio as unsigned 8-Bit PCM.
