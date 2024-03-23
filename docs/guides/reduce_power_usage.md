---
sidebar_position: 2
---

# Reducing Power Usage


## Use ESP32-S3 deep sleep

The lowest sleep state ESP32-S3 can be in is deep sleep. ESP32-S3 can be woken up either
on a timer, or by a signal change on a pin.


## Turn off 3.3V outputs

PowerFeather has two 3.3 V outputs: `3V3` and `VSQT`. Each of them can be individually
enabled/disabled using [Mainboard::enable3V3](../sdk/api/mainboard.md#result-enable3v3bool-enable)
and [Mainboard::enableVSQT](../sdk/api/mainboard.md#result-enablevsqtbool-enable).


```cpp
Board.enable3V3(true); // enable 3V3 output
Board.enable3V3(false); // disable 3V3 output
```

```cpp
Board.enableVSQT(true); // enable 3V3 output
Board.enableVSQT(false); // disable 3V3 output
```

The setting persists even across deep sleep. This way users can continue to power connected
3.3 V devices if necessary. But if not, they can turn these off completely.

On power-on reset, `3V3` and `VSQT` are enabled after the call to `init`. On wake from deep-sleep,
the last state is retained.

## Disable Feather Wings using `EN`

Feather Wings connected to the board can be enabled/disabled by using the function
[Mainboard::setEN](../sdk/api/mainboard.md#result-setenbool-high). Much like the 3.3 V outputs `3V3` and
`VSQT`, the last `EN` state persists across deep sleep.

```cpp
Board.setEN(true); // set EN high
Borad.setEN(false); // set EN low
```

## Use ship or shutdown mode

Ship and shutdown mode are special power modes in which the battery is cut off
from the board. Use [Mainboard::enterShipMode](../sdk/api/mainboard.md#result-entershipmode)
and [Mainboard::enterShutdownMode](../sdk/api/mainboard.md#result-entershutdownmode) to enter these
modes.

```cpp
Board.enterShipMode(); // enter ship mode
Board.enterShutdownMode(); // enter shutdown mode
```