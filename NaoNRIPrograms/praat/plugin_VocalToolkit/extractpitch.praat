include batch.praat
procedure action
include minmaxf0.praat
	To Pitch... 0.01 100 500
	avg = Get mean... 0 0 Hertz
	printline 'avg'
endproc
