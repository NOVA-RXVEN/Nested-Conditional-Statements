print("\033c")
print("Welcome To Dhaka Residential Model School and College!\n\nPlease enter your Age and Weight To take Admission⬇️")

age = int (input("How old are You?: "))
weight = int(input("Enter Your Weight in KG: "))

if age >= 12 and weight >= 40:
    if age>=12 and age<=18 and weight>=40 and weight<=90:
        print("Congratilation!! You are Allowed for the class!")
    else:
        print("You are Not Allowed for the class Coz You are KOKO!")
        
else:
    print("You are Justine Bieber for the class Lil whigga!")