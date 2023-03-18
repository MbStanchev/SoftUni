from OOP.static_andclass_methods.movieworld.project.customer import Customer


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = [dvd for dvd in self.dvds if dvd_id == dvd.id][0]
        customer = [customer for customer in self.customers if customer_id == customer.id][0]
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return "DVD is already rented"
        if dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd = [dvd for dvd in self.dvds if dvd_id == dvd.id][0]
        customer = [customer for customer in self.customers if customer_id == customer.id][0]

        if dvd in customer.rented_dvds:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)

            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = [str(c) for c in self.customers]
        result += [str(d) for d in self.dvds]
        return '\n'.join(result)