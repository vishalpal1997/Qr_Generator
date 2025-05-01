import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog
import qrcode
import re
import os
import sys

def resize_bg_image(event):
    global bg_photo, background_label
    
    # Get the updated window size
    window_width = event.width
    window_height = event.height
    
    # Calculate the aspect ratio of the image
    image_width, image_height = bg_image.size
    aspect_ratio = image_width / image_height
    
    # Calculate the new size of the image while maintaining aspect ratio
    if (window_width / window_height) > aspect_ratio:
        new_width = window_width
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = window_height
        new_width = int(new_height * aspect_ratio)
    
    # Resize the image
    # resized_bg_image = bg_image.resize((new_width, new_height), Image.ANTIALIAS)
    # bg_photo = ImageTk.PhotoImage(resized_bg_image)
    
    # Update the image on the background label
    background_label.configure(image=bg_photo)

def generate_qr():
    """Generates QR code based on user input and displays it."""
    name = name_entry.get()
    student_id = student_id_entry.get()
    phone = phone_entry.get()
    email_id = email_id_entry.get()
    location = location_entry.get()
    branch = branch_entry.get()
    message = message_entry.get()

    # Basic data validation (check if all fields are filled)
    if not all([name, student_id, email_id, phone]):
        messagebox.showerror("Error", "Please fill in all required fields (name, student ID, email, phone)")
        return
    
    if not re.match(r'^[a-zA-Z\s]+$', name):
        messagebox.showerror("Error", "Please enter a valid name!")
        return

    # Validate phone number format
    phone_pattern = re.compile(r'^[0-9]\d{9}$')  # Indian phone number format
    if not phone_pattern.match(phone):
        messagebox.showerror("Error", "Please enter a valid phone number!")
        return

    # Validate email ID format
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{3,}$')
    if not email_pattern.match(email_id):
        messagebox.showerror("Error", "Please enter a valid email address!")
        return

    # Concatenate information
    data = f"Name: {name}, Employee ID: {student_id}, Phone: {phone}, Email ID: {email_id}, Location: {location}, Department: {branch}, Message: {message}"

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=qr_size.get(), border=5)
    qr.add_data(data)
    qr.make(fit=True)

    # Generate QR code image
    img = qr.make_image(fill_color="red", back_color="white")

    # Get the path to the directory containing the script
    script_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

    # Construct the full path to the 'vishall.png' file
    file_path = os.path.join(script_dir, 'vishal.png')

    # Load the 'vishall.png' file
    logo = Image.open(file_path)

    logo_size = 85  # Adjust size as needed
    img.paste(logo.resize((logo_size, logo_size), Image.LANCZOS), ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2))

    # Convert QR code to a tkinter image
    qr_image = ImageTk.PhotoImage(img)
    qr_label.config(image=qr_image)
    qr_label.image = qr_image  # Keep a reference to avoid garbage collection

    # Store the generated QR image
    global generated_qr_image
    generated_qr_image = img

def save_qr():
    """Saves the generated QR code image to a chosen file."""
    if 'generated_qr_image' not in globals():
        messagebox.showerror("Error", "Please generate a QR code first!")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
    if file_path:
        generated_qr_image.save(file_path)
        messagebox.showinfo("Success", "QR code saved successfully!")

def clear_all():
    """Clears all entry fields."""
    name_entry.delete(0, tk.END)
    student_id_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_id_entry.delete(0, tk.END)
    location_entry.delete(0, tk.END)
    branch_entry.delete(0, tk.END)
    message_entry.delete(0, tk.END)
    qr_label.config(image="")  # Clear the QR code image

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Load the image using PIL
bg_image = Image.open("vishal.jpg")  # Replace "background_image1.jpg" with your image file
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a Label widget to display the image
background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover the entire window

# Bind the resize function to the window resize event
root.bind("<Configure>", resize_bg_image)

# Set the window size
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Labels
font = ("Arial", 14)
tk.Label(root, text="Name:",fg="blue",font=font).place(x=70, y=50)
tk.Label(root, text="Employee ID:",fg="blue",font=font).place(x=70, y=80)
tk.Label(root, text="Phone:",fg="blue",font=font).place(x=70, y=110)
tk.Label(root, text="Email ID:",fg="blue",font=font).place(x=70, y=140)
tk.Label(root, text="Location:",fg="blue",font=font).place(x=70, y=170)
tk.Label(root, text="Department:",fg="blue",font=font).place(x=70, y=200)
tk.Label(root, text="Message:",fg="blue",font=font).place(x=70, y=230)

# Entry fields
name_entry = tk.Entry(root,bd=3)
name_entry.place(x=200, y=50)
student_id_entry = tk.Entry(root,bd=3)
student_id_entry.place(x=200, y=80)
phone_entry = tk.Entry(root,bd=3)
phone_entry.place(x=200, y=110)
email_id_entry = tk.Entry(root,bd=3)
email_id_entry.place(x=200, y=140)
location_entry = tk.Entry(root,bd=3)
location_entry.place(x=200, y=170)
branch_entry = tk.Entry(root,bd=3)
branch_entry.place(x=200, y=200)
message_entry = tk.Entry(root,bd=3)
message_entry.place(x=200, y=230)

# QR Code Size Option
qr_size = tk.IntVar(value=10)  # Default size
size_label = tk.Label(root,fg="blue", text="QR Code Size:",font=font)
size_label.place(x=50, y=270)
size_radio_small = tk.Radiobutton(root, text="Small",fg="blue",font=font, variable=qr_size, value=5)
size_radio_small.place(x=250, y=270)
size_radio_medium = tk.Radiobutton(root, text="Medium",fg="blue",font=font, variable=qr_size, value=10)
size_radio_medium.place(x=350, y=270)
size_radio_large = tk.Radiobutton(root, text="Large",fg="blue",font=font, variable=qr_size, value=15)
size_radio_large.place(x=460, y=270)

# Buttons
def on_enter(e, button):
    button.config(bg="lightblue")

# Function to revert back to the original color
def on_leave(e, button):
    button.config(bg="SystemButtonFace")  # Default button color

# Create the main window
# root = tk.Tk()
# root.title("QR Generator")
# root.geometry("400x400")

# Set the font for buttons
font = ("Arial", 14)

# Create the buttons with hover effect
generate_button = tk.Button(root, text="Generate QR", fg="blue", font=font, command=generate_qr)
generate_button.place(x=190, y=310)
generate_button.bind("<Enter>", lambda e, button=generate_button: on_enter(e, button))
generate_button.bind("<Leave>", lambda e, button=generate_button: on_leave(e, button))

clear_button = tk.Button(root, text="Clear", fg="blue", font=font, command=clear_all)
clear_button.place(x=150, y=350)
clear_button.bind("<Enter>", lambda e, button=clear_button: on_enter(e, button))
clear_button.bind("<Leave>", lambda e, button=clear_button: on_leave(e, button))

save_button = tk.Button(root, text="Save QR", fg="blue", font=font, command=save_qr)
save_button.place(x=250, y=350)
save_button.bind("<Enter>", lambda e, button=save_button: on_enter(e, button))
save_button.bind("<Leave>", lambda e, button=save_button: on_leave(e, button))

# QR code display
qr_label = tk.Label(root)
qr_label.place(x=400, y=50)

# Run the Tkinter event loop
root.mainloop()
