/*Inner join-to find related data in two tables*/
/*Includes the ProductName from the products table and the corresponding Category from the product category table. 
Because the query uses an INNER join, any products that do not have corresponding categories, and any categories that contain no products 
are omitted from the results*/

SELECT SalesLT.Product.Name AS ProductName, SalesLT.ProductCategory.Name AS Category
 FROM SalesLT.Product
 INNER JOIN SalesLT.ProductCategory
 ON SalesLT.Product.ProductCategoryID = SalesLT.ProductCategory.ProductCategoryID;

/* INNER joins are the default kind of join and hence returns same result as that of previous query*/
SELECT SalesLT.Product.Name AS ProductName, SalesLT.ProductCategory.Name AS Category
 FROM SalesLT.Product
 JOIN SalesLT.ProductCategory
     ON SalesLT.Product.ProductCategoryID = SalesLT.ProductCategory.ProductCategoryID;

/*It returns the same results as before. The use of table aliases can greatly simplify a query, particularly when multiple joins must be used*/
 SELECT p.Name AS ProductName, c.Name AS Category
 FROM SalesLT.Product AS p
 JOIN SalesLT.ProductCategory AS c
     ON p.ProductCategoryID = c.ProductCategoryID;

/*Retrieves sales order data from the SalesLT.SalesOrderHeader, SalesLT.SalesOrderDetail, and SalesLT.Product tables*/
SELECT oh.OrderDate, oh.SalesOrderNumber, p.Name AS ProductName, od.OrderQty, od.UnitPrice, od.LineTotal
 FROM SalesLT.SalesOrderHeader AS oh
 JOIN SalesLT.SalesOrderDetail AS od
     ON od.SalesOrderID = oh.SalesOrderID
 JOIN SalesLT.Product AS p
     ON od.ProductID = p.ProductID
 ORDER BY oh.OrderDate, oh.SalesOrderID, od.SalesOrderDetailID;

 /*Outer  join-used to retrieve all rows from one table, and any corresponding rows from a related table.
 In cases where a row in the outer table has no corresponding rows in the related table, NULL values are returned for the related table fields. For example, 
 suppose you want to retrieve a list of all customers and any orders they have placed, including customers who have registered but never placed an order*/

 SELECT c.FirstName, c.LastName, oh.SalesOrderNumber
 FROM SalesLT.Customer AS c
 LEFT OUTER JOIN SalesLT.SalesOrderHeader AS oh
     ON c.CustomerID = oh.CustomerID
 ORDER BY c.CustomerID;

/*Note the use of the LEFT keyword. This identifies which of the tables in the join is the outer table (the one from which all rows should be preserved). 
In this case, the join is between the Customer and SalesOrderHeader tables, so a LEFT join designates Customer as the outer table. 
Had a RIGHT join been used, the query would have returned all records from the SalesOrderHeader table and only matching data from the Customer table.*/

/*A cross join matches all possible combinations of rows from the tables being joined. In practice, it’s rarely used; 
but there are some specialized cases where it is useful.*/

SELECT p.Name, c.FirstName, c.LastName, c.EmailAddress
FROM SalesLT.Product AS p
CROSS JOIN SalesLT.Customer AS c;

/*Scalar functions
Transact-SQL provides a large number of functions that you can use to extract additional information from your data. 
Most of these functions are scalar functions that return a single value based on one or more input parameters, often a data field.*/

/*YEAR function is retrieved the year from the SellStartDate field*/
SELECT YEAR(SellStartDate) AS SellStartYear, ProductID, Name FROM SalesLT.Product ORDER BY SellStartYear;

/*Note that the DATENAME function returns a different value depending on the datepart parameter that is passed to it. 
In this example, mm returns the month name, and dw returns the weekday name.*/

/*Note also that the DATEDIFF function returns the specified time interval between and start date and an end date. 
In this case the interval is measured in years (yy), and the end date is determined by the GETDATE function; 
which when used with no parameters returns the current date and time*/
SELECT YEAR(SellStartDate) AS SellStartYear,
        DATENAME(mm,SellStartDate) AS SellStartMonth,
        DAY(SellStartDate) AS SellStartDay,
        DATENAME(dw, SellStartDate) AS SellStartWeekday,
        DATEDIFF(yy,SellStartDate, GETDATE()) AS YearsSold,
        ProductID,
        Name
FROM SalesLT.Product
ORDER BY SellStartYear;

/*Returns the concatenated first and last name for each customer*/
SELECT CONCAT(FirstName + ' ', LastName) AS FullName FROM SalesLT.Customer;

/*Additional string functions*/
 SELECT UPPER(Name) AS ProductName,
        ProductNumber,
        ROUND(Weight, 0) AS ApproxWeight,
        LEFT(ProductNumber, 2) AS ProductType,
        SUBSTRING(ProductNumber,CHARINDEX('-', ProductNumber) + 1, 4) AS ModelCode,
        SUBSTRING(ProductNumber, LEN(ProductNumber) - CHARINDEX('-', REVERSE(RIGHT(ProductNumber, 3))) + 2, 2) AS SizeCode
 FROM SalesLT.Product;

/*The product name, converted to upper case by the UPPER function*/
/*The product number, which is a string code that encapsulates details of the product*/
/*The weight of the product, rounded to the nearest whole number by using the ROUND function*/
/*The product type, which is indicated by the first two characters of the product number, starting from the left (using the LEFT function)*/
/*The model code, which is extracted from the product number by using the SUBSTRING function, which extracts the four characters immediately following 
the first - character, which is found using the CHARINDEX function*/
/*The size code, which is extracted using the SUBSTRING function to extract the two characters following the last - in the product code. 
The last - character is found by taking the total length (LEN) of the product ID and finding its index (CHARINDEX) in the reversed (REVERSE) first three 
characters from the right (RIGHT). This example shows how you can combine functions to apply fairly complex logic to extract the values you need*/

/*Logical Functions*/


/*Display results only products with a numeric size*/
SELECT Name, Size AS NumericSize
 FROM SalesLT.Product
 WHERE ISNUMERIC(Size) = 1;

/*Below query nests the ISNUMERIC function used previously in an IF function; 
which in turn evaluates the result of the ISNUMERIC function and returns Numeric if the result is 1 (true), and Non-Numeric otherwise*/
 SELECT Name, IIF(ISNUMERIC(Size) = 1, 'Numeric', 'Non-Numeric') AS SizeType
 FROM SalesLT.Product;

 /*Aggregate functions*/

SELECT COUNT(*) AS Products,
        COUNT(DISTINCT ProductCategoryID) AS Categories,
        AVG(ListPrice) AS AveragePrice
 FROM SalesLT.Product;
/*The number of products in the table. This is returned by using the COUNT function to count the number of rows (*)*/
/*The number of categories. This is returned by using the COUNT function to count the number of distinct category IDs in the table*/
/*The average price of a product. This is returned by using the AVG function with the ListPrice field*/

/*Group aggregated results with the GROUP BY clause*/

/*Returns the number of customers assigned to each salesperson*/
 SELECT Salesperson, COUNT(CustomerID) AS Customers
 FROM SalesLT.Customer
 GROUP BY Salesperson
 ORDER BY Salesperson;

/*Returns the total sales revenue for each salesperson who has completed any sales*/
 SELECT c.Salesperson, SUM(oh.SubTotal) AS SalesRevenue
 FROM SalesLT.Customer c
 JOIN SalesLT.SalesOrderHeader oh
     ON c.CustomerID = oh.CustomerID
 GROUP BY c.Salesperson
 ORDER BY SalesRevenue DESC;

/*Filter groups with the HAVING clause*/
/**/
 SELECT Salesperson, COUNT(CustomerID) AS Customers
 FROM SalesLT.Customer
 WHERE COUNT(CustomerID) > 100
 GROUP BY Salesperson
 ORDER BY Salesperson;

 /*Above query returns an error. The WHERE clause is applied before the aggregations and the GROUP BY clause, 
 so you can’t use it to filter on the aggregated value*/

 SELECT Salesperson, COUNT(CustomerID) AS Customers
 FROM SalesLT.Customer
 GROUP BY Salesperson
 HAVING COUNT(CustomerID) > 100
 ORDER BY Salesperson;

/*Now it returns only salespeople who have more than 100 customers assigned to them*/

