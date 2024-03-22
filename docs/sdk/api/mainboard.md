---
sidebar_position: 1
---


# Mainboard

## class Mainboard

### enum class BatteryType

- `Generic_3V7` Generic Li-ion/LiPo battery with nominal voltage of 3.7 V
- `ICR18650` Samsung IC18650
- `UR18650ZY` Sanyo UR18650ZY

### [Result](./result) init(uint16_t capacity = 0, [BatteryType](#enum-class-batterytype) type = [BatteryType](#enum-class-batterytype)::`Generic_3V7`)

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

This function should be called once, before calls to all other [Mainboard](#class-mainboard) functions.

#### Parameters

- **capacity** [in] The capacity of the connected Li-ion/LiPo battery in milliamp-hours (mAh), from 50 mAh to 6000 mAh.
A value of zero indicates that no battery is connected, and therefore some of the other [Mainboard](#class-mainboard) functions
will return [Result](result.md)::`InvalidState`. If using multiple batteries connected in parallel, specify
only the capacity for one cell. Non-zero value is ignored when **type** is [BatteryType](#enum-class-batterytype)::`ICR18650` or [BatteryType](#enum-class-batterytype)::`UR18650ZY`.
- **type** [in] Type of Li-ion/LiPo battery; ignored when **capacity** is zero.

#### Return

Returns [Result](result.md)::`Ok` if initialization succeeded; returns a value other than [Result](result.md)::`Ok` if not.

### Result setEN(bool high)

        /**
         * @brief Set \a EN pin high or low.
         *
         * This is useful for enabling or disabling connected Feather Wings to reduce power consumption.
         *
         * @param[in] high If \c true, EN is set high; if \c false, EN is set low.
         * @return Result Returns \c Result::Ok if \a EN was set high or low successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result enable3V3(bool enable)

        /**
         * @brief Enable or disable \a VSQT.
         *
         * Enables or disables \a VSQT, the 3.3 V STEMMA QT power output. When disabled, power to the
         * connected STEMMA QT modules is cut, reducing power consumption.
         *
         * A side effect of disabling \a VSQT is that communications to the battery charger and fuel gauge is also disabled.
         * This means that some of the other \c [Mainboard](#class-mainboard) functions will return \c Result::InvalidState when
         * \a VSQT is disabled. Make sure to enable \a VSQT prior to calling these functions.
         *
         * @param[in] enable If \c true, \a VSQT is enabled; if \c false, \a VSQT is disabled.
         * @return Result Returns \c Result::Ok if \a VSQT was enabled or disabled successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result enableVSQT(bool enable)

        /**
         * @brief Enable or disable \a VSQT.
         *
         * Enables or disables \a VSQT, the 3.3 V STEMMA QT power output. When disabled, power to the
         * connected STEMMA QT modules is cut, reducing power consumption.
         *
         * A side effect of disabling \a VSQT is that communications to the battery charger and fuel gauge is also disabled.
         * This means that some of the other \c [Mainboard](#class-mainboard) functions will return \c Result::InvalidState when
         * \a VSQT is disabled. Make sure to enable \a VSQT prior to calling these functions.
         *
         * @param[in] enable If \c true, \a VSQT is enabled; if \c false, \a VSQT is disabled.
         * @return Result Returns \c Result::Ok if \a VSQT was enabled or disabled successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result getSupplyVoltage(uint16_t &voltage)

        /**
         * @brief Measure the supply voltage.
         *
         * Measures the \a VUSB or \a VDC voltage. \a VUSB is the power input from the USB-C connector,
         * while \a VDC is the power input from the header pin.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * This function can block for 100 ms.
         *
         * @param[out] voltage The measured voltage in millivolts (mV).
         * @return Result Returns \c Result::Ok if the supply voltage was measured successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result getSupplyCurrent(int16_t &current)

        /**
         * @brief Measure the supply current.
         *
         * Measures the current drawn from \a VUSB or \a VDC. \a VUSB is the power input from the USB-C connector,
         * while \a VDC is the power input from the header pin.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * This function can block for 100 ms.
         *
         * @param[out] voltage The measured current draw in milliamperes (mA).
         * @return Result Returns \c Result::Ok if the supply current was measured successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result checkSupplyGood(bool &good)

        /**
         * @brief Check if the supply is good.
         *
         * Checks if the supply, whether \a VUSB or \a VDC is good as determined by the battery charger. A good supply
         * means that it powers the board and connected loads, not the battery.
         *
         * @param[out] good If \c true, the charger has determined the supply to be good; \c false if not.
         * @return Result Returns \c Result::Ok if the supply was checked successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result setSupplyMaintainVoltage(uint16_t voltage)

        /**
         * @brief Set the supply voltage to maintain.
         *
         * The battery charger dynamically regulates the current drawn from the supply to prevent it from collapsing under
         * the set voltage to maintain. This is useful for specifying the maximum power point (MPP) voltage if using a
         * solar panel; allowing the battery charger to extract power from the panel at near-MPPT effectiveness.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * @param[in] voltage The supply voltage to maintain, up to 16800 mV.
         * @return Result Returns \c Result::Ok if the supply voltage to maintain was set successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result enterShipMode()

        /**
         * @brief Enter ship mode.
         *
         * Ship mode is a power state that only consumes around 1.5 μA. Only the battery charger and
         * the battery fuel gauge is powered.
         *
         * This mode can only be entered into if the battery is powering the board and connected loads;
         * that is, if \c checkSupplyGood output parameter \p good is \c false.
         *
         * Ship mode can be exited by either (1) pulling \a QON header pin low for around 800 ms or
         * (2) connecting a power supply which the battery charger determines to be good.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * This function can block for 20 ms if it fails to enter ship mode.
         *
         * @return Result Does not return if ship mode was successfully entered into;
         * returns a value other than \c Result::Ok if not.
         */

### Result enterShutdownMode()

        /**
         * @brief Enter shutdown mode.
         *
         * Shutdown mode is a power state that only consumes around 1.4 μA. Only the battery charger and
         * the battery fuel gauge is powered.
         *
         * This mode can only be entered into if the battery is powering the board and connected loads;
         * that is, if \c checkSupplyGood output parameter \p good is \c false.
         *
         * Shutdown mode can only be exited by connecting a power supply which the battery charger determines to be good.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * This function can block for 20 ms if it fails to enter shutdown mode.
         *
         * @return Result Does not return if shutdown mode was successfully entered into;
         * returns a value other than \c Result::Ok if not.
         */

### Result doPowerCycle()

        /**
         * @brief Perform a power cycle.
         *
         * For all components on the board and connected loads, except the battery fuel gauge
         * and loads connected to \a VS (supply output header pin, whichever of \a VUSB and \a VDC),
         * the power cycle provides complete reset by removing power and re-applying it after a short delay.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * @return Result Does not return if a power cycle was performed successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result enableBatteryCharging(bool enable)

        /**
         * @brief Enable or disable battery charging.
         *
         * This is useful when opting to not fully charge a battery in order to prolong its lifespan.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * A non-zero \p capacity should have been specified when \c [Mainboard](#class-mainboard)::init was called, else
         *  \c Result::InvalidState is returned.
         *
         * @param[in] enable If \c true, battery charging is enabled; if \c false, battery charging is disabled.
         * @return Result Returns \c Result::Ok if battery charging was enabled or disabled successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result setBatteryChargingMaxCurrent(uint16_t current)

        /**
         * @brief Set maximum battery charging current.
         *
         * Ensures that the battery is not charged with a current more than the amount specified using this function.
         * This is useful for batteries with small capacities, since it is not recommended to charge a battery at
         * more than 1C. For example, when charging a 550 mAh battery, a current of no more than 550 mA is
         * recommended. That current limit of 550 mA can be specified using this function.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * A non-zero \p capacity should have been specified when \c [Mainboard](#class-mainboard)::init was called, else
         *  \c Result::InvalidState is returned.
         *
         * @param[in] current The maximum charging current, up to 2000 mA.
         * @return Result Returns \c Result::Ok if the maximum battery charging current was set successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result enableBatteryTempSense(bool enable)

        /**
         * @brief Enable or disable battery temperature measurement.
         *
         * Enables or disables battery temperature measurement using the thermistor connected to the \a TS pin.
         * If enabled, aside from measurement, the battery charger performs temperature-based battery charging current
         * reduction or cutoff.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * A non-zero \p capacity should have been specified when \c [Mainboard](#class-mainboard)::init was called, else
         *  \c Result::InvalidState is returned.
         *
         * @param[in] enable If \c true, battery temperature measurement is enabled; if \c false, battery
         * temperature measurement is disabled.
         * @return Result Returns \c Result::Ok if the battery temperature measurement was enabled or
         * disabled successfully; returns a value other than \c Result::Ok if not.
         */

### Result enableBatteryFuelGauge(bool enable)

        /**
         * @brief Enable or disable the battery fuel guage.
         *
         * Disabling the battery fuel guage can save around 0.5 μA. However, once disabled, it
         * cannot keep track of battery information such as voltage, charge, health, cycle count, etc.
         * Nonetheless, this is useful when trying to reduce power as much as possible, such as when going
         * into ship mode or shutdown mode for a long time.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * A non-zero \p capacity should have been specified when \c [Mainboard](#class-mainboard)::init was called, else
         *  \c Result::InvalidState is returned.
         *
         * @param[in] enable If \c true, the battery fuel gauge is enabled; if \c false, the battery fuel gauge is disabled.
         * @return Result Returns \c Result::Ok if the battery fuel gauge was enabled or disabled successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result getBatteryVoltage(uint16_t &voltage)

        /**
         * @brief Measure battery voltage.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * A non-zero \p capacity should have been specified when \c [Mainboard](#class-mainboard)::init was called, else
         *  \c Result::InvalidState is returned.
         *
         * This function can block for 100 ms.
         *
         * @param[out] voltage Measured battery voltage in millivolts (mV).
         * @return Result Returns \c Result::Ok if the battery voltage was measured successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result getBatteryCurrent(int16_t &current)

        /**
         * @brief Measure battery current.
         *
         * Measures the current to or from the battery during charging and discharging, respectively.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * A non-zero \p capacity should have been specified when \c [Mainboard](#class-mainboard)::init was called, else
         *  \c Result::InvalidState is returned.
         *
         * This function can block for 100 ms.
         *
         * @param[out] current Measured battery voltage in milliamps (mA). If battery is discharging,
         * this value is negative; positive if battery is charging.
         * @return Result Returns \c Result::Ok if the battery current was measured successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result getBatteryCharge(uint8_t &percent)

        /**
         * @brief Estimate battery charge.
         *
         * Gives an estimate of battery state-of-charge from 0% to 100%. This is useful to get a sense
         * if the battery still has much charge or is nearly empty.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * A non-zero \p capacity should have been specified when \c [Mainboard](#class-mainboard)::init was called, else
         *  \c Result::InvalidState is returned.
         *
         * The battery The battery fuel gauge must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * @param[out] percent Estimated battery charge, from 0% to 100%.
         * @return Result Returns \c Result::Ok if the battery charge was estimated successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result getBatteryHealth(uint8_t &percent)

        /**
         * @brief Estimate battery health.
         *
         * Gives an estimate of battery state-of-health from 0% to 100%. This is useful to get a
         * sense of how much the battery has degraded over time.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * A non-zero \p capacity should have been specified when \c [Mainboard](#class-mainboard)::init was called, else
         *  \c Result::InvalidState is returned.
         *
         * The battery The battery fuel gauge must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * @param[out] percent Estimated battery health, from 0% to 100%.
         * @return Result Returns \c Result::Ok if the battery health was estimated successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result getBatteryCycles(uint16_t &cycles)

        /**
         * @brief Estimate battery cycle count.
         *
         * Gives an estimate of the battery cycle count. This is useful to compare against the number of
         * cycle counts the battery is rated for.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * A non-zero \p capacity should have been specified when \c [Mainboard](#class-mainboard)::init was called, else
         *  \c Result::InvalidState is returned.
         *
         * The battery fuel gauge must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * @param[out] cycles Estimated battery cycle count.
         * @return Result Returns \c Result::Ok if the battery cycle count was estimated successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result getBatteryTimeLeft(int &minutes)

        /**
         * @brief Estimate time left for battery to charge or discharge.
         *
         * Gives an estimate of the battery time-to-empty or time-to-full in minutes. The battery charge must have
         * previously dropped and/or risen by 10% to be able to estimate time-to-empty or time-to-full, respectively;
         * else \c Result::NotReady is returned.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * A non-zero \p capacity should have been specified when \c [Mainboard](#class-mainboard)::init was called, else
         *  \c Result::InvalidState is returned.
         *
         * The battery fuel gauge must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * @param[out] minutes Estimated time left for battery to charge or discharge in minutes. If battery is discharging,
         * this value is negative; if battery is charging, this value is positive.
         * @return Result Returns \c Result::Ok if the time left for battery to charge or discharge was estimated
         * successfully; returns a value other than \c Result::Ok if not.
         */

### Result getBatteryTemperature(float &celsius)

        /**
         * @brief Measure battery temperature.
         *
         * Requires a Semitec 103AT thermistor to be connected to the \a TS pin and attached to the battery
         * for the measurement to be accurate.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * A non-zero \p capacity should have been specified when \c [Mainboard](#class-mainboard)::init was called, else
         *  \c Result::InvalidState is returned.
         *
         * Battery temperature measurement must be enabled prior calling this function, else \c Result::InvalidState
         * is returned.
         *
         * This function can block for 100 ms.
         *
         * @param[out] celsius Measured battery temperature in celsius.
         * @return Result Returns \c Result::Ok if the battery temperature was measured successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result setBatteryLowVoltageAlarm(uint16_t voltage)

        /**
         * @brief Set an alarm for battery low voltage.
         *
         * If battery voltage is less than the set voltage, the \a ALARM pin is pulled low.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * A non-zero \p capacity should have been specified when \c [Mainboard](#class-mainboard)::init was called, else
         *  \c Result::InvalidState is returned.
         *
         * The battery fuel gauge must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * @param[in] voltage The voltage at which the low voltage alarm will trigger, from 2500 mV to 5000 mV.
         * If 0 mV, triggering of the alarm is disabled and any existing low voltage alarm is cleared.
         * @return Result Returns \c Result::Ok if the battery low voltage alarm was set successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result setBatteryHighVoltageAlarm(uint16_t voltage)

        /**
         * @brief Set an alarm for battery high voltage.
         *
         * If battery voltage is more than the set voltage, the \a ALARM pin is pulled low.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * A non-zero \p capacity should have been specified when \c [Mainboard](#class-mainboard)::init was called, else
         *  \c Result::InvalidState is returned.
         *
         * The battery fuel gauge must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * @param[in] voltage The voltage at which the high voltage alarm will trigger, from 2500 mV to 5000 mV.
         * If 0 mV, triggering of the alarm is disabled and any existing high voltage alarm is cleared.
         * @return Result Returns \c Result::Ok if the battery high voltage alarm was set successfully;
         * returns a value other than \c Result::Ok if not.
         */

### Result setBatteryLowChargeAlarm(uint8_t percent)

        /**
         * @brief Set an alarm for battery low charge.
         *
         * If battery charge is less than the set percentage, the \a ALARM pin is pulled low.
         *
         * \a VSQT must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * A non-zero \p capacity should have been specified when \c [Mainboard](#class-mainboard)::init was called, else
         *  \c Result::InvalidState is returned.
         *
         * The battery fuel gauge must be enabled prior to calling this function, else \c Result::InvalidState is returned.
         *
         * @param[in] percent The percentage at which the low charge alarm will trigger, from 1% to 100%.
         * If 0%, triggering of the alarm is disabled and any existing low charge alarm is cleared.
         * @return Result Returns \c Result::Ok if the battery low charge alarm was set successfully;
         * returns a value other than \c Result::Ok if not.
         */

## extern [Mainboard](#class-mainboard) &Board 

Singleton instance of [Mainboard](#class-mainboard).