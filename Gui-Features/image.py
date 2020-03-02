import cv2
from matplotlib import pyplot as plt

# Read an image
# Load a color image in grayscale
img = cv2.imread('messi.jpg',0)

# Display an image
cv2.imshow('image',img)

# keyboard binding function
k = cv2.waitKey(0)

# For a 64-bit Machine
# k = cv2.waitKey(0) & 0xFF

if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img) # Write an image
    cv2.destroyAllWindows()
    
# Using Matplotlib
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
