import csv

textFile = "gardeningData.txt"

def main():
    data = getData()
    use = "Yes"
    
    while use[0].lower() == 'y':
        item = input("What seed would you like to calculate? ")

        match = find_partial_match(data, item)
        while match is None:
            item = input("Invalid item, please write a valid seed: ")
            match = find_partial_match(data, item)

        print(f"You are currently calculating {match}\n")

        invest, selling = calculate(data, match)

        
        print(f"\nYou have to invest {invest} to get {selling} flux leaving you with {selling - invest} profit per plant")

        

        use = input("Do you want to calculate again (type 'y')? ")
        print()

def getData():
    data = {}
    with open(textFile, 'r') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
            data[row[0]] = row[1:9]
    return data

def find_partial_match(data, item):
    for key in data.keys():
        if item.lower() in key.lower():
            return key
    return None

def calculate(data, item):
    totalPrice = 0
    
    print("Calculating Investment:")
    
    for i in range(3):
        totalPrice += int(data[item][i]) * int(input(f"What is the current price of {data['Name'][i]} (type 0 if you have it)? "))
    for i in range(2):
        if(data[item][3 + (i*2)] != "Crystal"):
            totalPrice += int(data[item][4 + (i * 2)]) * int(input(f"What is the unit price of {data[item][3 + (i * 2)]}? "))

    return totalPrice, sellingPrice(data,item)

def sellingPrice(data,item):
    print("\nCalculating Revenue:")
    seedName = item.replace(" seed", "")
    revenue = (int(data[item][7]) * 5) * int(input(f"What is the price per unit of {seedName}? "))
    return revenue

if __name__ == "__main__":
    main()
