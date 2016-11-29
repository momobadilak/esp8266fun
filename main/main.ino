/*
  main.ino for esp8266fun project

  The MIT License (MIT)

  Copyright (c) 2016 Andy Idsinga (aka momobadilak)

  Permission is hereby granted, free of charge, to any person obtaining
  a copy of this software and associated documentation files (the "Software"), 
  to deal in the Software without restriction, including without limitation
  the rights to use, copy, modify, merge, publish, distribute, sublicense, 
  and/or sell copies of the Software, and to permit persons to whom the 
  Software is furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included 
  in all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
  IN THE SOFTWARE.

  Theory of operation:
  I'm using a menu system and a bunch of docs I've collected from the
  web to figure out how to work with a cheap ESP8266 board I purchased from
  amazon (https://amzn.com/B00O34AGSU)
  
  Power and logic levels:
  Arduino power by 5V.
  ESP board powered by external 3.3v supply
  SN74LVC245A bus transceiver to shift from Arduino 5v to 3.3v logic levels.
  
*/

#include <arduino.h>

/* andys_menu from: https://github.com/momobadilak/andys_menu */
#include <andys_menu.h>

/*
  Pin mapping:
  Arduino Pin 2           >> Bus xcvr OE
  Arduino Uart TX (Pin 1) >> Bus xcvr A1   >> B1 >> ESP URXD
  Arduino Uart RX (Pin 0) <<<<<<<<<<<<<<<<<<<<<<<<< ESP UTXD
  Arduino Pin 3           >> Bux xcvr A2   >> B3 >> ESP CH_PD 

*/
const int BUS_nOE    = 2;
const int ESP_TX     = 1;
const int ESP_RX     = 0;
const int ESP_CHPD   = 3;

/* create an instance of the menu class */
AndysMenu theMenu;

/* error handler function proto */
void menu_ErrorHandler(const uint8_t code, const char* msg);

/* 
   These prompt menus can reused throughout the code whenever a prompt is required
*/
AndysPromptItem okPrompt[] = {
  {'o', "ok"}
};

AndysPromptItem yesNoPrompt[] = {
  {'y', "Yes"},
  {'n', "No"}
};

/*
  Main, Top level menu definition and function protos
*/
void topmenu_EnableESP(void* context);
void topmenu_DisableESP(void* context);
void topmenu_SingleCmd(void* context);
AndysMenuItem topMenu[] = {
  {'e', "enable ESP via ESP_CHPD", topmenu_EnableESP },
  {'d', "disable ESP via ESP_CHPD", topmenu_DisableESP },
  {'s', "single command entry mode", topmenu_SingleCmd }
};

/* normal arduino setup function called on boot */
void setup() {

  /* this is the Serial back to the Host machine -- not the ESP */
  Serial.begin(115200);

  Serial.println("+setup()");

  /* setup pins */
  pinMode(BUS_nOE,  OUTPUT);
  pinMode(ESP_TX,   OUTPUT);
  pinMode(ESP_RX,   INPUT);
  pinMode(ESP_CHPD, OUTPUT);
  
  /* enable bus xcvr : two sides no longer isolated after this!*/
  digitalWrite(BUS_nOE, LOW);

  /* disable ESP ..for now*/
  digitalWrite(ESP_CHPD,LOW);

  Serial.println("finished pin setup");

  /* setup the UART to be used with the ESP */
  Serial1.begin(115200);
  
  Serial.println("-setup()");
}

/* arduino loop function called over and over forever */
void loop() {

  /* run the top level menu.
     Note: I'm not passing anything for the context arg, but
     that can be your goodies, and will not be touched by the menu code. */
  theMenu.run(
	      "=== Top Menu ===",
	      topMenu, 
	      sizeof(topMenu)/sizeof(AndysMenuItem), 
	      (void*)0,
	      menu_ErrorHandler);
}

/*****************************************************************************/
/* menu item implementation                                                  */
/*****************************************************************************/

void topmenu_EnableESP(void* context){
  Serial.print("+");Serial.println(__FUNCTION__);
  Serial.println("TODO");
}

void topmenu_DisableESP(void* context){
  Serial.print("+");Serial.println(__FUNCTION__);
  Serial.println("TODO");
}

void topmenu_SingleCmd(void* context){
  Serial.print("+");Serial.println(__FUNCTION__);
  Serial.println("TODO");
}

/*
  generic menu error handler - error code and message dumper
*/
void menu_ErrorHandler(const uint8_t code, const char* msg)
{
  Serial.print("+menu_ErrorHandler,");
  Serial.print("code,"); 
  Serial.print(code,HEX);
  Serial.print(",msg,"); 
  Serial.println(msg);
}
