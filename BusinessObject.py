class Customer:

    def __init__(self, customer_id=None, customer_name=None, contact_name=None, address=None, city=None, postal_code=None, country=None):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.contact_name = contact_name
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.country = country

    def fetch_data(self, row):
        self.customer_id = row[0]
        self.customer_name = row[1]
        self.contact_name = row[2]
        self.address = row[3]
        self.city = row[4]
        self.postal_code = row[5]
        self.country = row[6]

    def to_json(self):
        return {
            'customer_id': self.customer_id,
            'customer_name': self.customer_name,
            'contact_name': self.contact_name,
            'address': self.address,
            'postal_code': self.postal_code,
            'country': self.country,
            'city': self.city
        }