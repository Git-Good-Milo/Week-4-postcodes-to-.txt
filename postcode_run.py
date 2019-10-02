from postcodes_txt import *

append_to_file("postcodes_txt.txt" ,"My name is Miles and this is my hood post code")
append_to_file("postcodes_txt.txt", get_post_code("N169LN"))
open_read_file_using_with("postcodes_txt.txt")