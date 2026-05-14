class HashTable:
    # Just building "size" length array of None to stroe the key-value pairs
    # According to their Hash address
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def _hash(self, key):
        my_hash = 0
        # "ord is for getting the ascii value of the letter"
        # Then we are multiping it by 23 (use any prime number you want- prime to avoid collisions)
        # The modulo "%" will return the reminder of the dicision calc operation, so since 
        # the length of data_map is 7, than the reminder will always be a number between 0 to 6
        # So at the end the my_hash will be a number between 0 to 6 according the the key letters
        # which will fit to the size of our data_map array for storing the key-value pairs, in this address
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for idx, value in enumerate(self.data_map):
            print(idx, ": ", value)


my_hash_table = HashTable()
my_hash_table.print_table()
