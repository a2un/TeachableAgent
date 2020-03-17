select NicoStateKey,StateKey as UserStateKey,ns.DateTime as NicoTimeStamp, us.StepID as userStepId, ns.StepID as nicoStepId,us.DialogueAct,
us.DateTime as UserStateTimeStamp,us.ProblemID as ProblemID,
AnsweredStep as UserAnsweredStep, us.transcript,NicoResponse
from
dbo.User_State (nolock) us inner join dbo.Nico_State ns (nolock) on 
(us.UserID = ns.UserID and us.ProblemID = ns.ProblemID) 
where us.UserID = 'cobiprobs' and ns.DateTime>='2020-01-17 17:17:00'
order by ProblemID ASC	;

select * from USERS;

Select * from Nico_State (nolock) where userid='cobiprobs' and DateTime >='2020-02-14 11:04:00'

Select * from User_State (nolock) where userid='cobiprobs' and DateTime >='2020-02-14 11:04:00'

select * from Error_Log (nolock) where userid='cobiprobs' and DateTime >='2020-02-11 10:00:00';


update USERS set problemset='G' WHERE userid='shang';

