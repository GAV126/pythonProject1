central_angle_1=160
radius=30
sector_area_1 = central_angle_1 / 360 * 3.14 *radius ** 2
print("Area is:" + str(sector_area_1))
print(f"Area is:{ sector_area_1 }")

print('------------------------------------------------------')
# define a function. The code inside is not run in the function.
# It is when calling the function, the code inside will be run

def calculate_sector_1():
    central_angle_1 = 160
    radius = 30
    sector_area_1 = central_angle_1 / 360 * 3.14 * (radius ** 2)
    print("Area is:" + str(sector_area_1))
calculate_sector_1()

print('------------------------------------------------------')

# no return
def calculate_sector(central_angle, radius):
    sector_area = central_angle / 360 * 3.14 * (radius **2)
    print(f"Function Area is {sector_area}")
calculate_sector(160,30)

print('------------------------------------------------------')

# return give you the opportunity to use the value inside a function
# BMI function practice

def calculate_bmi(weight,height):
    BMI = weight / (height **2)
# output should use string
    if BMI<=18.5:
        category = 'Shou'
    elif 18.5<BMI<=25:
        category = 'Normal'
    elif 25<BMI<=30:
        category = 'fat'
    else:
        category = 'Too fat'
    print(f"you BMI is:{BMI:.2f}") # 2 decimal
    print(f"you BMI category is : {category}")
    return BMI

calculate_bmi(88,1.78)

print('------------------------------------------------------')
