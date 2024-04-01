---
unlisted: true
---

# Battery Usage Notes

## Charging Configuration

By default, charging is disabled; if enabled, the max current is only 50 mA.
User firmware needs to enable charging and set the max charging current depending on the battery capacity.


```cpp
Board.init(500);  // assuming a 500 mAh battery; disables charging, and sets max charging current to 50 mA
// ...
Board.setBatteryMaxChargingCurrent(350); // charge at 350 mA or 0.75 C, that is 500 * 0.75 = 350
Board.enableBatteryCharging(true); // enable charging
```

Tt is recommended to charge at 1 C or less to avoid overloading the battery.

If you need to disable charging again.

```cpp
Board.enableBatteryCharging(false); // disable charging
```

## Reducing Battery Wear

One way of reducing battery wear is to avoid a full charge/discharge cycle, that is, going from 0% to 100% and vice
versa - maybe only discharging down to 20% and charging only up to 80%.

PowerFeather has the necessary features for you to be able to implemenent such a scheme:

    - Charge estimation
    - Enabling/Disabling battery charging
    - Deep Sleep/ship mode/shutdown mode, turning off `VSQT` and `3V3`, setting `EN` low.

To prevent the battery from charging beyond a certain charge percentage, charging can simply
be disabled.

```cpp
uint8_t percent = 0;
if (Board.getBatteryCharge(percent) == Result::Ok && percent >= 80) // if charge exceeds 80%
{
    Board.enableBatteryCharging(false); // disable charging
}
```

In preventing the battery from discharging beyond a certain charge percentage, there are two scenarios
to consider:

    - There is an external power supply that can charge the battery. In this case, charging can just be re-enabled.
    ```cpp
    uint8_t percent = 0;
    if (Board.getBatteryCharge(percent) == Result::Ok && percent < 20) // if charge is below 20%
    {
        Board.enableBatteryCharging(true); // enable charging
    }
    ```

    - However, if there is no external supply that can charge the battery, power consumption should be minimized
    until such time when the battery can be charged. This is where deep sleep + turning off `3V3`, `VSQT`
    and connected Wings via `EN`, ship mode or shutdown mode comes in. Assuming entering ship mode is chosen:

    ```cpp
    if (Board.getBatteryCharge(percent) == Result::Ok && percent < 20) // if charge is below 20%
    {
        Board.enterShipMode(); // enter ship mode, consuming only 1.4 uA until external supply is plugged in
    }
    ```

## Battery Alarms

Enabling battery alarms are especially useful when using them as triggers from waking up from deep sleep.
