import streamlit as st
import numpy as np
import cv2
from PIL import Image
import pytesseract

# Tesseract location (uncomment if you need this path on Windows)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title("Document Scanner Application")

# Select document type
doc_type = st.selectbox(
    "Select Document Type",
    [
        "Egyptian National ID",
        "Egyptian Passport",
        "US Passport",
        "Business Card",
        "Other"
    ]
)

# Select language
language_choice = st.selectbox(
    "Select Document Language",
    ["Arabic", "English", "Arabic + English"]
)

# Map language to Tesseract codes
if language_choice == "Arabic":
    ocr_lang = "ara"
elif language_choice == "English":
    ocr_lang = "eng"
else:
    ocr_lang = "ara+eng"

# Default config
custom_config = "--psm 6"

# Override config if scanning Egyptian ID (digits only)
if doc_type == "Egyptian National ID":
    # Whitelist Arabic-Indic digits
    custom_config = "--psm 7 -c tessedit_char_whitelist=٠١٢٣٤٥٦٧٨٩"

# Sliders for preprocessing
threshold_value = st.slider("Threshold Value (0 = off)", 0, 255, 0)
blur_value = st.slider("Gaussian Blur Kernel Size (odd numbers only)", 1, 15, 1)
resize_factor = st.slider("Resize Factor", 1, 3, 1)

# File uploader
upload = st.file_uploader("Please upload an image", type=["jpg", "png", "webp"])

if upload is not None:
    img_pil = Image.open(upload)

    # Convert to OpenCV format
    img_cv = np.array(img_pil)
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)

    # Convert to grayscale
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

    # Optional blur
    if blur_value > 1:
        gray = cv2.GaussianBlur(gray, (blur_value, blur_value), 0)

    # Optional threshold
    if threshold_value > 0:
        _, gray = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

    # Optional resize
    if resize_factor > 1:
        gray = cv2.resize(
            gray,
            None,
            fx=resize_factor,
            fy=resize_factor,
            interpolation=cv2.INTER_CUBIC
        )

    # Show processed image
    st.image(gray, caption="Processed Image")

    # Crop logic if needed
    # Example: Cropping region for MRZ
    if doc_type == "US Passport":
        # For demo purposes, just using the lower 20% of the image as a "fake MRZ crop"
        h, w = gray.shape
        cropped_img = gray[int(h*0.8):, :]
        st.image(cropped_img, caption="Cropped MRZ Region")

        text = pytesseract.image_to_string(
            cropped_img,
            lang=ocr_lang,
            config=custom_config
        )
    else:
        # No cropping
        text = pytesseract.image_to_string(
            gray,
            lang=ocr_lang,
            config=custom_config
        )

    # Display OCR result
    text_list = text.splitlines()
    st.write("### OCR Text Output")
    st.write(text_list)
