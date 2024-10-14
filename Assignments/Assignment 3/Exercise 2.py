def generate(list,num1,str1):
    if num1 == 0:
        print (str1)
        return
    for letter in list:
        generate(list,num1-1,str1+letter)
 
# Test of the function 
        
Characters = ["a","b","c"]
generate(Characters,2,"")