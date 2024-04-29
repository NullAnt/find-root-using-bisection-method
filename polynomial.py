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
    
    def solve_for(self,x:float):
        ans = 0
        for i in range(self.degree,-1,-1):
            ans += self.coefficient[i]*(x**i)
        return ans

        
    def show_equation(self):
        for i in range(self.degree,-1,-1):
            #print(i)
            
            if self.coefficient[i] >= 0:
                print(" + ", end="")
            else:
                print(" - ",end="")

            print(f"{abs(self.coefficient[i])}X^{i}", end="")
            if i==0:
                return
            
            