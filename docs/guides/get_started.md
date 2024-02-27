---
sidebar_position: 1
---

# Getting Started

:::info
Work in progress.
:::

## First Use

PowerFeather comes pre-loaded with a simple program that blinks the green user `LED`. Use this to quickly check
if your board is OK. Simply connect your PowerFeather to a host computer using the USB-C connector:

![LED Blink](assets/led_blink.gif)

As illustrated above, the red `CHG` LED should flash momentarily, after which the green user `LED` will blink.

## Run Example

The demo application showcases some of the things you can do with PowerFeather. To run the it, ESP-IDF or Arduino
with the *PowerFeather SDK* must be installed on your system. If you have not done this yet,
please follow the instructions on the [PowerFeather SDK installation guide](/sdk/install.md).



### Arduino

Open Arduino IDE, and select the *PowerFeather SDK* > *Supply_and_Battery_Info* example.

![Open Example](assets/open_example.png)

Make sure *ESP32-S3 PowerFeather* is selected as the board.

![Select Board](assets/select_board.png)

Upload the example. If you have a battery, detach the USB-C cable first. Attach your battery, only
then reconnect the USB-C cable.

![Upload Example](assets/upload_example.png)

Open the *Serial Monitor*. The supply and battery voltage and current are reported; as well as the
battery charge estimated by the fuel gauge.

Notice that the battery current is zero, while the supply current is not. This indicates that:
- The board is being supplied by the external power source, in this case by `VUSB`.
- The battery is not charging.

![Serial Monitor](assets/serial_monitor.png)

Press `BTN` on PowerFeather to enable charging. When charging is enabled, notice the battery current
is no longer zero; and supply current also increases.

![Charging](assets/charging.png)

If you have one, you can try using a data-only (no power) USB-C cable, to see that in the absence of an external
supply, the battery supplies the board. In this case, the battery current is negative, indicating
discharging.

![Discharging](assets/discharging.png)

### ESP-IDF





<!-- ## Saying Hello

To get started, simply plugin your PowerFeather to a laptop. It should present a serial device.
If you open that serial device, it

Every new PowerFeather comes pre-programmed with ... It's it's way of saying hello.


## Development

The PowerFeather can be used with either Arduino or ESP-IDF.

### Arduino -->
