SELECT p.id, p.title, p.price, COUNT(pi.id) AS image_count
FROM product p 
LEFT JOIN product_image pi ON p.id = pi.product_id
GROUP BY p.id;