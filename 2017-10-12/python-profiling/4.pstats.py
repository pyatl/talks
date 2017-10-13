# python 4.pstats.py
# pip install gprof2dot
# brew/yum/apt install graphviz
# gprof2dot -f pstats output.pstats | dot -Tpng -o output.png

from profiler import profile

import cStringIO
from collections import OrderedDict
import pexpect

PROMPTS = OrderedDict({
    pexpect.EOF: None,
})

with profile():
    child = pexpect.spawn('cat', ['large'])
    child.logfile_read = cStringIO.StringIO()
    while child.isalive():
        index = child.expect(PROMPTS.keys())
        answer = PROMPTS.values()[index]
        if answer is not None:
            child.sendline(answer)
