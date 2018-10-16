from Xlib.display import Display
from Xlib import X, XK
import os
import subprocess

double_border = True

dpy = Display()

# ascend window
dpy.screen().root.grab_key(dpy.keysym_to_keycode(XK.string_to_keysym("A")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
# kill window
dpy.screen().root.grab_key(dpy.keysym_to_keycode(XK.string_to_keysym("Q")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)
# draw terminal
dpy.screen().root.grab_key(dpy.keysym_to_keycode(XK.string_to_keysym("Z")), X.Mod4Mask, 1, X.GrabModeAsync, X.GrabModeAsync)

# drag window
dpy.screen().root.grab_button(1, X.Mod1Mask, 1, X.ButtonPressMask|X.ButtonReleaseMask|X.PointerMotionMask,X.GrabModeAsync, X.GrabModeAsync, X.NONE, X.NONE)
# resize window
dpy.screen().root.grab_button(3, X.Mod1Mask, 1, X.ButtonPressMask|X.ButtonReleaseMask|X.PointerMotionMask,X.GrabModeAsync, X.GrabModeAsync, X.NONE, X.NONE)

startbutton = None
startkey = None
while 1:
	ev = dpy.next_event()

	############################################### key events
	if ev.type == X.KeyPress:
		# key down
		startkey = ev
		keycode = startkey.detail
		print("key down", keycode)
		if ev.child != X.NONE:
			#ascend
			if keycode == 38:
				startkey.child.configure(stack_mode = X.Above)
			#kill
			elif keycode == 24:
				startkey.child.destroy()
		#draw
		if keycode == 52:
			script_path = os.path.dirname(os.path.realpath(__file__)) + '/draw_term'
			subprocess.call(script_path)
			if double_border:
				subprocess.call("sleep 0.2; chwb -s 8 -c 0xafafaf $(lsw)", shell=True)
				subprocess.call("chwb2 -i 1 -o 9 -I 424365 -O $(xrdb -query | head -n 2 | tail -n 1 | cut -c 16-) $(lsw)", shell=True)
	if ev.type == X.KeyRelease:
		#key up
		print("key up")
		startkey = None

	############################################### button events
	if ev.type == X.ButtonPress and ev.child != X.NONE:
		# button down
		print("button down")
		attr = ev.child.get_geometry()
		startbutton = ev
	if startbutton:
		#dpy.screen().root.fill_rectangle(startbutton.child.create_gc(display=dpy), 10, 10, 300, 20)
		# window moving
		print('move')
		xdiff = ev.root_x - startbutton.root_x
		ydiff = ev.root_y - startbutton.root_y
		startbutton.child.configure(
			x = attr.x + (startbutton.detail == 1 and xdiff or 0),
			y = attr.y + (startbutton.detail == 1 and ydiff or 0),
			width = max(1, attr.width + (startbutton.detail == 3 and xdiff or 0)),
			height = max(1, attr.height + (startbutton.detail == 3 and ydiff or 0)))
	if ev.type == X.ButtonRelease:
		#button up
		print("button up")
		startbutton = None

