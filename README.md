# py-reess 

CLI application for deterministic password generation and recall

Failing to **REE**call your pa**SS**word? Try **py-REESS**!

[![Python Version](https://img.shields.io/pypi/pyversions/pyreess.svg?color=yellow&style=flat-square)](https://www.python.org/downloads/)
[![GitHub Licence](https://img.shields.io/github/license/BananaLoaf/pyreess.svg?color=blue&style=flat-square)](https://github.com/BananaLoaf/pyreess/blob/master/LICENSE)
[![Package Version](https://img.shields.io/pypi/v/pyreess.svg?color=green&style=flat-square)](https://pypi.org/project/pyreess/)

### Install
```bash
pip install pyreess
```

### Usage
```bash
pyreess --help
```
The core principle is simple - **for the same input you get the same output**. 
The input consists of input string, salt, length and alphabet (digits, lowercase, uppercase, symbols).
Output is the generated password and can always be restored with the same input.
