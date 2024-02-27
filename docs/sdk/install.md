---
sidebar_position: 0
---

# Installation

### ESP-IDF


Connect the PowerFeather to a host PC.

#### Arduino

1. [Install Arduino IDE 2](https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing/).
2. [Install Arduino-ESP32 support](https://espressif-docs.readthedocs-hosted.com/projects/arduino-esp32/en/latest/installing.html#installing-using-arduino-ide).
- Use the stable release link.
- Make sure `v3.0.0` or newer is installed.
3. Install the `PowerFeather` library.
4. Select the `hello_powerfeather` example. Build and flash.
5. Open the serial monitor, the serial should display details about the supply and battery.

#### ESP-IDF

1. [Install ESP-IDF v5 or newer](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/#installation).
2. Create project from example (https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/tools/idf-component-manager.html#creating-a-project-from-an-example).
3. Run `idf.py flash monitor`. The serial monitor should display about the supply and battery.