import time

class Calculation:
    def Addition(self, num1, num2):
        return num1 + num2
    def Subtraction(self,num1, num2):
        return num1 - num2
    def Multiplication(self,num1, num2):
        return num1 * num2
    def Division(self,num1, num2):
        return num1 / num2
    def Modulus(self,num1, num2):
        return num1 % num2
    def Exponent(self,num1, num2):
        return num1 ** num2
    def Floor(self,num1, num2):
        return num1 // num2
    
class Program:
    def __init__(self) -> None:
        self.calculation = Calculation()
        self.operators: list = [
            "Addition",
            "Subtraction",
            "Multiplication",
            "Division",
            "Modulus Division",
            "Exponent",
            "Floor Division"
            ]

        self.Main()
    
    def Main(self) -> None:
        while True:
            try:
                print("{:<10}{:<0}{:<0}".format(
                    "",
                    "Calculator!\n\n",
                    "Input 2 Non-Negative Number:"
                ))

                num1 = int(input("Num1: "))
                num2 = int(input("Num2: "))

                if num1 < 0 or num2 < 0:
                    print("Number is below 0. Try Again\n")
                    time.sleep(1)
                    continue

                print("\nSelect Operators:")
                for i in range(len(self.operators)):
                    print(f"{i + 1}. {self.operators[i]}")
                
                operator_Num: int = int(input("Enter Operator Number: "))

                if operator_Num > len(self.operators) or operator_Num < 0:
                    print("Operators Number is Out of Range. Try Again")
                    time.sleep(1)
                    continue

                if operator_Num == 1:
                    result = self.calculation.Addition(num1, num2)
                elif operator_Num == 2:
                    result = self.calculation.Subtraction(num1, num2)
                elif operator_Num == 3:
                    result = self.calculation.Multiplication(num1, num2)
                elif operator_Num == 4:

                    if num1 == 0 or num2 == 0:
                        print("Division by Zero is not Allowed. Try Again")
                        time.sleep(1)
                        continue
                    else:
                        result = self.calculation.Division(num1, num2)
                elif operator_Num == 5:
                    result = self.calculation.Modulus(num1, num2)
                elif operator_Num == 6:
                    result = self.calculation.Exponent(num1, num2)
                elif operator_Num == 7:
                    result = self.calculation.Floor(num1, num2)
                else:
                    print("Invalid Input. Try Again")
                    time.sleep(1)
                    continue
            
                print(f"\nnum1: {num1} num2: {num2} Operator: {self.operators[operator_Num - 1]}")
                print(f"Result: {result}\n")

                print("")

            except ValueError:
                print("Invalid Input. Try Again")
                time.sleep(1)
                continue



if __name__ == "__main__":
    program = Program()