from OOP.static_andclass_methods.gym.project.customer import Customer
from OOP.static_andclass_methods.gym.project.equipment import Equipment
from OOP.static_andclass_methods.gym.project.exercise_plan import ExercisePlan
from OOP.static_andclass_methods.gym.project.subscription import Subscription
from OOP.static_andclass_methods.gym.project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self,subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = [subscription for subscription in self.subscriptions if subscription_id == subscription.id][0]

        customer = [customer for customer in self.customers if subscription.customer_id == customer.id][0]

        trainer = [t for t in self.trainers if t.id == subscription.trainer_id][0]

        plan = [p for p in self.plans if p.id == subscription.exercise_id][0]

        equipment = [e for e in self.equipment if e.id == plan.equipment_id][0]

        return f'{subscription}\n'f"{customer}\n"f"{trainer}\n"f"{equipment}\n"f"{plan}"
