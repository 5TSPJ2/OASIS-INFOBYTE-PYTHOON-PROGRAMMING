#TASK - 2 (OASIS INFOBYTE INTERNSHIP)
#BMI - body mass index
height = float(input("Enter your height in Centemeters:"))
weight = float(input("Enter your weight in kg:"))

height = height/100
BMI= weight/(height*height)

print("Your body mass index is:",BMI)

if(BMI>0):
    if(BMI<=16):
        print(" you are severly underweight")
    elif(BMI<=18.5):
        print("you are underweight")
    elif(BMI<=25):
        print("you are healthy")
    elif(BMI<=30):
        print("you over weight")
    else:
        print("you are obessed")


else:
    print("Enter valid details.....")
    
