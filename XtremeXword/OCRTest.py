import numpy as np
import pytesseract
import pyautogui



def get_DW():
    try:
        Dwords=np.array(pyautogui.screenshot('screen1.png',region=(2609,1130, 50, 250)))
        Dword = (pytesseract.image_to_string(Dwords, config='--psm 15 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVQXYZ').replace(',',''))
        return Dword
    except ValueError:
        print("found nothing")

print(get_DW())