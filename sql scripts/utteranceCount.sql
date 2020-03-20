select TOP(1) convert(varchar(16),DateTime,100)
from dbo.User_State with (nolock) 
WHERE DialogueAct= 'statement' AND UserID = 'cobiprobs' AND DateTime>='2020-03-20'--GETDATE()
AND ProblemID=1 ORDER BY DateTime DESC;
--GROUP BY ProblemID