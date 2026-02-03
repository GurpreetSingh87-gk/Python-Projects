# GUI Login Form:-
# ---------------

'''
import customtkinter 
import tkinter as tk

# Main GUI Window:-
# ---------------

root = customtkinter.CTk()
root.title("Custom Login Form")
root.geometry("600x600")
customtkinter.set_appearance_mode("light")
root.resizable(False, False)

# =================================================================================================

# Login Form Title:-
# ----------------

login_label = customtkinter.CTkLabel(
    root,
    text="Login Form",
    font=("Arial", 30, "bold")
)
login_label.pack(pady=20)

# Gray Background Container:-
# -------------------------

frame = customtkinter.CTkFrame(root, width=335, height=460)
frame.pack(pady=20)
frame.grid_propagate(False)

# Username Label:-
# --------------

username_label = customtkinter.CTkLabel(
    frame,
    text="Username",
    font=("Arial", 20, "bold")
)
username_label.grid(sticky="w", padx=20, pady=10)


# Username within Frame Container:-
# ------------------------------

my_username = customtkinter.CTkEntry(
    frame,
    placeholder_text="Enter name",
    font=("Arial", 15),
    corner_radius=20,
    width=300,
    height=40
)
my_username.grid(padx=10, pady=10)

# =================================================================================================

# Password Label:-
# --------------

password_label = customtkinter.CTkLabel(
    frame,
    text="Password",
    font=("Arial", 20, "bold")
)
password_label.grid(sticky="w", padx=20, pady=10)


# Password within Frame Container:-
# -------------------------------

my_password = customtkinter.CTkEntry(
    frame,
    placeholder_text="Enter password",
    show="*",
    font=("Arial", 15),
    corner_radius=20,
    width=300,
    height=40
)    
my_password.grid(padx=10, pady=10)

# =================================================================================================

# Email Id Label:-
# --------------

email_label = customtkinter.CTkLabel(
    frame,
    text="Email Id",
    font=("Arial", 20, "bold")
)
email_label.grid(sticky="w", padx=20, pady=10)
    
# Email Id within Frame Container :-
# ------------------------------

my_email = customtkinter.CTkEntry(
    frame,
    placeholder_text="Enter email",
    font=("Arial", 15),
    corner_radius=20,
    width=300,
    height=40
)    
my_email.grid(padx=10, pady=10)

# =================================================================================================

# Send Button:-
# -----------

my_button = customtkinter.CTkButton(
    frame,
    text="Send",
    font=("Arial", 16),
    corner_radius=20,
    width=180,
)
my_button.grid(padx=10, pady=10)

# =================================================================================================

# Not a member and Sign up:-
# ------------------------

# Not a member ? label:-
# --------------------

not_label = customtkinter.CTkLabel(
    frame,
    text="Not a member ?",
    font=("Arial", 15)
)
not_label.grid(sticky="w", padx=20)


# Sign Up within Frame Container:-
# ------------------------------

def open_signup(event=None):
    print("Sign up clicked")

def on_enter(event):
    signup_label.configure(text_color="#1f6aa5")
    
def on_leave(event):
    signup_label.configure(text_color="blue")
    
signup_label = customtkinter.CTkLabel(
    frame,
    text="Sign up",
    font=("Arial", 16, "underline"),
    text_color="blue",
    cursor="hand2"
)
signup_label.grid(sticky="w", padx=20, pady=10)

signup_label.bind("<Button-1>", open_signup)

signup_label.bind("<Enter>", on_enter)

signup_label.bind("<Leave>", on_leave)

root.mainloop()
print(root)
'''











