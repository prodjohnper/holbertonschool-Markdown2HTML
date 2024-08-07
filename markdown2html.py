#!/usr/bin/python3
'''
	0-Start a script

	Script that converts a Markdown file to HTML
'''


import sys
import os


def main():
    '''
        Script that converts a Markdown file to HTML
    '''
    if len(sys.argv) < 3:

        err = "Usage: ./markdown2html.py README.md README.html"

        print(err, file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
