# Write a program which receives a text and a string of banned words, separated by a comma and space ", ".
# All words included in the ban list should be replaced with asterisks "*", equal to the word's length.
# The ban list will be entered on the first input line and the text - on the second input line.

banned = input().split(", ")
text = input()
for word in banned:
    while word in text:
        text = text.replace(word, len(word) * "*")

print(text)
