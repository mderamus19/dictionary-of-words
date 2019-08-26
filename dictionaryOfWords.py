
# Create a dictionary with key value pairs to
# represent words (key) and its definition (value)

word_definitions = dict()


# Add several more words and their definitions
#    Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"

word_definitions = {
    "assiduous" : "meticulous and diligent",
    "esurient" : "hungry",
    "rigging" : "lines of chains used in theater set design for support and movement",
    "alacrity" : "a prompt response"
}

# Use square bracket lookup to get the definition of two
# words and output them to the console with `print()`

print(word_definitions["rigging"])
print(word_definitions["esurient"])

# Loop over the dictionary to get the following output:
#     The definition of [WORD] is [DEFINITION]
#     The definition of [WORD] is [DEFINITION]
#     The definition of [WORD] is [DEFINITION]
for word, definition in word_definitions.items():
    print(f"The definition of {word} is {definition}")
