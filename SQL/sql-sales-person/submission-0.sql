-- Write your query below
select s.name from sales_person s
where not exists (
    select 1 from
    orders o 
    join company c
         on o.com_id = c.com_id
    where o.sales_id = s.sales_id 
        and c.name = 'CRIMSON'
);