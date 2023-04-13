select user_id, sum(sales.quantity * product.price) as spending from product join sales on product.product_id = sales.product_id
group by user_id order by spending desc; 
