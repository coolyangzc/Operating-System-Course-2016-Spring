# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 08:44:41 2016

@author: Jie
"""

import sys
from optparse import OptionParser
import random
import math

#
# main program
#
parser = OptionParser()
parser.add_option('-a', '--addresses', default='-1',   help='a set of comma-separated pages to access; -1 means randomly generate',  action='store', type='string', dest='addresses')
parser.add_option('-p', '--policy', default='WORKSET',    help='replacement policy: FIFO, LRU, OPT, CLOCK',                action='store', type='string', dest='policy')
parser.add_option('-c', '--compute', default=False,    help='compute answers for me',                                                action='store_true', dest='solve')
parser.add_option('-f', '--pageframesize', default='5',    help='size of the physical page frame, in pages',                                  action='store', type='string', dest='pageframesize')
parser.add_option('-r', '--parameter', default='3',    help='parameter value',                                  action='store', type='string', dest='param')

(options, args) = parser.parse_args()

print 'ARG addresses', options.addresses
print 'ARG policy', options.policy
print 'ARG pageframesize', options.pageframesize
print 'ARG param' ,options.param

addresses   = str(options.addresses)
policy      = str(options.policy)
pageframesize   = int(options.pageframesize)
param = int(options.param)

addrList = []
addrList = addresses.split(',')

if options.solve == False:
    print 'Assuming a replacement policy of %s, and a physical page frame of size %d pages,' % (policy, pageframesize)
    print 'figure out whether each of the following page references hit or miss'

    for n in addrList:
        print 'Access: %d  Hit/Miss?  State of Memory?' % int(n)
    print ''

else:
    count = 0
    memory = []
    hits = 0
    miss = 0
    if policy == 'WORKSET':
        for i in range(len(addrList)):
            if not addrList[i] in memory:
                miss += 1
                print 'Address %s missed' % (addrList[i])
            else:
                hits += 1
                print 'Address %s hit' % (addrList[i])
            memory = addrList[max(0, i - param + 1): i + 1]
    elif policy == 'MISSRATE':    
        lastmiss = -1
        for i in range(len(addrList)):
            if not addrList[i] in memory:
                if i - lastmiss > param:
                    memory = addrList[lastmiss : i + 1]
                else:
                    memory.append(addrList[i])
                lastmiss = i
                miss += 1
                print 'Address %s missed' % (addrList[i])
            else:
                hits += 1
                print 'Address %s hit' % (addrList[i])
    else:
        print 'Policy %s is not yet implemented' % policy
        exit(1)
    print ''
    print 'FINALSTATS hits %d   misses %d   hitrate %.2f' % (hits, miss, (100.0*float(hits))/(float(hits)+float(miss)))
    print ''