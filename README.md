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


#V.Smile
V.Smile has a few formats (and all but the sequences have headers!). Here's a list of them:
- SP_Tonemaker (not fully documented yet, but it's being worked on. Seems to be some sort of configuration data for the sound.)
- Sunplus Tech.02. (Instruments. Not all can be played back yet, but they're being worked on. Can be IMA ADPCM, Unsigned 8-Bit PCM or 16-Bit PCM.)
- SunplusTech.02. (Voices and sound effects. IMA ADPCM.)
