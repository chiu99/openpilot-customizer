import re
import datetime
from common.params import Params

opsd = "/data/openpilot/selfdrive/"
values_loc = opsd + "car/toyota/values.py"
interface_loc = opsd + "car/toyota/interface.py"
manager_loc = opsd + "manager/manager.py"
process_loc = opsd + "manager/process_config.py"
power_monitoring_loc = opsd + "thermald/power_monitoring.py"

# add fingerprint of UX250h 2020 Taiwan
with open(values_loc,"r") as f:
    str = f.read()

regex = r"CAR\.COROLLAH_TSS2:\s*{[^}]*},"
subst = "CAR.COROLLAH_TSS2: {\\n    (Ecu.engine, 0x700, None): [\\n      b'\\\\x01896637624000\\\\x00\\\\x00\\\\x00\\\\x00',\\n    ],\\n    (Ecu.eps, 0x7a1, None): [\\n      b'8965B76012\\\\x00\\\\x00\\\\x00\\\\x00\\\\x00\\\\x00',\\n    ],\\n    (Ecu.esp, 0x7b0, None): [\\n      b'F152676293\\\\x00\\\\x00\\\\x00\\\\x00\\\\x00\\\\x00',\\n    ],\\n    (Ecu.fwdRadar, 0x750, 0xf): [\\n      b'\\\\x018821F3301400\\\\x00\\\\x00\\\\x00\\\\x00',\\n    ],\\n    (Ecu.fwdCamera, 0x750, 0x6d): [\\n      b'\\\\x028646F7603100\\\\x00\\\\x00\\\\x00\\\\x008646G2601200\\\\x00\\\\x00\\\\x00\\\\x00',\\n    ],\\n  },"
str = re.sub(regex, subst, str, 0, re.MULTILINE)

with open(values_loc,"w") as f:
    f.write(str)

# tune for UX250h
with open(interface_loc,"r") as f:
    str = f.read()

regex = r"candidate.+CAR\.COROLLAH_TSS2[^[]+CV\.LB_TO_KG\s+\+\s+STD_CARGO_KG"
subst = "candidate in [CAR.COROLLA_TSS2, CAR.COROLLAH_TSS2]:\\n      stop_and_go = True\\n      ret.safetyParam = 73\\n      ret.wheelbase = 2.640\\n      ret.steerRatio = 15\\n      tire_stiffness_factor = 1\\n      ret.mass = 3500. * CV.LB_TO_KG + STD_CARGO_KG"
str = re.sub(regex, subst, str, 0, re.MULTILINE)

with open(interface_loc,"w") as f:
    f.write(str)

# disable logger
with open(manager_loc,"r") as f:
    str = f.read()

regex = r".{4}if.+freeSpacePercent.+\n.+loggerd\"\)"
subst = "    if sm['deviceState'].freeSpacePercent < 99:\\n      not_run.append(\"loggerd\")"
str = re.sub(regex, subst, str, 0, re.MULTILINE)

with open(manager_loc,"w") as f:
    f.write(str)

# disable uploader
with open(process_loc,"r") as f:
    str = f.read()

regex = r".+PythonProcess\(\"uploader\""
subst = "#  PythonProcess(\"uploader\""
str = re.sub(regex, subst, str, 0, re.MULTILINE)

with open(process_loc,"w") as f:
    f.write(str)

# power off after 30 minutes
with open(power_monitoring_loc,"r") as f:
    str = f.read()

regex = r"MAX_TIME_OFFROAD_S.+=.+"
subst = "MAX_TIME_OFFROAD_S = 1800"
str = re.sub(regex, subst, str, 0, re.MULTILINE)

with open(power_monitoring_loc,"w") as f:
    f.write(str)

# update flag
params = Params()
t = datetime.datetime.utcnow().isoformat()
params.put("LastUpdateTime", t.encode('utf8'))
