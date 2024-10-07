age = int(input("Enter your age"))
if age < 18:
    print ("insufficient age")
else:

    country = (input("Enter your country of residency")).lower()
    if country != "lebanon":
        print("foreign country")
    else:
    
        score = int(input("Enter your hackerrank score"))
        if score > 110:
            print("welcome to FCS!")
        else:
            print("insufficient hackerrank score")



