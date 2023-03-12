from OOP.static_andclass_methods.hotel_rooms.project import Animal
from OOP.static_andclass_methods.hotel_rooms.project import Lion


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        else:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = [w for w in self.workers if w.name == worker_name]
        if worker:
        # for worker in self.workers:
        #     if worker.name == worker_name:
            self.workers.remove(*worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        all_sallaries = sum(w.salary for w in self.workers)
        # for worker in self.workers:
        #     all_sallaries += worker.salary
        if self.__budget >= all_sallaries:
            self.__budget -= all_sallaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_cost = 0
        for animal in self.animals:
            animals_cost += animal.money_for_care
        if self.__budget >= animals_cost:
            self.__budget -= animals_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):

        lions = [repr(animal) for animal in self.animals if isinstance(animal, Lion)]
        tigers = [repr(animal) for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        cheetahs = [repr(animal) for animal in self.animals if animal.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals" + '\n'

        result += f'----- {len(lions)} Lions:' + '\n'
        result += "\n".join(lions) + '\n'

        result += f'----- {len(tigers)} Tigers:' + '\n'
        result += "\n".join(tigers) + '\n'

        result += f'----- {len(cheetahs)} Cheetahs:' + '\n'
        result += "\n".join(cheetahs)
        return result

    def workers_status(self):
        keepers = [repr(k) for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [repr(c) for c in self.workers if c.__class__.__name__ == "Caretaker"]
        vets = [repr(v) for v in self.workers if v.__class__.__name__ == "Vet"]

        result = f"You have {len(self.workers)} workers" + '\n'

        result += f'----- {len(keepers)} Keepers:\n' + '\n'.join(keepers) + '\n'

        result += f'----- {len(caretakers)} Caretakers:\n' + '\n'.join(caretakers) + '\n'

        result += f'----- {len(vets)} Vets:\n' + '\n'.join(vets)

        return result
