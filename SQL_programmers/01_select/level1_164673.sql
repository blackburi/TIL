-- 조건에 부합하는 중고거래 댓글 조회하기

select b.title, b.board_id, r.reply_id, r.writer_id, r.contents,
       date_format(r.created_date, '%Y-%m-%d') as created_date
from used_goods_board b join used_goods_reply r on b.board_id = r.board_id
where b.created_date like '%2022-10%'
order by r.created_date, b.title