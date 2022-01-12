# moddable
A moddable madlibs

# usage

You can change stuff in config.py
And implement in main.py

```python
# config.py
line1 = "Roses are red"
line2 = "I have depression"
line3 = "A man killed his friend for not "
```

```python
from config import *
from getch import getch
from os import system

print(line1+"\n"+line2+"\n"+line3+"_____\n")

print("Press any key to continue...")
getch()
system("clear")
b = input("Enter a something: ")
prnt("\n")
print(line1+"\n"+line2+"\n"+line3+b+"\n")
```

### output

```
Roses are red
I have depression
A man killed his friend for not _____

Press any key to continue...
```

```
Enter something: saying no-homo after 10 hours anal session
Roses are red
I have depression
A man killed his friend for notsaying no-homo after 10 hours anal session
```
