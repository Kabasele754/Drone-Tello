from djitellopy import Tello
import time

def connect_with_timeout(tello, timeout=50):
    start_time = time.time()
    while True:
        try:
            tello.connect()
            print("Tello connected successfully")
            return True
        except Exception as e:
            if time.time() - start_time > timeout:
                print(f"Error connecting to Tello: {e}")
                return False
            time.sleep(1)  # Wait a bit before retrying

def main():
    tello = Tello()
    
    if connect_with_timeout(tello):
        # Proceed with further actions
        print("Tello is ready for further commands.")
        # Add your further commands here, for example:
        # tello.takeoff()
        # tello.land()
    else:
        print("Failed to connect to Tello within the timeout period.")

if __name__ == "__main__":
    main()
