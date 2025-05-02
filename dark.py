import os
import base64
import time

# Show the banner from file
def show_banner():
    os.system("clear")
    with open("style/banner.txt", "r", encoding="utf-8") as f:
        print(f.read())
    print("\nCreated by: 𝑫𝑨𝑹𝑲 𝑯𝑨𝑪𝑲𝑬𝑹")
    print("Join our channel: https://t.me/+PFbp1Ayc_1I3ZTFk\n")
    time.sleep(2)

# Open Telegram channel
def open_channel():
    print("Redirecting you to our Telegram channel...")
    time.sleep(1)
    os.system("xdg-open https://t.me/+PFbp1Ayc_1I3ZTFk")

# Encrypt Python file
def encrypt_file(path):
    with open(path, "r") as f:
        code = f.read()
    encoded = base64.b64encode(code.encode()).decode()
    with open("files/encrypted.py", "w") as f:
        f.write(encoded)
    print("\nFile encrypted and saved as: files/encrypted.py")

# Decrypt Python file
def decrypt_file(path):
    with open(path, "r") as f:
        data = f.read()
    decoded = base64.b64decode(data.encode()).decode()
    with open("files/decrypted.py", "w") as f:
        f.write(decoded)
    print("\nFile decrypted and saved as: files/decrypted.py")

# Start program
show_banner()
open_channel()

print("Choose an option:\n[1] Encrypt Python file\n[2] Decrypt Python file")
choice = input(">> ")

file_path = input("Enter the file path: ")

if choice == "1":
    encrypt_file(file_path)
elif choice == "2":
    decrypt_file(file_path)
else:
    print("Invalid option.")
