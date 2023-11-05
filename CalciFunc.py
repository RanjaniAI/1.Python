class MathsFunc():
    def OddEven():  
        number=int(input("Enter a number:"))
        if((number%2)==0):
            print(number," Even number")
        else:
            print(number," Odd number")
        
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