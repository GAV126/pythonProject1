gpa_dict={"Tim":3.445,"Kai":3.432,"Julie":4.433,"Andy":3.41}

for name in gpa_dict:
    print("hello {0} , you gpa is : {1}".format(name,gpa_dict[name]))

print('------------------------------------------------------')

for name in gpa_dict:
    print("hello {NAME} , you gpa is : {GPA}".format(NAME=name, GPA=gpa_dict[name]))