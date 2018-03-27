# python-script

###  In Depth Tutorial for Understanding Why Python runs version 2.7 and Python3 runs 3.x




1. Download and Open the test.py file in the terminal by using the command

```cd```

2. Check that the first line in the python program starts with the **shebang** (which is the definition for this "#!") stating the path to python3 : 

```#!/usr/bin/env python3```  Or you can use the local path depending on what you are doing  ```#!/usr/local/bin/python3```



3. To enable permission to execute the file we will use **chmod** which stands for change mode.
    Chmod is commonly used to make a file executable, readable, or writable.
    For more information about chmod check this site: [check this site](https://www.computerhope.com/unix/uchmod.htm)
    We will use the command 755  which makes the file  executable, readable, and writable by the user.

```chmod 755 test.py``` the ```chmod 755 test_two.py```

4. Run the scripts with

```./test.py```   then run the second script with ```./test_two.py```  
