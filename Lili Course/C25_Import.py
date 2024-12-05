#Median - self define
# def median(num_list):
#     sorted_list = sorted(num_list)
#     print(sorted_list)
#     n = len(sorted_list)
#     #if it is a odd, get the middle one
#     if n%2==1:
#         return sorted_list[n//2]
#     # if is even
#     else:
#         return (sorted_list[n//2] + sorted_list[n//2+1])/2
#
# print(median([8,7,1,2,3,4,5,6]))

# print('------------------------------------------------------')


import statistics
print(statistics.median([8,7,1,2,3,4,5,6]))

#pypi.org for third party module
