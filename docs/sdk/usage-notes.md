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

## Shared Across 1.x And 2.x

### Battery handling

- Install the battery before first power-on and keep it connected until the device is powered off.
- Hot-swapping a battery on a live device is not supported.

### Power states

- `enterShipMode()` and `enterShutdownMode()` require external input power to be absent.
- If USB or another valid supply is still connected, the charger rejects these requests.

### Charger safety defaults

- Battery temperature-fault protection is disabled by default.
- Call `enableBatteryTempSense(true)` after `init()` if you want the charger to reduce or stop charging when the thermistor reading is out of range.

- `setBatteryChargingMaxCurrent()` clamps only to charger hardware limits.
- The SDK does not automatically enforce a 1C charging rule based on the configured battery capacity, so callers must choose a cell-safe current.

### Fuel-gauge and measurement behavior

- `getBatteryVoltage()` may temporarily use the charger's VBAT ADC path if the fuel gauge is unavailable.
- Normal readings come from the board's fuel gauge, but callers should not assume the same source is always used during early boot or transient recovery states.

- Charger-backed battery and supply getters can block for around 100 ms while waiting for ADC refresh.
- This affects functions such as `getSupplyVoltage()`, `getSupplyCurrent()`, `getBatteryCurrent()`, and `getBatteryTemperature()`.

## V2 Only

### Battery chemistry and profiles

- `BatteryType::Generic_LFP` is supported only on V2 boards.
- V1 uses the LC709204F fuel gauge and does not provide an LFP profile.

- Custom `MAX17260::Model` profiles must provide a sane `chargeVoltageMv`.
- The SDK validates the general `3500-4800 mV` range, but it does not verify that the chosen charge voltage matches the selected chemistry.

### Small-battery support

- On V2, configured battery capacities below `50 mAh` are supported for monitoring only.
- In that mode, battery charging remains unavailable and charge-current configuration is rejected.
