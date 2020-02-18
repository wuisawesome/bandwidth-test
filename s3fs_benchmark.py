import s3fs

fs = s3fs.S3FileSystem(anon=False)

files = fs.ls("anyscale-data/bandwidth-benchmark")

for path in files:
    data = fs.open(path, 'wb').read()
    x = 0
    for byte in data:
        x ^= byte
    print(".", end="", flush=True)



