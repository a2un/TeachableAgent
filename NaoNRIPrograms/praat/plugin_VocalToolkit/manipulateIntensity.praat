# Pitch, Intensity, and Rate Manipulator
# Nichola Lubold 3/10/2015
 
# Utilizing praat plugin toolkit, http://www.praatvocaltoolkit.com/, Ramon Corretge, 2012 

# This part presents a form to the user

form Intensity Rate Manipulator
	text manipulateFile C:\Nikki\ASU_Research\NRI_Project\System\VirtualAgent\(Billy)Emma_SingleSessions\(Billy)Emma_SingleSessions\Nico\data\agentAudio\response.wav
	positive intensity 70
	text output C:\Nikki\ASU_Research\NRI_Project\System\VirtualAgent\(Billy)Emma_SingleSessions\Nico\data\agentAudio\transformed.wav

endform

# If intensity...raises/lowers average intensity to that of the speaker

# Read in trans file
Read from file... 'manipulateFile$'
s1$ = selected$ ("Sound")

# Transform intensity	
To Intensity... 90 0
Formula... self+(intensity-self)
Down to IntensityTier
select IntensityTier 's1$'
plus Sound 's1$'
Multiply... 's2$'
result = Rename... 'transfile$'_shiftedFrequencies
select result
Write to WAV file... 'output$'


# create a copy with date and time
date$ = date$()
date$ = replace$(date$, ":", "-",0)
where = index(output$,".wav")
where = where - 1
head$ = left$(output$, where) + "_intensity_" + date$ + ".wav"
Write to WAV file... 'head$'
	
# Remove extraneous intensity sounds
select Sound 's1$'
plus IntensityTier 's1$'
plus Intensity 's1$'
Remove



printline "Script Finished"