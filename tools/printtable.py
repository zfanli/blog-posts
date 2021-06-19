from pathlib import Path
from urllib.parse import quote
from yaml import load, FullLoader


def maketable():
    res = {}

    for child in Path(".").parent.joinpath("leetcode").iterdir():
        if child.suffix == ".md":
            if child.stem == "README":
                continue
            name = child.stem
            difficulty = name.split("(")[-1].split(")")[0]
            title = name.split(".")[-1].split("(")[0].strip()
            res[int(name.split(".")[0])] = [title, difficulty, child.name, child]

    table = [
        "",
    ]

    for key in sorted(res):
        row = "|"
        row += str(key) + "|"
        row += f"[{res[key][0]}](./leetcode/{quote(res[key][2])})|"
        row += res[key][1] + "|"
        # Read tags.
        with open(res[key][3], "r") as f:
            lines = f.readlines()
            if lines[0] == "---\n":
                fm = load(
                    "".join(lines[1 : lines[1:].index("---\n") + 1]), Loader=FullLoader
                )
                row += ", ".join(fm["tags"]) + "|"
            else:
                row += "|"
        table.append(row)

    table.append("|-|-|-|-|")
    table.append("|#|Title|Difficulty|Topics|")
    table.append("")

    table.append(
        f"|{len(res)}|{len(list(filter(lambda x: res[x][1] == 'Easy', res)))}|{len(list(filter(lambda x: res[x][1] == 'Medium', res)))}|{len(list(filter(lambda x: res[x][1] == 'Hard', res)))}|"
    )
    table.append("|:-:|:-:|:-:|:-:|")
    table.append("|Total|Easy|Medium|Hard|")
    table.append("")

    return "\n".join(reversed(table))


if __name__ == "__main__":
    toc = maketable()
    with open("README.md", "r") as f:
        ctn = [x[:-1] for x in f.readlines()]
        ctn = ctn[: ctn.index("### TOC") + 1]
        ctn.append(toc)
        toc = "\n".join(ctn)
    with open("README.md", "w") as f:
        f.write(toc)
