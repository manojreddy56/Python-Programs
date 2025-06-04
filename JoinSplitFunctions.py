generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7'
]

values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

integer_list = []
for st in values_list:
    num = int(st)
    integer_list.append(num)
    
print(integer_list)
    