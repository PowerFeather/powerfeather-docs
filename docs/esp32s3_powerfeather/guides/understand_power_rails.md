---
sidebar_position: 1
---

# Understanding Power Rails


# Power Inputs

- Three power inputs: battery, USB and DC
- Between USB and DC, priority is given to DC when the same voltage.
- Between USB and DC, if DC falls below certain threshold, USB is used.
- If only USB, that is used.
- There is an api to get which is the active power source, battery/USB/DC.
- Battery is the automatic power source if no USB and DC.
- If USB or DC is plugged in with battery, those are used.
- Battery can supplement additional current if required.


# Power Outputs

- There are four power outputs: BAT, H3V3, SQT3V3 and 5V.
- H3V3, SQT3V3 and 5V can be turned off; BAT can't.
- BAT decreases as the battery discharges.