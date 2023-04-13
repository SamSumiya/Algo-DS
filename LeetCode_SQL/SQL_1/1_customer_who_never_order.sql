select Customers.name as Customers from Customers where Customers.id not in ( select customerId from orders) 

select name as Customers from customers left join orders on customers.id = orders.customerId where orders.customerId is null; 