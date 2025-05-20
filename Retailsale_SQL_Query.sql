--Creating a database
CREATE DATABASE sql_pro;

--after insertings csv file checking'
USE sql_pro
SELECT * FROM [dbo].[retail_sales] 

--renaming column name
EXEC sp_rename 'retail_sales.quantiy','quantity','COLUMN';

--checking null values
SELECT * FROM retail_sales
WHERE transactions_id IS NULL;

SELECT * FROM retail_sales
WHERE age IS NULL;

SELECT * FROM retail_sales
WHERE sale_date IS NULL
     OR 
	 sale_time IS NULL
	 OR
	 customer_id IS NULL
	 OR
	 gender IS NULL 
	 OR
	 age IS NULL
	 OR 
	 category IS NULL
	 OR
     quantity IS NULL
	 OR
	 price_per_unit IS NULL
	 OR
	 cogs IS NULL 
	 OR
	 total_sale IS NULL;


--now deleting the blank  or null value rows
DELETE FROM retail_sales
where sale_date IS NULL
     OR 
	 sale_time IS NULL
	 OR
	 customer_id IS NULL
	 OR
	 gender IS NULL 
	 OR
	 age IS NULL
	 OR 
	 category IS NULL
	 OR
     quantity IS NULL
	 OR
	 price_per_unit IS NULL
	 OR
	 cogs IS NULL 
	 OR
	 total_sale IS NULL;

--after deleting now check the data
SELECT * FROM retail_sales;

SELECT COUNT(*) FROM retail_sales;

--Write a SQL query to retrieve all columns for sales made on '2022-11-05:
SELECT * FROM retail_sales
WHERE sale_date = '2022-11-05';

--Write a SQL query to retrieve all transactions where the category is 'Clothing' and the quantity sold is more than 4 in the month of Nov-2022:
SELECT SUM(quantity) as total FROM retail_sales
WHERE category = 'Clothing'
  AND sale_date >= '2022-11-01'
  AND sale_date < '2022-12-01';

  SELECT * 
FROM retail_sales
WHERE category = 'Clothing'
  AND quantity > 4
  AND sale_date >= '2022-11-01'
  AND sale_date < '2022-12-01';

--Write a SQL query to calculate the total sales (total_sale) for each category.:
SELECT category,SUM(total_sale) as totalsale FROM retail_sales
GROUP BY category;

--Write a SQL query to find the average age of customers who purchased items from the 'Beauty' category.:
SELECT customer_id,AVG(age) as avgage FROM retail_sales
WHERE category = 'Beauty'
GROUP BY customer_id;

--Write a SQL query to find all transactions where the total_sale is greater than 1000.:
SELECT customer_id,transactions_id,total_sale FROM retail_sales
WHERE total_sale > 1000
ORDER BY customer_id ASC;

--Write a SQL query to find the total number of transactions (transaction_id) made by each gender in each category.:
SELECT gender, category, COUNT(transactions_id) AS transaction_count
FROM retail_sales
GROUP BY gender, category
ORDER BY transaction_count ASC;

--Write a SQL query to calculate the average sale for each month. Find out best selling month in each year:
SELECT 
    YEAR(sale_date) AS sale_year,
    MONTH(sale_date) AS sale_month,
    AVG(total_sale) AS avg_monthly_sale
FROM retail_sales
GROUP BY 
    YEAR(sale_date),
    MONTH(sale_date)
ORDER BY 
   sale_year,avg_monthly_sale DESC;

--Write a SQL query to find the top 5 customers based on the highest total sales
SELECT TOP 5 * FROM retail_sales
ORDER BY total_sale DESC;


--Write a SQL query to find the number of unique customers who purchased items from each category.:
SELECT category,COUNT(DISTINCT customer_id) numbers_of_customers FROM retail_sales
GROUP BY category;

--Write a SQL query to create each shift and number of orders (Example Morning <12, Afternoon Between 12 & 17, Evening >17):
SELECT 
  CASE
    WHEN DATEPART(HOUR, sale_time) < 12 THEN 'Morning'
    WHEN DATEPART(HOUR, sale_time) BETWEEN 12 AND 17 THEN 'Afternoon'
    ELSE 'Evening'
  END AS shift,
  COUNT(*) AS order_count
FROM retail_sales
GROUP BY 
  CASE
    WHEN DATEPART(HOUR, sale_time) < 12 THEN 'Morning'
    WHEN DATEPART(HOUR, sale_time) BETWEEN 12 AND 17 THEN 'Afternoon'
    ELSE 'Evening'
  END;

  --calculate the total number of orders per month year wise separate
  SELECT 
    YEAR(sale_date) AS sale_year,
    MONTH(sale_date) AS sale_month,
    COUNT(*) AS total_orders
FROM retail_sales
GROUP BY 
    YEAR(sale_date),
    MONTH(sale_date)
ORDER BY 
    sale_year,
    sale_month;


--which category got highest sale according year
SELECT 
    category,
    YEAR(sale_date) AS sale_year,
    SUM(total_sale) AS total_sales
FROM retail_sales
GROUP BY 
    category,
    YEAR(sale_date)
ORDER BY 
    total_sales DESC;


--end of project 
