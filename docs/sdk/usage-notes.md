---
title: Usage Notes
sidebar_position: 1
parse_number_prefixes: false
slug: /sdk/usage-notes
displayed_sidebar: defaultSidebar
keywords:
    - esp32
    - powerfeather
    - sdk
    - usage notes
    - battery
    - charging
---

# Usage Notes

This page lists behaviors, defaults, and call-sequence constraints that are intentional but may surprise callers. These items describe the SDK's supported usage envelope, not known bugs.

V1 and V2 refer to ESP32-S3 PowerFeather board revisions.

## Shared Across V1 And V2 Boards

### Battery handling

- Install the battery before first power-on and keep it connected until the device is powered off.
- Hot-swapping a battery on a live device is not supported.

### Power and sleep behavior

- `enterShipMode()` and `enterShutdownMode()` require external input power to be absent.
- If USB or another valid supply is still connected, the charger rejects these requests.

- `VSQT` controls power to the STEMMA QT connector.
- On V1, disabling `VSQT` also disables access to the power-management I2C devices. On V2, the charger and fuel gauge remain accessible with `VSQT` disabled.

- Across deep sleep or another RTC-retaining warm boot, charger settings changed through public setters are retained only when the battery or profile configuration still matches.
- If the battery capacity, battery type, profile, or no-battery mode changes, initialization re-applies safe defaults instead of reusing retained charger settings.

### Charger safety defaults

- In the 2.x API, high-level `Mainboard` voltage APIs use `float` volts. Current APIs use `float` milliamps.
- For example, code that passed `4600` mV to `setSupplyMaintainVoltage()` in 1.x should pass `4.6f` in 2.x.

- Battery temperature-fault protection is disabled by default.
- Call `enableBatteryTempSense(true)` after `init()` if you want the charger to reduce or stop charging when the thermistor reading is out of range.

- The SDK does not program cold-side NTC thresholds.
- If charging below 0 C is a concern, gate charging from your application using `getBatteryTemperature()`.

- `setBatteryChargingMaxCurrent()` clamps only to charger hardware limits, not to battery capacity.
- The SDK does not automatically enforce a 1C charging rule based on the configured battery capacity, so callers must choose a cell-safe current.

### Fuel-gauge and measurement behavior

- `getBatteryVoltage()` may temporarily use the charger's VBAT ADC path if the fuel gauge is unavailable.
- Normal readings come from the board's fuel gauge, but callers should not assume the same source is always used during early boot or transient recovery states.

- Charger-backed battery and supply getters can block for around 100 ms while waiting for ADC refresh.
- This affects functions such as `getSupplyVoltage()`, `getSupplyCurrent()`, `getBatteryTemperature()`, and V1 `getBatteryCurrent()`.
- On V2, `getBatteryCurrent()` reads from the MAX17260 fuel gauge and requires the fuel gauge to be enabled.

- `getBatteryTemperature()` requires a Semitec 103AT thermistor on the `TS` pin.
- The function returns `Failure` when the thermistor reading is outside the plausible range, such as when the thermistor is missing, open, or shorted.

## V2 Boards Only

### Battery chemistry and profiles

- `BatteryType::Generic_LFP` is supported only on V2 boards.
- V1 uses the LC709204F fuel gauge and does not provide an LFP profile.

- Custom `MAX17260::Model` profiles must provide a sane `chargeVoltage`.
- The SDK validates the general `3.5-4.8 V` range, but it does not verify that the chosen charge voltage matches the selected chemistry.

### Small-battery support

- On V2, configured battery capacities below `50 mAh` are supported for monitoring only.
- In that mode, battery charging remains unavailable and charge-current configuration is rejected.
