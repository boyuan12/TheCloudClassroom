import os

def add_static():
    files = os.listdir(r"templates/")
    checks = os.listdir(r"static/")
    paths = []
    for c in checks:
        fs = os.listdir(f"static/{c}")
        for f in fs:
            paths.append(c + "/" + f)

    for f in files:
        with open(f"templates/{f}", "r+") as r:
            c = str(r.read())
            for i in paths:
                c = c.replace(i, f"/static/{i}")

            with open(f"templates/{f}", "w") as a:
                a.write(c)
                a.close()

            r.close()

print(add_static())