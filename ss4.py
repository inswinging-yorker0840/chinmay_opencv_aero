import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image

def download_and_unzip(url, save_path):
    print("Downloading and extracting assests....", end="")

    # Downloading zip file using urllib package.
    urlretrieve(url, save_path)
    
    try:
        # Extracting zip file using the zipfile package.
        with ZipFile(save_path) as z:
            # Extract ZIP file contents in the same directory.
            z.extractall(os.path.split(save_path)[0])

        print("Done")

    except Exception as e:
        print("\nInvalid file.", e)

URL = "https://www.dropbox.com/s/0oe92zziik5mwhf/opencv_bootcamp_assets_NB4.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), "opencv_bootcamp_assets_NB4.zip")

if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path) 

img_bgr = cv2.imread("New_Zealand_Coast.jpg", cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

Image(filename="New_Zealand_Coast.jpg")

'''matrix = np.ones(img_rgb.shape, dtype="uint8") * 50
img_rgb_brighter = cv2.add(img_rgb, matrix)
img_rgb_darker   = cv2.subtract(img_rgb, matrix)

# Show the images
plt.figure(figsize=[15, 5])
plt.subplot(131); plt.imshow(img_rgb_darker);  plt.title("Darker");
plt.subplot(132); plt.imshow(img_rgb);         plt.title("Original");
plt.subplot(133); plt.imshow(img_rgb_brighter);plt.title("Brighter");'''

'''matrix1 = np.ones(img_rgb.shape) * 0.8
matrix2 = np.ones(img_rgb.shape) * 1.2

img_rgb_darker   = np.uint8(cv2.multiply(np.float64(img_rgb), matrix1))#convert to float64 to avoid overflow
#multiply the image with a matrix of 0.8 to reduce the contrast
#convert back to uint8 to display the image
img_rgb_brighter = np.uint8(np.clip(cv2.multiply(np.float64(img_rgb), matrix2), 0, 255))#stop changing colour due to overflow by clipping the values between 0 and 255

# Show the images
plt.figure(figsize=[18,5])
plt.subplot(131); plt.imshow(img_rgb_darker);  plt.title("Lower Contrast");
plt.subplot(132); plt.imshow(img_rgb);         plt.title("Original");
plt.subplot(133); plt.imshow(img_rgb_brighter);plt.title("Higher Contrast");
plt.show()'''

# Read the original image
'''img_read = cv2.imread("Piano_Sheet_Music.png", cv2.IMREAD_GRAYSCALE)

# Perform global thresholding
retval, img_thresh_gbl_1 = cv2.threshold(img_read, 50, 255, cv2.THRESH_BINARY)

# Perform global thresholding
retval, img_thresh_gbl_2 = cv2.threshold(img_read, 130, 255, cv2.THRESH_BINARY)

# Perform adaptive thresholding
img_thresh_adp = cv2.adaptiveThreshold(img_read, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,7 )
img_thresh_adp1 = cv2.adaptiveThreshold(img_read, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17,9)'''


# Show the images
'''plt.figure(figsize=[18,15])
plt.subplot(231); plt.imshow(img_read,        cmap="gray");  plt.title("Original");
plt.subplot(232); plt.imshow(img_thresh_gbl_1,cmap="gray");  plt.title("Thresholded (global: 50)");
plt.subplot(233); plt.imshow(img_thresh_gbl_2,cmap="gray");  plt.title("Thresholded (global: 130)");
plt.subplot(234); plt.imshow(img_thresh_adp,  cmap="gray");  plt.title("Thresholded (adaptive)");
plt.subplot(235); plt.imshow(img_thresh_adp1, cmap="gray");  plt.title("Thresholded (adaptive, mean)");
plt.show()'''


apple = cv2.imread(
    r"C:\Users\User\Downloads\apple.jpg",
    cv2.IMREAD_GRAYSCALE
)
ball=cv2.imread(
    r"C:\Users\User\Downloads\ball.jpg",
    cv2.IMREAD_COLOR
)
print(apple.shape)
print(ball.shape)

width=ball.shape[1]
height=ball.shape[0]
apple_resized=cv2.resize(apple,(width,height),interpolation=cv2.INTER_LINEAR)
result = cv2.bitwise_and(ball, ball, mask=apple_resized)
plt.imshow(result[:,:,::-1])
plt.show()