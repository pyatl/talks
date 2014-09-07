#!/usr/bin/env python

import string

values = {'var': 'foo'}

t = string.Template("""
$var
$$
${var}iable
""")

print 'TEMPLATE:', t.substitute(values)
