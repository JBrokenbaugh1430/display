def stutter(word):
	
    first_two = word[0:2]
    first_two += "... "
   
    
    return first_two + first_two + word + "?" 

word = input("Type a word to stutter\n")
print(stutter(word))
