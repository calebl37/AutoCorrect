from segmentation import load_text
from segmentation import text_to_word_list
from difflib import SequenceMatcher

#from 0-1, how similar are a and b?
def similar(a, b):
  return SequenceMatcher(None, a, b).ratio() #returns a number between 0 and 1, 0 being no similarity and 1 being the same

#a text file with errors
bad_stuff = load_text('usertxt')

#the dictionary
good_stuff = load_text('dcttxt')

#the error prone text file as a list of words
word_list_con_errores = text_to_word_list(bad_stuff) 

#the dictionary as a list of words
word_list_sin_errores = text_to_word_list(good_stuff) 

num_errors = 0
#iterates through all the words in the user text
for i in range(0,len(word_list_con_errores)): 
  if word_list_con_errores[i] not in word_list_sin_errores: #if a word in the user text is not in the dictionary, it is a mispelling 
    word_list_con_errores[i] = "<" + word_list_con_errores[i] + ">" #singles out mispelled words
    num_errors +=1 #counts the numer of mispelled words
string = ' '
string = string.join(word_list_con_errores) 
print("\nThis paragraph has " + str(num_errors) +  " errors:\n")
print(string)
print("\nThis paragraph has been corrected:\n")
corrected_list = []
for i in word_list_con_errores: #iterates through all the words in the user text
  if i not in word_list_sin_errores: #if a word in the user text is not in the dictionary, it goes through the closest match process
    closest_ratio = 0 #no matches yet
    for j in word_list_sin_errores: #iterates through all the words in the dictionary
      if similar(i,j) > closest_ratio: #compares the mispelled word with every word in the dictionary, to see which is the closest match
        closest_ratio = similar(i,j) #stores the highest ration of simliarity
        closest_word = j #stores the closest dictionary match
    print(str(closest_ratio) + ", " + closest_word)
    i = "<" + closest_word + ">" 
    corrected_list.append(i) #replaces the mispelled words with their closest dictionary matches, in brackets
  else:
    corrected_list.append(i) #does not do anything to the words from the user text that were originally correct
print()
newstring = ' '
newstring = newstring.join(corrected_list) 
print(newstring) #prints the autocorrected text