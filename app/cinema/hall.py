from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str,
                      customers: list,
                      cleaning_staff: str) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer_dict in customers:
            customer = Customer(name=customer_dict["name"],
                                food=customer_dict["food"])
            Customer.watch_movie(customer, movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff = Cleaner(name=cleaning_staff)
        Cleaner.clean_hall(cleaning_staff, self.number)