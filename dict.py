meme_dict = {
            "CRINGE": "Something very strange or embarrassing",
            "LOL": "A common response to something funny",
            "ROFL": "typically used to respond for a great joke",
            "SHEESH": "used to express disbelief or exasperation",
            "CREEPY": "causing an unpleasant feeling of fear or unease",
            "AGGRO": "aggressive, violent behavior",
            }

word = input("Enter the word that you don't understand!  (All capital!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("no word in dictionary! Please add the new word in dictionary")
