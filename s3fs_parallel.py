import ray
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
ids = [download.remote(path) for path in files]
ray.get(ids)
end = clock()

print("Total download time: ", (end - start))
