# jakes-python-menu
> Source code for my python menu library

# How to install
```bash
pip install jakes-python-menu
```

# API
> How to make a menu
```py
import jakespymenu

retval = jakespymenu.pyMenu.createMenu("Menu Name", ["Option 1", "Option 2", "Option 3"])

if retval == "Option 1":
    print("Option 1 chosen")
elif retval == "Option 2":
    print("Option 2 chosen")
elif retval == "Option 3":
    print("Option 3 chosen")
```
