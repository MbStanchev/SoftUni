import calendar


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, year = [int(x) for x in date.split(".")]
        month_name = calendar.month_name[month]
        return cls (name, id, year, month_name, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"


# d = DVD.from_date(5, 'gosho', '12.01.1233', 5)
# print(d)