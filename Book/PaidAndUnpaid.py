def predict_paid(experience_years):
    if experience_years < 3.5:
        return "paid"
    elif experience_years < 8.5:
        return "unpaid"
    else:
        return "paid"

experience_years = int(input("Digite os anos de experência: "))
print(predict_paid(experience_years))