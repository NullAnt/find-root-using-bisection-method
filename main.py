from polynomial import Polynomial

def get_x_astrick_1(equation:Polynomial):
    return round(equation.get_coefficient_of(equation.get_degree()-1) / equation.get_coefficient_of(equation.get_degree()))

def get_x_astrick_max(equation:Polynomial):
    return round(pow(((equation.get_coefficient_of(equation.get_degree()-1)/equation.get_coefficient_of(equation.get_degree()))**2) - 2*(equation.get_coefficient_of(equation.get_degree()-2)/equation.get_coefficient_of(equation.get_degree())),1/2))

def get_root(A:float,B:float,equation:Polynomial,stopping_criteria:float=0.0001,show_table:bool=True) -> float:
    iter=1
    fA:float=equation.solve_for(A)
    fB:float=equation.solve_for(B)
    C:float=(A+B)/2
    fC:float=equation.solve_for(C)
    accuracy:float=abs((B-A)/B)

    if show_table==True:
        print("Iteration\tA\tB\tf(A)\tf(B)\tC\tf(C)\tAcc")
        print(f"{iter}\t\t{A:.4f}\t{B:.4f}\t{fA:.4f}\t{fB:.4f}\t{C:.4f}\t{fC:.4f}\t{accuracy:.4f}\t")

    while accuracy>stopping_criteria:
        iter += 1
        if fA*fC<0:
            B=C
        elif fB*fC<0:
            A=C
        fA=equation.solve_for(A)
        fB=equation.solve_for(B)
        C=(A+B)/2
        fC=equation.solve_for(C)
        accuracy=abs((B-A)/B)

        if show_table==True:
            print(f"{iter}\t\t{A:.4f}\t{B:.4f}\t{fA:.4f}\t{fB:.4f}\t{C:.4f}\t{fC:.4f}\t{accuracy:.4f}\t")

    return C
    



def root_using_bisection_method(equation:Polynomial,show_table:bool=True) -> float:
    min_range = get_x_astrick_1(equation)
    max_range = get_x_astrick_max(equation)

    #error if there cant be a table or only 1 table
    if max_range-min_range <=0:
        return 

    current_x = max_range
    got_positive = False
    got_negative = False
    positive_fx_aauni_x=0
    negative_fx_aauni_x=0

    while not (got_positive == True and got_negative == True):
        if got_positive==False and equation.solve_for(current_x)>=0:
            got_positive=True
            positive_fx_aauni_x=current_x
        elif got_negative==False and equation.solve_for(current_x)<0:
            got_negative=True
            negative_fx_aauni_x=current_x

        current_x-=1

        #error, no positive or negative fx
        if(current_x<min_range):
            print("ERROR! no positive or negative fx")
            return 
    
    return get_root(A=positive_fx_aauni_x,B=negative_fx_aauni_x,equation=equation)


def main():
    #take input
    degree : int = int(input("Enter the degree of equation:"))
    hamro_equation = Polynomial(degree)

    hamro_answer = root_using_bisection_method(hamro_equation)

    print(f"The root value is {hamro_answer:.4f}")

    print("Equation:",end="")
    hamro_equation.show_equation()


if __name__ == "__main__":
    main()