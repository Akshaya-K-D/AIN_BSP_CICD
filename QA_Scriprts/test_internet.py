import socket

def test_internet():
    try:
        socket.create_connection(("8.8.8.8", 53))
        print("✅ Internet connectivity test passed.")
    except Exception as e:
        print("❌ Internet connectivity test failed:", e)

if __name__ == "__main__":
    test_internet()