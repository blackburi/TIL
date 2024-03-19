-- 물고기 종류별 대어 찾기

select i.id, n.fish_name, i.length
from fish_info as i, fish_name_info as n
where i.fish_type = n.fish_type and
      (i.fish_type, i.length) in (select fish_type, max(length)
                                  from fish_info
                                  group by fish_type)