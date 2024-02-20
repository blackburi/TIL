-- 흉부외과 또는 일반외과 의사 목록 출력하기

select dr_name, dr_id, mcdp_cd, date_format(hire_ymd, '%Y-%m-%d') as hire_ymd
from doctor
where mcdp_cd = 'GS' or mcdp_cd = 'CS'
order by hire_ymd desc, dr_name asc