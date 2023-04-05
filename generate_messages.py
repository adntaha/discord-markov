import markovify

with open("data/model.json") as f:
    print("Fetching saved Markov chain...")
    text_model = markovify.NewlineText.from_json(f.read())
    text_model = text_model.compile()

def generate_messages(count):
    print("Generating sentences...")
    for _ in range(count):
        sentence = text_model.make_sentence()
        if sentence:
            yield sentence
        else:
            count += 1

def main():
    while True:
        try:
            count = int(input("How many messages do you want to generate? "))
        except Exception:
            count = 1

        for message in generate_messages(count):
            print(">", message)

if __name__ == "__main__":
    main()
