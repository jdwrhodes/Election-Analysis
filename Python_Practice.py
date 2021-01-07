print("Hello World")

#%%

counties = ["Arapahoe", "Denver", "Jefferson"]

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
# %%
temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")
# %%
score = int(input("What is your grade?"))

if score >= 90:
    print("You got an A.")
elif score >= 80:
    print("You got a B.")
elif score >= 70:
    print("You got a C.")
elif score >= 60:
    print("you got a D.")
else:
    print("You got an F.")
# %%
numbers = [1,2,3,4,5,6]

for i in numbers:
    if i % 2 == 1:
        print(str(i) + " is an odd number.")
    else:
        print(str(i) + " is an even number.")
# %%

if 2 in numbers:
    print(2)

# %%
if 12 not in numbers:
    print(2)

# %%
numbers = 0

while numbers < 10:
    print(numbers)
    numbers += 1

# %%

numbers = [0,1,2,3,4,5,6]

for i in range(3):
    print(i)

# %%
for i in range(40):
    print(i)
# %%
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"There are {voters} in {county}!")
#%%

voting_data = [{'state': 'Texas', 'county': 'Arapahoe', 'registered_voters': 422829, }, {'state': 'Arizona', 'county': 'Denver', 'registered_voters': 463353}, {'state': 'Ohio', 'county': 'Jefferson', 'registered_voters': 432438}, {'city': 'Houston', 'registered_voters': 3400000}]


for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

print(len(voting_data))
# %%
for i in voting_data:
    print(i)

# %%
myName = input("What is your name?")
myAge = input("How old are you?")

print(f"Hi! My name is {myName} and I'm {myAge} years old")
# %%
candidate_votes = int(input("How many votes did you receive?"))
total_votes = int(input("How many votes were cast?"))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes."
)

print(message_to_candidate)
# %%
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for key, value in counties_dict.items():
    print(f"{key} county has {value:,} registered voters.")
# %%
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

#for i in voting_data:
    #print(i)

voterNumber = 0

for list in voting_data:
    for dict in list.values():
        if dict == int:
            voterNumber = dict
    print(f"{dict} county has {voterNumber:,} registered voters.")




# %%
# %%
#Assign a variable for the file to load and the path
#file_to_load = os.path.join('Resources', 'election_results.csv')


#Open the election results and read the file
#with open(file_to_load) as election_data:
    
    #Print the file object
#    print(election_data)

#%%
#desktop = os.path.join('analysis', 'election_analysis.txt')

# %%
#outfile = open(desktop, 'w')

#outfile.write("Hello World")
# %%
#outfile.close()
# %%
#with open(desktop, 'w') as txt_file:
#    txt_file.write("Countines in the Election\n--------------------\nArapahoe\nDenver\nJefferson")
# %%
