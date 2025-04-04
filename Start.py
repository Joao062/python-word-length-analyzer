word_list = ["Banana", "Liver", "faucet", "paralelepiped", "Absorvent", "Pickaxe"]

def largestWord(param):
    if not param:
        return "The list is empty."
    list = word_list
    largest = ""
    for word in list:
        if len(word) > len(largest):
            largest = word
    return largest

print(largestWord(word_list))