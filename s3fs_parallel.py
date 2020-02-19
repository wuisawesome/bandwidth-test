import ray
import s3fs
from time import perf_counter as clock

ray.init()
fs = s3fs.S3FileSystem(anon=False)

files = sorted(fs.ls("anyscale-data/bandwidth-benchmark"))[:1000]

@ray.remote
def download(path):
    data = fs.open(path, 'rb').read()
    return data


start = clock()
ids = [download.remote(path) for path in files]
results = ray.get(ids)
end = clock()
for data in results:
    x = 0
    if not data:
        print("f", end="", flush=True)
        continue
    for byte in data:
        x ^= byte
    print(".", end="", flush=True)

print("Total download time: ", (end - start))
