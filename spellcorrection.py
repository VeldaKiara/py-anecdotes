from textblob import TextBlob

def change_string(string):
    list_items = list(string.split())
    return list_items
user_txt = input("Enter your word: ")
words = change_string(user_txt) 
corrected_words = [ ]
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words: ", words)
print("Corrected Words are: ")
for i in corrected_words:
    print(i.correct(), end="")