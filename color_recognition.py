import cv2
import pandas as pd

# Load color data
csv_path = 'colors.csv'
colors_df = pd.read_csv(csv_path, names=["color", "hex", "R", "G", "B"], header=1)

# Read image
img = cv2.imread('sample_image.jpg') 
img = cv2.resize(img, (800, 600))

clicked = False
r = g = b = xpos = ypos = 0

def get_color_name(R, G, B):
    minimum = float('inf')
    closest_color = "Unknown"
    for i in range(len(colors_df)):
        r_db = int(colors_df.loc[i, "R"])
        g_db = int(colors_df.loc[i, "G"])
        b_db = int(colors_df.loc[i, "B"])
        d = ((R - r_db) ** 2 + (G - g_db) ** 2 + (B - b_db) ** 2) ** 0.5  # Euclidean Distance
        if d < minimum:
            minimum = d
            closest_color = colors_df.loc[i, "color"]
    return closest_color


def draw_function(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('Color Recognition App')
cv2.setMouseCallback('Color Recognition App', draw_function)

while True:
    cv2.imshow("Color Recognition App", img)
    if clicked:
        # Draw rectangle and text
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        text = f"{get_color_name(r, g, b)} R={r} G={g} B={b}"
        color = (255, 255, 255) if r+g+b <= 400 else (0, 0, 0)
        cv2.putText(img, text, (50, 50), 2, 0.8, color, 2, cv2.LINE_AA)
        clicked = False

    if cv2.waitKey(20) & 0xFF == 27:  # Press Esc to exit
        break

cv2.destroyAllWindows()
