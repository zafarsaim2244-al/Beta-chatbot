# 🤖 AI Beta-chatbot 

An AI-powered desktop chatbot built with **Python**, **CustomTkinter**, and the **Google Gemini API**. The application provides a modern graphical interface similar to ChatGPT, allowing users to interact with an AI assistant and save multiple chat sessions.

---

## 📌 Features

- Modern GUI built using CustomTkinter
- Google Gemini AI integration
- ChatGPT-style sidebar
- Create multiple chat sessions
- Save chat history in JSON files
- Load previous conversations
- Scrollable chat interface
- Dark mode user interface
- Send messages using the Enter key or the Send button

---

## 📂 Project Structure

AI_ChatBot/
│
├── main.py              # Starts the application
├── gui.py               # GUI implementation
├── chatbot.py           # Gemini API communication
├── history.py           # Chat history management
├── config.py            # API key configuration
│
├── chats/
│   ├── chat_1.json
│   ├── chat_2.json
│   └── ...
│
├
│   
│   
│
└── README.md

---

## 🛠 Technologies Used

- Python 3.13+
- CustomTkinter
- Google Gemini API
- JSON
- Object-Oriented Programming (OOP)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/zafarsaim2244-al/Beta-chatbot.git
```

### 2. Move into the project folder

```bash
cd Beta-Chatbot
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install customtkinter google-genai
```

---

## 🔑 Configure the API Key

Create a file named `config.py`.

```python
GEMINI_API_KEY = "YOUR_API_KEY"
```

Replace `"YOUR_API_KEY"` with your Google Gemini API key.

---

## ▶ Running the Application

Run

```bash
python main.py
```

---

## 💬 How It Works

1. Launch the application.
2. Create a new chat.
3. Type a message.
4. The message is sent to the Google Gemini API.
5. The AI response is displayed.
6. Messages are saved automatically.
7. Previous chats can be reopened from the sidebar.

---


## 🚀 Future Improvements

- Voice input
- Voice output (Text-to-Speech)
- Image generation
- File upload support
- Markdown rendering
- Code syntax highlighting
- Light/Dark theme switch
- Export chats to PDF
- Search chat history
- Rename/Delete chats

---

## 👨‍💻 Author

**Saim Zafar**

Bachelor of Computer Science

FAST National University

2nd Semesterv
---

## 📄 License

This project is developed for educational purposes.
