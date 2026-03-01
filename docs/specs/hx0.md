# `hx0` Specification

## 1. Introduction

`hx0` is a data representation format designed for the absolute lowest level of a bootstrap chain. It allows raw machine code bytes to be annotated with comments and structured with whitespace without affecting the resulting binary output. This enables the implementation of more complex algorithms in raw hex while having human-readable documentation and structural clarity within the source file.


## 2. Lexical Rules
### 2.1 Hexadecimal Tokens

* **Alphabet**: `0-9`, `A-F`.

* **Parsing**: The parser identifies and groups valid characters into pairs. Every pair represents a single 8-bit byte in the output binary.

  > **Example**: The ASCII sequence `4D` is parsed into the numerical byte `0x4D`.

* **Endianness**: The parser writes bytes strictly in the order they appear in the source. Multi-byte values must be written according to the target architecture's endianness.


### 2.2 Ignored Characters

* **Rule**: Any character that is not a valid Hexadecimal Token, the Comment Trigger (`#`), or the Comment Terminator (`\n`) is unconditionally ignored.

* **Implication**: Spaces, tabs, carriage returns, and completely invalid characters (like `Z` or `a`) are simply dropped by the lexer.


### 2.3 Comments

* **Trigger**: The `#` (`0x23`) character.

* **Behavior**: Upon encountering the trigger, the parser enters an "ignore state". It discards all subsequent characters (including valid hex tokens) until a Newline (`0x0A`) is reached, which resets the parser to normal operation.


## 3. Implementation Requirements

Any implementinon of `hx0` specification must do to the following:

1. **Minimalist Lexing**: Drop any character that is not a defined hex digit, the comment trigger, or the comment terminator. Do not halt execution for "invalid" characters.

1. **Byte Buffering**: Buffer exactly two hexadecimal digits before emitting a single byte to the output stream.

1. **State Reset**: Reset the comment state strictly upon encountering the '\n' character.
