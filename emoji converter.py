message = input(">")
words = message.split(" ")
emojis = {
    ":)": "smiley face",
    ":(": "sad face"
}
output= ""
for word in words:
    output += emojis.get(word, word) +" "
print(output)