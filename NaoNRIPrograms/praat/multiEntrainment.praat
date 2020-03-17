# Intensity extractor
# Nichola Lubold 3/10/2015
 
form Multi Entrainment
	text user C:\Nikki\ASU_Research\NRI_Project\System\NRI_Git_Hub\automated_system\Nico_V2\Nico\data\userAudio\blob.wav
	optionmenu analysis_type: 2
	option intensity
	option pitch
	option sr
	option none
endform

# Intensity manipulation
if analysis_type = 1

	Read from file... 'user$'
	soundname$ = selected$("Sound")

	# Get mean intensity
	start = Get start time
	end = Get end time
	To Intensity... 130 0 yes
	meanint = Get mean... start end energy
	
	printline 'meanint'

	select Sound 'soundname$'
	plus Intensity 'soundname$'
	Remove

# Pitch manipulation
elsif analysis_type = 2

	floor = 100
	ceiling = 500

	Read from file... 'user$'
	s1$ = selected$("Sound")
	To Pitch... 0.01 floor ceiling
	avgUser = Get mean... 0 0 Hertz
	
	printline 'avgUser'

	select Sound 's1$'
	plus Pitch 's1$'
	Remove

# speech rate manipulation
elsif analysis_type = 3

	silencedb = -25
	mindip = 2
	minpause = 0.3

	Read from file... 'user$'

	soundname$ = selected$("Sound")
	soundid = selected("Sound")
	
	originaldur = Get total duration
	# allow non-zero starting time
	bt = Get starting time

	# Use intensity to get threshold
	#printline use intensity to get threshold
	To Intensity... 130 0 yes
	intid = selected("Intensity")
	start = Get time from frame number... 1
	nframes = Get number of frames
	end = Get time from frame number... 'nframes'

	# estimate noise floor
	minint = Get minimum... 0 0 Parabolic
	# estimate noise max
	maxint = Get maximum... 0 0 Parabolic
	#get .99 quantile to get maximum (without influence of non-speech sound bursts)
	max99int = Get quantile... 0 0 0.99

	# estimate Intensity threshold
	threshold = max99int + silencedb
	threshold2 = maxint - max99int
	threshold3 = silencedb - threshold2
	if threshold < minint
		threshold = minint
	endif
	
	# get pauses (silences) and speakingtime
	To TextGrid (silences)... threshold3 minpause 0.05 silent sounding
	textgridid = selected("TextGrid")
	silencetierid = Extract tier... 1
	silencetableid = Down to TableOfReal... sounding
	nsounding = Get number of rows
	npauses = 'nsounding'
	speakingtot = 0
	for ipause from 1 to npauses
		beginsound = Get value... 'ipause' 1
		endsound = Get value... 'ipause' 2
		speakingdur = 'endsound' - 'beginsound'
		speakingtot = 'speakingdur' + 'speakingtot'
	endfor

	select 'intid'
	Down to Matrix
	matid = selected("Matrix")
	# Convert intensity to sound
	To Sound (slice)... 1
	sndintid = selected("Sound")

	# use total duration, not end time, to find out duration of intdur
	# in order to allow nonzero starting times.
	
	intdur = Get total duration

	intmax = Get maximum... 0 0 Parabolic

	# estimate peak positions (all peaks)
	To PointProcess (extrema)... Left yes no Sinc70
	ppid = selected("PointProcess")

	numpeaks = Get number of points
	#printline 'numpeaks'

	# fill array with time points
	for i from 1 to numpeaks
		t'i' = Get time from index... 'i'
	endfor

	# fill array with intensity values
	select 'sndintid'
	peakcount = 0
	for i from 1 to numpeaks
		value = Get value at time... t'i' Cubic
		if value > threshold
			peakcount += 1
			int'peakcount' = value
			timepeaks'peakcount' = t'i'
		endif
	endfor

	# fill array with valid peaks: only intensity values if preceding
	# dip in intensity is greater than mindip
	select 'intid'
	validpeakcount = 0
	if numpeaks < 1
		currenttime = 0
		currentint = 0
	elsif numpeaks >= 1
		currenttime = timepeaks1
		currentint = int1
	endif

	for p to peakcount-1
		following = p + 1
		followingtime = timepeaks'following'
		dip = Get minimum... 'currenttime' 'followingtime' None
		diffint = abs(currentint - dip)

		if diffint > mindip
			validpeakcount += 1
			validtime'validpeakcount' = timepeaks'p'
		endif
	
		currenttime = timepeaks'following'
		currentint = Get value at time... timepeaks'following' Cubic
	endfor

	# Look for only voiced parts
	select 'soundid'
	To Pitch (ac)... 0.02 75 4 no 0.03 0.25 0.01 0.35 0.25 600
	# keep track of id of Pitch
	pitchid = selected("Pitch")

	voicedcount = 0
	for i from 1 to validpeakcount
		querytime = validtime'i'

		select 'textgridid'
		whichinterval = Get interval at time... 1 'querytime'
		whichlabel$ = Get label of interval... 1 'whichinterval'

		select 'pitchid'
		value = Get value at time... 'querytime' Hertz Linear

		if value <> undefined
			if whichlabel$ = "sounding"
				voicedcount = voicedcount + 1
				voicedpeak'voicedcount' = validtime'i'
			endif
		endif
	endfor

  
	# calculate time correction due to shift in time for Sound object versus
	# intensity object
	timecorrection = originaldur/intdur

	# Insert voiced peaks in TextGrid
	select 'textgridid'
	Insert point tier... 1 syllables
    
	for i from 1 to voicedcount
		position = voicedpeak'i' * timecorrection	
		Insert point... 1 position 'i'
	endfor

	# clean up before next sound file is opened
	select 'intid'
	plus 'matid'
	plus 'sndintid'
	plus 'ppid'
	plus 'pitchid'
	plus 'silencetierid'
	plus 'silencetableid'

	Remove

	select 'soundid'
	plus 'textgridid'
	Remove
 

	# summarize results in Info window
	speakingrate = 'voicedcount'/'originaldur'
	printline 'speakingrate:2'

elsif analysis_type = 4
	printline 0
endif