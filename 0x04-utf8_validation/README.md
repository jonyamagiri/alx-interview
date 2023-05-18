# 0x04. UTF-8 Validation

> This repository contains the tasks for `UTF-8 Validation` project and a description of what each program or function does:


## Learning Objectives

* UTF-8 is a character encoding standard that is widely used to represent text in computers and communication protocols. It can encode characters from the Unicode character set, which encompasses a vast range of characters from various writing systems.

* UTF-8 uses a variable-length encoding scheme, which means that characters can be represented using different numbers of bytes depending on their code points (numeric representation of a character). The encoding scheme allows for efficient storage and transmission of text, as it uses fewer bytes to represent commonly used characters while still accommodating less frequently used characters.

### Example to understand UTF-8 encoding:

* Emojis and Symbols:
UTF-8 can encode emojis, symbols, and other special characters. These characters often have higher code points and require more bytes for encoding. Let's consider the example of the thumbs-up emoji (👍), which has the code point 128077 (0x1F44D in hexadecimal):

- [x] In UTF-8, this emoji is represented using four bytes: 0xF0 0x9F 0x91 0x8D.
- [x] The leading byte 0xF0 indicates that four bytes are used for the character.
- [x] The following three bytes, 0x9F 0x91 0x8D, contain the binary representation of the code point.


## Tasks

### Task: 0-validate_utf8.py

* Write a method that determines if a given data set represents a valid UTF-8 encoding.

- [x] Prototype: `def validUTF8(data)`
- [x] Return: `True` if data is a valid UTF-8 encoding, else return `False`
- [x] A character in UTF-8 can be 1 to 4 bytes long
- [x] The data set can contain multiple characters
- [x] The data will be represented by a list of integers
- [x] Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer



