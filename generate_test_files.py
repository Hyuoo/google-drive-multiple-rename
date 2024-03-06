import os

if not os.path.exists("test"):
    os.mkdir("test")

for i in range(10):
    with open(f"test/test_file_{i}.txt", "w") as f:
        ...
