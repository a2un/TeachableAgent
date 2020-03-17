# Pitch, Intensity, and Rate Manipulator
# Nichola Lubold 3/10/2015
 
# Description: Manipulates a sound file in a variety of ways depending on selected option. 
# Update: Reduced number of options; took out IPU options
#		Added in pitch_contour_raise 
#		Added in pitch_median
#		Modified copying_pitch_contour option to include sizing speaker's speech to duration of Quinn's speech 

# This part presents a form to the user
form Pitch Intensity Rate Manipulator
	comment type of analysis (rate is currently unavailable):
	optionmenu analysis_type: 1
	option intensity
	option pitch_flat
	option pitch_median
	option pitch_copycontour_dur
	option pitch_contour_raise
	option rate
	comment gender:
	choice gender: 1
	button male
	button female
	comment feature file:
	text featurefile E:\Nikki\Research\Tag\PraatScripts\wavfiles\blob_05.wav
	comment transform file:
	text transfile E:\Nikki\Research\Tag\PraatScripts\wavfiles\response.wav
	comment output file:
	text output E:\Nikki\Research\Tag\PraatScripts\wavfiles\transformed.wav
endform

# If intensity...raises/lowers average intensity to that of the speaker
if analysis_type = 1

	#meanIntensity = Get mean... 0 duration energy
	#printline 'meanIntensity'

	# Read in feature file
	Read from file... 'featurefile$'
	soundname$ = selected$ ("Sound")

	# Get mean intensity
	start = Get start time
	end = Get end time
	To Intensity... 100 0
	meanint = Get mean... start end dB

	# Read in trans file
	Read from file... 'transfile$'
	sound_two$ = selected$ ("Sound")

	# Transform intensity	
	To Intensity... 100 0
	Formula... self+(meanint-self)
	Down to IntensityTier
	select IntensityTier 'sound_two$'
	plus Sound 'sound_two$'
	Multiply

	select Sound 'sound_two$'
	Write to WAV file... 'output$'

	# Save to WAV file
	Save as WAV file... 'output$'
	
	# Remove extraneous intensity sounds
	select Sound 'soundname$'
	plus Sound 'sound_two$'
	plus IntensityTier 'sound_two$'
	plus Intensity 'soundname$'
	Remove

# else if pitch_flat - maps Quinn to a flat pitch based on the mean pitch of the speaker
elsif analysis_type = 2
	if gender = 1
		floor = 75
		ceiling = 300
	else
		floor = 100
		ceiling = 500
	endif

	# Read in feature file & get mean pitch
	Read from file... 'featurefile$'
	sound$ = selected$ ("Sound")
	To Pitch... 0 floor ceiling
	mean = Get mean... 0 0 Hertz
	
	# Read in transform file
	Read from file... 'transfile$'
	sound_one$ = selected$ ("Sound")
	select Sound 'sound_one$'
	start = Get start time
	end = Get end time
	
	To Manipulation... 0.01 floor ceiling
	Create PitchTier... 'sound_one$' start end
	Add point... start mean
	Add point... end mean

	# Combine and save the changed file
	select Manipulation 'sound_one$'
	plus PitchTier 'sound_one$'
	Replace pitch tier
	select Manipulation 'sound_one$'
	Get resynthesis (PSOLA)
	Write to WAV file... 'output$'

	select Sound 'sound_one$'
	plus Manipulation 'sound_one$'
	plus Sound 'sound$'
	plus Pitch 'sound$'
	plus PitchTier 'sound_one$'
	Remove

# else if pitch_median - puts the median of Quinn's speech at the median of the speaker's
elsif analysis_type = 3

Read from file... 'featurefile$'
s1tmp = selected("Sound",1)
s1$ = selected$("Sound",1)
Read from file... 'transfile$'
s2tmp = selected("Sound",1)
s2$ = selected$("Sound",1)
select s1tmp
execute workpre.praat
s1 = selected("Sound")
select s2tmp
execute workpre.praat
s2 = selected("Sound")
select s1
include minmaxf0.praat
minF0_1 = minF0
maxF0_1 = maxF0
To Pitch... 0 minF0_1 maxF0_1
f0_1 = Get quantile... 0 0 0.50 Hertz
Remove
select s2
include minmaxf0.praat
minF0_2 = minF0
maxF0_2 = maxF0
To Pitch... 0 minF0_2 maxF0_2
f0_2 = Get quantile... 0 0 0.50 Hertz
Remove
f0_f = f0_1/f0_2
select s2
dur = Get total duration
pitch = To Pitch... 0.01 minF0 maxF0
plus s2
manipulation = To Manipulation
pitchtier = Extract pitch tier
durationtier = Create DurationTier... 's2$' 0 dur
Add point... 0 1
plus manipulation
Replace duration tier
select pitchtier
Formula... self*f0_f
plus manipulation
Replace pitch tier
select manipulation
resynthesis = Get resynthesis (overlap-add)
execute workpost.praat
result = Rename... 's2$'_copypitchmedian_'s1$'
select s1
plus s2
plus pitch
plus manipulation
plus pitchtier
plus durationtier
plus resynthesis
Remove
select result
Write to WAV file... 'output$'
	
# else if pitch_contour_turn - map the whole turn and then smooth out the rest of Quinn's speech if longer...
elsif analysis_type = 4

	# -------------------------should map the whole turn and then smooth out the rest of Quinn's speech if longer...add smothing

	# Set floor and ceiling
	if gender = 1
		floor = 75
		ceiling = 300
	else
		floor = 100
		ceiling = 500	
	endif

	Read from file... 'featurefile$'
	sound$ = selected$ ("Sound")

	# Create a manipulation object from feature file and extract pitch tier
	To Manipulation... 0.01 floor ceiling
	select Manipulation 'sound$'
	Extract pitch tier
	select PitchTier 'sound$'
	Rename... featureTier

	# Read in trans file and create a manipulation object
	Read from file... 'transfile$'
	sound_two$ = selected$ ("Sound")
	To Manipulation... 0.01 floor ceiling
	select Manipulation 'sound_two$'
	plus PitchTier featureTier
	Replace pitch tier
	select Manipulation 'sound_two$'
	Get resynthesis (PSOLA)
	Write to WAV file... 'output$'

	select Sound 'sound_two$'
	plus Manipulation 'sound_two$'
	plus Sound 'sound$'
	plus Manipulation 'sound$'
	plus PitchTier featureTier
	Remove

# else if pitch_stylize
elsif analysis_type = 5

	# ------------------------ same as the above except we stylize the pitch first and then smooth out the rest...

	Read from file... 'featurefile$'
	soundname$ = selected$ ("Sound")
	filedur = Get total duration
	printline 'filedur'

# else if pitch_raise
elsif analysis_type = 6

	# ----------------------- Most important one in terms of distinction - should keep contour same but raise mean of pitch...complicated

	Read from file... 'featurefile$'
	soundname$ = selected$ ("Sound")
	filedur = Get total duration
	printline 'filedur'

# else rate
else
	Read from file... 'featurefile$'
	soundname$ = selected$ ("Sound")
	filedur = Get total duration
	printline 'filedur'
endif



printline "Script Finished"