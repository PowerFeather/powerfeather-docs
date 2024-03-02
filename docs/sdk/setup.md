---
sidebar_position: 0
---

# Setup

## Arduino

Arduino IDE needs to be [installed]((https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing/)) first. Arduino IDE v2 or newer is recommended. Once done, Arduino ESP32 also needs to be [installed](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html). 

:::info
As of the time of this writing, Arduino ESP32 v3.0.0 is not yet released and is only in beta. In order to setup PowerFeather-SDK, use the development release link while following the Arduino ESP32 installation instructions.

```
https://espressif.github.io/arduino-esp32/package_esp32_dev_index.json
```
:::

After Arduino ESP32 has been installed, PowerFeather-SDK can now be installed. Follow the [instructions for installing a library](https://docs.arduino.cc/software/ide-v2/tutorials/ide-v2-installing-a-library/), with the name of the library being `PowerFeather-SDK`.


To test whether the setup has been done successfuly, we'll create a sample Arduino sketch, with the contents:

```cpp
#include <PowerFeather.h>

using namespace PowerFeather;

void setup()
{
    Board.init();
}

void loop()
{
}
```

Build the sample sketch, it should proceed without any compilation errors.

## ESP-IDF

ESP-IDF needs to be installed first. PowerFeather-SDK requires ESP-IDF v5.1 or newer.
Please follow Espressif's installation guide for [Windows](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/windows-setup.html) or [Linux and macOS](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-setup.html).

To demonstrate adding PowerFeather-SDK to an ESP-IDF project, we'll create a sample project.
Open a terminal with the ESP-IDF environment set up on [Windows](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/windows-setup.html#launching-esp-idf-environment) or [Linux and macOS](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/linux-macos-setup.html#step-4-set-up-the-environment-variables). Navigate to a directory where the sample ESP-IDF project can be created, and enter the command:

```bash
```

Navigate into the created sample ESP-IDF project directory, and then enter the command:

```bash
```

Edit the `main.cpp` file inside the `main` directory to include.


```cpp
#include <PowerFeather.h>

using namespace PowerFeather;

extern "C" void app_main()
{
    Board.init();
}
```

Build the sample project by issuing the command:

```
idf.py build
```

If everything was set up correctly, the build should proceed without any compilation errors.