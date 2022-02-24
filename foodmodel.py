class Food:
  '''
    define food details received from the API.
  '''
  def __init__(self, food_name, brand_name, serving_qty, serving_unit, serving_weight_grams, nf_calories, nf_total_fat, nf_saturated_fat, nf_cholesterol, nf_sodium, nf_total_carbohydrates, nf_dietary_fiber, nf_sugars, nf_proteins, nf_potassium, photo, meal_type):
    self.food_name = food_name
    self.brand_name = brand_name
    self.serving_qty = serving_qty
    self.serving_unit = serving_unit
    self.serving_weight_grams = serving_weight_grams
    self.nf_calories = nf_calories
    self.nf_total_fat = nf_total_fat
    self.nf_saturated_fat = nf_saturated_fat
    self.nf_cholesterol = nf_cholesterol
    self.nf_sodium = nf_sodium
    self.nf_total_carbohydrates = nf_total_carbohydrates
    self.nf_dietary_fiber = nf_dietary_fiber
    self.nf_sugars = nf_sugars
    self.nf_proteins = nf_proteins
    self.nf_potassium = nf_potassium
    self.photo = photo
    self.meal_type = meal_type
