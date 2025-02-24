while True:
    try:
        bill = float(input('Enter Bill Amount: '))
        tax = 0.07 * bill
        total = bill + tax
        print(f'Total Amount is: {total}')
        break
    except ValueError:
        print('Enter The Valid Value (like: 10.5, 5)')