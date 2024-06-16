# aplikasi emoji converter

emoji_mapping = {
    ":)": "😀",
    ":D": "😀",
    ":|": "😐",
}

message = input(">>> ")

words = message.split(" ")

output = ""
for word in words:
    output = output + emoji_mapping.get(word, word) + " "

print(output)
