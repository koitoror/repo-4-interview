# Assume we have a list of words from the English dictionary, like:  

english_Words = ["water","big","apple","watch","banana","york","amsterdam","orange","macintosh","bottle","book"]

# And another long list of string to process, write a function to identify "compound words" and return them:  

input_words = ["paris","applewatch","ipod","amsterdam","bigbook","orange","waterbottle"]

 # output: ["applewatch","bigbook","waterbottle"]

# import itertools

# # result = itertools.combinations_with_replacement(english_Words, 4)

# result = set(zip(english_Words, input_words))

# for item in result:
#     if item in input_words:
#         print (item)
#     print(item)

# print(list(list(result)[0]))


def compound_words(english_Words, input_words):
     
    # return [input_word for input_word in input_words for words in english_Words if words in input_word and input_word[len(words):] in english_Words]

    wordset = set()

    for eng_word in english_Words:
      for input_word in input_words:
    # for input_word in input_words:
        # for eng_word in english_Words: 
    # for input_word in input_words:
        #       if any(eng_word in input_words for eng_word in english_Words):
        
            if eng_word in input_word and input_word[len(eng_word):] in english_Words:
            # if eng_word in input_word:
            # # if input_word in eng_word:
            #       if input_word[len(eng_word):] in english_Words:
            #           wordset.add(input_word)
            # if input_word.startswith(eng_word):
            #       if input_word.endswith(eng_word):
            #             if len(eng_word) > len(input_word):
            # if eng_word.startswith(input_word) and eng_word.endswith(input_word):
                              wordset.add(input_word)
    # print(wordset)                   
    return list(wordset)

print(compound_words(english_Words, input_words))


def checkCompound(EnglishWords_dict, input_word):
  if input_word in EnglishWords_dict: return False # easy win is single word
  # else:
  j = 0 #index of the words
  count = 0 #count single words in compound word
  for i in range(1,len(input_word)+1):
    eng_word = input_word[j:i]
    if eng_word in EnglishWords_dict:
      count +=1
      j = i
  return True if count>1 else False


englishWords_dict =  {a:1 for a in english_Words} # transform in dict
# print (englishWords_dict)
out_put = []
for inputword in input_words:
  # out_put.append(inputword) if checkCompound(englishWords_dict, inputword) else None
  if checkCompound(englishWords_dict,inputword):
        out_put.append(inputword)
  
print(out_put)

