---
keywords:
    - esp32
    - powerfeather
    - esphome
sidebar_position: 4
---

# Creating an ESPHome Device

:::info
ESPHome support is currently a work-in-progress. Currently there is only a single component, `powerfeather_mainboard`.
:::

## Configuration

Since the components lives out-of-tree from the official [`esphome` repository](https://github.com/esphome/esphome),
ESPHome needs to know where the external components are. This can be done with the following snippet:

```yaml
external_components:
  - source: 
      type: git
      url: https://github.com/PowerFeather/esphome-powerfeather
      ref: main # for latest version of the component, can also be another branch or tag
    components: [powerfeather_mainboard]
```

### `powerfeather_mainboard`

This component allows easy access to the PowerFeather's power monitoring and management features. 

#### Main

In order to actually use the component, its basic configuration needs to be specified:

```yaml
powerfeather_mainboard:
  id: "my_powerfeather"
  battery_capacity: 1000 # 1000 mAh
  battery_type: "Generic_3V7" # generic Lipo/Li-ion cell
  update_interval: 5s # sensors are updated every 5s
```

- **battery_capacity**: the design capacity of the battery connected to the board, minimum 50 mAh; defaults to 0 mAh if not specified (assumes no battery is connected - some sensors might not work).
- **battery_type**: type of LiPo/Li-Ion battery connected to the board (other values are `"ICR18650_26H"` and `"UR18650ZY"`); defaults to `Generic_3V7` if not specified.
- **id**: identifier for the current board; used in sensor, switch, etc. configuration
- **update_interval**: how often the sensors (all types) are updated, defaults to `10s` if not specified.

#### Sensor

The required arguments are `platform` and `mainboard_id`. For `platform`, specify `"powerfeather_mainboard"`.

For `mainboard_id`, specify the same as `id` in the `powerfeather_mainboard` main configuration.

```yaml
sensor:
  - platform: "powerfeather_mainboard"
    mainboard_id: "my_powerfeather"
    supply_voltage:
      name: "Supply Voltage"
    supply_current:
      name: "Supply Current"
    battery_voltage:
      name: "Battery Voltage"
    battery_current:
      name: "Battery Current"
    battery_charge:
      name: "Battery Charge"
    battery_health:
      name: "Battery Health"
    battery_cycles:
      name: "Battery Cycles"
    battery_time_left:
      name: "Battery Time Left"
    battery_temperature:
      name: "Battery Temperature"
```

Pick and choose from below which sensors are enabled:

- **supply_voltage**: supply voltage plugged into the USB port or `VDC` pin, in mV.
- **supply_current**: current supplied by the USB or `VDC` supply, in mA.
- **battery_voltage**: battery voltage in mV.
- **battery_current**: battery current in mA, negative when discharging and positive when charging.
- **battery_charge**: battery charge level estimate in percent
- **battery_health**: battery health estimate in percent
- **battery_cycles**: battery cycles estimate count
- **battery_time_left**: time-to-full/time-to-empty in minutes, negative when discharging and positive when charging.
- **battery_temperature**: battery temperature measured from the 103AT thermistor connected to the `TS` pin in celsius.

For each of the above a `name` should be specified, which serves as the corresponding sensor's label in the dashboard.

#### Binary Sensor

The required arguments are `platform` and `mainboard_id`. For `platform`, specify `"powerfeather_mainboard"`.

For `mainboard_id`, specify the same as `id` in the `powerfeather_mainboard` main configuration.

```yaml
binary_sensor:
  - platform: "powerfeather_mainboard"
    mainboard_id: "my_powerfeather"
    supply_good:
      name: "Supply Good"
```

- **supply_good**: indicates if the supply (USB or `VDC`) is good, as determined by the battery charger IC.

A `name` should be specified, which serves as the binary sensor's label in the dashboard.

#### Switch

The required arguments are `platform` and `mainboard_id`. For `platform`, specify `"powerfeather_mainboard"`.

For `mainboard_id`, specify the same as `id` in the `powerfeather_mainboard` main configuration.

```yaml
switch:
  - platform: "powerfeather_mainboard"
    mainboard_id: "my_powerfeather"
    enable_3V3:
      name: "Enable 3V3"
    enable_VSQT:
      name: "Enable VSQT"
    enable_battery_temp_sense:
      name: "Enable Battery Temperature Sense"
    enable_battery_charging:
      name: "Enable Battery Charging"
    enable_battery_fuel_gauge:
      name: "Enable Battery Fuel Gauge"
    enable_stat:
      name: "Enable STAT LED"
```

Pick and choose from below which switches are available:

- **enable_3V3**: enables/disables 3.3V output on the `3V3` pin
- **enable_VSQT**: enables/disables the 3.3V output on the STEMMA QT header; note that by disabling this, access to the fuel gauge and charger IC is also disabled, disabling most power monitoring and management.
- **enable_battery_temp_sense**: enables/disables battery temperature sensing.
- **enable_battery_charging**: enables/disables battery charging.
- **enable_battery_fuel_gauge**: enables/disables the battery fuel gauge; note that by disabling this some sensors will be also be disabled.
- **enable_stat**: enables/disables the STAT LED from turning on during charging, or blinking in error conditions.

For each of the above a `name` should be specified, which serves as the corresponding switch's label in the dashboard.

#### Number

The required arguments are `platform` and `mainboard_id`. For `platform`, specify `"powerfeather_mainboard"`.

For `mainboard_id`, specify the same as `id` in the `powerfeather_mainboard` main configuration.

```yaml
number:
  - platform: "powerfeather_mainboard"
    mainboard_id: "my_powerfeather"
    supply_maintain_voltage:
      name: "Supply Maintain Voltage"
    battery_charging_max_current:
      name: "Battery Charging Max Current"
```

- **supply_maintain_voltage**: the charger IC regulates current draw such that the supply voltage does not go below this value; can also be thought of the supply's max-power-point voltage.
- **battery_charging_max_current**: the maximum current at which the charger IC should charge the battery.

For each of the above a `name` should be specified, which serves as the corresponding number's label in the dashboard.

#### Button

The required arguments are `platform` and `mainboard_id`. For `platform`, specify `"powerfeather_mainboard"`.

For `mainboard_id`, specify the same as `id` in the `powerfeather_mainboard` main configuration.

```yaml
button:
  - platform: "powerfeather_mainboard"
    mainboard_id: "my_powerfeather"
    ship_mode:
      name: "Ship Mode"
    shutdown:
      name: "Shutdown"
    powercycle:
      name: "Powercycle"
```

- **ship_mode**: put the board in ship mode, a low-power (~1.5uA) power state which can only be exited by pulling `QON` low or plugging in a supply.
- **shutdown**: put the board in ship mode, a low-power (~1.4uA) power state which can only be exited by plugging in a supply.
- **powercycle**: powercycle the components on the board powered by the charger IC (not just a reset of the board's microcontroller).

For each of the above a `name` should be specified, which serves as the corresponding buttons's label in the dashboard.