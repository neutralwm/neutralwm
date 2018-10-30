# neutralwm

neutralwm is a collection of small scripts and programs which come together to make a window manager. It was made in less than a week.

## philosophy

- small, fast, not anymore than it needs to be.
- fixed release
- bloatless
- open to config

# versions:

## cocainewm (latest)

![screenshot](https://0x0.st/sEMj.png)

cocainewm is the second version of cocainewm. it is entirely written in python, and does not rely on sxhkd. it is much easier to install.

to install:

~~~

git clone https://github.com/torvim/neutralwm

~~~

to use:

- edit your ~/.xinitrc to read "python (clone location)"
- win + z to draw a terminal
- wix + q to quit a terminal
- wix + a to ascend a terminal
- hover over a terminal to select
- alt + right click to resize window
- alt + left to grab a window

## kebabwm

![screenshot](https://0x0.st/sghR.png)

kebabwm is the first version of neutralwm. the base wm is just a copy of tiny wm's python version, and the shortcuts are handled using sxhd. good luck.

to install:

~~~

git clone https://github.com/torvim/neutralwm
cd neutralwm/kebabwm
echo "!!! at this point, change INSTALL_LOCATION to where you have cloned kebabw !!!"
cp launch ~/.launch

~~~

to use:

- edit your ~/.xinitrc to read "bash ~/.launch"
- win + z to draw a terminal
- wix + q to quit a terminal
