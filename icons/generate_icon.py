import wx.tools.img2py as img2py
import os

# Iterate through all the png files in the icons directory
# and generate the icon file
# The icon file is generated in the src directory to be used in the application
append = False
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.png'):
            # Generate the icon file
            img2py.img2py(os.path.join(root, file), '../src/icons.py', append=append, imgName=file[:-4].lower(), icon=True, catalog=True, compressed=True)
            append = True
