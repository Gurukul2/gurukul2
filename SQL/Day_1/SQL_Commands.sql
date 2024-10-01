/* Display all columns of SalesLT.Product table*/
SELECT * FROM SalesLT.Product;

/* Display selected columns from SalesLT.Product table*/
SELECT Name, StandardCost, ListPrice FROM SalesLT.Product;

/* Include an expression that results in a calculated column*/
SELECT Name, ListPrice - StandardCost FROM SalesLT.Product;

/* Use a new name for the calculated column in the previous query*/
SELECT Name AS ProductName, ListPrice - StandardCost AS Markup FROM SalesLT.Product;

/* Include an expression that results in a calculated column which is the concatenation of 2 column values*/
SELECT ProductNumber, Color, Size, Color + ', ' + Size AS ProductDetails
FROM SalesLT.Product;

/* To perform operation on 2 columns with one numeric value (ProductID) and one text-based value (Name)*/
/*CAST function is to change the numeric ProductID column into a varchar (variable-length character data) value that can be 
concatenated with other text-based values.*/
 SELECT CAST(ProductID AS varchar(5)) + ': ' + Name AS ProductName
 FROM SalesLT.Product;

/*TRY_CAST is used when the numeric Size values are converted successfully to integers, but that non-numeric sizes are returned as NULL*/
SELECT Name, TRY_CAST(Size AS Integer) AS NumericSize
FROM SalesLT.Product;

/*ISNULL function replaces NULL values with the specified value*/
SELECT Name, ISNULL(TRY_CAST(Size AS Integer),0) AS NumericSize
 FROM SalesLT.Product;

 SELECT Name,Color
 FROM SalesLT.Product;
 
 /*Below query replaces the Color value “Multi” to NULL*/
 SELECT Name, NULLIF(Color, 'Multi') AS SingleColor
 FROM SalesLT.Product;

 /*CASE statement */
 SELECT Name,
     CASE
         WHEN SellEndDate IS NULL THEN 'Currently for sale'
         ELSE 'No longer available'
     END AS SalesStatus
 FROM SalesLT.Product;
 
  SELECT Name,
     CASE Size
         WHEN 'S' THEN 'Small'
         WHEN 'M' THEN 'Medium'
         WHEN 'L' THEN 'Large'
         WHEN 'XL' THEN 'Extra-Large'
         ELSE ISNULL(Size, 'n/a')
     END AS ProductSize
 FROM SalesLT.Product;

 /*ORDER BY-Sorting of column data */
SELECT Name, ListPrice FROM SalesLT.Product;
/*Sorting by column "Name" from SalesLT.Product*/
SELECT Name, ListPrice FROM SalesLT.Product ORDER BY Name;

/*Sorting by column "ListPrice" from SalesLT.Product*/
SELECT Name, ListPrice FROM SalesLT.Product ORDER BY ListPrice;

/*Sorting by column "ListPrice" in descending order from SalesLT.Product*/
SELECT Name, ListPrice FROM SalesLT.Product ORDER BY ListPrice DESC;

/*Sorting "ListPrice" in descending order and Name in ascending order from SalesLT.Product*/
SELECT Name, ListPrice FROM SalesLT.Product ORDER BY ListPrice DESC, Name ASC;

/*Restrict results using TOP-to return a specific number of rows*/

/*Query returns the first twenty products in descending order of ListPrice*/
SELECT TOP (20) Name, ListPrice FROM SalesLT.Product ORDER BY ListPrice DESC;

/*This time, there are 21 rows in the results, because there are multiple products that share the same price, 
one of which wasn’t included when ties were ignored by the previous query*/
SELECT TOP (20) WITH TIES Name, ListPrice FROM SalesLT.Product ORDER BY ListPrice DESC;

/*Query results contain the 20% most expensive products*/
SELECT TOP (20) PERCENT WITH TIES Name, ListPrice FROM SalesLT.Product ORDER BY ListPrice DESC;

/*Includes the color of each product in the table*/
SELECT ALL Color FROM SalesLT.Product;

/*Remove duplicate values for the column color in the table*/
SELECT DISTINCT Color FROM SalesLT.Product;

/*Apply filtering criteria using WHERE clause of a query*/
SELECT Name, Color, Size FROM SalesLT.Product WHERE ProductModelID = 6 ORDER BY Name;

/*Returns data not equal to ProductModelID 6*/
SELECT Name, Color, Size FROM SalesLT.Product WHERE ProductModelID <> 6 ORDER BY Name;

/*Returns data where ListPrice > 1000 in the table*/
SELECT Name, ListPrice FROM SalesLT.Product WHERE ListPrice > 1000.00 ORDER BY ListPrice;

/*LIKE operator enables you to match string patterns. 
The % character in the predicate is a wildcard for one or more characters, so the query returns all rows where the Name is HL Road Frame followed by 
any string*/
SELECT Name, ListPrice FROM SalesLT.Product WHERE Name LIKE 'HL Road Frame %';

/*Results include products with a ProductNumber that matches patterns similar to FR-xNNx-NN (in which x is a letter and N is a numeral)*/
SELECT Name, ListPrice FROM SalesLT.Product WHERE ProductNumber LIKE 'FR-_[0-9][0-9]_-[0-9][0-9]';

/*BETWEEN operator is to define a filter based on values within a defined range*/
SELECT Name
FROM SalesLT.Product
WHERE SellEndDate BETWEEN '2006/1/1' AND '2006/12/31';

/*Following query retrieves products with a ProductCategoryID value that is in a specified list*/
SELECT ProductCategoryID, Name, ListPrice FROM SalesLT.Product WHERE ProductCategoryID IN (5,6,7);

/* AND/OR operator*/
SELECT ProductCategoryID, Name, ListPrice, SellEndDate
FROM SalesLT.Product
WHERE ProductCategoryID IN (5,6,7) AND SellEndDate IS NULL;

SELECT Name, ProductCategoryID, ProductNumber
FROM SalesLT.Product
WHERE ProductNumber LIKE 'FR%' OR ProductCategoryID IN (5,6,7);



