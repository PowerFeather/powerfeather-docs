---
sidebar_position: 1
---


# Mainboard

:::info
Work in progress.
:::

## class Mainboard

### [Result](./result) init(uint16_t capacity = 0)

Initialize and set defaults.

- Max charging current: 100 mA
- Max input current: 500 mA
- Charging: disabled
- 3V3: enabled
- VSQT: enabled
- EN: high

#### Parameters

capacity[in] Battery capacity in mAh.


### [Result](./result) setEN(bool high)

Set EN pin state.

#### Parameters

high[in] EN pin is set high if true, set low if false.


### [Result](./result) enable3V3(bool enable)

Enable or disable the header 3.3 V power output.

#### Parameters

enable[in] Enable 3.3 V header output if true, disable if false.


### [Result](./result) enableVSQT(bool enable);

Enable or disable the STEMMA QT 3.3 V power output.

#### Parameters

enable[in] Enable STEMMA QT 3.3 V output if true, disable if false.

### [Result](./result) getSupplyVoltage(uint16_t& voltage)

Measure the supply voltage.

#### Parameters

voltage[out] Measured supply voltage in mV.


### [Result](./result) getSupplyCurrent(int16_t& current)

Measure the supply current.

#### Parameters

current[out] Measured supply current in mA.


### [Result](./result) getSupplyStatus(bool& good)

Check that the power supply is a 'good' source as determined by the charger.

#### Parameters

good[out] If true, supply is good; if false, battery is powering the board.



### [Result](./result) setSupplyMinVoltage(uint16_t voltage)

Sets the minimum supply voltage that should be maintained.

This is usually the MPP (maximum power point) voltage of the power supply. The
voltage is maintained by automatically reducing current draw. This [Result](./result)s to
the maximum power extracted from the supply.

#### Parameters

voltage[in] The maintained voltage in mV.



### [Result](./result) setSupplyMaxCurrent(uint16_t current)

Set the maximum current draw from the power supply.

This includes current draw from on-board components, the load on the VS pin,
and the charger current. The sum of all these current draws must not exceed this
current.

#### Parameters
current[in] The maximum current draw from supply in mA.


### [Result](./result) setVBATMinVoltage(uint16_t voltage)

Set VBAT minimum output voltage.

When supply is connected, the lowest output voltage of VBAT even if there is no battery or the
battery is fully depleted. Valid range is 2200 to 3800 mV.

#### Parameters

voltage[in] Minimum voltage to set VBAT output to.

### [Result](./result) enterShipMode()

Enter ship mode.

Ship mode is a low power state that consumes about 1.5 uA. It is only possible to
exit this mode by pulling down QON or by plugging in supply. Only able to enter
ship mode if battery is powering the board.


### [Result](./result) enterShutdownMode()

Enter shutdown mode.

Ship mode is a low power state that consumes about 1.4 uA. It is only possible
to exit this mode by plugging in supply. Only able to enter shutdown if battery
is powering board.


### [Result](./result) doPowerCycle()

Power cycle board.

This power cycles all components on-board, and all loads connected to power outputs.


### [Result](./result) enableCharging(bool enable)

Enable battery charging.

#### Parameters

enable[in] Charging is enabled if true; otherwise disabled.


### [Result](./result) enableTempSense(bool enable)
Enable temperature monitor.

If enabled, the value of the 103AT thermistor connected on TS will be monitored.
Charging current will be reduced as temperature approaches 0 °C and 60 °C, and will
be disabled past them.

#### Parameters
enable[in] Battery temperature sensing is enabled if true; otherwise disabled.


### [Result](./result) enableFuelGauge(bool enable)

Enable the fuel gauge.

Fuel gauge enabled consumes around 2 μA when enabled; disabling the fuel gauge saves around 0.7 μA.

#### Parameters

enable[in] Fuel gauge is enabled if true; otherwise disabled.


### [Result](./result) setChargingMaxCurrent(uint16_t current)
Set maximum charging current.

Set value depending on preference between safety and speed. A charging
current of 1C is usually a good value, i.e. if battery has capacity of 520 mAh, set charging
current to 520 mA (520 * 1 = 520). Check datasheet for your battery for maximum charging current.

#### Parameters
current[in] Maximum charging current in mA.


### [Result](./result) getBatteryVoltage(uint16_t& voltage)

Measure battery voltage.

#### Parameters
voltage[out] Battery voltage current in mV.


### [Result](./result) getBatteryCharge(uint8_t& percent)

Get an estimate of battery state-of-charge from 0 (empty) to 100 (full).

#### Parameters

percent[out] Battery charge percentage from 0 to 100.


### [Result](./result) getBatteryHealth(uint8_t& percent)

Get an estimate of battery state-of-health from 0 to 100 of the original design capacity.

#### Parameters
percent[out] Battery health percentage from 0 to 100.


### [Result](./result) getBatteryTimeLeft(int& minutes)

Get the time left before fully empty/fully charged.


#### Parameters
minutes[out] Charge/discharge time left in minutes.



### [Result](./result) getBatteryTemperature(float& celsius)

Measure the battery temperature.

Temperature sensing must be enabled via enableTempSense to get a reading.

#### Parameters
celsius[out] Battery current in °C.



### [Result](./result) getBatteryCurrent(int16_t& current)

Measure the charge/discharge current to/from the battery.

#### Parameters
current[out] Battery current in mA.


## [Mainboard&](class-mainboard) Board

Singleton instance of Mainboard. 