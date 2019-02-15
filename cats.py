class Cats:
"""This is a class that creates a cat"""
    def __init__(self, name, preffered_food, meal_time):
        self.name = name
        self.meal_time = meal_time
        self.preffered_food = preffered_food

    def eats_at(self):
        if self.meal_time == 0:
            return "12 AM"
        elif self.meal_time == 12:
            return "12 PM"
        elif self.meal_time > 0 and self.meal_time < 12:
            return "{} AM".format(self.meal_time)
        elif self.meal_time > 12 and self.meal_time < 24:
            return "{} PM".format(self.meal_time- 12)

    def meow(self):
        return "My name is {} and I eat {} at {}".format(self.name, self.preffered_food, self.eats_at())

    def __str__(self):
        return "This is your cat. Their name is {}, their favourite food is {}, and they eat at {}".format(self.name, self.preffered_food, self.eats_at())

cat1 = Cats("Roscoe", "tuna", 23)
cat2 = Cats("Einstein", "tuna", 2)

print(cat1)
print(cat2)
print(cat1.meow())
print(cat2.meow())
