# My Setup
I'm using this application on a Windows 10 tablet, with a USB ELM327 OBD-II reader. Bluetooth OBD-II readers are not tested. This application should be able to run on any platform supported by Kivy (python GUI framework), but will likely require changes to do so. There's also a good chance you'll have to fiddle with Prolific USB-to-Serial drivers to get the ELM327 device to work - many of the cheap cables contain counterfeit chips which are ignored by the newest drivers that get loaded automatically by Windows. 

## Specific Hardware
[Asus Windows 10 Tablet/2-in-1 T101HA](https://www.asus.com/ca-en/2-in-1-PCs/ASUS-Transformer-Book-T101HA/)  
[USB ELM327 OBD-II Code Reader](https://www.ebay.ca/sch/i.html?_odkw=elm327+USB+OBD2+Scan&_osacat=0&_from=R40&_trksid=m570.l1313&_nkw=elm327+USB+OBD2+Scan+-bluetooth&_sacat=0)  
[Magic Mount XL](https://www.amazon.ca/SCOSCHE-magicMOUNT-Headrest-Magnetic-Smartphones/dp/B00XPRQRGG/ref=sr_1_1)


# Installing Dependencies
## Required 
1. [Python 3 for Windows](https://www.python.org/downloads/)  
2. install python modules below
```sh
python -m pip install --upgrade pip wheel setuptools
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy
python -m pip install obd
```
## Optional (skip 'em)
```sh
python -m pip install kivy.deps.gstreamer
python -m pip install kivy_examples
```

# User Guide
![alt text](https://github.com/dabell-cc/NavODO/blob/master/NavODO_UserGuide.png "User Guide Image")


## Contributers
- David Bell
- Alex Thorburn

## Testers
- Scott Wood
