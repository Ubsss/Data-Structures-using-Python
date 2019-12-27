from Data_Structures.hashtables.hash_table import hash_table

my_hash_table = hash_table()


my_hash_table.insert('chuks', 27)
my_hash_table.insert('rody', 27)
my_hash_table.insert('lizzie', 28)
my_hash_table.insert('jp', 23)

print(my_hash_table.delete('jp'))
print(my_hash_table.delete('rody'))
print(my_hash_table.delete('jp'))


my_hash_table.print()
