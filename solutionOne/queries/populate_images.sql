INSERT OR REPLACE INTO product_image (product_id, url) 
SELECT ?, ? 
WHERE NOT EXISTS (SELECT 1 FROM product_image WHERE url = ?);