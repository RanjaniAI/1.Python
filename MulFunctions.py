#print area and perimeter of triangle using class and functions
class triangle():
    def triangle():
        H=int(input("Height : "))
        B=int(input("Breadth : "))
        print("Area formula: (Height*Breadth)/2")
        area=(H*B)/2
        print("Area of Triangle: ",area)
        H1=int(input("Height1 = "))
        H2=int(input("Height2 = "))
        Br=int(input("Breadth = "))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter=H1+H2+Br
        print("Perimeter of Triangle:",perimeter)
        
class SubfieldsInAI():
    def Subfields():
        list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for temp in list:
            print(temp)
            
# Create a function that checks whether the given number is Odd or Even
class OddEven():
    def OddEven():    
        number=int(input("Enter a number:"))
        if((number%2)==0):
            print(number," is a Even number")
        else:
            print(number," is a Odd number")
            
# Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
class ElegiblityForMarriage():
    def Elegible():
        Gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(Gender=="Female"):
            if(age>=21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            if(age>=25):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")

# calculate the percentage of your 10th mark
class FindPercent():
    def percentage():
        S1=int(input("Subject1 = "))
        S2=int(input("Subject2 = "))
        S3=int(input("Subject3 = "))
        S4=int(input("Subject4 = "))
        S5=int(input("Subject5 = "))
        Total=S1+S2+S3+S4+S5
        print("Total :",Total)
        percent=(S1+S2+S3+S4+S5)/5
        print("Percentage :",percent)