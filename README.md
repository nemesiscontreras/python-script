# python-script

###  In Depth Tutorial for running a Python 3 script on MAC from the terminal




1. Download and Open the test.py file in the terminal by using the command

```cd```

2. Check that the first line in the python program starts with the **shebang** (which is the definition for this "#!") stating the path to python3 : 

```#!/usr/bin/env python3```



3. To enable permission to execute the file we will use **chmod** which stands for change mode.
    Chmod is commonly used to make a file executable, readable, or writable.
    For more information about chmod check this site: [check this site](https://www.computerhope.com/unix/uchmod.htm)
    We will use the command -x which makes the file e*x*ecutable.

```chmod 755 test.py```

4. Run the script with

```./test.py```
