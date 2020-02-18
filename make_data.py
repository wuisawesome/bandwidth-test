import os

from random import randint

def gen_size():
    # 1KB - 1 MB is a generally representative range for imagenet pictures
    return randint(2**10, 2**20)

num_files = 50*1000

output_dir = "data/"

os.makedirs(output_dir, exist_ok=True)

for i in range(num_files):
    file_path = "%s/%i.dat" % (output_dir, i)
    size = gen_size()
    num_blocks = size / (2**10)
    os.system("dd if=/dev/urandom of=%s bs=1024 count=%i" % (file_path, num_blocks))
    print(i)

print("Done.")

