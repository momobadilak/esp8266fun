# Why
I built this arduino project to mess around with some cheap ESP8266EX based
WiFi module I picked up from amazon (here: https://amzn.com/B00O34AGSU )

I want to be able to use the module in conjunction with other arduino
boards and projects witht the ESP module acting primarily as a WIFI
"modem"

# Dependencies
"andys_menu" - a small text based menu system. https://github.com/momobadilak/andys_menu

Arduino micro board : https://www.arduino.cc/en/Main/ArduinoBoardMicro

If you don't have an arduino micro, I *believe* this code could be modified to be
use with a Leonardo or Mega board as they also have more than one Uart.

# Use
Build main/main.ino and run it on an arduino micro. Use your Host/PC to interact
with the text menu that appears via the serial monitor (or better - use minicom or
putty)

# Schematic / Board setup / Pics
TODO

# Video
TODO

# Contact
Drop me a note on twitter - @andyidsinga - if you find amu of this useful or
need some help.


# The authoritative source for ESP info
You probably won't need to go much further than this site, I suspect
this site and documentation has improved a lot over the past few
years as this part appears to be farly popular.

https://espressif.com/en/products/hardware/esp8266ex/resources


***

# Product description from amazon page

https://amzn.com/B00O34AGSU

Esp8266 Serial Wifi Wireless Transceiver Module _Esp-01_ Arduino Compatible Switch

Description:
- 802.11 b/g/n
- Serial/UART baud rate: 115200 bps
- Integrated TCP/IP protocol stack
- Input power: 3.3V
- I/O voltage tolerance: 3.6V Max
- Regular operation current draw: ~70mA
- Peak operating current draw: ~300mA
- Power down leakage current: <10?A
- +19.5dBm output in 802.11b mode
- Flash Memory Size: 1MB (8Mbit)
- WiFi security modes: WPA, WPA2


***


# Various links I've collected while researching these modules

## Here are the technical links from the amazon item page:
Arduino library: https://github.com/sleemanj/ESP8266_Simple

## A good picture of the board and pin labels
http://fabacademy.org/archives/2015/doc/networking-esp8266.html

## Tool for uploading new firmware to the device itself (not the arduino)
https://github.com/espressif/esptool

## A youtube tutorial: 
https://www.youtube.com/watch?v=qU76yWHeQuw 

## Some interesting tech details
https://nurdspace.nl/ESP8266#Introduction 

## Another repo of ESP info (referenced from nurdspace)
http://www.electrodragon.com/w/index.php?title=Category:ESP8266&redirect=no


## Lots of stuff on Hackaday.com
http://hackaday.com/?s=esp8266
