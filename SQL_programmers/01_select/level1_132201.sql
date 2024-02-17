select PT_NAME, PT_NO, GEND_CD, AGE, ifnull(TLNO, 'NONE') as TLNO
from patient
where AGE <= 12 and GEND_CD = 'W'
order by AGE desc, PT_NAME asc