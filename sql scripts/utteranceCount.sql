<<<<<<< HEAD
IF Object_ID('dbo.current_session') IS NOT NULL
    DROP VIEW dbo.current_session;

GO
create VIEW dbo.current_session AS 
select TOP(1) DateTime
=======
select TOP(1) convert(varchar(16),DateTime,100)
>>>>>>> 50e73f975d74750a5e7ae74832068f0173651ed0
from dbo.User_State with (nolock) 
WHERE DialogueAct= 'statement' AND UserID = 'cobiprobs' AND DateTime>='2020-03-20'--GETDATE()
AND ProblemID=1 ORDER BY DateTime DESC;
--GROUP BY ProblemID