---
keywords:
    - esp32
    - powerfeather
    - sdk
    - api
    - mainboard
    - power management
    - power monitoring
sidebar_position: 1
---

# Mainboard

## class Mainboard

### enum class BatteryType

- `Generic_3V7` Generic Li-ion/LiPo, 3.7 V nominal and 4.2 V max
- `ICR18650_26H` Samsung ICR18650-26H
- `UR18650ZY` Panasonic UR18650ZY

### [Result](./result.md#enum-class-result) init(uint16_t capacity = 0, [BatteryType](#enum-class-batterytype) type = [BatteryType](#enum-class-batterytype)::`Generic_3V7`)

#### Brief
Initialize the board power management and monitoring features.

#### Description
Initializes the battery charger, battery fuel gauge and other hardware related to power management and monitoring.

Sets the following defaults:
 - `EN`: high
 - `3V3`: enabled
 - `VSQT`: enabled
 - Charging: disabled
 - Maximum battery charging current: 50 mA
 - Maintain supply voltage: 4600 mV
 - Fuel gauge: enabled if **capacity** is non-zero; disabled if **capacity** is zero
 - Battery temperature sense: disabled
 - Battery alarms (low charge, high/low voltage): disabled

This function should be called once, before calling all other [Mainboard](#class-mainboard) functions.

#### Parameters

- **capacity** [in] The capacity of the connected Li-ion/LiPo battery in milliamp-hours (mAh), from 50 mAh to 6000 mAh.
A value of zero indicates that no battery is connected, and therefore some of the other [Mainboard](#class-mainboard) functions
will return [Result](./result.md#enum-class-result)::`InvalidState`. If using multiple batteries connected in parallel, specify
only the capacity for one cell. Ignored when **type** is [BatteryType](#enum-class-batterytype)::`ICR18650_26H` or [BatteryType](#enum-class-batterytype)::`UR18650ZY`.
- **type** [in] Type of Li-ion/LiPo battery; ignored when **capacity** is zero, except when value is [BatteryType](#enum-class-batterytype)::`ICR18650_26H` or [BatteryType](#enum-class-batterytype)::`UR18650ZY`.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the board was initialized successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) setEN(bool high)

#### Brief

Set `EN` pin high or low.

#### Description

This is useful for enabling or disabling connected Feather Wings to reduce power consumption.

#### Parameters

- **high** [in] If `true`, EN is set high; if `false`, EN is set low.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if `EN` was set high or low successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) enable3V3(bool enable)

#### Brief

Enable or disable `3V3`.

#### Description

Enables or disables `3V3`, the 3.3 V header pin power output. When disabled, power to the connected loads on `3V3` is cut, reducing power consumption.

#### Parameters

- **enable** [in] If `true`, `3V3` is enabled; if `fals`, `3V3` is disabled.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if `3V3` was enabled or disabled successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) enableVSQT(bool enable)

#### Brief

Enable or disable `VSQT`.

#### Description

Enables or disables `VSQT`, the 3.3 V STEMMA QT power output. When disabled, power to the
connected STEMMA QT modules is cut, reducing power consumption.

A side effect of disabling `VSQT` is that communications to the battery charger and fuel gauge is also disabled.
This means that some of the other [Mainboard](#class-mainboard) functions will return [Result](./result.md#enum-class-result)::`InvalidState` when
`VSQT` is disabled. Make sure to enable `VSQT` prior to calling these functions.

#### Parameters

- **enable** [in] If `true`, `VSQT` is enabled; if `false`, `VSQT` is disabled.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if `VSQT` was enabled or disabled successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) enableSTAT(bool enable)

#### Brief

Enable or disable the `STAT`  LED.

#### Description

Normally, the `STAT` LED turns on when charging, or blinks when there is an error preventing
charging (when battery temperature exceeds the set threshold, for example).
This function can enable/disable this LED from turning on in these cases.

One instance where disabling this LED is desirable is during low-sunlight charging conditions,
where the current extracted from the solar panel should be used to charge the battery as
much as possible.

#### Parameters

- **enable** [in] If `true`, `STAT` LED is enabled; if `false`, `STAT` LED is disabled.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if `STAT` LED was enabled or disabled successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) getSupplyVoltage(uint16_t &voltage)

#### Brief

Measure the supply voltage.

#### Description

Measures the `VUSB` or `VDC` voltage. `VUSB` is the power input from the USB-C connector,
while `VDC` is the power input from the header pin. Resolution is 4 mV.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

This function can block for 100 ms.

#### Parameters

- **voltage** [out] The measured voltage in millivolts (mV).

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the supply voltage was measured successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) getSupplyCurrent(int16_t &current)

#### Brief

Measure the supply current.

#### Description

Measures the current drawn from `VUSB` or `VDC`. `VUSB` is the power input from the USB-C connector,
while `VDC` is the power input from the header pin. Resolution is 2 mA.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

This function can block for 100 ms.

#### Parameters

- **voltage** [out] The measured current draw in milliamperes (mA).

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the supply current was measured successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) checkSupplyGood(bool &good)

#### Brief

Check if the supply is good.

#### Description

Checks if the supply, whether `VUSB` or `VDC` is good as determined by the battery charger. A good supply
means that it powers the board and connected loads, not the battery.

#### Parameters

- **good** [out] If `true`, the charger has determined the supply to be good; `false` if not.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the supply was checked successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) setSupplyMaintainVoltage(uint16_t voltage)

#### Brief

Set the supply voltage to maintain.

#### Description

The battery charger dynamically regulates the current drawn from the supply to prevent it from collapsing under
the set voltage to maintain. This is useful for specifying the maximum power point (MPP) voltage if using a
solar panel; allowing the battery charger to extract power from the panel at near-MPPT effectiveness.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

#### Parameters

- **voltage** [in] The supply voltage to maintain in millivolts (mV), up to 16800 mV.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the supply voltage to maintain was set successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) enterShipMode()

#### Brief

Enter ship mode.

#### Description

Ship mode is a power state that only consumes around 1.5 μA. Only the battery charger and
the battery fuel gauge is powered.

This mode can only be entered into if the battery is powering the board and connected loads;
that is, if [Mainboard](#result-checksupplygoodbool-good)::`checkSupplyGood` output parameter **good** is `false`.

Ship mode can be exited by either (1) pulling `QON` header pin low for around 800 ms or
(2) connecting a power supply which the battery charger determines to be good.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

This function can block for 30 ms if it fails to enter ship mode.

#### Return

Does not return if ship mode was successfully entered into;
returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) enterShutdownMode()

#### Brief

Enter shutdown mode.

#### Description

Shutdown mode is a power state that only consumes around 1.4 μA. Only the battery charger and
the battery fuel gauge is powered.

This mode can only be entered into if the battery is powering the board and connected loads;
that is, if [Mainboard](#result-checksupplygoodbool-good)::`checkSupplyGood` output parameter **good** is `false`.

Shutdown mode can only be exited by connecting a power supply which the battery charger determines to be good.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

This function can block for 30 ms if it fails to enter shutdown mode.

#### Return

Does not return if shutdown mode was successfully entered into;
returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) doPowerCycle()

#### Brief

Perform a power cycle.

#### Description

For all components on the board and connected loads, except the battery fuel gauge
and loads connected to `VS` (supply output header pin, whichever of `VUSB` and `VDC`),
the power cycle provides complete reset by removing power and re-applying it after a short delay.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

#### Return

Does not return if a power cycle was performed successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) enableBatteryCharging(bool enable)

#### Brief

Enable or disable battery charging.

#### Description

This is useful when opting to not fully charge a battery in order to prolong its lifespan.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

A non-zero **capacity** or **type** of  [BatteryType](#enum-class-batterytype)::`ICR18650_26H`/[BatteryType](#enum-class-batterytype)::`UR18650ZY` should have been specified when [Mainboard](#class-mainboard)::init was called, else
 [Result](./result.md#enum-class-result)::`InvalidState` is returned.

#### Parameters

- **enable** [in] If `true`, battery charging is enabled; if `false`, battery charging is disabled.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if battery charging was enabled or disabled successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) setBatteryChargingMaxCurrent(uint16_t current)

#### Brief

Set maximum battery charging current.

#### Description

Ensures that the battery is not charged with a current more than the amount specified using this function.
This is useful for batteries with small capacities, since it is not recommended to charge a battery at
more than 1C. For example, when charging a 550 mAh battery, a current of no more than 550 mA is
recommended. That current limit of 550 mA can be specified using this function.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

A non-zero **capacity** or **type** of  [BatteryType](#enum-class-batterytype)::`ICR18650_26H`/[BatteryType](#enum-class-batterytype)::`UR18650ZY` should have been specified when [Mainboard](#class-mainboard)::init was called, else
 [Result](./result.md#enum-class-result)::`InvalidState` is returned.

#### Parameters

- **current** [in] The maximum charging current in milliamps (mA), up to 2000 mA.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the maximum battery charging current was set successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) enableBatteryTempSense(bool enable)

#### Brief

Enable or disable battery temperature measurement.

#### Description

Enables or disables battery temperature measurement using the thermistor connected to the `TS` pin.
If enabled, aside from measurement, the battery charger performs temperature-based battery charging current
reduction or cutoff.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

A non-zero **capacity** or **type** of  [BatteryType](#enum-class-batterytype)::`ICR18650_26H`/[BatteryType](#enum-class-batterytype)::`UR18650ZY` should have been specified when [Mainboard](#class-mainboard)::init was called, else
 [Result](./result.md#enum-class-result)::`InvalidState` is returned.

#### Parameters

- **enable** [in] If `true`, battery temperature measurement is enabled; if `false`, battery
temperature measurement is disabled.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the battery temperature measurement was enabled or
disabled successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) enableBatteryFuelGauge(bool enable)

#### Brief

Enable or disable the battery fuel guage.

#### Description

Disabling the battery fuel guage can save around 0.5 μA. However, once disabled, it
cannot keep track of battery information such as voltage, charge, health, cycle count, etc.
Nonetheless, this is useful when trying to reduce power as much as possible, such as when going
into ship mode or shutdown mode for a long time.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

A non-zero **capacity** or **type** of  [BatteryType](#enum-class-batterytype)::`ICR18650_26H`/[BatteryType](#enum-class-batterytype)::`UR18650ZY` should have been specified when [Mainboard](#class-mainboard)::init was called, else
 [Result](./result.md#enum-class-result)::`InvalidState` is returned.

#### Parameters

- **enable** [in] If `true`, the battery fuel gauge is enabled; if `false`, the battery fuel gauge is disabled.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the battery fuel gauge was enabled or disabled successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) getBatteryVoltage(uint16_t &voltage)

#### Brief

Measure battery voltage.

#### Description

Resolution is 2 mV.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

A non-zero **capacity** or **type** of  [BatteryType](#enum-class-batterytype)::`ICR18650_26H`/[BatteryType](#enum-class-batterytype)::`UR18650ZY` should have been specified when [Mainboard](#class-mainboard)::init was called, else
 [Result](./result.md#enum-class-result)::`InvalidState` is returned.

This function can block for 100 ms.

#### Parameters

- **voltage** [out] Measured battery voltage in millivolts (mV).

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the battery voltage was measured successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) getBatteryCurrent(int16_t &current)

#### Brief

Measure battery current.

#### Description

Measures the current to or from the battery during charging and discharging, respectively. Resolution is 4 mA.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

A non-zero **capacity** or **type** of  [BatteryType](#enum-class-batterytype)::`ICR18650_26H`/[BatteryType](#enum-class-batterytype)::`UR18650ZY` should have been specified when [Mainboard](#class-mainboard)::init was called, else
 [Result](./result.md#enum-class-result)::`InvalidState` is returned.

This function can block for 100 ms.

#### Parameters

- **current** [out] Measured battery voltage in milliamps (mA). If battery is discharging,
this value is negative; positive if battery is charging.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the battery current was measured successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) getBatteryCharge(uint8_t &percent)

#### Brief

Estimate battery charge.

#### Description

Gives an estimate of battery state-of-charge from 0% to 100%. This is useful to get a sense
if the battery still has much charge or is nearly empty.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

A non-zero **capacity** or **type** of  [BatteryType](#enum-class-batterytype)::`ICR18650_26H`/[BatteryType](#enum-class-batterytype)::`UR18650ZY` should have been specified when [Mainboard](#class-mainboard)::init was called, else
 [Result](./result.md#enum-class-result)::`InvalidState` is returned.

The battery fuel gauge must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

#### Parameters

- **percent** [out] Estimated battery charge in percent, from 0% to 100%.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the battery charge was estimated successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) getBatteryHealth(uint8_t &percent)

#### Brief

Estimate battery health.

#### Description

Gives an estimate of battery state-of-health from 0% to 100%. This is useful to get a
sense of how much the battery has degraded over time.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

A non-zero **capacity** or **type** of  [BatteryType](#enum-class-batterytype)::`ICR18650_26H`/[BatteryType](#enum-class-batterytype)::`UR18650ZY` should have been specified when [Mainboard](#class-mainboard)::init was called, else
 [Result](./result.md#enum-class-result)::`InvalidState` is returned.

The battery fuel gauge must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

#### Parameters

- **percent** [out] Estimated battery health in percent, from 0% to 100%.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the battery health was estimated successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) getBatteryCycles(uint16_t &cycles)

#### Brief

Estimate battery cycle count.

#### Description

Gives an estimate of the battery cycle count. This is useful to compare against the number of
cycle counts the battery is rated for.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

A non-zero **capacity** or **type** of  [BatteryType](#enum-class-batterytype)::`ICR18650_26H`/[BatteryType](#enum-class-batterytype)::`UR18650ZY` should have been specified when [Mainboard](#class-mainboard)::init was called, else
 [Result](./result.md#enum-class-result)::`InvalidState` is returned.

The battery fuel gauge must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

#### Parameters

- **cycles** [out] Estimated battery cycle count.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the battery cycle count was estimated successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) getBatteryTimeLeft(int &minutes)

#### Brief

Estimate time left for battery to charge or discharge.

#### Description

Gives an estimate of the battery time-to-empty or time-to-full in minutes. The battery charge must have
previously dropped and/or risen by a certain percentage to be able to estimate time-to-empty or time-to-full, respectively;
else [Result](./result.md#enum-class-result)::`NotReady` is returned.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

A non-zero **capacity** or **type** of  [BatteryType](#enum-class-batterytype)::`ICR18650_26H`/[BatteryType](#enum-class-batterytype)::`UR18650ZY` should have been specified when [Mainboard](#class-mainboard)::init was called, else
 [Result](./result.md#enum-class-result)::`InvalidState` is returned.

The battery fuel gauge must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

#### Parameters

- **minutes** [out] Estimated time left for battery to charge or discharge in minutes. If battery is discharging,
this value is negative; if battery is charging, this value is positive.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the time left for battery to charge or discharge was estimated
successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) getBatteryTemperature(float &celsius)

#### Brief

Measure battery temperature.

#### Description

Requires a Semitec 103AT thermistor to be connected to the `TS` pin and attached to the battery
for the measurement to be accurate.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

A non-zero **capacity** or **type** of  [BatteryType](#enum-class-batterytype)::`ICR18650_26H`/[BatteryType](#enum-class-batterytype)::`UR18650ZY` should have been specified when [Mainboard](#class-mainboard)::init was called, else
 [Result](./result.md#enum-class-result)::`InvalidState` is returned.

Battery temperature measurement must be enabled prior calling this function, else [Result](./result.md#enum-class-result)::`InvalidState`
is returned.

This function can block for 100 ms.

#### Parameters

- **celsius** [out] Measured battery temperature in celsius.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the battery temperature was measured successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) setBatteryLowVoltageAlarm(uint16_t voltage)

#### Brief

Set an alarm for battery low voltage.

#### Description

If battery voltage is less than the set voltage, the `ALARM` pin is pulled low.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

A non-zero **capacity** or **type** of  [BatteryType](#enum-class-batterytype)::`ICR18650_26H`/[BatteryType](#enum-class-batterytype)::`UR18650ZY` should have been specified when [Mainboard](#class-mainboard)::init was called, else
 [Result](./result.md#enum-class-result)::`InvalidState` is returned.

The battery fuel gauge must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

#### Parameters

- **voltage** [in] The voltage at which the low voltage alarm will trigger in millivolts (mV), from 2500 mV to 5000 mV.
If zero, triggering of the alarm is disabled and any existing low voltage alarm is cleared.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the battery low voltage alarm was set successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) setBatteryHighVoltageAlarm(uint16_t voltage)

#### Brief

Set an alarm for battery high voltage.

#### Description

If battery voltage is more than the set voltage, the `ALARM` pin is pulled low.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

A non-zero **capacity** or **type** of  [BatteryType](#enum-class-batterytype)::`ICR18650_26H`/[BatteryType](#enum-class-batterytype)::`UR18650ZY` should have been specified when [Mainboard](#class-mainboard)::init was called, else
 [Result](./result.md#enum-class-result)::`InvalidState` is returned.

The battery fuel gauge must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

#### Parameters

- **voltage** [in] The voltage at which the high voltage alarm will trigger in millivolts (mV), from 2500 mV to 5000 mV.
If zero, triggering of the alarm is disabled and any existing high voltage alarm is cleared.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the battery high voltage alarm was set successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) setBatteryLowChargeAlarm(uint8_t percent)

#### Brief

Set an alarm for battery low charge.

#### Description

If battery charge is less than the set percentage, the `ALARM` pin is pulled low.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

A non-zero **capacity** or **type** of  [BatteryType](#enum-class-batterytype)::`ICR18650_26H`/[BatteryType](#enum-class-batterytype)::`UR18650ZY` should have been specified when [Mainboard](#class-mainboard)::init was called, else
 [Result](./result.md#enum-class-result)::`InvalidState` is returned.

The battery fuel gauge must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

#### Parameters

- **percent** [in] The percentage at which the low charge alarm will trigger in percent, from 1% to 100%.
If zero, triggering of the alarm is disabled and any existing low charge alarm is cleared.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the battery low charge alarm was set successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.

### [Result](./result.md#enum-class-result) updateBatteryFuelGaugeTemp(float temperature)

#### Brief

Update fuel guage with measured battery temperature.

#### Description

In order to increase fuel gauge accuracy, you can update the fuel gauge with the battery temperature obtained from `getBatteryTemperature()` or other sources.

`VSQT` must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

A non-zero **capacity** or **type** of  [BatteryType](#enum-class-batterytype)::`ICR18650_26H`/[BatteryType](#enum-class-batterytype)::`UR18650ZY` should have been specified when [Mainboard](#class-mainboard)::init was called, else
 [Result](./result.md#enum-class-result)::`InvalidState` is returned.

The battery fuel gauge must be enabled prior to calling this function, else [Result](./result.md#enum-class-result)::`InvalidState` is returned.

#### Parameters

- **temperature** [in] The temperature of the battery cell.

#### Return

Returns [Result](./result.md#enum-class-result)::`Ok` if the fuel gauge's battery temperature has been update successfully; returns a value other than [Result](./result.md#enum-class-result)::`Ok` if not.


## extern [Mainboard](#class-mainboard) &Board 

Singleton instance of [Mainboard](#class-mainboard).