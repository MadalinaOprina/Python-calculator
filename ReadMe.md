# Contribuția membrilor din grupă

- **Mădălina**:
-- m-am ocupat de căutat coduri sau modele de realizare a unui calculator, atât aritmetic, cât și științific.
-- am căutat tutoriale pe w3Schools despre cum se utilizează biblioteca tkinter.
-- am participat la partea de testare a calculatorului.

- **Fabian**:
-- am lucrat la partea de cod utilizând Python IDLE, ultima versiune de pe python.org.
-- am testat calculatorul (am împarțit la 0, am testat să văd dacă îmi calculează o ecuație copiată si am adăugat caractere pe care calculatorul nu le poate identifica, cum ar fi litere din alfabet)

Fiecare am contribuit în felul nostru în realizarea acestui calculator.

# Research efectuat

**Pe parte de testare**:
- am preluat mesajul "Happy (20+24)+(20+24)×(20+24)+(20+24)" și am observat că calculatorul nu recunoaște "×" (cross product). Am înlocuit pe "×" cu "*" și calculatorul mi-a returnat valoarea 2024.
- totodată, cu mesajul de mai sus, am testat și ordinea operațiilor pe care le efectuează calculatorul.
- am împărțit la 0 și calculatorul mi-a returnat "Syntax error". De asemenea, am testat și la funcțiile "cot", "ln", "log" și a returnat "Syntax Error".
- am încercat să adaug numere negative în funcțiile "ln" și "log" și calculatorul returna "Syntax error".
- permite operații cu numere întregi (pozitive și/sau negative) și cu virgulă.

**Referințe**:
- https://thecleverprogrammer.com/2020/12/05/calculator-gui-with-python/ -> de pe acest site am preluat ideea de cod pentru calculator.
- https://www.geeksforgeeks.org/make-simple-calculator-using-python/ -> la început am creat un simplu calculator aritmetic, ca apoi să îl dezvoltăm într-un calculator științific.
- https://www.w3schools.com/python/python_math.asp / https://www.w3schools.com/python/module_math.asp -> tutoriale despre biblioteca "math" pe care o are Python privind funcțiile știintifice (sin, cos, tg, radical etc.)
- https://www.geeksforgeeks.org/scientific-gui-calculator-using-tkinter-in-python/ -> codul de la care am plecat pentru a putea realiza calculatorul știintific.
- https://youtu.be/NzSCNjn4_RI?si=zospE5rckisxcjOQ -> am utilizat acest videoclip de pe YouTube pentru a putea înțelege cum se lucrează cu interfața bibliotecii tkinter.
- https://chat.openai.com/share/a8dbdb1f-d61d-4ec9-95d0-9d8a8892d504 -> am folosit ChatGPT pentru a aduce modificări în cod și să ne ajute să creem interfața, dar de cele mai multe ori nu făcea ceea ce doream (de exemplu, punea butonul "backspace" separat de restul calculatorului)
- https://chat.openai.com/share/48def38f-ea6d-4b00-a00b-8073287d39f6 -> cu ChatGPT, versiunea Premium, am reușit să rezolvăm problemele pe care versiunea gratuită a acestuia nu a reușit.

# Cum rulez programul?
1) Descarcă Python IDLE de pe python.org (recomand să fie instalată ultima versiune disponibilă în acel moment).
2) Bibliotecile utilizate sunt: **tkinter** și **math**. Acestea vin în pachetul de instalare al lui Python. Nu sunt necesare și alte biblioteci suplimentare.
3) Deschideți "Command Prompt".
4) Navigați la directorul în care se află fișierul respectiv utilizând comanda "cd".
5) Executați în "Command Prompt" comanda: "python calculator.py".