from brackets import brackets


def split_by_bracket(earnings, filing_status, _i=0, _already_taxed=0):
    bracket = brackets[_i]
    bracket_amount = getattr(bracket, filing_status)

    if not bracket_amount or earnings <= bracket_amount:
        return [(earnings - _already_taxed, bracket.tax_rate)]
    else:
        return [(bracket_amount - _already_taxed, bracket.tax_rate)] + \
                split_by_bracket(earnings, filing_status, 
                    _i=_i + 1, _already_taxed=bracket_amount)


if __name__ == '__main__':
    for amount in (5000, 11000, 24000):
        print 'single ${}:'.format(amount), \
              split_by_bracket(amount, 'single')

    print

    for amount in (7000, 15000, 19000, 31000):
        print 'married ${}:'.format(amount), \
              split_by_bracket(amount, 'married_joint')
