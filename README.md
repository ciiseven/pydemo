# pydemo
A quick tool for creating Python demo projects

## Install
```
pip install pydemo
```
## Example
demo.py
```
import pydemo

print(pydemo.version())

pydemo.demo('test', './', author='', email='', github='')


```
The results 
```
test
├── LIENSE
├── README.md
├── install.sh
├── setup.py
└── test
    ├── __init__.py
    └── test.py
```
