include batch.praat
procedure action
include minmaxf0.praat
	# Get mean intensity
	start = Get start time
	end = Get end time
	To Intensity... 130 0 yes
	meanint = Get mean... start end energy

	printline 'meanint'
endproc