import cv2
import os

def image_contains_numbers(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use thresholding to isolate potential numbers (adjust the threshold as needed)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Perform contour detection
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the detected contours
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)

        # Define a threshold area for a contour to be considered as a number
        if area > 1000:  # Adjust the area threshold as needed
            # Draw a rectangle around the detected area
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #cv2.imshow('Detected Numbers', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return True

    return False

# Directory containing the images
directory = r'C:\Users\seher\Desktop\Fall 2023\CPSC599\AdobeVFR\unsupervised_data_thumb'
count=0
# Iterate through each image in the directory
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # You can add more extensions as needed
        image_path = os.path.join(directory, filename)

        if image_contains_numbers(image_path):
            #os.remove(image_path)
            print(f"Deleted: {filename} as it contains numbers.")
            count+=1

        else:
            print(f"No numbers found in {filename}.")


print(count)