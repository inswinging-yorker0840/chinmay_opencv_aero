# Import libraries
import os
import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

matplotlib.rcParams['figure.figsize'] = (9.0, 9.0)

def download_and_unzip(url, save_path):
    print(f"Downloading and extracting assests....", end="")

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


URL = r"https://www.dropbox.com/s/48hboi1m4crv1tl/opencv_bootcamp_assets_NB3.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_NB3.zip")

# Download if assest ZIP does not exists. 
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)

# Read in an image
image = cv2.imread("Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

# Display the original image
#plt.imshow(image)

#adding line
'''imgcpy=image.copy()
cv2.line(imgcpy,(100,100),(400,400),(0,255,255),5,cv2.LINE_8)
plt.subplot(1,3,1)
plt.imshow(imgcpy)

#adding rectangle
imgcpy1=image.copy()
cv2.rectangle(imgcpy1,(446,59),(745,519),(0,255,255),4)
plt.subplot(1,3,2)
plt.imshow(imgcpy1[:,:,::-1])

#adding circle
imgcpy2=image.copy()
cv2.circle(imgcpy2,(250,250),100,(0,255,255),6)
plt.subplot(1,3,3)
plt.imshow(imgcpy2)'''
#putting text
imgcpy3=image.copy()
imageText = image.copy()
text = "Apollo 11 Saturn V Launch, July 16, 1969"
fontScale = 2.3
fontFace = cv2.FONT_HERSHEY_PLAIN
fontColor = (0, 255, 0)
fontThickness = 3

cv2.putText(imageText, text, (270, 700), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA);

# Display the image
plt.imshow(imageText)


plt.show()

