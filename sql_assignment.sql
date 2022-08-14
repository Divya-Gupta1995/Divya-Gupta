DROP DATABASE IF EXISTS assignment_1;

CREATE DATABASE assignment_1;

USE assignment_1;

CREATE TABLE salespeople(Snum INT PRIMARY KEY ,
Sname VARCHAR(100) UNIQUE KEY,
City VARCHAR(100),
Comm INT
) ;

INSERT INTO salespeople (Snum, Sname, City, Comm)
VALUES (1001,'Peel', 'London', 12),
(1002, 'Serres', 'Sanjose', 13),
(1004, 'Motika', 'London', 11),
(1007, 'Rifkin', 'Barcelona', 15),
(1003, 'Axelrod', 'Newyork', 10);


CREATE TABLE Customers
(Cnum INT PRIMARY KEY,
Cname VARCHAR(100),
CITY VARCHAR (100) NOT NULL,
Snum INT, 
FOREIGN KEY(Snum) REFERENCES salespeople(Snum)
);

USE assignment_1;
INSERT INTO customers (Cnum, Cname, City, Snum)
VALUES
(2001,'Hoffman', 'London', 1001),
(2002, 'Giovanni' ,'Rome',1003),
(2003, 'Liu', 'Sanjose' , 1002),
(2004, 'Grass' , 'Berlin', 1002),
(2006, 'Clemens' , 'London' ,1001),
(2008, 'Cisneros' , 'Sanjose' ,1007),
(2007, 'Pereira', 'Rome' ,1004)
;

CREATE TABLE orders(
Onum INT PRIMARY KEY,
Amt FLOAT,
Odate DATE,
Cnum INT,
Snum INT,
FOREIGN KEY (Cnum) REFERENCES customers(Cnum),
FOREIGN KEY (Snum) REFERENCES salespeople(Snum)
);

USE assignment_1;

INSERT INTO orders (Onum, Amt, Odate, Cnum, Snum)
VALUES
(3001, 18.69, '1990-10-03', 2008, 1007),
(3003, 767.19, '1990-10-03', 2001, 1001),
(3002, 1900.10, '1990-10-03', 2007, 1004),
(3005, 5160.45, '1990-10-03', 2003, 1002),
(3006, 1098.16, '1990-10-03', 2008, 1007),
(3009, 1713.23, '1990-10-04', 2002, 1003),
(3007, 75.75, '1990-10-04', 2004, 1002),
(3008, 4273.00, '1990-10-05', 2006, 1001),
(3010, 1309.95, '1990-10-06', 2004, 1002),
(3011, 9891.88, '1990-10-06', 2006, 1001)
;


-- 1.  Count the number of Salesperson whose name begin with ‘a’/’A’.
SELECT count(Sname) AS COUNT
FROM salespeople
WHERE  (Sname REGEXP  '^a' OR '^A');
  

-- 2.  Display all the Salesperson whose all orders worth is more than Rs. 2000.
SELECT  SP.Sname, O.Amt
FROM salespeople SP
JOIN orders AS O ON SP.Snum= O.Snum
WHERE O.Amt>=2000.00 ;


-- 3.Count the number of Salesperson belonging to Newyork
SELECT count(Sname) AS COUNT_NEWYORK_RESIDING_SALESPEOPLE
FROM salespeople
WHERE  City='Newyork';


-- 4. Display the number of Salespeople belonging to London and belonging to Paris
SELECT count(City) AS COUNT, City
FROM salespeople
WHERE  City='London' OR City='Paris'
GROUP BY City;

-- 5.Display the number of orders taken by each Salesperson and their date of orders.
SELECT Snum, count(Onum) , Odate
FROM orders 
GROUP BY Snum;



   
   



