def store(path, extracted):
    with open(path, "a") as file:
        file.write(extracted + "\n")


def read(path):
    with open(path, "r") as file:
        data = file.read()
        return data