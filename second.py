mood_index = int(input("your mood leve is :"))

# the return value of input is String, so need to convert to int
if mood_index>=60:
    print ("You can")
    print('YYYY77')
else:
    print ("d not")


#
slang_dict={"ZYP":"Julie","YYDS":"God","Kai":"Yao Kai"}
print(slang_dict)
slang_dict["Tim"]='Yang'
print(slang_dict)
print(slang_dict["ZYP"])

query=input("please input:")
if query in slang_dict:
    print("yes, here it is:" + query)
    print(slang_dict[query])
else:
    print('what you want is not available')
print('we have: ' + str(len(slang_dict)))