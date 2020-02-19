import s3fs
from time import perf_counter as clock

fs = s3fs.S3FileSystem(anon=False)

files = sorted(fs.ls("anyscale-data/bandwidth-benchmark"))[:1000]

start = clock()
results = []
for path in files:
    results.append(fs.open(path, 'rb').read())

end = clock()

for data in results:
    x = 0
    for byte in data:
        x ^= byte
    print(".", end="", flush=True)


print("Total download time: ", (end - start))

