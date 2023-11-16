#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(description="Language Identifier")
    subparsers = parser.add_subparsers(dest="command")

    # Train command
    train_parser = subparsers.add_parser("train", help="Train the frequency model")
    train_parser.add_argument("lang_id", type=str, help="Language code in two letter ISO 639-1 format")
    train_parser.add_argument("file", type=str, help="File to train on")

    # Identify command
    identify_parser = subparsers.add_parser("identify", help="Identify the language")
    identify_parser.add_argument("file", type=str, help="File to identify")

    args = parser.parse_args()
    if args.command == "train":
        pass # train(args.file)
    elif args.command == "identify":
        pass # identify(args.file)

if __name__ == "__main__":
    main()
