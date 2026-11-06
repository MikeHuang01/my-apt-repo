from pathlib import Path

path = Path("Packages")
entries = path.read_text(encoding="utf-8").split("\n\n")
output = []
for entry in entries:
    lines = entry.splitlines()
    if not lines:
        continue
    if lines[0] == "Package: com.mikehuang01.noads":
        lines = [
            "Icon: https://mikehuang01.github.io/my-apt-repo/NoAds-Plugin.png"
            if line.startswith("Icon:") else line
            for line in lines
        ]
        lines.append("SileoDepiction: https://mikehuang01.github.io/my-apt-repo/NoAds-Depiction.json")
    if lines[0] == "Package: com.be-huge.floating-view":
        lines.append("SileoDepiction: https://mikehuang01.github.io/my-apt-repo/FloatingView-Depiction.json")
    if lines[0] == "Package: netskao.actionbarreborns":
        lines.append("SileoDepiction: https://mikehuang01.github.io/my-apt-repo/ActionBar-Depiction.json")
    if lines[0] == "Package: cn.zqbb.stopautolaunchapps":
        lines.append("SileoDepiction: https://mikehuang01.github.io/my-apt-repo/Hello3Q-Depiction.json")
    output.append("\n".join(lines))
path.write_text("\n\n".join(output).rstrip() + "\n", encoding="utf-8")
