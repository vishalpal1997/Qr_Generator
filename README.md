# 🧾 QR Code Generator GUI App

This is a simple **QR Code Generator** built with **Python**, using **Tkinter** for the GUI and **qrcode** and **Pillow (PIL)** for generating and customizing QR codes. The app lets users input details like name, ID, phone, email, location, department, and a custom message, then generates a QR code with an embedded logo.

---

## 📌 Features

- User-friendly graphical interface using Tkinter  
- Input validation for name, phone, and email  
- QR code generation with:
  - Custom content from form fields
  - Adjustable QR size (Small, Medium, Large)
  - Embedded image/logo at the center  
- Preview and save the generated QR code as a `.png` file  
- Background image support  
- Hover effects for buttons  

---

## 🛠️ Technologies Used

- Python 3  
- Tkinter (GUI library)  
- Pillow (`PIL`) – for image processing  
- qrcode – for generating QR codes  
- re – for input validation (regex)

---

## ▶️ How to Run

1. Make sure you have Python installed.
2. Install dependencies:
   ```bash
   pip install pillow qrcode
   ```
3. Place the required background image (`vishal.jpg`) and logo (`vishal.png`) in the same folder as the script.
4. Run the Python file:
   ```bash
   python your_script_name.py
   ```

---

## 📷 Screenshot (optional)
![App Screenshot](image.png)

## 📄 License

MIT License — feel free to use, modify, and distribute.
