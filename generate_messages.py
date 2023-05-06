import readline
import markovify

input_history = []

with open("data/model.json", encoding="utf-8") as f:
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
            count = input("How many messages do you want to generate? ")
            input_history.append(count)
            count = int(count)
        except Exception:
            count = 1

        for message in generate_messages(count):
            print(">", message)

if __name__ == "__main__":
    readline.set_history_length(100)
    readline.set_completer(lambda: input_history[-1])
    main()
