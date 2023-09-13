---
sidebar_position: 0
---

# Overview

ESP32-S3 PowerFeather is the ultimate development board for your Li-Po powered projects.

## Features

### Low Power

- Low quiescent current components
- Load switch 3.3V rails

### Battery
- Fuel Guage
- Charger interface

### Compatibility with modules

- FeatherWing
- Stemma QT/ QWIIC


## Specifications

- Form factor
    - 23 mm x 57 mm x 6mm
    - USB-C connector
    - Feather-compatible
- Header
    - 23 digital input/output
    - 6 analog capable
    - 1 SPI
    - 1 I2C
- Processor: ESP32-S3-WROOM-1-N16R8
    - Dual-core 240MHz Xtensa @ 240MHz
    - 16 MB SPI Flash, 768 KB SRAM + 8 MB PSRAM
    - 2.4 GHz Wi-Fi b/g/n
    - Bluetooth 5.0 LE + Mesh
- Current consumption
    - 1.5uA shutdown mode
    - 2uA ship mode
    - 10 uA deep sleep
    - 40 mA light sleep
    - 120 mA active
    - 250 mA Wi-Fi active
- Power Inputs
    - DC: 5.5V max, 2.5A max
    - USB: 5V max, 2.5A max
    - Battery: 3.7-4.2V, 6A max
- Power Outputs
    - 3.3V, 750 mA, two switchable outputs
    - 5V, 2A max
    - BAT, 3.7 - 4.2V, 3A max
- Charging
    - Battery
        - 1S
        - Li-Ion/Li-Polymer, Lithium Phosphate/LiFePO4
    - 2A max current
- Others
    - 1 Stemma QT
    - User Button
    - Reset Button
    - User LED
    - Battery Charging LED



## Pinout

![ESP32-S3 PowerFeather Pins](board.jpg)


## Comparison

| Detail | ESP32-S3 PowerFeather | Unexpected Maker FeatherS3 | DFRobot ESP32 Firebeetle (DFR0654) |
|-|-|-|-|
| Module | ESP32-S3-WROOM-N16R8 | N/A<sup>1</sup> | ESP32-WROOM-32E-N4 |
| Processor | ESP32-S3 | ESP32-S3 | ESP32 |
| Flash | 16MB | 16 MB | 4 MB |
| SRAM | 512 KB | 512 KB | 520 KB |
| PSRAM | 8MB | 8 MB | N/A |
| Wi-Fi | 2.4 GHz b/g/n | 2.4 GHz b/g/n | 2.4 GHz b/g/n |
| Bluetooth | Bluetooth 5 LE + Mesh | Bluetooth 5 LE + Mesh | Bluetooth 4.2 BR/EDR + LE |
| Deep Sleep Current | 10 uA | 20 uA | 13 uA<sup>2</sup> |
| Lowest Power State/Current | Shutdown Mode/1.5 uA  | Deep Sleep/20 uA | Deep Sleep/13 uA |
| 3.3V Output Max Current | 750 mA | 2 x 700 mA | 600 mA |
| Turn On/Off 3.3V Output | Yes | Yes | No |
| 5V Output Max Current | 2 A | N/A<sup>3</sup> | N/A<sup>3</sup> |
| Max Charging Current (no board modifications) | 2 A<sup>4</sup> | 330 mA<sup>5</sup> | 500 mA<sup>5</sup> |
| Battery charge measurement | Fuel Gauge Chip | Voltage divider<sup>6</sup> | Voltage divider<sup>6</sup> |
| STEMMA QT | 1 | 2 | N/A |
| Feather-compatible | Yes | Yes | No |
| Extra DC power input, aside from USB | Yes | No | No |
| Load while charging | Yes<sup>7</sup> | Yes | Yes |
| Battery can temporarily supplement USB/DC supply | Yes<sup>7</sup> | No | No |
| Battery power output when no/depleted battery, but has USB/DC supply | Yes<sup>7</sup> | No | No |
| Castellated Header Pins | No | No | Yes |
| Header GPIOs | 23 input/output | 21 input/output | 18 input/output + 4 input only |
| Onboard LED | Charger Status + User LED | Charger Status + RGB User LED | Charger Status + RGB User LED <sup>2</sup>
| Onboard Buttons | Reset + User Button | Reset + User Button | Reset + User Button
| USB Connector | USB-C | USB-C | USB-C |
| Native USB | Yes | Yes | No |
| Display Connector | No | No | 18-Pin FPC <sup>8</sup> |
| Price | $27 | $22 | $9 |


1. The *FeatherS3* does not use a module, instead using a bare ESP32-S3 chip. On the other hand, *ESP32-S3 PowerFeather* and *ESP32-Firebeetle* uses official Espressif modules, which comes with [certifications](https://www.espressif.com/en/support/documents/certificates?keys=&field_product_value%5B%5D=ESP32-S3-WROOM-1&field_product_value%5B%5D=ESP32-WROOM-32E).
2. To achieve low deep-sleep current consumption, an onboard trace on the *ESP32 Firebeetle* has to be cut which disables the onboard RGB LED.
3. On *FeatherS3* and *ESP32 Firebeetle*, the maximum 5V output current depends directly on the maximum current the USB input power supply can deliver.
4. The battery charger chip on the *ESP32-S3 PowerFeather* has an I2C interface, which can accept configuration command for setting the max charging current from the firmware. This makes it easy to set max charging current to balance charging speed and safety for a specific battery size.
5. On *FeatherS3* and *ESP32 Firebeetle*, a resistor on the board has to be replaced to change max charging current.
6. The voltage dividers on *FeatherS3* and *ESP32 Firebeetle* [may not be sufficient to determine the battery's state-of-charge](https://www.analog.com/jp/technical-articles/how-to-achieve-greater-accuracy-in-battery-capacity-readings-for-portable-designs.html).
7. *ESP32-S3 PowerFeather* battery charger chip has integrated power path management, which enables these features.
8. The 18-pin FPC on the *ESP32 Firebeetle* shares some GPIO pins with header; so pins used as part of the display interface can't be used on the header.