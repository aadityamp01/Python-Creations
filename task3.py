# Python function that takes a list of words and returns the length of the longest one

def find_longest_word(word_list):  
    longest_word = ''  
    for word in word_list:    
          print(word,len(word))  


words = input('Please enter a words separating with commas:: \n')  
word_list = words.split(',')  
find_longest_word(word_list)  
