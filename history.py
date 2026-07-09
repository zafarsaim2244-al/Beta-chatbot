import os
import json

CHAT_FOLDER = "chats"

# Create chats folder if it doesn't exist
if not os.path.exists(CHAT_FOLDER):
    os.makedirs(CHAT_FOLDER)


def get_chat_files():
    """
    Return all chat files.
    """

    files = []

    for file in os.listdir(CHAT_FOLDER):
        if file.endswith(".json"):
            files.append(file)

    return sorted(files)


def create_new_chat():
    """
    Create a new chat file.
    """

    chat_number = len(get_chat_files()) + 1

    filename = f"chat_{chat_number}.json"

    filepath = os.path.join(CHAT_FOLDER, filename)

    with open(filepath, "w") as file:
        json.dump([], file)

    return filename


def save_message(chat_file, sender, message):
    """
    Save one message into a chat file.
    """

    filepath = os.path.join(CHAT_FOLDER, chat_file)

    history = []

    if os.path.exists(filepath):

        with open(filepath, "r") as file:
            history = json.load(file)

    history.append({
        "sender": sender,
        "message": message
    })

    with open(filepath, "w") as file:
        json.dump(history, file, indent=4)


def load_chat(chat_file):
    """
    Load one chat.
    """

    filepath = os.path.join(CHAT_FOLDER, chat_file)

    if not os.path.exists(filepath):
        return []

    with open(filepath, "r") as file:
        return json.load(file)