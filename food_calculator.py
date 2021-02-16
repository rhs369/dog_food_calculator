NORMAL_FOOD_PERCENT = 0.95
TREAT_PERCENT = (1 - NORMAL_FOOD_PERCENT)
LBS_TO_KG_FACTOR = 0.45359237

# Resting energy requirement factor based on life stage.
life_stage_RER_factor_dict = {
    "Puppy: 0 to 4 months": 3,
    "Puppy: 4 months to Adult": 2,
    "Intact Adult": 1.8,
    "Neutered/Spayed Adult": 1.6,
    "Active/Working Dog": 2,
    "Inactive/Obese Dog": 1
}


class FoodCalculator:
    def __init__(self, dog_weight, food_calories_per_cup, treat_calories_per_unit, life_stage):
        # Calculate the total calories based on the formula found here:
        # https://platopettreats.com/connect/dogs-daily-calorie-calculator/
        self.total_calories = (70 * (int(dog_weight) * LBS_TO_KG_FACTOR) ** (3 / 4)) * \
                              life_stage_RER_factor_dict[life_stage]

        self.food_calories, self.food_quantity = self.calculate_quantity(self, NORMAL_FOOD_PERCENT,
                                                                         int(food_calories_per_cup))
        self.treat_calories, self.treat_quantity = self.calculate_quantity(self, TREAT_PERCENT,
                                                                           int(treat_calories_per_unit))

    @staticmethod
    def calculate_quantity(self, percent, cal_per_unit):
        calories = percent * self.total_calories

        quantity = round((calories/cal_per_unit), 2)
        return calories, quantity


def main():
    """
    Run this main function if this script is called directly.
    :return: None
    """
    pass


if __name__ == "__main__":
    main()







