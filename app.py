# NexaShop Web Application - Main Module

def get_product(product_id):
    """Retrieve a product from the catalogue"""
    products = {
        1: {"name": "Laptop", "price": 999.99},
        2: {"name": "Phone", "price": 499.99},
        3: {"name": "Tablet", "price": 299.99}
    }
    return products.get(product_id, None)

def calculate_total(items):
    """Calculate order total"""
    return sum(item["price"] for item in items)

if __name__ == "__main__":
    print("NexaShop Application Running")
    print(get_product(1))
