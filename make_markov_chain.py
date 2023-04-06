import markovify

with open("data/messages.txt", encoding="utf-8") as f:
    print("Reading messages...")
    text = f.read()

print("Turning into a Markov chain...")
text_model = markovify.NewlineText(text, well_formed=False)

with open("data/model.json", "w") as f:
    print("Saving...")
    f.write(text_model.to_json())
