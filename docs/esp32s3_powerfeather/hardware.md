---
sidebar_position: 0
---

# Hardware

## Specifications

- Form factor
    - Feather-compatible
    - 23 mm x 57 mm x 6mm
    - USB-C connector
- Processor: ESP32-S3-WROOM-1-N16R8
    - Dual-core 240MHz Xtensa @ 240MHz
    - 16 MB SPI Flash, 768 KB SRAM + 8 MB PSRAM
    - 2.4 GHz Wi-Fi b/g/n
    - Bluetooth 5.0 LE + Mesh
- Header
    - 23 digital input/output
    - 6 analog capable
    - 1 SPI
    - 1 I2C
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

![An image from the static](board.jpg)


## Comparison


N/A - Not available/applicable

| Feature | ESP32-S3 PowerFeather | Unexpected Maker FeatherS3 | DFRobot ESP32 Firebeetle (DFR0654) |
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
| 3.3V Output Max Current | 750mA | 2 x 700mA | 600 mA |
| 5V Output Max Current | 2A | N/A<sup>2</sup> | N/A<sup>2</sup> |
| Max Charging Current | 2A | 1A | 1A |
| Max Charging Current Adjustment | Firmware send command to charger via I2C interface| Replace soldered resistor | Replace soldered resistor |
| Charge measurement | Fuel Gauge IC | Voltage divider<sup>3</sup> | Voltage divider<sup>3</sup> |
| STEMMA QT | 1 | 2 | N/A |
| Feather-compatible | Yes | No | No |
| Extra DC power input, aside from USB | Yes | No | No |
| Load while charging | Yes<sup>4</sup> | Yes | Yes |
| Battery can temporarily supplement USB/DC supply | Yes<sup>4</sup> | No | No |
| BAT power output when no/depleted battery, but has USB/DC supply | Yes<sup>4</sup> | No | No |
| Castellated Pins | No | No | Yes |
| Header GPIOs | 23 input/output | 21 input/output | 18 input/output + 4 input only |
| Onboard LED | Red Charger Status + Green User LED | Red Charger Status + RGB User LED | Charger Status + RGB User LED <sup>2</sup>
| Onboard Buttons | Reset + User | Reset + User | Reset + User
| USB Connector | USB-C | USB-C | USB-C |
| Native USB | Yes | Yes | No |
| Price | $27 | $22 | $9 |


1. FeatherS3 does not use a module, instead using bare ESP32-S3 chip. The advantage of using modules is that they have [certifications](https://www.espressif.com/en/support/documents/certificates).
2. To achieve this, an onboard trace needs to be cut rendering the RGB LED unusable.
2. The 5V output current depends on the USB output current.
3. Voltage divider may not represent state-of-charge of a battery, [since it is non-linear](https://www.analog.com/jp/technical-articles/how-to-achieve-greater-accuracy-in-battery-capacity-readings-for-portable-designs.html)
4. ESP32-S3 PowerFeather uses charger IC with PowerPath.