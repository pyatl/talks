# python -m cProfile -s cumulative 3.display_file.py | less

import cStringIO
from collections import OrderedDict
import pexpect

PROMPTS = OrderedDict({
    pexpect.EOF: None,
})

child = pexpect.spawn('cat', ['large'])
child.logfile_read = cStringIO.StringIO()
while child.isalive():
    index = child.expect(PROMPTS.keys())
    answer = PROMPTS.values()[index]
    if answer is not None:
        child.sendline(answer)
