import cv2
import numpy as np
import mss
import pyautogui
import win32gui

debug = False

#template

bluearrow = cv2.cvtColor(cv2.imread('templates/bluearrow.png'), cv2.COLOR_BGR2GRAY)
redarrow = cv2.cvtColor(cv2.imread('templates/redarrow.png'), cv2.COLOR_BGR2GRAY)
greenarrow = cv2.cvtColor(cv2.imread('templates/greenarrow.png'), cv2.COLOR_BGR2GRAY)
yellowarrow = cv2.cvtColor(cv2.imread('templates/yellowarrow.png'), cv2.COLOR_BGR2GRAY)
purplecircle = cv2.cvtColor(cv2.imread('templates/purplecircle.png'), cv2.COLOR_BGR2GRAY)


# settings
Action_key = 'z'
Left_key = 'a'
Right_key = 'd'
Up_key = 'w'
Down_key = 's'

# template to key

ttk = [
    Down_key,
    Up_key,
    Right_key,
    Left_key,
    Action_key
]

def main():
    with mss.mss() as sct:
        monitor_n = 1
        mon = sct.monitors[monitor_n]

        monitor = {
            "top": mon["top"] + 503,  # 100px from the top
            "left": mon["left"] + 752,  # 100px from the left
            "width": 74,
            "height": 66,
            "mon": monitor_n,
        }
        while (True):
            sct_img = sct.grab(monitor)
            # save image
            if debug:
                cv2.imshow("OpenCV/Numpy normal", np.array(sct_img))
                cv2.waitKey(1)

            pixel1 = sct_img.pixel(41, 0)
            pixel2 = sct_img.pixel(42, 63)
            pixel3 = sct_img.pixel(0, 33)
            pixel4 = sct_img.pixel(73, 32)

            if (pixel1 == (251,251,251) or pixel2 == (248,248,248) or pixel3 == (250,250,250) or pixel4 == (249,249,249)):
                match_template(sct_img)                
            else:

                if debug:
                    print("not ingame")
                press_key(Action_key)

def match_template(img):
    img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    count = 0
    for each in [bluearrow, redarrow, greenarrow, yellowarrow, purplecircle]:
        res = cv2.matchTemplate(img, each, cv2.TM_CCOEFF_NORMED)
        threshold = 0.9
        loc = np.where(res >= threshold)
        if len(loc[0]) > 0:
            press_key(ttk[count])
            break
        count += 1

def press_key(key):
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
    if debug:
        print("pressed " + key)

def move_window(hwnd, ctx):
    if win32gui.IsWindowVisible( hwnd ):
        if win32gui.GetWindowText(hwnd) == 'HoloCure':
            win32gui.MoveWindow(hwnd, 0, 0, 0, 0, True)
            # set window to foreground
            win32gui.SetForegroundWindow(hwnd)            

if __name__ == "__main__":
    win32gui.EnumWindows(move_window, None)
    main()
