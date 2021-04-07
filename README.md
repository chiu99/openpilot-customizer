# openpilot-customizer
Simple script to add your car [fingerprints](https://github.com/commaai/openpilot/wiki/Fingerprinting) and small tunings after every openpilot release.
## What this script will do
It is written in python and will replace certain strings in openpilot.
* Change Toyota Corolla Hybrid TSS2 fingerprints, in this example, to Lexus UX250h 2020 Taiwan. Edit **tune.py** to fulfill your need.
* Tuning Toyota Corolla Hybrid TSS2 by the wheelbase, steerRatio, tire_stiffness_factor and mass, in this example, of Lexus UX250h. Edit **tune.py** to fulfill your need.
* Disable camera logger
* Disable data uploader
* Change auto power off timer to 30 minutes offroad
* Update LastUpdateTime (to get rid of Internet connection warning)
## How to use
[SSH into](https://github.com/commaai/openpilot/wiki/SSH) your openpilot device.
```
git clone https://github.com/chiu99/openpilot-customizer.git
bash openpilot-customizer/t.sh
```
Reboot device to take effect.

Openpilot's routine update will override the change, you have to run it again manually.
