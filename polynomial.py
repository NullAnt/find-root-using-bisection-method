class Polynomial():
    def __init__(self, degree:int) -> None:
        self.degree : int= degree
        self.coefficient = []
        for i in range(self.degree,-1,-1):
            self.coefficient.insert(0,int(input(f"Enter coefficient of X to the power {i}:")))
    
    def get_degree(self):
        return self.degree

    def get_coefficient_of(self,power):
        return self.coefficient[power]

        
    def show_equation(self):
        for i in range(self.degree,-1,-1):
            #print(i)
            #to do: if negative make the sign negative
            #       if power 0 write coefficient only

            if self.coefficient[i] >= 0:
                print(" + ", end="")
            else:
                print(" - ",end="")

            print(f"{abs(self.coefficient[i])}X^{i}", end="")
            if i==0:
                return
            
            