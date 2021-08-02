#summary of the basics

def sentence_maker(phrase):
    interrogative = ("how", "what","why")
    capitalize_phrase = phrase.capitalize()
    if phrase.startswith(interrogative):
        return "{}?".format(capitalize_phrase)
    else:
        return "{}.".format(capitalize_phrase)

results = []
while True:
    user_input = input("Say something:")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))



