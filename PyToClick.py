import keyboard
import mouse
import time

isLeftClicking = False
isRightClicking = False

print("Hello! It's the 'PyToClick'!")
print("Press F6 + L for activating / deactivating left mouse button.")
print("Press F6 + N for activating / deactivating right mouse button.")

def set_right_clicker():
	global isRightClicking
	if isRightClicking:
		isRightClicking = False
		print('Right mouse button autoclicker deactivated')
	else:
		isRightClicking = True
		print('Right mouse button autoclicker activated')
def set_left_clicker():
	global isLeftClicking
	if isLeftClicking:
		isLeftClicking = False
		print('Left mouse button autoclicker deactivated')
	else:
		isLeftClicking = True
		print('Left mouse button autoclicker activated')

keyboard.add_hotkey('F6 + R', set_right_clicker)
keyboard.add_hotkey('F6 + L', set_left_clicker)

while True:
	if isRightClicking:
		mouse.double_click(button = 'right')
		time.sleep(0.01)
	elif isLeftClicking:
		mouse.double_click(button = 'left')
		time.sleep(0.01)