def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Calculate BMI
    bmi = weight / (height * height)

    print("BMI =", bmi)

    # Determine BMI classification
    if bmi < 18.5:
        classification = "Under Weight"
        return -1
    elif 18.5 <= bmi <= 25.0:
        classification = "Normal Weight"
        return 0
    else:
        classification = "Over Weight"
        return 1

    print("Weight Classification =", classification)

result = calculate_bmi(weight=57, height=1.73)
if result == -1:
    print("Weight Classification: Under Weight")
elif result == 0:
    print("Weight Classification: Normal Weight")
else:
    print("Weight Classification: Over Weight")


