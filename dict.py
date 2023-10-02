meme_dict = {
            "CRINGE": "Something very strange or embarrassing",
            "LOL": "A common response to something funny",
            }

word = input("Enter the word that you don't understand!  (All capital!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("no word in dictionary!")
