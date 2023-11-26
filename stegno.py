import cv2
import os

def create_mapping():
    d = {}
    c = {}
    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)
    return d, c

def encrypt_message(img, msg):
    m, n, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    return img

def save_encrypted_image(img, filename):
    cv2.imwrite(filename, img)
    os.system(f"start {filename}")

def decrypt_message(img, password):
    message = ""
    n, m, z = 0, 0, 0
    password2 = input("Enter password for Decryption: ")
    if password == password2:
        for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("Decrypted message:", message)
    else:
        print("Not a valid password")

# Load image
img = cv2.imread("india.jpg")

# User input
msg = input("Enter the secret message: ")
password = input("Enter password: ")

# Create mapping
d, c = create_mapping()

# Encrypt message
img = encrypt_message(img, msg)

# Save encrypted image
save_encrypted_image(img, "Encrypted_msg.jpg")

# Decrypt message
decrypt_message(img, password)
