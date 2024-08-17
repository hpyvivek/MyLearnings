# name = input("Enter your name:= ")
# print(f" Good afternoon {name}")

#replace function

letter = ''' Dear <|name|>, you are selected on <|date|>
'''
print(letter.replace("<|name|>","Vivek").replace("<|date|" ,"15th Aug 2024"))