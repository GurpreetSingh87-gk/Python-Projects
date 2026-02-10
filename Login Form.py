# GUI Login Form:-
# ---------------

'''
import customtkinter 
import tkinter as tk
from customtkinter import CTkImage
from PIL import Image, ImageTk
import webbrowser

# Main GUI Window:-
# ---------------

root = customtkinter.CTk()
root.title("Custom Login Form")
root.geometry("600x600")
customtkinter.set_appearance_mode("light")
#root.resizable(False, False)

# =================================================================================================

# Card Frame Background:-
# ---------------------

Card_frame = customtkinter.CTkFrame(
    root,
    width=390,
    height=550,
    fg_color="white"
)
Card_frame.pack(pady=40)
Card_frame.grid_propagate(False)

# =================================================================================================

# Login Form Title:-
# ----------------

login_label = customtkinter.CTkLabel(
    Card_frame,
    text="Login Form",
    font=("Segoe UI", 25, "bold")
)
login_label.place(x=130, y=20)

# =================================================================================================

# Username Label:-
# ---------------

username_label = customtkinter.CTkLabel(
    Card_frame,
    text="Username",
    font=("Segoe UI", 20)
)
username_label.place(x=70, y=90)

# Username Image:-
# --------------

username_image = customtkinter.CTkImage(
    light_image=Image.open(r"C:\Users\HARMEET KAUR\Downloads\icons8-username-60.png"),
    size=(30,30)
)

# Username Image Placement:-
# ------------------------

username_icon = customtkinter.CTkLabel(
    Card_frame,
    text="",
    image=username_image
)
username_icon.place(x=20, y=90)


# Username Entry widget:-
# ---------------------

username_entry = customtkinter.CTkEntry(
    Card_frame,
    placeholder_text="Username or Email",
    font=("Segoe UI", 15),
    corner_radius=20,
    width=350,
    height=40
)
username_entry.place(x=20, y=140)

# =================================================================================================

# Password Label:-
# ---------------

password_label = customtkinter.CTkLabel(
    Card_frame,
    text="Password",
    font=("Segoe UI", 20)
)
password_label.place(x=70, y=210)

# Password Image:-
# --------------

password_image = customtkinter.CTkImage(
    light_image=Image.open(r"C:\Users\HARMEET KAUR\Downloads\icons8-password-60.png"),
    size=(30,30)
)

# Password Image Placement:-
# ------------------------

password_icon = customtkinter.CTkLabel(
    Card_frame,
    text="",
    image=password_image
)
password_icon.place(x=20, y=210)


# Password Entry Widget:-
# ---------------------

password_ent = customtkinter.CTkEntry(
    Card_frame,
    placeholder_text="Enter your Password",
    show="*",
    font=("Segoe UI", 15),
    corner_radius=20,
    width=350,
    height=40
)    
password_ent.place(x=20, y=260)


# =================================================================================================

# Send Button:-
# -----------

my_button = customtkinter.CTkButton(
    Card_frame,
    text="Send",
    font=("Segoe UI", 16, "bold"),
    fg_color="#2196F3",
    corner_radius=20,
    width=160,
)
my_button.place(x=100, y=330)

# =================================================================================================

# Don't have an account label:-
# --------------------------

not_label = customtkinter.CTkLabel(
    Card_frame,
    text="Don't have an account?",
    font=("Segoe UI", 15)
)
not_label.place(x=20, y=370)

# =================================================================================================

# Sign Up Link Function:-
# ---------------------

def open_signup(event=None):
    print("Sign up clicked")

def on_enter(event):
    signup_label.configure(text_color="red")
    
def on_leave(event):
    signup_label.configure(text_color="#2196F3")

# ================================================================================================

# Button Function:-
# ---------------

def on_event(event):
    my_button.configure(fg_color="#6fc276")

def on_out(event):
     my_button.configure(fg_color="#2196F3")

    
signup_label = customtkinter.CTkLabel(
    Card_frame,
    text="Sign up",
    font=("Arial", 16 ,"underline"),
    text_color="#2196F3",
    cursor="hand2"
)
signup_label.place(x=20, y=400)

# Hovering Button Color:-
# ---------------------

signup_label.bind("<Button-1>", open_signup)

signup_label.bind("<Enter>", on_enter)

signup_label.bind("<Leave>", on_leave)

my_button.bind("<Enter>", on_event)

my_button.bind("<Leave>", on_out)

# =================================================================================================

# Open Links:-
# ----------

def open_facebook():
    webbrowser.open("https://www.facebook.com/login")

def open_google():
    webbrowser.open("https://accounts.google.com")

def open_youtube():
    webbrowser.open("http://youtube.com")

# =================================================================================================

# Icons Frame:-
# -----------

icons_frame = customtkinter.CTkFrame(Card_frame, fg_color="transparent")
icons_frame.place(x=30, y=450)

# =================================================================================================

# Load Images:-
# -----------

fb_img = customtkinter.CTkImage(
    Image.open(r"C:\Users\HARMEET KAUR\Downloads\facebook.png"),
    size=(38, 38)
)

google_img = customtkinter.CTkImage(
    Image.open(r"C:\Users\HARMEET KAUR\Downloads\google.png"),
    size=(35, 35)
)

youtube_img = customtkinter.CTkImage(
    Image.open(r"C:\Users\HARMEET KAUR\Downloads\youtube.png"),
    size=(38, 38)
)

# =================================================================================================

# Icon Buttons:-
# ------------

# FacebookL:-

customtkinter.CTkButton(
    icons_frame,
    image=fb_img,
    text="",
    width=50,
    height=50,
    corner_radius=25,
    fg_color="white",
    hover_color="#f2f2f2",
    command=open_facebook
).pack(side="left", padx=10)

# Google:-

customtkinter.CTkButton(
    icons_frame,
    image=google_img,
    text="",
    width=50,
    height=50,
    corner_radius=25,
    fg_color="white",
    hover_color="#f2f2f2",
    command=open_google
).pack(side="left", padx=12)

# YouTube:-

customtkinter.CTkButton(
    icons_frame,
    image=youtube_img,
    text="",
    width=50,
    height=50,
    corner_radius=25,
    fg_color="white",
    hover_color="#f2f2f2",
    command=open_youtube
).pack(side="left", padx=12)

root.mainloop()
print(root)
'''


























