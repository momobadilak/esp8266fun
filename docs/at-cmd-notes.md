# Some notes I captured while working / stumbling around with the ESP-01 module's AT command set

### Pre-installed firmware version info (from AT+GMR):

  AT version:0.60.0.0(Jan 29 2016 15:10:17)

  SDK version:1.5.2(7eee54f4)

  Ai-Thinker Technology Co. Ltd.

  May  5 2016 17:30:30

### Firmware after successful AT+CIUPDATE

  AT version:1.1.0.0(May 11 2016 18:09:56)

  SDK version:1.5.4(baaeaebb)

  Ai-Thinker Technology Co. Ltd.

  May 28 2016 10:42:12


### Command Log
Note that I had the AT command manual for version 2.0.0 from July 15, 2016. I couldn't
find the manual that matched my firmware version

  * AT+GMR
    * show firmeware and SDK version info

  * AT+CWMODE_CUR
    * show current station mode
    * tried using values 1 and 3, then tried connecting to my home network
    
  * AT+CWLAP
    * List visible APs

  * AT+CWJAP_CUR=<ssid>,<pwd>,<mac>
    * Connect to an AP
    * I had to add the <mac> portion to get this command to work. I figure its
    becuase I have two access points with the same SSID ...one is the main AP and
    one is a wifi extender. Note that in the AT command docs they call the <mac> "bssid"

  * AT+CIPSTA?
    * view local IP address (including those received via DHCP)

  * AT+CIFSR
    * view local IP address AND mac address
    

  * AT+CWDHCP_CUR?
    * view DHCP settings
    

  * AT+PING=<IP or DNS>
    * DNS appeared to "just work" assuming it got correct config via DHCP
    * need to figure out where its sending its DNS requests

  * AT+CIUPDATE
    * This worked, and new AT firmware and SDK firmware were downloaded (as of 11/28/2016)

  * AT+CIPSTATUS
    * get connection status
    * 

### These don't appear to work

