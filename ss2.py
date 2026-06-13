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
URL = "https://www.dropbox.com/s/rys6f1vprily2bg/opencv_bootcamp_assets_NB2.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_NB2.zip")

# Download if assest ZIP does not exists. 
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)   

# Read image as gray scale.
img = cv2.imread("checkerboard_18x18.png", 0)

# Set color map to gray scale for proper rendering.
'''plt.imshow(img, cmap="gray")
print(img)'''

'''imgcpy=img.copy()
imgcpy[1:4,1:4]=255
plt.imshow(imgcpy, cmap="gray")
plt.show()'''

img_NZ_bgr = cv2.imread("New_Zealand_Lake.jpg", 1)
'''plt.subplot(1, 2, 1)
plt.imshow(img_NZ_bgr[:, :, ::-1])
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(img_NZ_bgr)
plt.title("BGR Image")
plt.show()

cropped_region = img_NZ_bgr[200:400, 300:600]
plt.imshow(cropped_region[:,:,::-1])
plt.show()'''

imgrez=cv2.resize(img_NZ_bgr, None, fx=3,fy=3,interpolation=cv2.INTER_CUBIC)
plt.subplot(1, 3, 1)
plt.imshow(imgrez[:,:,::-1])

imgrez=cv2.resize(img_NZ_bgr, None, fx=2,fy=2,interpolation=cv2.INTER_AREA)
plt.subplot(1, 3, 2)
plt.imshow(imgrez[:,:,::-1])

imgrez=cv2.resize(img_NZ_bgr, None, fx=2,fy=2,interpolation=cv2.INTER_NEAREST)
plt.subplot(1, 3, 3)
plt.imshow(imgrez[:,:,::-1])
plt.show()
