import os

def test_usb():
    usb_path = "/dev/bus/usb"
    if os.path.exists(usb_path):
        print("✅ USB devices directory found.")
    else:
        print("❌ USB devices directory not found.")

if __name__ == "__main__":
    test_usb()