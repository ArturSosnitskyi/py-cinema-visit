from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str) -> object:
    # Створення екземплярів класів
    cleaner = Cleaner(name= cleaner)
    cinema_bar = CinemaBar()

    for customer_info in customers:
        name = customer_info["name"]
        food = customer_info["food"]
        customer = Customer(name=name, food=food)
        cinema_bar.sell_product(product=food, customer=customer)

    for customer_info in customers:
        name = customer_info["name"]
        customer = Customer(name=name, food=None)
        customer.watch_movie(movie=movie)

    cleaner.clean_hall(hall_number=hall_number)


if __name__ == "__main__":
    customers = [
        {"name": "Bob", "food": "Coca-cola"},
        {"name": "Alex", "food": "popcorn"}
    ]
    hall_number = 5
    cleaner_name = "Anna"
    movie = "Madagascar"
    cinema_visit(customers=customers, hall_number=5, cleaner="Anna", movie="Madagascar")