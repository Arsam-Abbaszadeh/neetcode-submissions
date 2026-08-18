-- Write your query below
select c.name
from customers c
where (
    select count(*)
    from orders o
    where o.customer_id = c.id
) = 0