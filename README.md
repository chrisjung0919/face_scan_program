# 📷 Face Detection Program

This Python program detects human faces using either a **live webcam feed** or an **uploaded image**. It uses OpenCV’s Haar Cascade Classifier for face detection.

I developed this project based on a tutorial from this YouTube video:  
🔗 [YouTube Tutorial](https://www.youtube.com/watch?v=7IFhsbfby9s&list=WL&index=3&t=6s)

---

## 🚀 Features
- Detects faces in real-time using your computer's webcam.
- Can also scan and detect faces in static image files.
- Uses OpenCV's Haar cascade model for face recognition.

---

## 🛠️ Requirements
Make sure you have the following installed:
- Python 3.x
- OpenCV

You can install OpenCV using pip:
```bash
pip install opencv-python
```

---

## 📁 How to Use

**1. Run with live camera:**
```bash
python detect_face_live.py
```

**2. Run with an image file:**
```bash
python detect_face_image.py path/to/your/image.jpg
```

---

## 📌 Notes
- You may need to download the [`haarcascade_frontalface_default.xml`](https://github.com/npinto/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) file from OpenCV’s GitHub repo.
- Adjust the detection sensitivity using parameters in `detectMultiScale()` if you’re getting false positives (e.g., squares on arms or chins).

---

## ✅ To-Do / Future Improvements
- Improve face detection accuracy (limit box to upper part of the head).
- Add emotion detection using deep learning (e.g., CNN or pre-trained models like FER+).
- Deploy a basic GUI with Tkinter or Streamlit.
