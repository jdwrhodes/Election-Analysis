
#%%

class NewCar():
    def __init__(self, year, make, model, color):
        self.userYear = year
        self.userMake = make
        self.userModel = model
        self.userColor = color
    
    def printMyCar(self):
        print(f'You have a {self.userYear} {self.userMake} {self.userModel} that is {self.userColor}!.')

#%%
userCar = NewCar(input("What year is your car?"), input("What is the make?"), input("What is the model?"), input("What color is it?"))
#%%
print(userCar)
userCar.printMyCar()

#%%

print(userCar.userColor)


#%%

someList = [0,1,2,3,4,5,6,7,8,9]

#%%
def calculateMean(someList):
    numberOfElemnents = 0
    sumOfElements = 0
    for number in someList:
        sumOfElements = sumOfElements + number
        numberOfElemnents = numberOfElemnents + 1
    return sumOfElements/numberOfElemnents
# %%
class Animal():

    def __init__(self, somethingElse):
        self.animalType = somethingElse

    def printAnimalType(self):
        print(self.animalType)

#%%
myPet = Animal("cat")
dog = Animal("dog")


# %%
dog.animalType
# %%
class Mammal(Animal):

    def __init__(self, animalType):
        self.animalType = animalType
        self.warmBlooded = True
        self.hasFur = True

    def isHuman(self):
        if self.hasFur:
            return False
        else:
            return True

#%%
human = Mammal('homo sapien')

human.isHuman()

# %%
class Human():
    def __init__(self, height):
        self.myHeight = height
#%%
me = Human(100)

# %%
print(me.myHeight)
# %%
 