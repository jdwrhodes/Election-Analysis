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

if "o" in someString:
    print("nope")


# %%
nextList = [9,8,7,6,5,4,3,2,1]

for i in nextList:
    if i % 2 == 1:
        print(i)
    


# %%
nextList[-1:2]
# %%
nextList[::-1]
# %%
len(nextList)
# %%
nextList += [10,11,12]
print(nextList)
# %%
nextList.insert(2, 432)
print(nextList)

nextList.remove(9)
print(nextList)
# %%
cityPopDict = {}
cityPopDict["Houston"] = 4000000
print(cityPopDict["Houston"])

# %%
voting_data = []
# %%
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})

# %%
for i in voting_data:
    print(i)
# %%
# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100

if percentage_votes > 50:
    print("I received " + str(percentage_votes)+"% of the total votes.")

else:    
    print("I'm sorry, you lost.")
# %%
