# python 2.filesize.py

import cStringIO
from collections import OrderedDict
import pexpect
import re

PROMPTS = OrderedDict({
    pexpect.EOF: None,
    re.compile(r'Enter passphrase for .*:\s*?$', re.M): 'some-ssh-passphrase'
})

child = pexpect.spawn('du', ['-h', __file__])
child.logfile_read = cStringIO.StringIO()
while child.isalive():
    index = child.expect(PROMPTS.keys())
    answer = PROMPTS.values()[index]
    if answer is not None:
        child.sendline(answer)

print child.logfile_read.getvalue()
