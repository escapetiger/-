"""
作者：Escape
功能：Currency Converter
版本：3.0
日期：2020-04-20
"""
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError


def main():
    print("*"*60)
    print("Welcome to Currency Converter")
    CRate, CCode = CurrencyRates(), CurrencyCodes()
    k = 1
    while input("Continue? (Y/N): ").upper() == 'Y':
        print("="*25+" Round "+str(k)+' '+"="*25)
        # Input
        amount = input("Enter the amount you wish to convert: ")
        base = input("Input the base currency: ").upper()
        target = input("Input the target currency: ").upper()
        try:
            result = CRate.convert(base, target, float(amount))
            print("{} {}({}) is {} {}({})".format(amount, base, CCode.get_symbol(base),
                                      round(result, 2), target, CCode.get_symbol(target)))
        except RatesNotAvailableError:
            print('The base or target currency are not supported, please refer to '
                  'https://forex-python.readthedocs.io/en/latest/currencysource.html')
        except ValueError:
            print('Please enter correct amount! Only number!')
        print("="*60, '\n')
        k += 1
    print("*"*60)
    print("Thanks for your support! Welcome come to use next time!")

if __name__ == '__main__':
    main()



