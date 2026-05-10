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
- Depending on the state of `VBUS` during a live battery swap, charger or fuel-gauge power-on-reset can occur, and the fuel gauge can retain learned state from the previous cell.
- If charger power-on-reset occurs, the cell can briefly see the charger's 4.2 V power-on default until the next SDK call that touches the charger. For LFP packs configured below 4.2 V, power the device off before changing cells.

### Power and sleep behavior

- `enterShipMode()` and `enterShutdownMode()` require `VBUS` to be below the charger's UVLO threshold.
- If USB or another valid supply is still connected, the charger rejects these requests. Unplug USB before calling either function.

- `VSQT` controls power to the STEMMA QT connector.
- On V1, disabling `VSQT` also disables access to the power-management I2C devices. On V2, the charger and fuel gauge remain accessible with `VSQT` disabled.

- Across deep sleep or another RTC-retaining warm boot, charger settings changed through public setters are retained only when the battery or profile configuration still matches.
- If the battery capacity, battery type, profile, or no-battery mode changes, initialization re-applies safe defaults instead of reusing retained charger settings.

### Charger safety defaults

- In the 2.x API, high-level `Mainboard` voltage APIs use `float` values in volts. Current APIs use `float` values in milliamperes.
- For example, code that passed `4600` mV to `setSupplyMaintainVoltage()` in 1.x should pass `4.6f` in 2.x.

- Battery temperature-fault protection is disabled by default.
- Call `enableBatteryTempSense(true)` after `init()` if you want the charger to reduce or stop charging when the thermistor reading is out of range.

- The SDK does not program cold-side NTC thresholds (`TH1`-`TH3`).
- If charging below 0 C is a concern, gate charging from your application using `getBatteryTemperature()`.

- `setBatteryChargingMaxCurrent()` clamps only to charger hardware limits (40-2000 mA), not to battery capacity.
- The SDK does not automatically enforce a 1C charging rule based on the configured battery capacity, so callers must choose a cell-safe current.
- The BQ charger encodes charge current in 40 mA steps. The SDK rounds requests down to the nearest supported step, so the default 50 mA request programs a 40 mA charger limit.

- `setSupplyMaintainVoltage()` programs the charger VINDPM request, not a guaranteed exact input threshold.
- The BQ charger's input-voltage regulation behavior can also be influenced by its battery-tracking policy, so the effective regulation point can be higher than the value written by the SDK.

### Fuel-gauge and measurement behavior

- `getBatteryVoltage()` may temporarily use the charger's VBAT ADC path if the fuel gauge is unavailable.
- This fallback can happen during early boot or when the fuel gauge is not ready or not responding. Normal readings come from the board's fuel gauge, but callers should not assume the same source is always used during transient recovery states.
- The charger fallback is less precise: about 1.99 mV LSb. Normal fuel-gauge readings are 78.125 uV LSb on V2 (MAX17260) and 1 mV LSb on V1 (LC709204F).

- Fuel-gauge learned state, such as state of health (SOH), cycle count, and time-to-empty, is not valid after a battery change.
- If a battery is swapped without a clean power-off and fresh `init()` sequence, the fuel gauge can report plausible-looking values from the previous cell until enough full charge and discharge cycles overwrite them.

- Charger-backed battery and supply getters can block for around 100 ms while waiting for ADC refresh.
- Power-management I2C faults can add several 50 ms transaction timeout windows before the call returns failure.
- The SDK releases its internal mutex while waiting for ADC refresh, but other tasks can still wait up to the mutex timeout before receiving `Result::LockFailed`.
- This affects functions such as `getSupplyVoltage()`, `getSupplyCurrent()`, `getBatteryTemperature()`, V1 `getBatteryCurrent()`, and the charger fallback path in `getBatteryVoltage()`.
- On V2, `getBatteryCurrent()` reads from the MAX17260 fuel gauge and requires the fuel gauge to be enabled.
- On V1, `getBatteryCurrent()` uses the BQ25628E charger `IBAT_ADC` reading and cannot report discharge current while charging is disabled. BQ25628E Table 8-35 states that `IBAT_ADC` resets to zero when `EN_CHG=0`, so the SDK returns `Result::NotReady` instead of reporting a misleading zero current.

- `getBatteryTemperature()` requires a Semitec 103AT thermistor on the `TS` pin.
- The function returns `Failure` when the thermistor reading is outside the plausible range, such as when the thermistor is missing, open, or shorted.

## V2 Boards Only

### Battery chemistry and profiles

- `BatteryType::Generic_LFP` is supported only on V2 boards.
- V1 uses the LC709204F fuel gauge and does not provide an LFP profile.
- On V2, `BatteryType::Generic_LFP` uses the MAX17260 EZ LFP profile. The SDK programs a 3.6 V charge voltage and an LFP-tuned fuel-gauge empty threshold (`VE = 2.50 V`, `VR = 3.00 V`).
- For production-grade LFP state-of-charge (SOC) and state-of-health (SOH) reporting, prefer a cell-characterized `MAX17260::Model` passed to `init(const MAX17260::Model &)`.

- Custom `MAX17260::Model` profiles must provide a sane `chargeVoltage`.
- The SDK validates the general `3.5-4.8 V` range, but it does not verify that the chosen charge voltage matches the selected chemistry.
- The `chargeVoltage` field is applied directly to the charger VREG/CV constant-voltage limit. An incorrect value can overcharge the connected cell.
- The profile's `ichgTerm` is converted from MAX17260 register units and applied to the charger termination-current setting. Profiles whose termination current is outside the charger-supported `5-310 mA` range are rejected.
- When upgrading from SDK versions that used the older raw-byte custom-profile hash, the first boot with a custom profile may treat the profile as changed and reinitialize the MAX17260 once, discarding learned state. Built-in battery profiles are not affected, and later boots with the same custom profile preserve learned state normally.

### Small-battery support

- On V2, configured battery capacities below `50 mAh` are supported for monitoring only.
- In that mode, battery charging remains unavailable and charge-current configuration is rejected.

### Long idle with charging enabled

- LFP charging is not an unattended charger-POR supervision feature. For LFP deployments, call a charger-backed getter at least every 30 s while charging.
- `getSupplyVoltage()` and `getSupplyCurrent()` qualify. `getBatteryTemperature()` also qualifies after `enableBatteryTempSense(true)`.
- These calls talk to the charger and trigger the SDK's post-power-on-reset reapply check. Rare charger power-on-reset events from pack-protection trips or supply transients otherwise leave the chip at POR defaults, including the default 4.2 V charge limit, until the next SDK call that touches the charger. `getBatteryVoltage()` normally reads from the fuel gauge and does not trigger the reapply check.
  `getBatteryCurrent()` on V2 also reads from the fuel gauge, so it is not a charger-backed keepalive call.

### Alarms

- `setBatteryHighVoltageAlarm(0)` disables the high-voltage alarm by writing an unreachable 5100 mV threshold internally.
- This is the documented disable mechanism; it does not mean "alarm at 0 V."
