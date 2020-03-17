# Pitch Extractor
# Nichola Lubold 3/10/2015
 
# Description: Extracts Mean Pitch from given audio 

# This part presents a form to the user
form Pitch Extractor
	comment user audio:
	text user C:\Nikki\ASU_Research\NRI_Project\System\NRI_Git_Hub\automated_system\Nico_V1\Nico\data\userAudio\blob.wav
endform



# Set floor and ceiling
#if gender = 1
#	floor = 75
#	ceiling = 300
#else
#	floor = 100
#	ceiling = 500	
#endif

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
