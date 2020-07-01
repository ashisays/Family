import sys

from src.familyapi import FamilyAPI


def main():
    file = sys.argv[1]
    if file != '':
        family_api = FamilyAPI()
        family_api.process_input_file("data/input.txt")
        family_api.process_input_file(file,print_result=True)


if __name__ == "__main__":
    main()
