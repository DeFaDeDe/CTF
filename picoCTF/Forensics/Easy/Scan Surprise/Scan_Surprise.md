# Scan Surprise

![image.png](images/image.png)

```bash
└─$ tree
.
├── challenge.zip
└── home
    └── ctf-player
        └── drop-in
            └── flag.png

4 directories, 2 files

```

We got a QR code inside the zip

![image.png](images/image%201.png)

We can use a phone or a online site to scan it to get the flag. However we can also get the flag using a python code

```bash
import cv2

image = cv2.imread('flag.png')

detector = cv2.QRCodeDetector()

data, bbox, straight_qrcode = detector.detectAndDecode(image)

print(data)

```

In the above code:

1. Import the cv2 library which is commonly used in image manipulation
2. Read the flag.png using the `imread()` function(https://www.scaler.com/topics/cv2imread/). It will return a Numpy array representation of that image
3. Create a QRCodeDetector object(https://docs.opencv.org/3.4/de/dc3/classcv_1_1QRCodeDetector.html) using `QRCodeDetector()`
4. Use the `detectAndDecode()` method(https://docs.opencv.org/3.4/de/dc3/classcv_1_1QRCodeDetector.html#a3ae501d2e9061d6122ae59c005d05edc) in the QRCodeDetector object, which will return data, points, and the straight_qrcode

Flag: `picoCTF{p33k_@_b00_b5ce2572}`
