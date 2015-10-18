import ConfigParser
from subprocess import *

config = ConfigParser.ConfigParser()
config.read('config.ini');

TEXT = ''

# SNMT info
DEST_IP = config.get('SNMT', 'dest_ip')
THRESH = config.getfloat('SNMT', 'thresh')

# mtr pipes a report without name resolution on the DEST_IP to awk
mtr = Popen(('mtr', '-rn', DEST_IP), stdout=PIPE)
# tail grabs the last line of the mtr report
tail = Popen(('tail', '-n', '1'), stdin=mtr.stdout, stdout=PIPE)
# awk returns the columns 2, 5 and 6 piped in from tail
awk = check_output(('awk', '{ print $2, $5, $6}'), stdin=tail.stdout)
# l is a list of awk split on each word
l = awk.split()
# WORST, AVG, RET_IP just pop strings in order, as SNMT is only concerned with the DEST_IP
WORST = float(l[2])
AVG = float(l[1])
RET_IP = l[0]

# In an instance where mtr returns ??? for RET_IP
if DEST_IP != RET_IP:
    TEXT = 'The DEST_IP - %s, could not be found.' % DEST_IP

# In an instance where the threshold is reached
if AVG > THRESH or WORST > THRESH:
    TEXT = 'The THRESH: %1.1fms was exceeded either by AVG: %1.1fms, or WORST: %1.1fms.' % (THRESH, AVG, WORST)

if not TEXT:
    print 'No problems!'
else:
    print TEXT
