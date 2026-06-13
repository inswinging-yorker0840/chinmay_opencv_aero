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
URL = "https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), "opencv_bootcamp_assets_NB1.zip")

# Download if assest ZIP does not exists.
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)
# Display 84x84 pixel image.
'''Image(filename="checkerboard_84x84.jpg")
img = cv2.imread("checkerboard_84x84.jpg",0)
print(img.dtype)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#colour image
'''cl=cv2.imread("coca-cola-logo.png",1)
print(cl.shape)
plt.imshow(cl)
plt.show()'''

#reversed
'''coke_img_channels_reversed = cl[:, :, ::-1]
plt.imshow(coke_img_channels_reversed)
plt.show()'''

# Split the image into the B,G,R components
imgNZ = cv2.imread("New_Zealand_Lake.jpg", cv2.IMREAD_COLOR)
b, g, r = cv2.split(imgNZ)

# Show the channels
'''plt.figure(figsize=[20, 5])

plt.subplot(141);plt.imshow(r, cmap="gray");plt.title("Red Channel")
plt.subplot(142);plt.imshow(g, cmap="gray");plt.title("Green Channel")
plt.subplot(143);plt.imshow(b, cmap="gray");plt.title("Blue Channel")'''

# Merge the individual channels into a BGR image
imgMerged = cv2.merge((b, g, r))
# Show the merged output
'''plt.subplot(144)
plt.imshow(imgMerged[:, :, ::-1])
plt.title("Merged Output")
plt.show()'''

'''img_NZ_rgb = cv2.cvtColor(imgNZ, cv2.COLOR_BGR2HSV)
plt.imshow(img_NZ_rgb)
plt.show()'''

h_new = h + 10
img_NZ_merged = cv2.merge((h_new, s, v))
img_NZ_rgb = cv2.cvtColor(img_NZ_merged, cv2.COLOR_HSV2RGB)

# Show the channels
plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h, cmap="gray");plt.title("H Channel");
plt.subplot(142);plt.imshow(s, cmap="gray");plt.title("S Channel");
plt.subplot(143);plt.imshow(v, cmap="gray");plt.title("V Channel");
plt.subplot(144);plt.imshow(img_NZ_rgb);   plt.title("Original");