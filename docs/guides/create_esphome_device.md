---
keywords:
    - esp32
    - powerfeather
    - esphome
sidebar_position: 4
---

# Creating an ESPHome Device

The ESPHome integration exposes the board's supply, battery, output,
charging, and power-state controls to Home Assistant. The current integration is the `powerfeather` external component and uses PowerFeather-SDK V2.

## Start a Device Config

Create a normal ESPHome config for an ESP32-S3 board, then add the PowerFeather external component:

```yaml
substitutions:
  name: powerfeather
  friendly_name: PowerFeather

esphome:
  name: ${name}
  friendly_name: ${friendly_name}
  platformio_options:
    board_build.flash_mode: dio

esp32:
  board: esp32-s3-devkitc-1
  variant: esp32s3
  framework:
    type: esp-idf

logger:

api:
  encryption:
    key: !secret api_encryption_key

ota:
  - platform: esphome
    password: !secret ota_password

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  ap:
    ssid: "${friendly_name} Fallback"
    password: !secret fallback_ap_password

captive_portal:

external_components:
  - source: github://powerfeatherdev/esphome-powerfeather@main
    components: [powerfeather]
```

The source repository is
[`PowerFeather/esphome-powerfeather`](https://github.com/PowerFeather/esphome-powerfeather).
For production devices, use a tagged release instead of `@main` once one is
available.

## Configure the Mainboard

Add one `powerfeather.mainboard` object. Each ESPHome config represents one
physical PowerFeather board.

```yaml
powerfeather:
  mainboard:
    id: powerfeather_mainboard
    board_revision: v2
    battery:
      capacity: 1000
      type: Generic_3V7
    update_interval: 10s
```

Choose the settings that match your hardware:

| Option | Values | Notes |
| --- | --- | --- |
| `board_revision` | `v1`, `v2` | Defaults to PowerFeather V1. Use the value `v2` for PowerFeather V2 hardware. |
| `battery.capacity` | `0`, or a board-specific mAh value | Use `0` when no battery is configured. V1 accepts 50 to 6000 mAh. V2 accepts 1 to 16383 mAh. |
| `battery.type` | `Generic_3V7`, `ICR18650_26H`, `UR18650ZY`, `Generic_LFP` | `Generic_LFP` requires `board_revision: v2`. |
| `update_interval` | `500ms` or longer | Defaults to `10s`. Applies to published measurements. |

The component supports both `esp-idf` and `arduino` ESPHome frameworks.

## Add Home Assistant Entities

Entities are configured under the same `mainboard` block. Add only the entities
you want exposed.

```yaml
powerfeather:
  mainboard:
    id: powerfeather_mainboard
    board_revision: v2
    battery:
      capacity: 1000
      type: Generic_3V7

    sensors:
      supply_voltage:
        name: "${friendly_name} Supply Voltage"
      supply_current:
        name: "${friendly_name} Supply Current"
      battery_voltage:
        name: "${friendly_name} Battery Voltage"
      battery_current:
        name: "${friendly_name} Battery Current"
      battery_charge:
        name: "${friendly_name} Battery Charge"
      battery_health:
        name: "${friendly_name} Battery Health"
      battery_cycles:
        name: "${friendly_name} Battery Cycles"
      battery_time_left:
        name: "${friendly_name} Battery Time Left"
      battery_temperature:
        name: "${friendly_name} Battery Temperature"

    binary_sensors:
      supply_good:
        name: "${friendly_name} Supply Good"

    switches:
      enable_EN:
        name: "${friendly_name} Enable EN Pin"
      enable_3V3:
        name: "${friendly_name} Enable 3V3"
      enable_VSQT:
        name: "${friendly_name} Enable VSQT"
      enable_battery_temp_sense:
        name: "${friendly_name} Enable Battery Temperature Sense"
      enable_battery_charging:
        name: "${friendly_name} Enable Battery Charging"
      enable_battery_fuel_gauge:
        name: "${friendly_name} Enable Battery Fuel Gauge"
      enable_stat:
        name: "${friendly_name} Enable STAT LED"

    numbers:
      supply_maintain_voltage:
        name: "${friendly_name} Supply Maintain Voltage"
      battery_charging_max_current:
        name: "${friendly_name} Battery Charging Max Current"

    buttons:
      update_battery_fuel_gauge_temp:
        name: "${friendly_name} Update Fuel Gauge Temperature"
```

Keep `ship_mode`, `shutdown`, and `powercycle` buttons out of routine dashboards
unless you want those actions available from Home Assistant:

```yaml
powerfeather:
  mainboard:
    buttons:
      ship_mode:
        name: "${friendly_name} Ship Mode"
      shutdown:
        name: "${friendly_name} Shutdown"
      powercycle:
        name: "${friendly_name} Powercycle"
```

## LiFePO4 Batteries

LiFePO4 support is available on ESP32-S3 PowerFeather V2 only:

```yaml
powerfeather:
  mainboard:
    board_revision: v2
    battery:
      capacity: 1000
      type: Generic_LFP
```

## Migrating from the Old Syntax

ESPHome integration v2.0.0.  changes the component name and moves all entities under
`powerfeather.mainboard`.

| Old syntax | New syntax |
| --- | --- |
| `components: [powerfeather_mainboard]` | `components: [powerfeather]` |
| `powerfeather_mainboard:` | `powerfeather: mainboard:` |
| `battery_capacity: 1000` | `battery: capacity: 1000` |
| `battery_type: Generic_3V7` | `battery: type: Generic_3V7` |
| Separate `sensor:`, `binary_sensor:`, `switch:`, `number:`, and `button:` platform blocks | Nested `sensors:`, `binary_sensors:`, `switches:`, `numbers:`, and `buttons:` under `mainboard` |
| `platform: powerfeather_mainboard` and `mainboard_id` | Removed |

For example, this old sensor block:

```yaml
sensor:
  - platform: "powerfeather_mainboard"
    mainboard_id: "my_powerfeather"
    battery_voltage:
      name: "Battery Voltage"
```

becomes:

```yaml
powerfeather:
  mainboard:
    sensors:
      battery_voltage:
        name: "Battery Voltage"
```

## Entity Reference

### Sensors

| Key | Unit | Notes |
| --- | --- | --- |
| `supply_voltage` | V | Input supply voltage. |
| `supply_current` | mA | Input supply current. |
| `battery_voltage` | V | Battery voltage. |
| `battery_current` | mA | Battery current. |
| `battery_charge` | % | Fuel gauge state of charge. |
| `battery_health` | % | Fuel gauge state of health. |
| `battery_cycles` | count | Fuel gauge cycle count. |
| `battery_time_left` | min | Fuel gauge time estimate. |
| `battery_temperature` | C | Battery temperature; unknown when battery temperature sensing is disabled. |

### Binary Sensors

| Key | Notes |
| --- | --- |
| `supply_good` | Whether the USB or `VDC` input supply is good. |

### Switches

| Key | Notes |
| --- | --- |
| `enable_EN` | Controls the `EN` pin for connected Feather Wings. |
| `enable_3V3` | Enables or disables the `3V3` output. |
| `enable_VSQT` | Enables or disables the STEMMA QT `VSQT` output. Disabling this also cuts off access to the fuel gauge and charger IC. |
| `enable_battery_temp_sense` | Enables or disables battery temperature sensing. |
| `enable_battery_charging` | Enables or disables battery charging. |
| `enable_battery_fuel_gauge` | Enables or disables the battery fuel gauge. Disabling this also disables fuel-gauge-backed sensors. |
| `enable_stat` | Enables or disables the charger STAT LED. |

### Numbers

| Key | Unit | Range | Step | Notes |
| --- | --- | --- | --- | --- |
| `supply_maintain_voltage` | V | 4.6 to 16.8 | 0.012 | Charger input voltage regulation target. |
| `battery_charging_max_current` | mA | 40 to 2000 | 4 | Charger current limit. |
| `battery_low_voltage_alarm` | V | 0 to 5.0 on V1, 0 to 5.1 on V2 | 0.01 | Battery low-voltage alarm threshold. |
| `battery_high_voltage_alarm` | V | 0 to 5.0 on V1, 0 to 5.1 on V2 | 0.01 | Battery high-voltage alarm threshold. |
| `battery_low_charge_alarm` | % | 0 to 100 | 1 | Battery low-charge alarm threshold. |

Battery alarm thresholds are write-only in the SDK. ESPHome will show them as
unknown at boot until you set them from Home Assistant or a YAML automation.

### Buttons

| Key | Notes |
| --- | --- |
| `update_battery_fuel_gauge_temp` | Sends the current battery temperature to the fuel gauge. |
| `ship_mode` | Enters ship mode, which exits by pulling `QON` low or plugging in a supply. |
| `shutdown` | Enters shutdown mode, which exits by plugging in a supply. |
| `powercycle` | Requests a board power cycle. |
