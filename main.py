from polynomial import Polynomial

def find_x_astrick_1(equation:Polynomial):
    return equation.get_coefficient_of(equation.get_degree-1) / equation.get_coefficient_of(equation.get_degree)

def find_x_astrick_max(equation:Polynomial):
    return pow(equation.get_coefficient_of(equation.get_degree-1),1/2)

def root_using_bisection_method(equation:Polynomial):
    find_x_astrick_1(equation)
    find_x_astrick_max(equation)



def main():
    #take input
    degree : int = int(input("Enter the degree of equation:"))
    hamro_equation = Polynomial(degree)

    hamro_answer = root_using_bisection_method(hamro_equation)

    hamro_equation.show_equation()


if __name__ == "__main__":
    main()