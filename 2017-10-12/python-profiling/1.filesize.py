# python 1.filesize.py

import cStringIO
from collections import OrderedDict
import pexpect

PROMPTS = OrderedDict({
    pexpect.EOF: None,
})

child = pexpect.spawn('du', ['-h', __file__])
child.logfile_read = cStringIO.StringIO()
while child.isalive():
    index = child.expect(PROMPTS.keys())
    answer = PROMPTS.values()[index]
    if answer is not None:
        child.sendline(answer)

print child.logfile_read.getvalue()
