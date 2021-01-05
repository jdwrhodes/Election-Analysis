x = "one"

print("Hello")

someString = "hello"

type(someString)


myAge = 3


myName = "Joshua Rhodes"
myAge = 31
myBDay = "08/13/1989"
#%%
myx = 1

myIntroduction = f"""

My name is {myName} and I am {myAge} years old. 
My birthday is {myBDay}."""


# %%

# %%


#Lists

someList = [1,2,3,4,5,6]

# %%
someList[2]
# %%
someList[:2]
# %%

# %%

for i in someList:
    print(i)
    

# %%
myDictionary = {

    "myName" : myName,
    "myAge" : myAge,
}
#%%
print(myDictionary)
# %%
for key,value in myDictionary.items():
    print(f"The type for the key: {key} is {type(value)}")
# %%
