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
