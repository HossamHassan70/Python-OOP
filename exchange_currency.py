def convert_currency(amount, from_currency, to_currency):  
    rates = {  
        "USD": {"EUR": 0.99, "SAR": 3.75},  
        "EUR": {"USD": 1 / 0.99, "SAR": 3.75 / 0.99},  
        "SAR": {"USD": 1 / 3.75, "EUR": 0.99 / 3.75},  
    }  

    if from_currency == to_currency:  
        return amount  

    converted_amount = amount * rates[from_currency][to_currency]  
    return converted_amount  

def main():  
    print("=" * 30)  
    print("Welcome to $$ EXCHANGE STORE $$")  
    print("=" * 30)  
    print("1 USD = 3.75 SAR")  
    print("1 USD = 0.99 EUR")  
    print()  

    from_currency = input("Exchange FROM (USD, EUR, SAR): ").upper()  
    if from_currency not in ["USD", "EUR", "SAR"]:  
        print("Invalid currency. Please use USD, EUR, or SAR.")  
        return  

    amount = float(input("How much? "))  
    
    to_currency = input("Exchange TO (USD, EUR, SAR): ").upper()  
    if to_currency not in ["USD", "EUR", "SAR"]:  
        print("Invalid currency. Please use USD, EUR, or SAR.")  
        return  

    print(f"\nYou will give {amount} {from_currency}, and you will take ", end="")  
    
    converted_amount = convert_currency(amount, from_currency, to_currency)  
    print(f"{converted_amount:.2f} {to_currency}")  


main()