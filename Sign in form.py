'''
import customtkinter
from customtkinter import CTkImage
from PIL import Image
import webbrowser
from tkinter import messagebox


# Main Window:-
# -----------

root = customtkinter.CTk()
root.title("Fist GUI Window")
root.geometry("650x525")

# =================================================================================

# White Background Frame:-
# ----------------------

my_frame = customtkinter.CTkFrame(
     root,
     width=450,
     height=425,
     fg_color="white"
)
my_frame.place(x=100, y=50)

# =================================================================================

# Heading:-
# -------

my_label = customtkinter.CTkLabel(
     my_frame,
     text="Sign in",
     font=("Segoe UI", 25, "bold"),
     text_color="#2196F3"
)
my_label.place(x=186, y=20)

# ==================================================================================

# Username Image:-
# --------------

username_image = customtkinter.CTkImage(
     light_image=Image.open(r"C:\Users\HARMEET KAUR\Downloads\icons8-username-60.png"),
     size=(20,20)
)

# Username Image Placement:-
# ------------------------

username_label = customtkinter.CTkLabel(
     my_frame,
     text="",
     image=username_image
)
username_label.place(x=100, y=100)

# Username Entry Widget:-
# ---------------------

username_entry = customtkinter.CTkEntry(
     my_frame,
     placeholder_text="Username or Email",
     font=("Segoe UI", 17),
     width=280,
     height=20,
     corner_radius=20,
     border_width=0,
     fg_color="white"
)
username_entry.place(x=120, y=100)

# Frame:-
# ------

frame = customtkinter.CTkFrame(
     my_frame,
     width=250,
     height=2,
     bg_color="black",
     border_width=0
).place(x=100, y=135)

# =================================================================================

# Password Image:-
# --------------

password_image = customtkinter.CTkImage(
     light_image=Image.open(r"C:\Users\HARMEET KAUR\Downloads\icons8-password-60.png"),
     size=(20,20)
)

# Password Image Placement:-
# ------------------------

password_label = customtkinter.CTkLabel(
     my_frame,
     text="",
     image=password_image
)
password_label.place(x=100, y=160)

# Password Entry Widget:-
# ---------------------

password_entry = customtkinter.CTkEntry(
     my_frame,
     placeholder_text="Password",
     show="*",
     font=("Segoe UI", 17),
     width=280,
     height=20,
     corner_radius=20,
     border_width=0,
     fg_color="white"
)
password_entry.place(x=120, y=160)

# Frame:-
# -----

frame = customtkinter.CTkFrame(
     my_frame,
     width=250,
     height=2,
     bg_color="black",
     border_width=0
).place(x=100, y=195)

# Hide Frame:-
# ----------

hide_frame = customtkinter.CTkFrame(
     my_frame,
     fg_color="white",
     width=30,
     height=30
)
hide_frame.place(x=320, y=160)

# Hide Image:-
# -----------

hide_image = customtkinter.CTkImage(
     light_image=Image.open(r"C:\Users\HARMEET KAUR\Downloads\icons8-hide-24.png"),
     size=(18,18)
)

# Hide Function:-
# -------------

def open_hide():
     if password_entry.cget('show') == '':
          password_entry.configure(show='*')
     else:
          password_entry.configure(show='')
               
# Hide button:-
# ------------

Hide_btn = customtkinter.CTkButton(
     hide_frame,
     image=hide_image,
     text="",
     width=25,
     height=25,
     fg_color="white",
     hover_color="#f2f2f2",
     corner_radius=25,
     command=open_hide
)
Hide_btn.pack(side="right")

# =================================================================================

# Send Backend logic:-
# ------------------

def login():
     username = username_entry.get()
     password = password_entry.get()
     
     if username == "" or password == "":
          messagebox.showerror("Error","Please fill all fields!")
     else:
          messagebox.showinfo("Success","Sign in Successfully")     

# Send Button:-
# -----------

btn = customtkinter.CTkButton(
     my_frame,
     text="Sign in",
     font=("Segoe UI", 15),
     fg_color="#2196F3",
     corner_radius=20,
     width=250,
     command=login,
)
btn.place(x=100, y=230)
     
# =================================================================================

# Don't have an account label:-
# ---------------------------

title_label = customtkinter.CTkLabel(
     my_frame,
     text="Don't have an account?",
     font=("Segoe UI", 15),
)
title_label.place(x=120, y=270)

# =================================================================================

# Sign in Link:-
# ------------

def open_google():
    webbrowser.open("https://accounts.google.com")

signin_label = customtkinter.CTkButton(
     my_frame,
     text="Sign in",
     font=("Segoe UI", 15, "underline"),
     text_color="#2196F3",
     fg_color="white",
     width=10,
     corner_radius=25,
     command=open_google,
     hover_color="#f2f2f2",
)
signin_label.place(x=270, y=270)

# Sign in Function:-
# ----------------

def open_signin(event=None):
     print("Sign in clicked")
     
def on_enter(event):
     signin_label.configure(text_color="red")  

def on_leave(event):
     signin_label.configure(text_color="#2196F3")  

signin_label.bind("<Button-1>", open_signin)

signin_label.bind("<Enter>", on_enter)

signin_label.bind("<Leave>", on_leave)

# =================================================================================

# line frame:-
# ----------

line_frame = customtkinter.CTkFrame(
     my_frame,
     width=350,
     height=2,
     bg_color="#f2f2f2",
     border_width=0
)      
line_frame.place(x=50, y=330) 

# or connect with label:-
# ---------------------

text_label = customtkinter.CTkLabel(
     my_frame,
     text="or connect with",
     font=("Segoe UI", 16),
     fg_color="white"
) 
text_label.place(x=170, y=314)

# =================================================================================

# Social Media Link:-
# -----------------

def open_facebook():
    webbrowser.open("https://www.facebook.com/login")

def open_google():
    webbrowser.open("https://accounts.google.com")

def open_youtube():
    webbrowser.open("http://youtube.com")

# =================================================================================

# Icons Frame:-
# -----------

icons_frame = customtkinter.CTkFrame(
     my_frame, 
     fg_color="white",
     width=250,
     height=50,
)
icons_frame.place(x=90, y=360)

# ==================================================================================

# Load Images:-
# -----------

fb_img = customtkinter.CTkImage(
    Image.open(r"C:\Users\HARMEET KAUR\Downloads\facebook.png"),
    size=(28, 28)
)

google_img = customtkinter.CTkImage(
    Image.open(r"C:\Users\HARMEET KAUR\Downloads\google.png"),
    size=(25, 25)
)

youtube_img = customtkinter.CTkImage(
    Image.open(r"C:\Users\HARMEET KAUR\Downloads\youtube.png"),
    size=(28, 28)
)

# =================================================================================

# Icon Buttons:-
# ------------

# Facebook:-

customtkinter.CTkButton(
    icons_frame,
    image=fb_img,
    text="",
    width=40,
    height=40,
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
    width=40,
    height=40,
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
    width=40,
    height=40,
    corner_radius=25,
    fg_color="white",
    hover_color="#f2f2f2",
    command=open_youtube
).pack(side="left", padx=12)

root.mainloop()
'''
