from pathlib import Path
from yaml import load, FullLoader, dump
from datetime import timedelta, datetime


def get_iso_time(file, day):
    mtime = datetime.fromtimestamp(file.stat().st_mtime)
    mtime -= timedelta(days=day)
    return mtime.isoformat()[:-3] + "Z"


def format():
    res = {}

    for child in Path(".").parent.joinpath("leetcode").iterdir():
        if child.suffix == ".md":
            if child.stem == "README":
                continue
            name = child.stem
            difficulty = name.split("(")[-1].split(")")[0]
            title = name.split(".")[-1].split("(")[0].strip()
            res[int(name.split(".")[0])] = [title, difficulty, child.name, child]

    day = 0
    for key in sorted(res, reverse=True):
        fm = None
        lines = []
        with open(res[key][3], "r") as f:
            # read lines
            lines = f.readlines()
            # read front matters
            fm_end = lines[1:].index("---\n") + 1
            fm = load("".join(lines[1:fm_end]), Loader=FullLoader)
            # remove front matter from lines
            lines = lines[fm_end + 1 :]

        # adding new properties to front matter data
        if "date" not in fm:
            fm["date"] = get_iso_time(res[key][-1], day)
            day += 2

        remove = None
        if "title" not in fm:
            for line in lines:
                if line.startswith("# "):
                    fm["title"] = line.replace("# ", "").strip()
                    remove = line
                    break
        if "excerpt" not in fm:
            fm["excerpt"] = ""
        if remove:
            lines = filter(lambda x: x != remove, lines)

        # write back to file
        with open(res[key][3], "w") as f:
            f.write("---\n")
            f.write(dump(fm, allow_unicode=True))
            f.write("---\n")
            f.writelines(lines)

    # return "\n".join(reversed(table))


if __name__ == "__main__":
    format()
