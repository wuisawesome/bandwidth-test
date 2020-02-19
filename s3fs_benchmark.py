import s3fs
from time import perf_counter as clock

fs = s3fs.S3FileSystem(anon=False)

files = fs.ls("anyscale-data/bandwidth-benchmark")[:1000]


start = clock()
for path in files:
    data = fs.open(path, 'rb').read()
    x = 0
    for byte in data:
        x ^= byte
    print(".", end="", flush=True)

end = clock()

print("Total download time: ", (end - start))

