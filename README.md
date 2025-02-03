# Wordlist Generator

Wordlist Generator is a Python script that generates customized wordlists based on input words with a variety of transformations. It applies multiple modifications—such as case variations, accent removal, and character substitutions—to create extensive lists suitable for password cracking, testing, and security assessments.

## Features

- **Variant Generation:** Creates multiple versions of each word (uppercase, lowercase, capitalize, title, swapcase).
- **Normalization:** Removes accents and special characters for consistency.
- **Character Substitutions:** Applies predefined substitutions to generate alternative word forms.
- **Numeric Suffixes:** Optionally appends numeric suffixes (including the current year and sequential numbers) to each variant.
- **Flexible Input:** Supports input via a text file or manual entry.
- **Memory Efficiency:** Uses a generator to write the wordlist line-by-line, reducing memory usage.
- **Customizable:** Options to set the maximum numeric suffix and disable numeric suffix generation entirely.
- **Logging:** Uses Python’s `logging` module to provide informative output and error messages.

## Requirements

- Python 3.x

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/WordlistGenerator.git
```
```bash
cd WordlistGenerator
```
```bash
chmod +x WordlistGenerator.py
```
```bash
./WordlistGenerator.py
```
or 
```bash
Python3 WordlistGenerator.py
```

Ensure you have Python 3 installed on your system.

## Usage
You can run the script directly from the command line. The available arguments are:

  -i, --input: Specify a text file with words (one per line).

  -w, --write: Provide words manually, separated by the pipe character (|).

  -o, --output: Define the output filename (default is derived from the input filename or custom_wordlist.txt).

  --max-num: Set the maximum numeric suffix to append (default is 1000).

  --no-numeric: Disable numeric suffix generation.

## Examples

Generate a wordlist from an input file:
```bash
./WordlistGenerator.py -i input.txt -o my_wordlist.txt
```
Generate a wordlist from manually provided words:
```bash
./WordlistGenerator.py -w "password|admin|user" --max-num 500
```
Generate a wordlist without numeric suffixes:
```bash
./WordlistGenerator.py -w "example|test" --no-numeric
```

## How It Works

- **Normalization:** Each input word is normalized by removing accents and special characters.

- **Character Substitutions:** The script applies a set of predefined substitutions to each normalized word, creating alternative representations.

- **Variant Generation:** Multiple case variations are generated for each word, including uppercase, lowercase, capitalize, title, and swapcase forms.

- **Numeric Suffixes:** For each variant, numeric suffixes (e.g., the current year, sequential numbers, and versions with an "@" symbol) are appended unless disabled by the user.

## Logging
The script utilizes Python’s logging module to provide detailed output on the process and error messages, making it easier to debug and track the generation process.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests if you have suggestions or improvements.

## Disclaimer
This tool is designed for educational and testing purposes only. The creator strictly discourages and disclaims any responsibility for its use in unauthorized or malicious activities. Always obtain explicit permission before deploying this tool in any environment.

## Donations
If you find these tools useful and would like to support ongoing development and maintenance, please consider making a donation. Your contribution helps ensure that these tools are regularly updated and improved, benefiting the cybersecurity community. Any amount is greatly appreciated and will make a significant difference in supporting this project. Thank you for considering supporting this work!

- **Address Bitcoin:**
```bash
bc1qkdh3eqpj87q5hlhc7pvm025hmsd9zp2kadxf76
```
