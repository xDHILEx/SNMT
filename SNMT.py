import ConfigParser
from subprocess import *

config = ConfigParser.ConfigParser()
config.read('config.ini');

TEXT = ''

# SNMT info
DEST_IP = config.get('SNMT', 'dest_ip')
THRESH = config.getfloat('SNMT', 'thresh')

mtr = Popen(('mtr', '-rwn', DEST_IP), stdout=PIPE)
awk = check_output(('awk', '{ print $2, $5, $6}'), stdin=mtr.stdout)
l = awk.split()
WORST = float(l.pop())
AVG = float(l.pop())
RET_IP = l.pop()

if DEST_IP != RET_IP:
    TEXT = 'The DEST_IP - %s, could not be found.' % DEST_IP

if AVG > THRESH or WORST > THRESH:
    TEXT = 'The THRESH: %1.1fms was exceeded either by AVG: %1.1fms, or WORST: %1.1fms.' % (THRESH, AVG, WORST)

if len(TEXT) == 0:
    print 'No problems!'
else:
    print TEXT
