import psycopg2

from BusinessObject import Customer as CustomerEntity

class Customer:

    def __init__(self, connection_data):
        self.connection_data = connection_data

    def insert(self, customer: CustomerEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """INSERT INTO TblCustomers(CustomerName, ContactName, Address, City, PostalCode, Country)
                VALUES(%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (customer.customer_name, customer.contact_name, customer.address, customer.city, customer.postal_code, customer.country))
        conn.commit()
        return 'Insert successfully'
    
    def get_all(self):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "SELECT * FROM TblCustomers"
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        result = []
        for row in rows:
            customer = CustomerEntity()
            customer.fetch_data(row)
            result.append(customer.to_json())
        return result

    def delete(self, customer: CustomerEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = "DELETE FROM TblCustomers WHERE CustomerID = %s"
        cursor.execute(sql, (customer.customer_id, ))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Deleted successfully', 200
        return 'Id not found', 404

    def update(self, customer: CustomerEntity):
        conn = psycopg2.connect(host=self.connection_data['host'],
                                port=self.connection_data['port'],
                                user=self.connection_data['user'],
                                password=self.connection_data['password'],
                                database=self.connection_data['database'])
        cursor = conn.cursor()
        sql = """UPDATE TblCustomers SET
                    CustomerName=%s, ContactName=%s, Address=%s,
                    City=%s, PostalCode=%s, Country=%s WHERE CustomerID=%s"""
        cursor.execute(sql, (customer.customer_name, customer.contact_name, customer.address, customer.city, customer.postal_code, customer.country, customer.customer_id))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Updated successfully', 200
        return 'Id not found', 404
