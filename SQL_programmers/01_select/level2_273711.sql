-- 업그레이드 된 아이템 구하기

select b.item_id, a.item_name, a.rarity
from item_info a join item_tree b on a.item_id = b.item_id
where b.parent_item_id in (select item_id
                            from item_info
                            where rarity = 'RARE')
order by a.item_id desc