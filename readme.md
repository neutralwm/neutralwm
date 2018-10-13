# neutralwm

neutralwm is a collection of small scripts and programs which come together to make a window manager. It was made in less than a week.

# versions:

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
