##  lr-hr-cr

## ##  Variables

LED_COUNT--------Number of LED in STRIP
LED_PIN----------GPIO pin
LED_FREQ_HZ------LED signal frequency in hertz
LED_DMA----------DMA channel
LED_BRIGHTNESS---Set to 0 for darkest and 255 for brightest
LED_INVERT-------True or False invert the signal


 
## ##  System Commands
restart--------------restart equipment



| Global Commands  

| :------ | :---: |
|Command | Explanation |
|quit | Leave application |
|clear | Clear and Leds off|
|reset | Clear strip scenario|
|reload | Reload APP|

## Pre-defined Configuration
R - Red Slot
G - Green Slot
B - Blue Slot
Y - Yellow Slot
Intiger - Nunber of space in slot

cars01 - R9-G0-B0-Y0
cars02 - R8-G1-B0-Y0
cars03 - R7-G2-B0-Y0
cars04 - R7-G1-B1-Y0
cars05 - R6-G3-B0-Y0
cars06 - R6-G2-B1-Y0
cars07 - R6-G1-B1-Y1
cars08 - R5-G4-B0-Y0
cars09 - R5-G3-B1-Y0
cars10 - R5-G2-B2-Y0
cars11 - R5-G2-B1-Y1
cars12 - R4-G4-B1-Y0
cars13 - R4-G3-B2-Y0
cars14 - R4-G3-B1-Y1
cars15 - R4-G2-B2-Y1
cars16 - R3-G3-B3-Y0 
cars17 - R3-G3-B2-Y1
cars18 - R3-G2-B2-Y2

   
## App Commands
start - Start shopping 
sred - Light up Red Slot
sgreen - Light up Green Slot
sblue - Light up Blue Slot
syellow - Light up Yellow Slot
finalized - Shop finalized


## Configuration Commands from mobile device
caaRGBY - R number of space in slot Red
          G number of space in slot Green
          B number of space in slot Blue
          Y number of space in slot Yellow
rgb-CCCCCCCCCIIEE - CCCCCCCCC - Color in RGB format - Ex: rgb-255092092IIEE for rgb(255, 92, 92) IndianRed
                  - II inital led position (00 to xx) It is always calculated using the formula: LED number -1
				  - EE final led position (00 to xx)

