# Pitch and Intensity Manipulator
# Nichola Lubold 3/10/2015

# Utilizing praat plugin toolkit, http://www.praatvocaltoolkit.com/, Ramon Corretge, 2012 

# This part presents a form to the user
form Pitch Manipulator
	text manipulateFile C:\Nikki\ASU_Research\NRI_Project\System\VirtualAgent\(Billy)Emma_SingleSessions\(Billy)Emma_SingleSessions\Nico\data\agentAudio\response.wav
	positive pitch 180
	text output C:\Nikki\ASU_Research\NRI_Project\System\VirtualAgent\(Billy)Emma_SingleSessions\Nico\data\agentAudio\transformed.wav

endform

floor = 75
ceiling = 350

Read from file... 'manipulateFile$'
s1$ = selected$("Sound",1)
select Sound 's1$'
To Pitch... 0 floor ceiling
avg = Get mean... 0 0 Hertz
max = Get maximum... 0 0 Hertz Parabolic
min = Get minimum... 0 0 Hertz	Parabolic


diff = pitch - avg


select Sound 's1$'
manipulation = To Manipulation... 0.01 floor ceiling
pitch = Extract pitch tier
Shift frequencies... 0 1000 diff Hertz
plus manipulation
Replace pitch tier
select manipulation
resynthesis = Get resynthesis (overlap-add)
result = Rename... 'transfile$'_shiftedFrequencies
select result
Write to WAV file... 'output$'

# create a copy with date and time
date$ = date$()
date$ = replace$(date$, ":", "-",0)
where = index(output$,".wav")
where = where - 1
head$ = left$(output$, where) + "_mean_" + date$ + ".wav"
Write to WAV file... 'head$'

# Cleanup
select Sound 's1$'
plus manipulation
plus pitch
plus result
plus Pitch 's1$'
Remove



printline "Script Finished"