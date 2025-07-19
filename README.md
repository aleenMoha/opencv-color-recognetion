# 🎨 Color Recognition App using OpenCV

This Python project detects and displays the name and RGB values of any color you click on in an image. It uses OpenCV for image processing and Pandas for handling a color data CSV.

---

## 🛠️ Tools & Technologies

- Python 3.9+
- OpenCV (`cv2`)
- Pandas
- Anaconda (for environment management)
- VS Code (for editing & running the code)

---

## 📁 Project Structure

ColorRecognition/
├── color_recognition.py # Main Python script
├── colors.csv # CSV file with color names and RGB values
├── sample_image.jpg # Image file to analyze
└── README.md # This documentation file


---

## 🚀 Features

- Load an image and resize it
- Click anywhere to detect color
- Shows color name and RGB values on the image
- Uses Euclidean distance to match the most accurate color
- Press `Esc` key to exit cleanly

---

🧠 How It Works
The script loads colors.csv, which contains color names and their RGB values.

The user clicks on a point in the image.

The script captures the pixel’s color at the click location.

It finds the closest matching color using Euclidean distance in RGB space.

Displays a rectangle with the detected color and its name + RGB values.

---

🙋‍♀️ Author
Aleen Moh – Computer Science Student
Project built as part of learning Artificial Intelligence and Computer Vision using OpenCV.
