import cv2

image = cv2.imread('flag.png')
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(image)

print(data)

