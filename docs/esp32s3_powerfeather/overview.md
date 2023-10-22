---
sidebar_position: 0
slug: /
---

# Overview

## Features & Specifications

### Form Factor

- Board Dimensions
    - L: 57 mm
    - W: 23 mm
    - H: 6 mm
- [Feather-compatible](https://learn.adafruit.com/adafruit-feather/feather-specification)
    - 2 D=2.5mm mounting holes
    - 2 1x16 2.54 mm headers
- Connectors
    - 1 Battery JST PH
    - 1 USB-C
    - 1 STEMMA QT

### Processing

- 240 Mhz Dual-Core Xtensa LX7 Processor
- RISC-V / FSM Ultra Low Power Coprocessor
- 16 MB Quad-SPI Flash
- 8 MB Quad-SPI PSRAM
- 512 KB SRAM
- 16 KB RTC SRAM


### Connectivity

#### Radio
- 150 Mbps 2.4 GHz Wi-Fi 802.11b/g/n with on-board PCB antenna
- 2 Mbps Bluetooth 5 LE + Mesh with on-board PCB antenna

#### Input/Output
- USB OTG Full-Speed on USB-C connector
- 23 digital I/O pins on 2.54 mm headers
    - 6 analog output capable pin
    - 5 touch capable pin
    - 12 RTC capable pin
    - 3 UART, 2 SPI, 1 I2C, 1 I2S, 2 SDIO, 1 CAN on any pin
- 1 I2C via STEMMA QT connector
- 1 Red Charger Status LED
- 1 Reset Button
- 1 Green User LED
- 1 User Button


### Power

#### Input

- 5 V, 2 A `VUSB` via USB-C connector
- 3.9 V - 18 V, 2A via `VDC` pin
- 4.2 V, 2 A via battery JST PH connector

#### Output

- 3.3 V, 500 mA shared between `3V3` pin and `VSQT` on STEMMA QT connector
- 3.3 V - 4.2 V, 3 A via `VBAT` pin
- 5 V - 18 V, 2 A max via `VS` pin

#### Consumption

| State | Conditions | Current
|-|-|-|
|Active| External DC Supply (up to 18V) | Digital Output
|Deep-Sleep| External DC Supply (up to 18V) | Digital Output
|Ship Mode| External DC Supply (up to 18V) | Digital Output
|Shut Down| External DC Supply (up to 18V) | Digital Output

#### Battery

- Support Li-Ion/Li-Poly batteries with 3.7 V nominal, 4.2 V max voltage
- 2 A max charging current, configurable from firmware
- Battery Protections
    - Undervoltage Detect @2.2 V, Release @2.4 V
    - Overvoltage Detect @4.37 V, Release @4.28 V
    - Discharge overcurrent @1.5 A
    - Trickle charging safety timer @1 hr
    - Temperature cutoff @0 °C and @60 °C (needs 10k NTC thermistor on battery)

## Pins & Signals

![ESP32-S3 PowerFeather Pins](assets/pinout.jpg)

### IO

These are signals routed to the ESP32-S3 GPIO pins.

#### Free IO

IO signals not connected to anything on-board and user code is free to configure and use it for any purpose, as long as it is within its capabilities. Note that the `Description` in the table below are only suggestions, and together with `Name` only there to maintain compatibility with other Feather and FeatherWings.

|Name| Description | Digital | Analog Input | RTC | Touch | JTAG |
|-|-|-|-|-|-|-|
|A0| Analog Input 0 | GPIO10 | ADC1_9 | RTCIO10 | TOUCH10 | |
|A1| Analog Input 1 | GPIO9 | ADC1_8 | RTCIO9 | TOUCH9 | |
|A2| Analog Input 2 | GPIO8 | ADC1_7 | RTCIO8 | TOUCH8 | |
|A3| Analog Input 3 | GPIO3 | ADC1_2 | RTCIO3 | TOUCH3 | |
|A4| Analog Input 4 | GPIO2 | ADC1_1 | RTCIO2 | TOUCH2 | |
|A5| Analog Input 5 | GPIO1 | ADC1_0 | RTCIO1 | TOUCH1 | |
|D5|  Digital Input/Output 5 | GPIO15 | ADC2_4 | RTCIO15 | | |
|D6|  Digital Input/Output 6 | GPIO16 | ADC2_5 | RTCIO16 | | |
|D7|  Digital Input/Output 7 | GPIO37 | | | | |
|D8|  Digital Input/Output 8 | GPIO6 | ADC1_5 | RTCIO6 | TOUCH6 | |
|D9|  Digital Input/Output 9 | GPIO17 | ADC2_6 | RTCIO17 | | |
|D10| Digital Input/Output 10 | GPIO18 | ADC2_7 | RTCIO18 | | |
|D11| Digital Input/Output 11 | GPIO45 | | | | |
|D12| Digital Input/Output 12 | GPIO12 | ADC2_1 | RTCIO12 | TOUCH12 | |
|D13| Digital Input/Output 13 | GPIO11 | ADC2_0 | RTCIO11 | TOUCH11 | |
|MOSI| SPI MOSI | GPIO40 | | | | MTDO |
|MISO| SPI MISO | GPIO41 | | | | MTDI |
|SCK| SPI SCK | GPIO39 | | | | MTCK |
|RX| UART RX | GPIO32 | | | | MTMS |
|TX| UART TX | GPIO44 | | | | |
|TX0| Serial Log Output | GPIO43 | | | | |
|SCL| I2C SCL | GPIO36 | | | | |
|SDA| I2C SDA | GPIO35 | | | | |

##### Capabilities

- Digital -  IO that can output or accept input of 3.3 V digital logic; supports UART, I2C, SPI, I2S, SDIO, PWM, CAN, RMT, Camera, LCD peripherals.
- RTC - IO  that can hold output during deep-sleep; or be used as a wake source from deep-sleep.
- Touch - IO  that can be used as capacitive touch input.
- Analog Input - IO that can read analog signals; `X`, `Y` denotes the ADC number and channel respectively in `ADCX_Y`
- JTAG - IO used for JTAG debugging.

#### User-Managed Fixed IO

IO signals connected to a component on-board, limiting its use. For example, it does not  make sense to use `BTN` as UART TX due to being connected to a button, even though it is technically capable of doing so. User code is still in control in terms of configuring and using these IO.

| Pin | Description | Digital | RTC |
|-|-|-|-|
|ALARM| Fuel Gauge Alarm Input | GPIO21 | RTCIO21 |
|INT| Battery Charger Interrupt Input | GPIO5 | RTCIO5 |
|BTN| User Button Input | GPIO0 | RTCIO0 |
|LED| Green User LED Output | GPIO46 | RTCIO7 | |

#### SDK-Managed Fixed IO

IO signals connected to a component on-board, whose configuration and use is managed by the SDK. User code should not configure and use these IO, as doing so can cause faulty behavior.

| Pin | Description |
|-|-|
|USB_DP| USB Data Positive |
|USB_DM| USB Data Negative |
|PG| Power Supply Good Indicator Input |
|3V3_EN| 3V3 Enable Output|
|VSQT_EN| VSQT Enable Output |
|EN0| Board Enable Output |

### Special Function

Signals not routed to the ESP32-S3 GPIO pins, or are routed to other integrated circuits on-board such as the charger and fuel gauge.

| Name | Description |
|-|-|
|CHG| Battery Charger Status LED |
|RST| ESP32-S3 Module Reset |
|QON| Ship Mode Exit|
|TS| Battery 10k NTC Thermistor Input|

### Power Input

Powers the components on-board.

| Name | Description
|-|-|
|BATN| Li-Ion/Li-Poly Negative Terminal
|BATP| Li-Ion/Li-Poly Positive Terminal
|VUSB| 5V USB Power Supply |
|VDC| 3.8 V - 18 V DC Power Supply

### Power Output

Powers loads connected to the board.

| Name | Description
|-|-|
|VBAT| 3.7 V - 4.2 V Battery Output
|VS| 3.8 V - 18 V Supply Voltage; Higher of `VDC` and `VUSB`
|3V3| Header 3.3V |
|VSQT| STEMMA QT 3.3V |

### Ground

0 V reference for the components on-board, input power supplies and connected loads.

| Name | Description |
|-|-|
|GND| Ground Pin |


## Feather Differences

ESP32-S3 PowerFeather has a few differences from standard Feather mainboards.

### `EN` Behavior

On other Feather boards, the `EN` pin is connected to the enable pin of the on-board 3.3 V regulator. Pulling `EN` low means disabling the 3.3 V regulator and everything powered from it.

On PowerFeather, `EN` is connected to an ESP32-S3 GPIO pin. User code can read the state of this pin and act accordingly, i.e. it can disable the `3V3` and `VSQT` load switches and put itself to deep-sleep to emulate behavior on standard boards; or it might do something completely different.

Furthermore, the ESP32-S3 itself can pull `EN` low via `EN0` if user code needs to disable connected FeatherWings.

### `QON` Pull-Up

`QON` replaces `AREF` on ESP32-S3 PowerFeather, and is normally pulled high to 3.3 V. Make sure when connecting FeatherWings that it is able to handle this voltage on its `AREF` pin, or the FeatherWing does not use `AREF` at all.

If this is an issue, `QON` can be removed by breaking a solder bridge.

### `VS` Up to 18 V

On standard Feather boards, the pin occupied by `VS` is the `5V` output (there is no on-board 5 V regulator, the 5 V comes from the USB supply). On PowerFeather, `VS` outputs either `VUSB` or `VDC`, whichever has a higher voltage. Since `VDC` can be up to 18 V, this means that `VS` can also be up to 18 V.

Keep this in mind if using a power supply with voltage higher than 5 V on `VDC`, as it might destroy FeatherWings that only expects 5 V on its `5V`/`VS` pin.



## Misc


<!-- ## Comparison
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
| Enable/Disable 3.3V Output | Yes | Yes | No |
| 5V Output Max Current | 2 A | N/A<sup>3</sup> | N/A<sup>3</sup> |
| Max Charging Current (no board modifications) | 2 A<sup>4</sup> | 330 mA<sup>5</sup> | 500 mA<sup>5</sup> |
| Battery voltage measurement | Fuel Gauge | Voltage divider | Voltage divider |
| Battery state-of-charge (SOC) measurement | Fuel Gauge | Estimate using battery voltage<sup>6</sup>| Estimate using battery voltage<sup>6</sup> |
| Battery state-of-health (SOH) measurement | Fuel Gauge | N/A | N/A |
| Battery charging/discharging time-to-full/time-to-empty estimate | Fuel Gauge | N/A | N/A |
| STEMMA QT/QWIIC | 1 | 2 | N/A |
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
| Price | $29 | $22 | $9 |


1. The *FeatherS3* does not use a module, instead using a bare ESP32-S3 chip. On the other hand, *ESP32-S3 PowerFeather* and *ESP32-Firebeetle* uses official Espressif modules, which comes with [certifications](https://www.espressif.com/en/support/documents/certificates?keys=&field_product_value%5B%5D=ESP32-S3-WROOM-1&field_product_value%5B%5D=ESP32-WROOM-32E).
2. To achieve low deep-sleep current consumption, an onboard trace on the *ESP32 Firebeetle* has to be cut which disables the onboard RGB LED.
3. On *FeatherS3* and *ESP32 Firebeetle*, the maximum 5V output current depends directly on the maximum current the USB input power supply can deliver.
4. The battery charger chip on the *ESP32-S3 PowerFeather* has an I2C interface, which can accept configuration command for setting the max charging current from the firmware. This makes it easy to set max charging current to balance charging speed and safety for a specific battery size.
5. On *FeatherS3* and *ESP32 Firebeetle*, a resistor on the board has to be replaced to change max charging current.
6. Estimation of state-of-charge using battery voltage on *FeatherS3* and *ESP32 Firebeetle* [may not be sufficient](https://www.analog.com/jp/technical-articles/how-to-achieve-greater-accuracy-in-battery-capacity-readings-for-portable-designs.html).
7. *ESP32-S3 PowerFeather* battery charger chip has integrated power path management, which enables these features.
8. The 18-pin FPC on the *ESP32 Firebeetle* shares some GPIO pins with header; so pins used as part of the display interface can't be used on the header. -->


### Related Links

#### Datasheets

- [ESP32-S3-WROOM-1-N16R8](https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf)
- [BQ25628E](https://www.ti.com/lit/ds/symlink/bq25628e.pdf?ts=1697957319709&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FBQ25628E)
- [LC709204F](https://www.ti.com/lit/ds/symlink/tps62840.pdf?ts=1697940153313&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FTPS62840)
- [TPS62840](https://www.ti.com/lit/ds/symlink/tps62840.pdf?ts=1697940153313&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FTPS62840)

#### GitHub Repository

https://github.com/PowerFeather/esp32s3-powerfeather