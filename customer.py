class Customer:

    def __init__(self, first_name, family_name, ones_age):
        self.first_name = first_name
        self.family_name = family_name
        self.ones_age = ones_age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def age(self):
        return self.ones_age

    def entry_fee(self):
        if self.ones_age < 3:
            return 0
        if self.ones_age < 20:
            return 1000
        if 20 <= self.ones_age < 60:
            return 1500
        if 65 <= self.ones_age < 75:
            return 1200
        if 75 <= self.ones_age:
            return 500

    def info_csv(self):
        # return f"{self.full_name()},{self.age()},{self.entry_fee()}"

        # return f"{self.full_name()}\t{self.age()}\t{self.entry_fee()}"

        print(f"{self.full_name()}|{self.age()}|{self.entry_fee()}")


ken = Customer("Ken", "Tanaka", 15)
ken.info_csv()

tom = Customer("Tom", "Ford", 55)
tom.info_csv()

ieyasu = Customer("Ieyasu", "Tokugawa", 73)
ieyasu.info_csv()
