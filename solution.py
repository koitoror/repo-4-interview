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


    a = set()
    for input_word in input_words:
        for words in english_Words:
            if words in input_word and input_word[len(words):] in english_Words:
                a.add(input_word)
    return list(a)

    # if input_word in english_Words:
    #     return False 
    # j = 0 
    # count = 0 
    # for i in range(1,len(input_word)+1):
    #     words= input_word[j:i]
    #     if words in english_Words:
    #         count +=1
    #         j = i
    # return True if count>1 else False

def checkCompound(EnglishWords_dict,input_word):
  if input_word in EnglishWords_dict:
    return False # easy win is single word
  else:
    j = 0 #index of the words
    count = 0 #count single words in compound word
    for i in range(1,len(input_word)+1):
      w_ = input_word[j:i]
      if w_ in EnglishWords_dict:
        count +=1
        j = i
    return True if count>1 else False


englishWords_dict =  {a:1 for a in english_Words} # transform in dict
# print (englishWords_dict)
out_put = []
for w in input_words:
  out_put.append(w) if checkCompound(englishWords_dict,w) else None
  
print(out_put)
print(compound_words(english_Words, input_words))

