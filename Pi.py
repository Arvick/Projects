import math
def generate_pi(radius,num):
    rounding=(2*math.pi*radius)/(2*radius)
    return(round(rounding,num))





radius=int(input('enter radius: '))
length_of_pi=int(input('How many digits? '))

print(generate_pi(radius,length_of_pi))