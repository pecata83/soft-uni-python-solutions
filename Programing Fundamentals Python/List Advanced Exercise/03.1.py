# version = [int(n) for n in input().split(".")]
version = input().split(".")

next_version = str(int("".join(version)) + 1)

print(".".join(list(next_version)))
