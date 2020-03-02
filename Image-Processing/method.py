import cv2

# all color-space conversion methods
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

