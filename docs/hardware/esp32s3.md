---
sidebar_position: 0
slug: /
---

# ESP32-S3 PowerFeather

:::info
Work in progress.
:::


## Features & Specifications

### Physical

- Board Dimensions: 65 mm L x 23 mm W  x 7 mm H
- Feather format, FeatherWing support
- Board Features
    - USB-C connector
    - Two 2.5 mm mounting holes
    - Two 1x16 2.54 mm header pin holes
    - Thermistor pin hole
    - 2-pin JST PH Li-ion/LiPo battery connector
    - 4-pin JST SH STEMMA QT connector
    - Green user LED
    - Red charger status LED
    - User button
    - Reset button
    - On-board PCB antenna

### Capabilities

#### Compute Resources

- 240 Mhz Dual-Core Xtensa LX7 Processor
- RISC-V / FSM Ultra Low Power Coprocessor
- 8 MB Quad-SPI Flash
- 2 MB Quad-SPI PSRAM
- 512 KB SRAM
- 16 KB RTC SRAM

#### Power Management

- Supply Monitoring
    - Current measurement
    - Voltage measurement
    - Good supply detection
- Supply Management
    - Set maintained supply voltage (can be used to set MPP voltage)
- Battery Monitoring
    - Voltage measurement
    - Temperature measurement
    - Current measurement (charge/discharge)
    - Charge estimation
    - Health & cycle count estimation
    - Time-to-empty and time-to-full estimation
    - Low charge, high/low voltage alarm
- Battery Management
    - Enable/disable charging
    - Set max charging current
- Others
    - `3V3` enable/disable
    - `VSQT` enable/disable
    - FeatherWing enable/disable via `EN` pin
    - Power States
        - Ship mode
        - Shutdown mode
        - Power cycle
    - Battery Protections
        - Undervoltage Detect @2.2 V, Release @2.4 V
        - Overvoltage Detect @4.37 V, Release @4.28 V
        - Discharge overcurrent @1.5 A
        - Trickle charging safety timer @1 hr
        - Temperature-based charging current reduction based on JEITA, cutoff at 0 °C and 60 °C.

### Interfaces

#### Radio
- 2.4 GHz Wi-Fi 802.11b/g/n on PCB antenna
- Bluetooth 5 LE + Mesh on PCB antenna

#### Connectors
- USB 1.1 Full-Speed OTG on USB-C connector
- I2C on STEMMA QT connector

#### Pin Holes
- 23 I/O on the two 1x16 2.54 mm pitch header pin holes
    - All digital input and output capable
    - All UART, I2C, SPI, I2S, SDIO, PWM, CAN, RMT, Camera, LCD capable
    - 6 analog input capable
    - 5 touch input capable
    - 12 RTC capable (deep sleep pin hold, wake-up source)
- 103AT input on thermistor pin hole

### Power

#### Input

- 5 V, 2 A max on `VUSB` USB-C connector
- 5 V - 18 V, 2A max on `VDC` header pin
- 4.2 V max, 2 A max on `BATP` and `BATN` JST PH Li-ion/LiPo battery connector

#### Output

- 3.3 V, 1 A max shared between board, `3V3` header pin and `VSQT` STEMMA QT connector
- 3.3 V - 4.2 V, 3 A max shared between board and `VBAT` header pin
- 5 V - 18 V, 2 A max shared between board and `VS` header pin

#### Current Consumption

| Power State | `BATP` Current |
|-|-|
|Deep-Sleep, Fuel Gauge Enabled (Initial) | 26 μA |
|Deep-Sleep, Fuel Gauge Enabled (Settled) | 18.5 μA |
|Deep-Sleep, Fuel Gauge Disabled | 18 μA |
|Ship Mode, Fuel Gauge Disabled | 1.5 μA |
|Shut Down, Fuel Gauge Disabled | 1.4 μA |

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
|RX| UART RX | GPIO42 | | | | MTMS |
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
|EN| Open-drain board enable|

### Power Input

Powers the components on-board. Loads directly connected to these are excluded in the board current measurement.

| Name | Description
|-|-|
|BATN| Li-ion/LiPo Negative Terminal
|BATP| Li-ion/LiPo Positive Terminal
|VUSB| 5V USB Power Supply |
|VDC| 3.8 V - 18 V DC Power Supply

### Power Output

Powers loads connected to the board. These are exclusively output, don't connect input supplies to them.

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

While ESP32-S3 PowerFeather is in a Feather format and is largely compatible with that ecosystem, it has has a few differences from the [Feather specification](https://learn.adafruit.com/adafruit-feather/feather-specification).

### `EN` Behavior

On other Feather boards, the `EN` pin is connected to the enable pin of the on-board 3.3 V regulator. Pulling `EN` low means disabling the 3.3 V regulator and everything powered from it.

On PowerFeather, `EN` is connected to an ESP32-S3 GPIO pin. User code can read the state of this pin and act accordingly, i.e. it can disable the `3V3` and `VSQT` load switches and put itself to deep-sleep to emulate behavior on standard boards; or it might do something completely different.

Furthermore, the ESP32-S3 itself can pull `EN` low via `EN0` if user code needs to disable connected FeatherWings.

### `QON` Pull-Up

`QON` replaces `AREF` on ESP32-S3 PowerFeather, and is normally pulled high up to 5 V. Make sure when connecting FeatherWings that it is able to handle this voltage on its `AREF` pin, or the FeatherWing does not use `AREF` at all.

If this is an issue, `QON` can be removed by breaking a solder bridge labeled `B2`.

### `VS` Up to 18 V

On standard Feather boards, the pin occupied by `VS` is the `5V` output (there is no on-board 5 V regulator, the 5 V comes from the USB supply). On PowerFeather, `VS` outputs either `VUSB` or `VDC`, whichever has a higher voltage. Since `VDC` can be up to 18 V, this means that `VS` can also be up to 18 V.

Keep this in mind if using a power supply with voltage higher than 5 V on `VDC`, as it might destroy FeatherWings that only expects 5 V on its `5V`/`VS` pin.

<!--
TODO: turn this into a 'notes' section

## FAQ

#### Can the USB and DC adapter be plugged in at the same time?

Yes, but the supply with the higher voltage will be used. If they are roughly the same, the current load will be shared between the two supplies. The circuitry also ensures that one supply does not backfeed into the other.

#### Can USB/DC adapter be used to power the system and charge the battery at the same time?

Yes. PowerFeather uses a charger chip with an integrated power path. This means that when USB/DC power is provided, it is used to power the board even with the battery in a depleted state, charging it along the way. The battery is disconected once full to avoid overcharging. If the USB/DC power is removed, the battery automatically takes over powering the board. Furthermore, the battery can also supplement the USB/DC supply in case of load spikes.

#### Does this board support LiFePO4 batteries?

No, the board as a whole does not support LiFePO4 batteries. While the charger IC supports LiFePO4, the fuel gauge IC does not. Furthermore,
PowerFeather uses a linear regulator to provide the 3.3 V power rail, which won't function properly under a LiFePO4 battery with nominal voltage of 3.2 V.

#### Does this board support MPPT for solar panels?

No, this board does not support 'true' MPPT in the sense that it does not do full tracking of the panel's I-V curve. However, the panel MPP voltage can be set, and the charger IC will dynamically regulate charging current to prevent the panel voltage from collapsing below it. This provides near/pseudo-MPPT performance, since the MPP voltage for a typical panel remains roughly the same across varying illumination levels.

For more details, please read [this Adafruit design note](https://learn.adafruit.com/adafruit-bq24074-universal-usb-dc-solar-charger-breakout/design-notes) for one of their solar chargers that uses the same dynamic charging current regulation technology. However, the advantage of PowerFeather compared to their solar charger is that their solar charger has a fixed MPP voltage at 4.5 V, while for PowerFeather it can be adjusted in firmware up to 16.8 V. -->

## Appendix

### Current Measurements

These are measurements for the figures in [Current Consumption](#current-consumption). These were measured using Nordic Power Profiler Kit II (a.k.a PPK2) acting as a battery @3.7 V plugged into `BATP` and `BATN`; and with no external supply (`VBUS` or `VDC`).

| Deep Sleep, Fuel Gauge Enabled (Initial) | Deep Sleep, Fuel Gauge Enabled (Settled) |
|-|-|
| [![](assets/fg_initial.png)](assets/fg_initial.png) <br/> The fuel gauge *initially* samples around every ~1 s, with each sample registering a current spike to up ~5 mA. | [![](assets/fg_settled.png)](assets/fg_settled.png) <br/> The fuel gauge samples *settles* down to around every ~2 s, with each sample registering a current spike up to ~50 μA. |


| Deep Sleep, Fuel Gauge Disabled | Ship Mode, Fuel Gauge Disabled | Shutdown Mode, Fuel Gauge Disabled |
|-|-|-|
| [![](assets/nofg.png)](assets/nofg.png) | [![](assets/ship.png)](assets/ship.png) | [![](assets/shutdown.png)](assets/shutdown.png) |

You can download the raw traces obtained from PPK2 using the links below, and open them with your nRF Connect Power Profiler Software.

- [Trace for Deep Sleep with Fuel Gauge Enabled - Initial and Settled](assets/trace_initial-settled.ppk)
- [Trace for Deep Sleep with Fuel Gauge Disabled, Ship Mode and Shutdown Mode](assets/trace_nofg-ship-shutdown.ppk)



