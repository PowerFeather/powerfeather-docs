---
sidebar_position: 1
---

# Getting Started

:::info
Work in progress.
:::

## First Use

PowerFeather comes pre-loaded with a simple program that blinks the green user `LED`. Use this to quickly check
if your board is OK. Simply connect your PowerFeather to a host computer using the USB-C connector:

![LED Blink](assets/led_blink.gif)

As illustrated above, the red `CHG` LED should flash momentarily, after which the green user `LED` will blink.

## Run Example

The demo application showcases some of the things you can do with PowerFeather. To run the it, ESP-IDF or Arduino
with the *PowerFeather SDK* must be installed on your system. If you have not done this yet,
please follow the instructions first on the [PowerFeather SDK setup guide](/sdk/install.md).

### Arduino

Open Arduino IDE, and select the *PowerFeather SDK* > *Supply_and_Battery_Info* example.

![Open Example](assets/open_example.png)

If you have a battery, detach the USB-C cable first. Attach your battery, only
then reconnect the USB-C cable. Then, make sure *ESP32-S3 PowerFeather* is selected as the board.

![Select Board](assets/select_board.png)

Upload the example, then open the *Serial Monitor* when done.

![Upload Example](assets/upload_example.png)
![Serial Monitor Hover](assets/serial_monitor_hover.png)

On the *Serial Monitor*, the supply and battery voltage and current are reported; as well as the
battery charge estimated by the fuel gauge. Notice that the battery current is zero, while the supply current is not.
This indicates that:
- The board is being supplied by the external power source, in this case by `VUSB`.
- The battery is not charging.

![Serial Monitor](assets/serial_monitor.png)

Press `BTN` on PowerFeather to enable charging. When charging is enabled, notice the battery current
is no longer zero; and supply current also increases.

![Charging](assets/charging.png)

If you have one, you can try using a data-only (no power) USB-C cable, to see that in the absence of an external
supply, the battery supplies the board. In this case, the battery current is negative, indicating
discharging.

![Discharging](assets/discharging.png)

### ESP-IDF


On Mac OS and Linux, open a terminal with [ESP-IDF environment set up](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-setup.html#step-4-set-up-the-environment-variables). On Windows you can just open the [ESP-IDF x.y CMD or ESP-IDF x.y PowerShell](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/windows-setup.html#launching-esp-idf-environment), where `x.y` is the specific version of ESP-IDF you installed.

Navigate to a directory where the example project can be downloaded to and run the following command:

```bash
idf.py create-project-from-example "powerfeather/powerfeather-sdk^1.0.0:supply_and_battery_info"
```
![Download example](assets/download_example.png)

If you have a battery, detach the USB-C cable first. Attach your battery, only then reconnect the USB-C cable.
Go into the `supply_and_battery_info` directory where the example project was downloaded to.  Then build and flash the project.

```bash
idf.py set-target esp32s3
idf.py flash monitor
```

![Set target](assets/set_target_esp32s3.png)

On *idf.py monitor*, the supply and battery voltage and current are reported; as well as the
battery charge estimated by the fuel gauge. Notice that the battery current is zero, while the supply current is not.
This indicates that:
- The board is being supplied by the external power source, in this case by `VUSB`.
- The battery is not charging.

![Monitor not charging](assets/monitor_no_charge.png)


Press `BTN` on PowerFeather to enable charging. When charging is enabled, notice the battery current
is no longer zero; and supply current also increases.

![Monitor charging](assets/monitor_charging.png)

If you have one, you can try using a data-only (no power) USB-C cable, to see that in the absence of an external
supply, the battery supplies the board. In this case, the battery current is negative, indicating
discharging.

![Monitor discharge](assets/monitor_discharge.png)