import cv2
import numpy as np
import argparse

def resize_image(image, height):
    """Resize the image while maintaining aspect ratio."""
    ratio = height / image.shape[0]
    return cv2.resize(image, (int(ratio * image.shape[1]), height))

def preprocess_image(image):
    """Preprocess the image for document detection."""
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Bilateral Filter to reduce noise and preserve edges
    filtered = cv2.bilateralFilter(gray, 11, 50, 50)
    
    # Adaptive Thresholding to create binary image
    binary = cv2.adaptiveThreshold(filtered, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 4)
    
    # Median Blur to further remove noise
    blurred = cv2.medianBlur(binary, 11)
    
    # Add a black border to handle edge cases
    bordered = cv2.copyMakeBorder(blurred, 4, 4, 4, 4, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    
    return bordered

def detect_document(image):
    """Detect document corners in the preprocessed image."""
    # Detect edges using Canny edge detector
    edges = cv2.Canny(image, 200, 250)
    
    # Find contours in the edge-detected image
    _, contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    # Sort contours by area and select the largest 10
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    
    # Iterate through contours and approximate polygon
    for cnt in contours:
        perimeter = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.03 * perimeter, True)
        
        # If the contour has 4 corners, it's likely the document
        if len(approx) == 4:
            return approx.reshape(4, 2)
    
    return None

def transform_image(image, corners):
    """Transform the image to correct perspective."""
    # Define target points for perspective transformation
    height = max(np.linalg.norm(corners[0] - corners[1]), np.linalg.norm(corners[2] - corners[3]))
    width = max(np.linalg.norm(corners[1] - corners[2]), np.linalg.norm(corners[3] - corners[0]))
    target = np.array([[0, 0], [0, height], [width, height], [width, 0]], np.float32)
    
    # Calculate perspective transformation matrix
    M = cv2.getPerspectiveTransform(corners, target)
    
    # Warp the image to correct perspective
    return cv2.warpPerspective(image, M, (int(width), int(height)))

def main():
    # Construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-img", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    # Load the image
    image = cv2.imread(args['image'])
    
    # Resize the image
    image = resize_image(image, 800)
    
    # Preprocess the image
    preprocessed_image = preprocess_image(image.copy())
    
    # Detect document corners
    corners = detect_document(preprocessed_image)
    if corners is None:
        print("No document found.")
        return
    
    # Transform the image
    transformed_image = transform_image(image, corners)
    
    # Display the original and transformed images
    cv2.imshow("Original Image", image)
    cv2.imshow("Transformed Image", transformed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
