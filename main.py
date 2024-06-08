import cv2
import numpy as np
import pygetwindow as gw
import pyautogui
import keyboard
import os

window_position = None

def take_screenshot(window_title):
    global window_position
    try:
        window = gw.getWindowsWithTitle(window_title)[0]

        if window is not None:
            window.activate()
            window.restore()

            window_position = window.box
            screenshot = pyautogui.screenshot(region=window_position)

            return screenshot
        else:
            return None
    except Exception as e:
        return None


def find_nearest_pixel_color(image, target_color, tolerance=10, prev_loc=(0, 0)):
    if image is None:
        return None

    s = 60
    h, w, _ = image.shape

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image_rgb[max(prev_loc[0] - s, 0):min(prev_loc[0] + s, h), max(prev_loc[1] - s, 0):min(prev_loc[1] + s, w)] = 0
    lower_bound = np.array([max(0, tc - tolerance) for tc in (255, 119, 136)])
    upper_bound = np.array([min(255, tc + tolerance) for tc in (255, 119, 136)])

    mask = cv2.inRange(image_rgb, lower_bound, upper_bound)
    matching_pixels = np.where(mask)

    if matching_pixels[0].size > 0:  # red
        first_matching_pixel = (matching_pixels[1][-1], matching_pixels[0][-1])
        return first_matching_pixel

    lower_bound = np.array([max(0, tc - tolerance) for tc in (133, 222, 230)])
    upper_bound = np.array([min(255, tc + tolerance) for tc in (133, 222, 230)])

    mask = cv2.inRange(image_rgb, lower_bound, upper_bound)
    matching_pixels = np.where(mask)

    if matching_pixels[0].size > 0:  # blue
        first_matching_pixel = (matching_pixels[1][-1], matching_pixels[0][-1])
        if first_matching_pixel[1] / h > 0.75:
            return first_matching_pixel

    lower_bound = np.array([max(0, tc - tolerance) for tc in target_color])
    upper_bound = np.array([min(255, tc + tolerance) for tc in target_color])

    mask = cv2.inRange(image_rgb, lower_bound, upper_bound)
    matching_pixels = np.where(mask)

    if matching_pixels[0].size > 0:  # green
        first_matching_pixel = (matching_pixels[1][-1], matching_pixels[0][-1])
        return first_matching_pixel
    else:
        return None


def click(x, y):
    pyautogui.PAUSE = 0.001
    pyautogui.click(x, y)


def run():
    global is_running
    window_title = 'TelegramDesktop'
    locations = (0, 0)

    while not keyboard.is_pressed('e'):

        screenshot = take_screenshot(window_title)

        opencv_image = np.array(screenshot)
        opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)

        target_color = (205, 221, 0)
        locations = find_nearest_pixel_color(opencv_image, target_color, prev_loc=locations or (0, 0))
        try:
            click_x = locations[0] + window_position.left
            click_y = locations[1] + window_position.top

            click(click_x, click_y)
        except Exception as e:
            pass



if __name__ == "__main__":
   ascii = """
                         ______
 _________        .---"""      """---.
:______.-':      :  .--------------.  :
| ______  |     | : BLUM AUTOCLICKER : |
|:______B:|     | |                  | |
|:______B:|     | |  Created by :    | |
|:______B:|     | |  Faust           | |
|         |     | |  Timbyxty        | |
|:_____:  |     | |  BaldrCoal       | |
|    ==   |     | :                  : |
|       O |      :  '--------------'  :
|       o |      :'---...______...---'
|       o |-._.-i___/'             \._
|'-.____o_|   '-.   '-...______...-'  `-._
:_________:      `.____________________   `-.___.-.
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
               .'.eeeeeeeeeeeeeeeeeeeeee.'.
              :____________________________:"""
   print(ascii)
   run()
