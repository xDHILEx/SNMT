import ConfigParser
from subprocess import *

config = ConfigParser.ConfigParser()
config.read('config.ini');

TEXT = ''

# SNMT info
DEST_IP = config.get('SNMT', 'dest_ip')
THRESH = config.getfloat('SNMT', 'thresh')

# mtr pipes a wide report without name resolution on the DEST_IP to awk
mtr = Popen(('mtr', '-wn', DEST_IP), stdout=PIPE)
# awk returns the columns 2, 5 and 6 of the piped mtr report
awk = check_output(('awk', '{ print $2, $5, $6}'), stdin=mtr.stdout)
# l is a list of awk split on each word
l = awk.split()
# WORST, AVG, RET_IP just pop strings in order, as SNMT is only concerned with the DEST_IP
WORST = float(l.pop())
AVG = float(l.pop())
RET_IP = l.pop()

# In an instance where mtr returns ??? for RET_IP
if DEST_IP != RET_IP:
    TEXT = 'The DEST_IP - %s, could not be found.' % DEST_IP

# In an instance where the threshold is reached
if AVG > THRESH or WORST > THRESH:
    TEXT = 'The THRESH: %1.1fms was exceeded either by AVG: %1.1fms, or WORST: %1.1fms.' % (THRESH, AVG, WORST)

if len(TEXT) == 0:
    print 'No problems!'
else:
    print TEXT
