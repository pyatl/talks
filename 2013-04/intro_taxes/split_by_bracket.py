from brackets import brackets


def split_by_bracket(earnings, filing_status):
    result = []
    remaining = earnings

    for bracket in brackets:
        # pull out the max amount for this
        # bracket and filing_status
        bracket_amount = getattr(bracket, filing_status)

        if bracket_amount and earnings > bracket_amount:
            remaining = earnings - bracket_amount
            result.append((bracket_amount, bracket.tax_rate))
        else:
            result.append((remaining, bracket.tax_rate))
            break

    return result



# as in brackets.py, this bit prints some examples if you run
#
#       python split_by_bracket
#

if __name__ == '__main__':
    for amount in (5000, 11000, 24000):
        print 'single ${}:'.format(amount), \
              split_by_bracket(amount, 'single')

    print

    for amount in (7000, 15000, 19000, 31000):
        print 'married ${}:'.format(amount), \
              split_by_bracket(amount, 'married_joint')
