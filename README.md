# Multilingual-ID-Passport-OCR-App-Arabic-English-
An AI-powered web app to extract text from international identity documents in multiple languages.

# Multilingual ID & Passport OCR App (Arabic + English)

An interactive web app built in Python and Streamlit that extracts text from identity documents in Arabic and English. The app reads:

- Egyptian National IDs
- Egyptian Passports
- US Passports
- Business Cards
- Other scanned documents

It’s perfect for digitizing documents in multilingual environments, especially where Arabic scripts are involved.

---

## Features

✅ Multilingual OCR (Arabic, English, or both)  
✅ Document type selector for specialized processing  
✅ Adjustable image preprocessing:
- Thresholding
- Blur
- Resize

✅ Cropping for passport Machine Readable Zones (MRZ)  
✅ Interactive Streamlit interface  
✅ Works with various image types (JPG, PNG, WEBP)

---

## Screenshots

![image](https://github.com/user-attachments/assets/60533f47-30b7-490e-a26a-c9622ae08284)

![Screenshot 2025-07-01 154859](https://github.com/user-attachments/assets/7c81c256-9d20-4d2f-b10e-0b3315bff90f)

![Screenshot 2025-07-01 155109](https://github.com/user-attachments/assets/cc546549-bcfc-49ae-b0d2-973ceb0ed80b)

![Screenshot 2025-07-01 155152](https://github.com/user-attachments/assets/a707aa5e-204a-4e76-9c45-72c652b03e61)


## 🔧 Installation

First, install Python (preferably Anaconda) and Tesseract OCR:

- Download Tesseract from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)  
- On Windows, set its path like this in your Python code:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
Then install Python dependencies:


pip install streamlit opencv-python pytesseract pillow

Running the App
Run the Streamlit app locally:

streamlit run my_ocr_app.py

Deployment
You can deploy it easily on Streamlit Cloud for free.

Configuration
The app allows tuning thresholding, blur, and resizing for better OCR.

Choose specific document types for language models and cropping.

Credits
Tesseract OCR

Streamlit

Author
Ragde Heikel

Connect with me on [LinkedIn](https://www.linkedin.com/in/ragdehikel/)!



