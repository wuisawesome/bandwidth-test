import ray
from ray.util import iter
import s3fs
from time import perf_counter as clock

ray.init()
fs = s3fs.S3FileSystem(anon=False)

files = fs.ls("anyscale-data/bandwidth-benchmark")[:1000]

@ray.remote
def download(path):
    data = fs.open(path, 'rb').read()
    x = 0
    for byte in data:
        x ^= byte


start = clock()
iter = iter.from_iterators(files).for_each(download)
results = iter.gather_sync()
for data in results:
    x = 0
    for byte in data:
        x ^= byte
    print(".", end="", flush=True)
end = clock()

print("Total download time: ", (end - start))
