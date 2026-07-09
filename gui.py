import customtkinter as ctk
from chatbot import get_response
from history import (
    save_message,
    load_chat,
    create_new_chat,
    get_chat_files
)

# Appearance
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class ChatBotGUI:

    def __init__(self):

        
        # Main Window
      
        self.window = ctk.CTk()
        self.window.title("Beta  ChatBot")
        self.window.geometry("1200x700")

        #current chat
        self.current_chat = create_new_chat()

        history = load_chat(self.current_chat)
        for item in history:
            self.display_message(item["sender"], item["message"])

        #=============== MAIN CONTAINER======
        self.main_frame = ctk.CTkFrame(self.window, corner_radius=15)
        self.main_frame.pack(padx=20,pady=20,fill="both",expand=True)


        #==== side bar=====
        self.sidebar_frame=ctk.CTkFrame(self.main_frame,width=230,corner_radius=15)
        self.sidebar_frame.pack(side="left", fill="y", padx=10, pady=10)

        # Prevent children from resizing the sidebar
        self.sidebar_frame.pack_propagate(False)

        # ==== SIDE BAR TITLE
        self.title = ctk.CTkLabel(
            self.sidebar_frame,
            text="🤖 BETA  ChatBot",
            font=("Arial",20,"bold")
        )
        self.title.pack(pady=20)

        # new chat button
        self.new_chat_button = ctk.CTkButton(
            self.sidebar_frame,
            text="+ New Chat",
            height=40,
            command=self.new_chat
        )
        self.new_chat_button.pack(
            padx=10,
            pady=10,
            fill="x"
        )
        print("Button Created")
        


        # CHAT LIST HERE
        self.chat_list = ctk.CTkScrollableFrame(self.sidebar_frame)

        self.chat_list.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0,10)
        )
        for chat in get_chat_files():
            button = ctk.CTkButton(
                self.chat_list,
                text=chat.replace(".json", ""),
                command=lambda c=chat: self.open_chat(c)
            )

            button.pack(
                fill="x",
                pady=5
            )

            

        # Right Side FRAME
        self.chat_frame = ctk.CTkFrame(self.main_frame,corner_radius=15)
        self.chat_frame.pack(side="left", fill="both", expand=True,padx=10,pady=10)

        

# =========chat area======
        # Use CTkTextbox for a scrollable, read-only chat area
        self.chat_area = ctk.CTkTextbox(
            self.chat_frame,
            width=920,
            height=520,
            font=("Arial", 15),
            corner_radius=15
        )

        self.chat_area.pack(padx=20, pady=(20, 10))
        self.chat_area.configure(state="disabled")

        # Bottom Frame
       
        self.bottom_frame = ctk.CTkFrame(
            self.chat_frame,
            fg_color="transparent"
        )

        self.bottom_frame.pack(fill="x", padx=20, pady=10)

        # Message  entering field
    
        self.message_entry = ctk.CTkEntry(
            self.bottom_frame,
            width=650,
            height=40,
            font=("Arial", 14),
            placeholder_text="Type your message..."
        )

        self.message_entry.pack(side="left", padx=(0, 10))

        # Press Enter to Send
        self.message_entry.bind("<Return>", self.send_message)

    
        # Send Button
       
        self.send_button = ctk.CTkButton(
            self.bottom_frame,
            text="Send",
            width=90,
            command=self.send_message
        )

        self.send_button.pack(side="left", padx=5)

        
        # Clear Button
     
        self.clear_button = ctk.CTkButton(
            self.bottom_frame,
            text="Clear",
            width=90,
            command=self.clear_chat
        )

        self.clear_button.pack(side="left", padx=5)

        # Exit Button
        
        self.exit_button = ctk.CTkButton(
            self.bottom_frame,
            text="Exit",
            width=90,
            fg_color="red",
            hover_color="darkred",
            command=self.window.destroy
        )
        self.exit_button.pack(side="left", padx=5)

     


    # Display Messages
    def display_message(self, sender, message):

        self.chat_area.configure(state="normal")

        self.chat_area.insert(
            "end",
            f"{sender}: {message}\n\n"
        )

        self.chat_area.configure(state="disabled")

        self.chat_area.see("end")



    def open_chat(self, chat_file):

        self.current_chat = chat_file

        self.clear_chat()

        history = load_chat(chat_file)

        for item in history:

            self.display_message(
                item["sender"],
                item["message"]
            )

    # Send Message
    
    def send_message(self, event=None):

        message = self.message_entry.get().strip()

        if message == "":
            return

        # Showing user message
        self.display_message("You", message)
        save_message(
            self.current_chat,
            "You",
            message
        )

        # Clearing entry
        self.message_entry.delete(0, "end")

        # Ask Gemini what you wanaaa ask
        reply = get_response(message)

        # Show AI reply
        self.display_message("Beta", reply)
        save_message(
            self.current_chat,
            "Beta",
            reply
        )

    # Clear Chat
  
    def clear_chat(self):

        self.chat_area.configure(state="normal")
        self.chat_area.delete("1.0", "end")
        self.chat_area.configure(state="disabled")


    # New chat function
  
    def new_chat(self):

        self.clear_chat()

        self.current_chat = create_new_chat()

        print("New Chat:", self.current_chat)
    
    # Run function to start the gui

    def run(self):

        self.window.mainloop()