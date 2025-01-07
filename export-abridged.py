"""
Exports complete CSV table to a smaller table with basic conjugations
The output can be imported on anki

Copyright (C) 2024 Gabriel B. Apolinário

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import numpy as np


def main():

    header = f"#tags: deutsch verbs abridged\n#deck: _Default::Deutsch\n#notetype: Deutsch-Cloze\n#separator: Semicolon\n\n"

    input = "Anki_Deutsch_Verbs_Complete.csv"
    output = "Anki_Deutsch_Verbs_Abridged.txt"

    table = np.loadtxt(input, delimiter=";", dtype=object)
    # 0. infinitiv
    # 5. er/sie präsens
    # 9. ich präteritum
    # 20. sie perfekt 
    # 11. er/sie präteritum, needed for impersonal verbs
    table = table[:, [0, 5, 9, 20, 11]]

    with open(output, "w") as file:
        file.write(header)

        # Präsens
        for line in table:
            s = "Er/Sie {{c1::" + f"{line[1]}" + "::" + f"{line[0]}" + ", Präsens}};\n"
            file.write(s)

        # Präteritum
        for line in table:
            if line[2] != "":
                s = "Ich {{c1::" + f"{line[2]}" + "::" + f"{line[0]}" + ", Präteritum}};\n"
                file.write(s)
            else:
                s = "Er/Sie {{c1::" + f"{line[4]}" + "::" + f"{line[0]}" + ", Präteritum}};\n"
                file.write(s)

        # Perfekt
        for line in table:
            s = "Sie {{c1::" + f"{line[3]}" + "::" + f"{line[0]}" + ", Perfekt}};\n"
            file.write(s)

    print("Export to brief Anki deck finished!")


if __name__ == "__main__":
    main()
