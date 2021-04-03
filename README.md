# openpilot-customizer
Simple script to add your car fingerprints and small tunings after every openpilot release.
## What this script will do
It is written in python and will replace certain strings in openpilot.
* Change Toyota Corolla Hybrid TSS2 fingerprints to your car, in this example, Lexus UX250h 2020 Taiwan. Edit to fulfill your need.
* Tuning Toyota Corolla Hybrid TSS2 by the wheelbase, steerRatio, tire_stiffness_factor and mass, in this example, of Lexus UX250h. Edit to fulfill your need.
* Disable camera logger
* Disable data uploader
* Change auto power off from 30 hours to 30 minutes
* Update LastUpdateTime
## How to use
SSH into your openpilot device.
```
git clone https://github.com/chiu99/openpilot-customizer.git
bash openpilot-customizer/t.sh
```
Reboot device to take effect.

Openpilot's routine update will override the change, you have to run it again manually.
