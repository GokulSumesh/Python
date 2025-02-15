import mysql.connector

class Database:
    abc = None  
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin123",
            database="gk_bakery"
        )
        if self.conn:
            print("Database connected")
            Database.abc = self.conn  
        else:
            print("Database not connected")

class Products:
    def __init__(self):
        self.conn = Database.abc 
    
    def add_products(self, name, price, quantity):
        if not self.conn:
            print("Database connection not available")
            return
        cor = self.conn.cursor(dictionary=True)
        query = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
        cor.execute(query, (name, price, quantity))
        self.conn.commit()
        print("Product added successfully!")
    
    def display_product(self):
        cor = self.conn.cursor(dictionary=True)
        cor.execute("SELECT * FROM products") 
        products = cor.fetchall()
        for product in products:
            print(product)

class Order_Table:
    def __init__(self):
        self.conn = Database.abc 
    
    def add_order(self, name, quantity):
        if not self.conn:
            print("Database connection not available")
            return
        cor = self.conn.cursor(dictionary=True)
        query = "INSERT INTO order_table (name, quantity) VALUES (%s, %s)"
        cor.execute(query, (name, quantity))
        self.conn.commit()
        print("Order table added successfully!")
    
    def display_order(self):
        cor = self.conn.cursor(dictionary=True)
        cor.execute("SELECT * FROM order_table") 
        order_table_data = cor.fetchall()  
        for order in order_table_data:
            print(order)

class Sales_Table:
    def __init__(self):
        self.conn = Database.abc 
    
    def add_sales(self, name, quantity, total_price):
        if not self.conn:
            print("Database connection not available")
            return
        cor = self.conn.cursor(dictionary=True)
        query = "INSERT INTO sales_table (name, quantity, total_price) VALUES (%s, %s, %s)"
        cor.execute(query, (name, quantity, total_price))
        self.conn.commit()
        print("Sales table added successfully!")
    
    def display_sales(self):
        cor = self.conn.cursor(dictionary=True)
        cor.execute("SELECT * FROM sales_table") 
        sales_table_data = cor.fetchall()  
        for sale in sales_table_data:
            print(sale)

class Customer_Table:
    def __init__(self):
        self.conn = Database.abc 
    
    def add_customer(self, name,phone_num,city,state):
        if not self.conn:
            print("Database connection not available")
            return
        cor = self.conn.cursor(dictionary=True)
        query = "INSERT INTO customer_table (name,phone_num,city,state) VALUES (%s, %s, %s,%s)"
        cor.execute(query, (name, phone_num,city,state))
        self.conn.commit()
        print("customer table added successfully!")
    
    def display_customer(self):
        cor = self.conn.cursor(dictionary=True)
        cor.execute("SELECT * FROM customer_table") 
        customer_table_data = cor.fetchall()  
        for customer in customer_table_data:
            print(customer)


class Payment_Table:
    def __init__(self):
        self.conn = Database.abc 
    
    def add_payment(self,payment_mode,order_id_fk):
        if not self.conn:
            print("Database connection not available")
            return
        cor = self.conn.cursor(dictionary=True)
        query = "INSERT INTO payment_table (payment_mode,order_id_fk) VALUES (%s,%s)"
        cor.execute(query, (payment_mode,order_id_fk))
        self.conn.commit()
        print("payment table added successfully!")
    
    def display_payment(self):
        cor = self.conn.cursor(dictionary=True)
        cor.execute("SELECT * FROM payment_table") 
        payment_table_data = cor.fetchall()  
        for payment in payment_table_data:
            print(payment)





data = Database()

product = Products()
product.add_products("Cake", 15.99, 10)
product.display_product()


order = Order_Table()
order.add_order("Karan", 50)
order.display_order()


sales = Sales_Table()
sales.add_sales("Cupcake", 25, 2500)
sales.display_sales()


customer = Customer_Table()
customer.add_customer("karthick",9541236875,"Tirupur","Tamil Nadu")
customer.display_customer()


payment = Payment_Table()
payment.add_payment("credit",1)
payment.display_payment()
