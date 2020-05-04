import logging
import cProfile
import pstats
import StringIO

from closure_chaining_example import smain

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
pr = cProfile.Profile()
pr.enable()
smain()
# do something
pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
logging.info("Profilestats: %s", s.getvalue())
