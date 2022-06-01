from cgitb import text
from turtle import width
from breezypythongui import EasyFrame
class sum(EasyFrame):

    def add(self):
            sum=0.0
            num1=self.num1.getNumber()
            num2=self.num2.getNumber()
            sum=num1+num2
            self.sumfield.setNumber(sum)

    def __init__(self):
        number1=""
        number2=""
        sum=""
        EasyFrame.__init__(self,width=500,height=300,title="Sum")
        self.setBackground("black")
        self.addLabel(text="Enter the 1st Number",row=1,column=0)
        self.num1=self.addFloatField(number1,row=2,column=1)
        self.addLabel(text="Enter the 2nd number",row=2,column=0)
        self.num2=self.addFloatField(number2,row=1,column=1)
        self.addButton(text="Compute Sum",row=3,column=0,columnspan=1,command=self.add)
        self.addLabel(text="The sum of the numbers is:",row=4,column=0,columnspan=2)
        self.sumfield=self.addFloatField(sum,row=4,column=1)

def main():
    sum().mainloop()
if __name__ == "__main__":
    main()

