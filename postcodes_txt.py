import requests
import json

def get_post_code(input_post_code):
    try:
        request_post_code = requests.get('https://api.postcodes.io/postcodes/' + input_post_code)
        return_postcode = request_post_code.json()["result"]["postcode"]

        return return_postcode
    except ConnectionError:
        print("Not a valid URL")


def append_to_file(file, order_item):
    try:
        with open(file, 'a') as opened_file:
            opened_file.write(order_item + '\n')

    except FileNotFoundError:
        print("File not found")

def open_read_file_using_with(file):
    try:
        with open(file, 'r') as open_file:
                for line in open_file.readlines():
                    print(line.rstrip('\n'))
    except FileNotFoundError as errmsg:
        print("File can not be found. Please check your input")
        print(errmsg)
        #raise
    finally:
        print('\n Execution complete')