/*Challenge 1.1 Retrieve customer details */
SELECT * FROM SalesLT.Customer;

/*Challenge 1.2 Retrieve customer name data */
SELECT Title, FirstName, MiddleName, LastName, Suffix
 FROM SalesLT.Customer;

/*Challenge 1.3 Retrieve customer names and phone numbers */
 SELECT Salesperson, ISNULL(Title,'') + ' ' + LastName AS CustomerName, Phone
 FROM SalesLT.Customer;

/*Challenge 2.1 Retrieve a list of cities */
 SELECT DISTINCT City, StateProvince
 FROM SalesLT.Address
 ORDER BY City;

/*Challenge 2.2 Retrieve the heaviest products */
 SELECT TOP (10) PERCENT WITH TIES Name
 FROM SalesLT.Product
 ORDER BY Weight DESC;

/*Challenge 3.1 Retrieve product details for product model 1 */
 SELECT Name, Color, Size
 FROM SalesLT.Product
 WHERE ProductModelID = 1;

/*Challenge 3.2 Filter products by color and size */
 SELECT ProductNumber, Name
 FROM SalesLT.Product
 WHERE Color IN ('Black','Red','White') AND Size IN ('S','M');

/*Challenge 3.3 Filter products by product number */
 SELECT ProductNumber, Name, ListPrice
 FROM SalesLT.Product
 WHERE ProductNumber LIKE 'BK-%';

/*Challenge 3.4 Retrieve specific products by product number */
 SELECT ProductNumber, Name, ListPrice
 FROM SalesLT.Product
 WHERE ProductNumber LIKE 'BK-[^R]%-[0-9][0-9]';

/*Challenge 4.1 Retrieve customer orders */
 SELECT c.CompanyName, oh.SalesOrderID, oh.TotalDue
 FROM SalesLT.Customer AS c
 JOIN SalesLT.SalesOrderHeader AS oh
     ON oh.CustomerID = c.CustomerID;

/*Challenge 4.2 Retrieve customer orders with addresses */
 SELECT c.CompanyName,
        a.AddressLine1,
        ISNULL(a.AddressLine2, '') AS AddressLine2,
        a.City,
        a.StateProvince,
        a.PostalCode,
        a.CountryRegion,
        oh.SalesOrderID,
        oh.TotalDue
 FROM SalesLT.Customer AS c
 JOIN SalesLT.SalesOrderHeader AS oh
     ON oh.CustomerID = c.CustomerID
 JOIN SalesLT.CustomerAddress AS ca
     ON c.CustomerID = ca.CustomerID
 JOIN SalesLT.Address AS a
     ON ca.AddressID = a.AddressID
 WHERE ca.AddressType = 'Main Office';
 
/*Challenge 5.1 Retrieve a list of all customers and their orders */
SELECT c.CompanyName, c.FirstName, c.LastName,
        oh.SalesOrderID, oh.TotalDue
 FROM SalesLT.Customer AS c
 LEFT JOIN SalesLT.SalesOrderHeader AS oh
     ON c.CustomerID = oh.CustomerID
 ORDER BY oh.SalesOrderID DESC;

/*Challenge 5.2 Retrieve a list of customers with no address */
 SELECT c.CompanyName, c.FirstName, c.LastName, c.Phone
 FROM SalesLT.Customer AS c
 LEFT JOIN SalesLT.CustomerAddress AS ca
     ON c.CustomerID = ca.CustomerID
 WHERE ca.AddressID IS NULL;

/*Challenge 6.1 Retrieve the order ID and freight cost of each order */
 SELECT SalesOrderID,
        ROUND(Freight, 2) AS FreightCost
 FROM SalesLT.SalesOrderHeader;
 
/*Challenge 6.2 Add the shipping method */
 SELECT SalesOrderID,
        ROUND(Freight, 2) AS FreightCost,
        LOWER(ShipMethod) AS ShippingMethod
 FROM SalesLT.SalesOrderHeader;

/*Challenge 6.3 Add shipping date details */
  SELECT SalesOrderID,
        ROUND(Freight, 2) AS FreightCost,
        LOWER(ShipMethod) AS ShippingMethod,
        YEAR(ShipDate) AS ShipYear,
        DATENAME(mm, ShipDate) AS ShipMonth,
        DAY(ShipDate) AS ShipDay
 FROM SalesLT.SalesOrderHeader;

/*Challenge 7.1 Retrieve total sales by product */
 SELECT p.Name,SUM(o.LineTotal) AS TotalRevenue
 FROM SalesLT.SalesOrderDetail AS o
 JOIN SalesLT.Product AS p
     ON o.ProductID = p.ProductID
 GROUP BY p.Name
 ORDER BY TotalRevenue DESC;

/*Challenge 7.2 Filter the product sales list to include only products that cost over 1,000 */
  SELECT p.Name,SUM(o.LineTotal) AS TotalRevenue
 FROM SalesLT.SalesOrderDetail AS o
 JOIN SalesLT.Product AS p
     ON o.ProductID = p.ProductID
 WHERE p.ListPrice > 1000
 GROUP BY p.Name
 ORDER BY TotalRevenue DESC;

/*Challenge 7.3 Filter the product sales groups to include only total sales over 20,000 */
  SELECT p.Name,SUM(o.LineTotal) AS TotalRevenue
 FROM SalesLT.SalesOrderDetail AS o
 JOIN SalesLT.Product AS p
     ON o.ProductID = p.ProductID
 WHERE p.ListPrice > 1000
 GROUP BY p.Name
 HAVING SUM(o.LineTotal) > 20000
 ORDER BY TotalRevenue DESC;


