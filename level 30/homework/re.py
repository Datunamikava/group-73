def manual_join(arr,symbol):
    result = ""


    for i in arr:
        result += f"{i}{symbol}"


        return result[0: -len(symbol)]
    
    print(manual_join(["nika", "dato", "giorgi","luka","    "]))


    

def manual_split(str, symbol):
    result = []
    characters = ""
    
    for i in str:
        if i != symbol:
            characters += i
        else:
            result.append(characters)
            characters = ""
    
    result.append(characters)
    return result


print(manual_split("dato hello how are you?", " "))