---
keywords:
    - esp32
    - powerfeather
    - low power
    - quiescent current
    - load switch
    - battery life
    - ship mode
    - shutdown mode
sidebar_position: 2
---

# Reducing Power Usage

These are strategies you can use in order to maximize your project's battery life.

## Use ESP32-S3 deep sleep

The lowest sleep state ESP32-S3 can be in is deep-sleep. At this state, PowerFeather's current consumption can be under 20 μA.
One common strategy to save power is for ESP32-S3 to be in deep-sleep most of the time, only waking up to do processing at set intervals or
from a trigger signal on a pin - then going back to deep-sleep.

## Turn off 3.3V outputs

PowerFeather has two 3.3 V outputs: `3V3` and `VSQT`. Each of them can be individually
enabled or disabled using [Mainboard::enable3V3](../sdk/api/mainboard.md#result-enable3v3bool-enable)
and [Mainboard::enableVSQT](../sdk/api/mainboard.md#result-enablevsqtbool-enable).
This is useful for turning off loads to save power, and only turning them on when necessary.

```cpp
Board.enable3V3(false); // cut power to connected loads on 3V3
// ...
Board.enable3V3(true); // restore power to connected loads on 3V3
```

```cpp
Board.enableVSQT(false); // cut power to connected STEMMA QT modules
// ...
Board.enableVSQT(true); // restore power to connected STEMMA QT modules
```

The set state persists across deep sleep. That is, if `3V3` or `VSQT` is enabled prior to deep-sleep,
it remains enabled during deep-sleep and after wake-up. Consequently, if `3V3` or `VSQT` is disabled
prior to deep-sleep, it remains disabled during deep-sleep and after wake-up.

## Disable Feather Wings using `EN`

Feather Wings connected to the board can be enabled or disabled by using the function
[Mainboard::setEN](../sdk/api/mainboard.md#result-setenbool-high). Much like the 3.3 V outputs `3V3` and
`VSQT`, the set `EN` state persists across deep sleep.

```cpp
Borad.setEN(false); // disable connected Feather Wings
// ...
Board.setEN(true); // enable connected Feather Wings
```

## Use ship or shutdown mode

Ship and shutdown mode are special power modes in which the battery is as good as cut off
from the board. Use [Mainboard::enterShipMode](../sdk/api/mainboard.md#result-entershipmode)
and [Mainboard::enterShutdownMode](../sdk/api/mainboard.md#result-entershutdownmode) to enter these
modes.

```cpp
Board.enterShipMode(); // enter ship mode
Board.enterShutdownMode(); // enter shutdown mode
```

There are entry and exit conditions for these modes. Read about these conditions in the
documentation for [Mainboard::enterShipMode](../sdk/api/mainboard.md#result-entershipmode) and 
[Mainboard::enterShutdownMode](../sdk/api/mainboard.md#result-entershutdownmode).