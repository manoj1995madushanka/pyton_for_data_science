import sys

a = []
print(sys.getrefcount(a))  # will output 2

b = a
print(sys.getrefcount(a))
print(sys.getrefcount(b))

del b
print(sys.getrefcount(a))

# Garbage collection
import gc

gc.enable()  # enable garbage collector

gc.collect()  # run the garbage collector manually

print(gc.get_stats())  # get garbage collection stats

print(gc.garbage)  # get unreachable objects

## Profiling memory usage
import tracemalloc


def create_list():
    return [i for i in range(10000)]


def main():
    tracemalloc.start()
    create_list()
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print("[Top 10]")
    for stat in top_stats[:10]:
        print(stat)

main()