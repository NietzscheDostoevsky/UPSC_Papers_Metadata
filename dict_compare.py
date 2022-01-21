dict1 = {"1": "one", "2": "two", "3": "three", "4": "four"}

dict2 = {"1": "eleven", "2": "two",
         "4": "thirteen", "5": "five", "6": "sixteen"}

for key1, value1 in dict1.items():
    for key2, value2 in dict2.items():
        if key1 == key2:
            print("Syl : {:<15s} : {:>1s} | Pap : {:<15s} : {:>1s} ".format(
                key1, value1, key2, value2))
