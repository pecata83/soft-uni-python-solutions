version = input()


def update_version(ver: str):
    version_list = ver.split(".")

    if version_list[-1] == "9":

        version_list[-1] = "0"

        if version_list[-2] == "9":
            version_list[-2] = "0"
            version_list[0] = str(int(version_list[0]) + 1)
        else:
            version_list[-2] = str(int(version_list[-2]) + 1)

        return ".".join(version_list)
    else:
        version_list[-1] = str(int(version_list[-1]) + 1)
        return ".".join(version_list)


print(update_version(version))
