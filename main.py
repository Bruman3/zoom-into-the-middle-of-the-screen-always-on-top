import pyautogui
import cv2
import numpy as np
#By bru_man3

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 300, 250)

while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot(region=(920,360, 150,150))

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Optional: Display the recording screen
    cv2.imshow('Live', frame)
    
    #keeps screen on top
    cv2.setWindowProperty( "Live", cv2.WND_PROP_TOPMOST, 1)
    
    # Stop this by pressing q
    if cv2.waitKey(1) == ord('q'):
        break


# Destroy all windows
cv2.destroyAllWindows()
