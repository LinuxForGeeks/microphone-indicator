# Microphone AppIndicator for Ubuntu
This Appindicator allows you to see if the microphone is currently muted and also to mute or unmute it.

# Preview
![Microphone Indicator Preview](./docs/preview.gif)

# Install

The following dependencies are required:
- python3
- python3-gi
- gir1.2-gtk-3.0
- gir1.2-appindicator3-0.1
- ... (ToDo: list remaining dependencies)

To install all the dependencies on debian or derivates, run:
```bash
sudo apt install python3 python3-gi gir1.2-gtk-3.0 gir1.2-appindicator3-0.1
```

Next, open a terminal in the micindicator folder & run install script:
```bash
sudo ./install.sh
```

To uninstall run:
```bash
sudo ./uninstall.sh
```

# Update

Simply run the install script in `sudo` mode & all files should be updated.

# Changing the keyboard shortcut
To change the global keyboard shortcut used to mute / unmute the microphone change keystroke combination in `keystr` variable in `micindicator.py` script and run the application again:

```python
keystr = "<Ctrl><Alt><Shift>M"
```

# Credits 
Icon made by [Smashicons](https://www.flaticon.com/authors/smashicons) from www.flaticon.com (modified version)
