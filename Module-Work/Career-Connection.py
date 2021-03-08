#  Write a function that takes a string input: 'str'
#  Return the number / count of vowels in the input string.
#  For the purpose of this assignment, consider 'a', 'e', 'i', 'o' and 'u'
#  as vowels
#  the input string will consist of lower case letters


#%%
def count_the_vowels(str):

    vowel = 0
    for char in str:
        if char in 'aeiouAEIOU':
            vowel += 1
    return f'There are {vowel} vowels in {str}'

userWord = input('Enter your word.')

count_the_vowels(userWord)
