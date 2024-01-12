import cv2

image_path = 'raw_generated_3.png'
image = cv2.imread(image_path)

# Check if the image is successfully loaded
if image is None:
    print(f"Error: Unable to load the image from {image_path}")
    print("Make sure the file path is correct and the image file is valid.")
    exit()

# Specify the desired window size (adjust as needed)
window_size = (800, 600)

# Resize the image to fit within the specified window size
height, width, _ = image.shape
if width > window_size[0] or height > window_size[1]:
    scale = min(window_size[0] / width, window_size[1] / height)
    image = cv2.resize(image, (int(width * scale), int(height * scale)))


roi_corners, cropping = [], False

# Mouse callback function
def click_and_crop(event, x, y, flags, param):
    global roi_corners, cropping, image
    if event == 1: 
        roi_corners, cropping = [(x, y)], True
    elif event == 4: 
        roi_corners.append((x, y))
        if cropping:
            # Create a copy of the image to draw the rectangle on
            img_copy = image.copy()
            cv2.rectangle(img_copy, roi_corners[0], roi_corners[1], (0, 255, 0), 2)
            cv2.imshow('Image', img_copy)

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', click_and_crop)

while True:
    cv2.imshow('Image', image)
    key = cv2.waitKey(1) & 0xFF
    if key in [ord('c'), ord('q')]: break

if len(roi_corners) == 2 and cropping:
    cropped_image = image[roi_corners[0][1]:roi_corners[1][1], roi_corners[0][0]:roi_corners[1][0]]
    cv2.imwrite('asset_5.png', cropped_image)
    print('Image cropped and saved as "cropped.png"')
else:
    print('Please select a valid region before pressing "c"')

# Close all OpenCV windows
cv2.destroyAllWindows()
