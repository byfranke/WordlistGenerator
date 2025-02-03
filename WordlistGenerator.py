#!/usr/bin/env python3
import sys
import datetime
import os
import argparse
import logging
from unicodedata import normalize
from typing import Set, List, Iterator

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

substitutions_dict: dict[str, str] = {'aioO': '@100', 'aeioOs': '43100$', 'aeiou': 'AEIOU', 'IilLsS': '1111$$'}
current_year: int = datetime.datetime.now().year

def generate_variants(word: str) -> Set[str]:
    return {word, word.upper(), word.lower(), word.capitalize(), word.title(), word.swapcase()}

def normalize_text(text: str) -> str:
    return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')

def apply_substitutions(word: str) -> Set[str]:
    modified: Set[str] = {word}
    for key, value in substitutions_dict.items():
        modified.add(word.translate(str.maketrans(key, value)))
    return modified

def append_numeric_suffixes(variant: str, max_num: int) -> Set[str]:
    variants: Set[str] = {f"{variant}{current_year}", f"{variant}@{current_year}"}
    for n in range(max_num + 1):
        variants.add(f"{variant}{n}")
        variants.add(f"{variant}@{n}")
    return variants

def generate_wordlist_gen(words: List[str], max_num: int, use_numeric: bool) -> Iterator[str]:
    seen: Set[str] = set()
    for word in words:
        normalized_word = normalize_text(word.strip())
        if not normalized_word:
            continue
        for mod_word in apply_substitutions(normalized_word):
            for variant in generate_variants(mod_word):
                if variant not in seen:
                    seen.add(variant)
                    yield variant
                if use_numeric:
                    for suff_variant in append_numeric_suffixes(variant, max_num):
                        if suff_variant not in seen:
                            seen.add(suff_variant)
                            yield suff_variant

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Wordlist Generator - Create password lists with different transformations.",
        epilog="More information: https://github.com/byfranke/WordlistGenerator"
    )
    parser.add_argument("-i", "--input", help="Import a text file with words", metavar="FILE")
    parser.add_argument("-w", "--write", help="Manually enter words separated by '|'", metavar="WORDS")
    parser.add_argument("-o", "--output", help="Specify the output filename", metavar="OUTPUT_FILE")
    parser.add_argument("--max-num", help="Maximum number for numeric suffix (default: 1000)", type=int, default=1000)
    parser.add_argument("--no-numeric", help="Disable numeric suffix generation", action="store_true")
    args = parser.parse_args()
    if args.max_num < 0:
        logging.error("The maximum numeric suffix must be non-negative.")
        sys.exit(1)
    if args.input:
        if not os.path.isfile(args.input):
            logging.error(f"File '{args.input}' not found.")
            sys.exit(1)
        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                words = [line.strip() for line in f if line.strip()]
        except Exception as e:
            logging.error(f"Error reading file: {e}")
            sys.exit(1)
        output_filename = args.output if args.output else f"{os.path.splitext(args.input)[0]}_wordlist.txt"
    elif args.write:
        words = [w.strip() for w in args.write.split("|") if w.strip()]
        output_filename = args.output if args.output else "custom_wordlist.txt"
    else:
        parser.print_help()
        sys.exit(1)
    try:
        with open(output_filename, 'w', encoding='utf-8') as out:
            for line in generate_wordlist_gen(words, args.max_num, not args.no_numeric):
                out.write(line + "\n")
        logging.info(f"Wordlist successfully generated: {output_filename}")
    except Exception as e:
        logging.error(f"Error writing file: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
