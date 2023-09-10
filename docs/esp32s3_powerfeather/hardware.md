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
    - 2.4 GHz Wi-Fi b/g/n + Bluetooth 5.0 LE
- Header
    - 23 Digital Input/Output
    - 6 Analog
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


## Pins




## Comparison

### Specifications

### Features

- BQ25628
    - Max charge current: 2A
    - Power Path
        - Can use load while charging
        - Battery can supplement USB/DC supply
        - Battery pin output without battery
    - I2C interface
```
Number of series cells	1
Charge current (max) (A)	2
Vin (max) (V)	18
Cell chemistry	Li-Ion/Li-Polymer, Lithium Phosphate/LiFePO4
Battery charge voltage (min) (V)	3.5
Battery charge voltage (max) (V)	4.8
Absolute max Vin (max) (V)	26
Control topology	Switch-Mode Buck
Control interface	I2C
Features	BAT temp thermistor monitoring (JEITA profile), IC thermal regulation, IINDPM (Input current limit), Input OVP, Integrated ADC, Integrated buck converter, Power Path, USB C/PD compatible, USB OTG integrated, VINDPM (Input voltage threshold to maximize adaptor power)
Vin (min) (V)	3.9
Rating	Catalog
Operating temperature range (°C)	-40 to 85


High-efficiency, 1.5-MHz, synchronous switching mode buck charger for single cell battery
>90% efficiency down to 25-mA output current from 5-V input
Charge termination from
Flexible JEITA profile for safe charging over temperature
BATFET control to support shutdown, ship mode and full system reset
1.5-µA quiescent current in battery only mode
0.15-µA battery leakage current in ship mode
0.1-µA battery leakage current in shutdown
Supports Boost Mode operation to power accesory
Boost Mode operation supporting 3.84-V to 5.2-V output
>90% boost efficiency down to 100-mA boost current for 5-V PMID
Supports a wide range of input sources
3.9-V to 18-V wide input operating voltage range with 26-V absolute maximum input voltage
Maximizes source power with input voltage regulation (VINDPM) and input current regulation (IINDPM)
VINDPM threshold automatically tracks battery voltage
Efficient battery operation with 15-mΩ BATFET
Narrow VDC (NVDC) power path management
System instant-on with depleted or no battery
Battery supplement when adapter is fully loaded
Flexible autonomous or I2C-controlled modes
Integrated 12-bit ADC for voltage, current, temperature monitoring
High Accuracy
±0.4% charge voltage regulation
±5% charge current regulation
±5% input current regulation
Safety
Thermal regulation and thermal shutdown
Input, system, and battery overvoltage protection
Battery, and converter overcurrent protection
Charging safety timer
```

- LC709
    - I2C interface
    - SOC state
    - Alarms
```
High accuracy gauging
Low power consumption
Stable gauging
Small footprint
Alarm function: RSOC / Voltage / Temperature
Battery lifetime measurement
Multi-thermistor support
I2C interface(up to 400kHz supported)
```


N/A - Not available/applicable

| Feature | ESP32-S3 PowerFeather | Unexpected Maker FeatherS3 | DFRobot ESP32 Firebeetle |
|-|-|-|-|
| Module | ESP32-S3-WROOM-N16R8 | N/A<sup>1</sup> | ESP32-WROOM32 |
| Processor | ESP32-S3 | ESP32-S3 | ESP32 |
| Flash | 16MB | 16 MB | 16 MB |
| SRAM | 512 KB | 512 KB | 520 KB |
| PSRAM | 8MB | 8 MB | N/A |
| Wi-Fi | 2.4 GHz b/g/n | 2.4 GHz b/g/n | 2.4 GHz b/g/n |
| Bluetooth | Bluetooth 5 LE | Bluetooth 5 LE | Bluetooth 4.2 LE |
| Deep Sleep Current | 10 uA | 20 uA | 12 uA |
| Lowest Power State Current | 1.5 uA (Shutdown Mode) | 20 uA (Deep Sleep) | 20 uA (Deep Sleep) |
| 3.3 Max Current | 750mA | 2 x 600mA | 300 mA |
| 5V Max Current | 2A | | |
| Max Charging Current | 2A | | |
| Max Charging Current Adjustment | Firmware - Charger I2C interface | Replace soldered resistor | Replace soldered resistor |
| Charge measurement | Fuel Gauge IC | Voltage divider | Voltage divider |
| STEMMA QT | 1 | 2 | N/A |


1. FeatherS3 does not use a module, instead using bare ESP32-S3 SOC. The advantage of using modules is that they have [certifications](https://www.espressif.com/en/support/documents/certificates).