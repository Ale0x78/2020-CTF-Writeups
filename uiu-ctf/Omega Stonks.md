
# Omega Stonks

## Challenge
![alt text](./images/omega_challange.png "If you solve this challenge, straightup you have Omega Stonks.(Buy this flag from IsabelleBot)")
## Plan of attack
You can type `!work` in the chat with ***IsabelleBot*** to earn stonks +  it's late at night, and I need to get 8 hours of sleep = automate sending `!work` to ***IsabelleBot***.

In High School I used to make costume controllers for our robotics team using Arduino Boards (essentially they would mimic a keyboard), so for nostalgia's sake (and because I didn't want to look into making a Discord bot), I grabbed my old friend DigiSpark (with an **ATTINY85**) and started automating!

## Setup
DigiSpark ships with a library called [DigiKeyboard](https://github.com/digistump/DigistumpArduino/blob/master/digistump-avr/libraries/DigisparkKeyboard/DigiKeyboard.h) which lets you send keystrokes over USB.

![alt text](./images/Digispark.png "My DigiSpark")

So after adding the `http://digistump.com/package_digistump_index.json` to my board manager URLs under Arduino Preferences, all I had to do is write the code to spam `!work`.

## Code

```Arduino
#include "DigiKeyboard.h"

void setup() {

}

void print(char *str) {
  char c = str[0];
  byte i = 0;
  DigiKeyboard.update();
  DigiKeyboard.sendKeyStroke(0); //this is generally not necessary but with some older systems it seems to prevent missing the first character after a delay
  while (c != 0) {
    if (c==' ')
      DigiKeyboard.sendKeyStroke(KEY_SPACE);
    if (c>='A' && c<='Z')
      DigiKeyboard.sendKeyStroke(KEY_A+(c-'A'), MOD_SHIFT_LEFT);
    if (c>='a' && c<='z')
      DigiKeyboard.sendKeyStroke(KEY_A+(c-'a'));
    if (c=='0')
      DigiKeyboard.sendKeyStroke(KEY_0);
    if (c>='1' && c<='9')
      DigiKeyboard.sendKeyStroke(KEY_1+(c-'1'));
    if (c == '!')
      DigiKeyboard.sendKeyStroke(KEY_1, MOD_SHIFT_LEFT);
    i++;
    c = str[ i ];
  }
}

void println (char *str) {
  print(str);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
}
void sleep(int seconds) { 
  delay(seconds * 1000); 
}
void loop() {
  println ("!work");
  sleep(17);
}
```
## Issues
The code took a few tries to upload to the board. I suspect it's because my Mac only has USB-C ports, and using a converter makes it go funky; however, after a few plug cycles, it started working, so I stayed with the DigiSpark. Alternatively, you could use an Arduino UNO. However, you would have to put it in [DFU mode and flash a custom firmware](http://mitchtech.net/arduino-usb-hid-keyboard/), which I didn't feel like doing. 

## It's Alive!! 

Ignore the chewed up USB-C dongle, my dog managed to get to it the day before. Now it's a matter of leaving it running overnight.

![alt text](./images/stonks1.gif "")

## My AtTiny Got in trouble

The next morning I noticed that I was muted from the chat, with got about 450,000 (you needed 500,000 for the flag). So close! What happened? Was automation against the rules? (I should mention I didn't really look into the challenge that much). Did my little Arduino mess up and started sending bad words? 

I opened a ticket with the CTF organizers, and after telling them honestly that my Arduino was doing most of the typing, and that it shall go to Android Hell for all of its wrongdoings, we were back in business. And they even let me keep using it!!

## Final Push

After re-plugging the DigiSpark into my computer and having it run for a little longer, we finally got enough Stonks to buy the flag! 

To avoid looking like a 🤖, I added a few random delays.

```Arduino
#include "DigiKeyboard.h"

void setup() {

}

void print(char *str) {
  char c = str[0];
  byte i = 0;
  DigiKeyboard.update();
  DigiKeyboard.sendKeyStroke(0); //this is generally not necessary but with some older systems it seems to prevent missing the first character after a delay
  while (c != 0) {
    if (c==' ')
      DigiKeyboard.sendKeyStroke(KEY_SPACE);
    if (c>='A' && c<='Z')
      DigiKeyboard.sendKeyStroke(KEY_A+(c-'A'), MOD_SHIFT_LEFT);
    if (c>='a' && c<='z')
      DigiKeyboard.sendKeyStroke(KEY_A+(c-'a'));
    if (c=='0')
      DigiKeyboard.sendKeyStroke(KEY_0);
    if (c>='1' && c<='9')
      DigiKeyboard.sendKeyStroke(KEY_1+(c-'1'));
    if (c == '!')
      DigiKeyboard.sendKeyStroke(KEY_1, MOD_SHIFT_LEFT);
    i++;
    c = str[ i ];
  }
}

void println (char *str) {
  print(str);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
}
void sleep(int seconds) { 
  delay(seconds * 1000); 
}
void loop() {
  println ("!work");
  sleep(16 + random(1,4));
}
```

And we get the flag!

![alt text](./images/flag.png "Finally! The flag!")


## Conclusion
Main takeaway, ask admins about automating something before doing it. But if you are going to do it `Arduino HID emulation >>>>> Any other kind of scripting`

If I had a Raspberry Pi doing the automation, I could have said that my ARM was doing the typing... 🤖
