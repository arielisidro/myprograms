##http://www.jeffknupp.com/blog/2012/10/04/writing-idiomatic-python/

list_from_comma_separated_value_file = ['dog', 'Fido', 10] 
(animal, name, age) = list_from_comma_separated_value_file
print animal
print name
print age

result_list = ['True', 'False', 'File not found']
result_string = ''
for result in result_list:
    result_string += result
print result_string

result_list = ['True', 'False', 'File not found']
result_string = '/'.join(result_list)
print result_string

log_severity = None
#if 'severity' in configuration:
#    log_severity = configuration['severity']
#else:
#    log_severity = log.Info
#print log_severity

#log_severity = configuration.get('severity', log.Info)
#import os
#file_handle = open(os.abspath(), 'r')
#for line in file_handle.readlines():
#    if some_function_that_throws_exceptions(line):
        # do something
#file_handle.close()

some_other_list=range(1,100)
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
        
my_odd_numbers=[element for element in some_other_list if is_odd(element)]
print my_odd_numbers
print my_odd_numbers[:3]

for index,element in enumerate(my_odd_numbers):
    print index,element,
    
tuple=1
tuple2=4
tuple,tuple2=tuple2,tuple
