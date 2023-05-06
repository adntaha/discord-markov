from pathlib import Path
from tqdm import tqdm
import zipfile
import csv

package_path = Path("data/package.zip")

removed = [
    # put words you want excluded here
]


FOLDER_NAME = package_path.parent / package_path.stem


def extract_package():
    print("Extracting package...")
    with zipfile.ZipFile(package_path, 'r') as compressed:
        compressed.extractall(FOLDER_NAME)


def get_messages():
    result = []
    for message_csv in tqdm(FOLDER_NAME.glob("messages/**/messages.csv"), desc="Getting messages", unit="msg"):
        with open(message_csv, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                content = row["Contents"]
                if not content:
                    continue

                content = content.replace("\n", " ")
                result.append(content)
    return result


def filter_messages(messages):
    result = []
    for message in tqdm(messages, desc="Filtering messages", total=len(messages), unit="msg"):
        if message is None or any(x in message for x in removed):
            continue
        result.append(message)
    return result


def write_messages(messages):
    with open("data/messages.txt", "w", encoding="utf-8") as file:
        for message in tqdm(messages, desc="Writing messages", total=len(messages), unit="msg"):
            file.write(message + "\n")


def main():
    if not FOLDER_NAME.exists():
        extract_package()
    messages = get_messages()
    filtered = filter_messages(messages)
    write_messages(filtered)


if __name__ == "__main__":
    main()
