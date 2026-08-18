-- Write your query below
select s.seller_name from
seller s left join orders o
ON s.seller_id = o.seller_id
AND o.sale_date >= DATE '2020-01-01'
AND o.sale_date < DATE '2021-01-01'
group by s.seller_name, s.seller_id
having count(o.order_id) = 0
order by s.seller_name asc