import random

# will generate and keep for later introspection the random parameters of the review
class PermutationGenerator:
    car = None
    unprofessional_statuses = []
    pets = None
    family = None
    choice_numerals = ["2", "3", "4"]

    choice_cars = [
        "2014 Toyota Camry",
        "2019 Ram 1500",
        "2020 Mazda Miata"
    ]
    pet_kinds = ["dogs", "cats", "pet pytons"]
    choice_pets = ["no pets"] + [f"{numeral} {pet}" for numeral in choice_numerals for pet in ["dogs", "cats", "pet pytons"]]
    choice_unprofessional_options = ["Give your address and phone number in case anyone wants to contact you. ", "Use unprofessional tone and some slurs in your review. ", "Mention your personal business by name. ", "Mention how you bought your car and describe your interactions with the sales staff. ", "Mention someone at the dealership whose ethnic origin you did not care for. ", "Mention how your car was serviced by an incompetent mechanic. ", "Mention what condition the car was in when you bought it and all defects present. "]
    choice_family = ["single"] +  [f"a single mom of {numeral}" for numeral in choice_numerals] + [f"a mother of {numeral}" for numeral in choice_numerals] + [f"a single father of {numeral}" for numeral in choice_numerals] + [ f"a father of {numeral}" for numeral in choice_numerals]
    def unprofessional_status_as_string(self) -> str:
        return ''.join(self.unprofessional_statuses)
    def generate_next(self):
        self.car = random.choice(self.choice_cars)
        self.unprofessional_statuses = random.sample(self.choice_unprofessional_options, random.choice(range(0, len(self.choice_unprofessional_options))))
        self.pets = random.choice(self.choice_pets)
        self.family = random.choice(self.choice_family)
