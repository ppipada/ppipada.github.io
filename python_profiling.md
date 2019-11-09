# Python Profiling

## cProfile a single function
```
import cProfile, pstats, StringIO

pr = cProfile.Profile()
pr.enable()
//change = self.emit_next_change()
//do something
pr.disable()
s = StringIO.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
SyncLog.info("Profilestats: %s", s.getvalue())
```