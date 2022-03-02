class Car:
    def __init__(self, year_model, make, speed): #create car object
        self.__year_model = year_model 
        self.__make = make
        self.__speed = speed
    def accelerate(self,speed): # accelerate method
        self.__speed += 5 
    def brake(self,speed): # break method
        self.__speed -= 5
    def get_speed(self): # return speed
        return self.__speed

def main():
    modelYear = int(input("Enter your model year: ")) # car attributes
    make = input("Enter your make : ") 
    speed = float(input("Enter your speed: "))
    userCar = Car(modelYear,make,speed)
    for i in range(0,5): # for loop to increase speed
        userCar.accelerate(speed)
        print("The car is going ", userCar.get_speed(), " miles per hour.")
    print("\n")
    for i in range(0,5): # for loop to decrease speed
        userCar.brake(speed)
        print("The car is going ", userCar.get_speed(), " miles per hour.")
               
main() # run driver
