import requests
import json

arguments = "N169LN"

request_post_code = requests.get('https://api.postcodes.io/postcodes/' + arguments)

converting_to_json = request_post_code.json()["result"]["postcode"]

#print(converting_to_json)

print(converting_to_json)

def append_to_file(file, order_item):
    try:
        opened_file = open(file, 'a')
        opened_file.write(order_item)

        opened_file.close()
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