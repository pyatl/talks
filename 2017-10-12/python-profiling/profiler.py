import cProfile
import pstats
from contextlib import contextmanager

@contextmanager
def profile():
    prof = cProfile.Profile()
    prof.enable()
    yield
    prof.disable()
    with open('output.pstats', 'w') as f:
        pstats.Stats(prof).dump_stats(f.name)
