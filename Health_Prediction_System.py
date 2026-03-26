# Health Prediction System
def heart_score(bmi, hr, br, age, bp, oxy):
    score = 0
    if bmi > 30:
        score += 1
    if hr > 90:
        score += 1
    if br > 20:
        score += 1
    if age > 50:
        score += 1
    if bp > 130:
        score += 1
    if oxy < 95:
        score += 1
    return score

def diabetes_score(bmi, age, bp):
    score = 0
    if bmi > 30:
        score += 1
    if age > 45:
        score += 1
    if bp > 130:
        score += 1
    return score

def lung_score(br, oxy, hr):
    score = 0
    if br > 24:
        score += 1
    if oxy < 94:
        score += 1
    if hr > 90:
        score += 1
    return score

def heart_result(score):
    if score >= 4:
        return "High Risk of Heart Disease"
    elif score >= 2:
        return "Moderate Risk of Heart Disease"
    else:
        return "Low Risk of Heart Disease"

def diabetes_result(score):
    if score >= 2:
        return "Diabetes Risk High"
    else:
        return "Diabetes Risk Low"

def lung_result(score):
    if score >= 2:
        return "Lung Disease Risk High"
    else:
        return "Lung Disease Risk Low"


def main():
    print("Health Prediction System")
    while True:
        print("\nEnter Details:")
        bmi = float(input("Enter BMI: "))
        heart = int(input("Enter Heart Rate: "))
        breath = int(input("Enter Breathing Rate: "))
        age = int(input("Enter Age: "))
        pressure = int(input("Enter Blood Pressure: "))
        oxygen = int(input("Enter Oxygen Level: "))
        # Scores
        heart_s = heart_score(bmi, heart, breath, age, pressure, oxygen)
        diabetes_s = diabetes_score(bmi, age, pressure)
        lung_s = lung_score(breath, oxygen, heart)

        # Results
        heart_r = heart_result(heart_s)
        diabetes_r = diabetes_result(diabetes_s)
        lung_r = lung_result(lung_s)

        # Output
        print("\nResults:")
        print(heart_r)
        print(diabetes_r)
        print(lung_r)

        # Save
        data = str(bmi)+","+str(heart)+","+str(breath)+","+str(age)+","+str(pressure)+","+str(oxygen)
        result = heart_r + " | " + diabetes_r + " | " + lung_r

        file = open("patients.txt", "a")
        file.write(data + " -> " + result + "\n")
        file.close()

        # Continue
        choice = input("\nCheck another? (yes/no): ")
        if choice != "yes":
            print("Program Ended")
            break

main()
