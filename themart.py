import mysql.connector

connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ammar@#$"
)

cursor = connect.cursor()
cursor.execute("DROP DATABASE IF EXISTS the_mart")
cursor.execute("CREATE DATABASE the_mart")
cursor.execute("USE the_mart")

cursor.execute("""
CREATE TABLE Customers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    city VARCHAR(50)
)
""")
cursor.execute("""
CREATE TABLE Products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,               
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
)
""")
cursor.execute("""
CREATE TABLE Orders(
    id INT AUTO_INCREMENT PRIMARY KEY,        
    customer_id INT,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES Customers(id)
)
""")
cursor.execute("""
CREATE TABLE Order_Details(
    id INT AUTO_INCREMENT PRIMARY KEY,               
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(id),
    FOREIGN KEY (product_id) REFERENCES Products(id)
)
""")
cursor.execute("""
CREATE TABLE Payments(
    id INT AUTO_INCREMENT PRIMARY KEY,               
    order_id INT,
    amount DECIMAL(10, 2) NOT NULL,
    method VARCHAR(50),
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES Orders(id)
)
""")

cursor.executemany("""
INSERT INTO Customers (name, email, phone, city) VALUES (%s, %s, %s, %s)
""",[
    ('Ammar','ammar@gmail.com','03001234567','Karachi'),
    ('Ali','ali@gmail.com','03007654321','Lahore'),
    ('Ahmed','ahmed@gmail.com','03009876543','Islamabad'),
    ('Saraq','saraq@gmail.com','03005432167','Peshawar'),
    ('Zain','zain@gmail.com','03002345678','Quetta'),
    ('Hassan','hassan@gmail.com','03006543210','Multan')
])
cursor.executemany("""
INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)
""",[
    ('Laptop', 800.00, 50),
    ('Smartphone', 500.00, 200),
    ('Tablet', 300.00, 150),
    ('Headphones', 100.00, 300),
    ('Smartwatch', 200.00, 100),
    ('Camera', 600.00, 80)
])
cursor.executemany("""
INSERT INTO Orders (Customer_id, status) VALUES (%s, %s)
""",[
    (1, 'Pending'),
    (2, 'Shipped'),
    (3, 'Delivered'),
    (4, 'Cancelled'),
    (5, 'Pending'),
    (6, 'Shipped')
])

cursor.executemany("""
INSERT INTO Order_Details (order_id, product_id, quantity) VALUES (%s, %s, %s)
""",[
    (1, 1, 1),
    (1, 4, 2),
    (2, 2, 1),
    (3, 3, 1),
    (4, 5, 1),
    (5, 6, 1),
    (6, 1, 1),
    (6, 2, 1)
])

cursor.executemany("""
INSERT INTO Payments (order_id, amount, method)
VALUES (%s, %s, %s)
""", [
    (1, 80000, "Credit Card"),
    (2, 80000, "Cash"),
    (3, 25000, "Bank Transfer"),
    (5, 15000, "Cash")
])

# SELECT QUERIES
cursor.execute("SELECT * FROM Customers")
for i in cursor.fetchall():
    print(i)

cursor.execute("SELECT * FROM Customers WHERE city='Karachi'")
for i in cursor.fetchall():
    print(i)

print("\n Select Orders with status = 'Pending'")
cursor.execute("SELECT * FROM Orders WHERE status='Pending'")
for i in cursor.fetchall():
    print(i)

print("\n Select Products with price > 500")
cursor.execute("SELECT * FROM Products WHERE price > 500")
for i in cursor.fetchall():
    print(i)

print("\n Select Payments with amount BETWEEN 20000 AND 80000")
cursor.execute("SELECT * FROM Payments WHERE amount BETWEEN 20000 AND 80000")
for i in cursor.fetchall():
    print(i)

#SORTING
print("\n Select Products ordered by price ascending")
cursor.execute("SELECT * FROM Products ORDER By price ASC")
for i in cursor.fetchall():
    print(i)

print("\n Select Customers ordered by name descending")
cursor.execute("SELECT * FROM Customers ORDER BY name DESC")
for i in cursor.fetchall():
    print(i)

print("\n Select all unique cities from Customers")
cursor.execute("SELECT DISTINCT city FROM Customers")
for i in cursor.fetchall():
    print(i)

#Aliases
print("\n Select name as Customer_Name from Customers")
cursor.execute("SELECT name AS Customer_Name FROM Customers")
for i in cursor.fetchall():
    print(i)

print("\n Select price as Product_Price from Products")
cursor.execute("SELECT price As Product_Price FROM Products")
for i in cursor.fetchall():
    print(i)

print("\n INNER JOIN: Select all orders with Customer names")
cursor.execute("""
SELECT o.id, c.name, o.order_date, o.status
FROM Orders o
INNER JOIN Customers c ON o.customer_id = c.id
""")
for i in cursor.fetchall():
    print(i)

print("\n LEFT JOIN: Select all Orders + Customer info (even if Customer missing)")
cursor.execute("""
SELECT o.id, c.name, c.email, c.phone, o.order_date, o.status
FROM Orders o 
LEFT JOIN Customers c ON o.customer_id = c.id
""")
for i in cursor.fetchall():
    print(i)

print("\n Join Orders → Order_Details → Products to get order_id, product_name, quantity")
cursor.execute("""
SELECT od.order_id, p.name, od.quantity, o.status
FROM Order_Details od
JOIN Products p ON od.product_id = p.id
JOIN Orders o ON od.order_id = o.id
""")
for i in cursor.fetchall():
    print(i)

print("\n Join Orders → Payments to get order_id, status, amount, method")
cursor.execute("""
SELECT o.id, o.status, p.amount, p.method
FROM Orders o
JOIN Payments p ON o.id = p.order_id
""")
for i in cursor.fetchall():
    print(i)

# Aggregation
print("\n Count total number of Customers")
cursor.execute("SELECT COUNT(*) FROM Customers")
for i in cursor.fetchall():
    print(i)

print("\n Count total Orders per status")
cursor.execute("SELECT status, COUNT(*) FROM Orders GROUP BY status")
for i in cursor.fetchall():
    print(i)

print("\n Sum of all Payments")
cursor.execute("SELECT SUM(amount) FROM Payments")
for i in cursor.fetchall():
    print(i)

print("\n Average price of Products")
cursor.execute("SELECT AVG(price) FROM Products")
for i in cursor.fetchall():
    print(i)

print("\n Max/Min price of Products")
cursor.execute("SELECT MAX(price), MIN(price) FROM Products")
for i in cursor.fetchall():
    print(i)

print("\n GROUP BY city → count number of customers per city")
cursor.execute("SELECT city, COUNT(*) FROM Customers GROUP BY city")
for i in cursor.fetchall():
    print(i)

print("\n GROUP BY status → sum of payments per status")
cursor.execute("SELECT o.status, SUM(p.amount) FROM Orders o JOIN Payments p ON o.id = p.order_id GROUP BY o.status")
for i in cursor.fetchall():
    print(i)

# Filtering Aggregated Data (HAVING)
print("\n GROUP BY status → sum of payments > 50000")
cursor.execute("SELECT o.status, SUM(p.amount) FROM Orders o JOIN Payments p ON o.id = p.order_id GROUP BY o.status HAVING SUM(p.amount) > 50000")
for i in cursor.fetchall():
    print(i)

# Subquery Examples
print("\n Select Customers who have Orders with status = 'Pending'")
cursor.execute("SELECT * FROM Customers WHERE id IN (SELECT customer_id FROM Orders WHERE status = 'Pending')")
for i in cursor.fetchall():
    print(i)

connect.commit()
cursor.close()
connect.close()