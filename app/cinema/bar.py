
class Customer:
    def __init__(self,name):
        self.name = name

class CinemaBar:
    @staticmethod
    def sell_product(product, customer):
        return f" Cinema bar sold {product} to {customer}"

# Приклад використання:
if __name__ == "__main__":
    customer = Customer("John")
    CinemaBar.sell_product("Popcorn", customer)