from split_by_bracket import split_by_bracket

def tax(earnings, filing_status):
    earnings_by_bracket = split_by_bracket(earnings, filing_status)

    tax_by_bracket = [amount * tax_rate 
                      for amount, tax_rate in earnings_by_bracket]

    return sum(tax_by_bracket)



if __name__ == '__main__':
    for amount in (5000, 11000, 24000):
        print 'single ${}:'.format(amount), tax(amount, 'single')

    print

    for amount in (7000, 15000, 19000, 31000):
        print 'married ${}:'.format(amount), tax(amount, 'married_joint')
