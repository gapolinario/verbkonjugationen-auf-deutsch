"""
Loads table of conjugated verbs and completes the conjugation
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
import re


def check_written(label, persons, line, start, i, new):

    try:
        assert line[start + i] == new
    except AssertionError:
        print(
            f"{label}, computed: {persons[i]} {new}, written: {persons[i]} {line[start+i]}"
        )


def main():

    header = f"#tags: deutsch verbs\n#deck: _Default::Deutsch-Verben\n#notetype: Deutsch-Verb\n#separator: Semicolon\n\n"

    persons = ["Ich", "Du", "Er/Sie/Dey/Es", "Wir", "Ihr", "Sie"]

    aux_pras = {
        "sein": ["bin", "bist", "ist", "sind", "seid", "sind"],
        "haben": ["habe", "hast", "hat", "haben", "habt", "haben"],
        "haben/sein": ["habe/bin", "hast/bist", "hat/ist", "haben/sind", "habt/seid", "haben/sind"],
        "werden": ["werde", "wirst", "wird", "werden", "werdet", "werden"],
    }

    aux_prat = {
        "sein": ["war", "warst", "war", "waren", "wart", "waren"],
        "haben": ["hatte", "hattest", "hatte", "hatten", "hattet", "hatten"],
        "haben/sein": ["hatte/war", "hattest/warst", "hatte/war", "hatten/waren", "hattet/wart", "hatten/waren"],
        "werden": ["wurde", "wurdest", "wurde", "wurden", "wurdet", "wurden"],
    }

    aux_k1pras = {
        "sein": ["sei", "seiest", "sei", "seien", "seiet", "seien"],
        "haben": ["habe", "habest", "habe", "haben", "habet", "haben"],
        "haben/sein": ["habe/sei", "habest/seiest", "habe/sei", "haben/seien", "habet/seiet", "haben/seien"],
        "werden": ["werde", "werdest", "werde", "werden", "werdet", "werden"],
    }

    aux_k2prat = {
        "sein": ["wäre", "wärst", "wäre", "wären", "wärt", "wären"],
        "haben": ["hätte", "hättest", "hätte", "hätten", "hättet", "hätten"],
        "haben/sein": ["hätte/wäre", "hättest/wärest", "hätte/wäre", "hätten/wären", "hättet/wärt", "hätten/wären"],
        "werden": ["würde", "würdest", "würde", "würden", "würdet", "würden"],
    }

    aux_refl = {
        False: ["", "", "", "", "", ""],
        True: ["mich", "dich", "sich", "uns", "euch", "sich"],
    }

    input = "Anki_Deutsch_Verbs.csv"
    output = "Anki_Deutsch_Verbs_Complete.csv"
    output2 = "Anki_Deutsch_Verbs_Complete.txt"

    table = np.loadtxt(input, delimiter=";", dtype=object)

    for line in table:

        assert len(line) == 91

        verb_inf = line[0]

        # Deal with werden separately
        if re.search(r"^werden", verb_inf) != None:
            verb_inf = "werden"

        verb_p2 = line[2]

        if re.search(r"^\w", verb_inf) != None:

            if re.search(r"^sich\s\w", verb_inf) != None:
                refl = True

                # remove 'sich' from infinitive verb
                verb_inf = re.split("\s", verb_inf)[1]
            else:
                refl = False

            # these entries must be added manually:
            # 1. Partizip I
            # 2. Partizip II
            # 3-8. Präsens
            # 9-14. Präteritum
            for i in range(1, 15):
                assert line[i] != ""

            if line[90] != "":
                verb_aux = line[90]
                try:
                    assert verb_aux == "sein" or verb_aux == "haben" or verb_aux == "haben/sein"
                except AssertionError:
                    print(f"Auxiliary verb must be sein or haben. Received {verb_aux}")
                    exit(1)
            else:
                raise ValueError(f"Auxiliary verb for {verb_inf} is empty")

                

            label = "Perfekt"
            start = 15
            for i in range(6):
                new = " ".join([aux_pras[verb_aux][i], aux_refl[refl][i], verb_p2])
                new = re.sub(r"\s+", " ", new)
                if line[start + i] == "":
                    line[start + i] = new
                else:
                    check_written(label, persons, line, start, i, new)

            label = "Plusquamperfekt"
            start = 21
            for i in range(6):
                new = " ".join([aux_prat[verb_aux][i], aux_refl[refl][i], verb_p2])
                new = re.sub(r"\s+", " ", new)
                if line[start + i] == "":
                    line[start + i] = new
                else:
                    check_written(label, persons, line, start, i, new)

            label = "Futur I"
            start = 27
            for i in range(6):
                new = " ".join([aux_pras["werden"][i], aux_refl[refl][i], verb_inf])
                new = re.sub(r"\s+", " ", new)
                if line[start + i] == "":
                    line[start + i] = new
                else:
                    check_written(label, persons, line, start, i, new)

            label = "Futur II"
            start = 33
            for i in range(6):
                new = " ".join(
                    [aux_pras["werden"][i], aux_refl[refl][i], verb_p2, verb_aux]
                )
                new = re.sub(r"\s+", " ", new)
                if line[start + i] == "":
                    line[start + i] = new
                else:
                    check_written(label, persons, line, start, i, new)

            label = "KI Präs"
            start = 39
            for i in range(6):
                assert line[start + i] != ""

            label = "KI Perf"
            start = 45
            for i in range(6):
                new = " ".join([aux_k1pras[verb_aux][i], aux_refl[refl][i], verb_p2])
                new = re.sub(r"\s+", " ", new)
                if line[start + i] == "":
                    line[start + i] = new
                else:
                    check_written(label, persons, line, start, i, new)

            label = "KI FI"
            start = 51
            for i in range(6):
                new = " ".join([aux_k1pras["werden"][i], aux_refl[refl][i], verb_inf])
                new = re.sub(r"\s+", " ", new)
                if line[start + i] == "":
                    line[start + i] = new
                else:
                    check_written(label, persons, line, start, i, new)

            label = "KI FII"
            start = 57
            for i in range(6):
                new = " ".join(
                    [aux_k1pras["werden"][i], aux_refl[refl][i], verb_p2, verb_aux]
                )
                new = re.sub(r"\s+", " ", new)
                if line[start + i] == "":
                    line[start + i] = new
                else:
                    check_written(label, persons, line, start, i, new)

            label = "KII Prät"
            start = 63
            for i in range(6):
                assert line[start + i] != ""

            label = "KII Plusq"
            start = 69
            for i in range(6):
                new = " ".join([aux_k2prat[verb_aux][i], aux_refl[refl][i], verb_p2])
                new = re.sub(r"\s+", " ", new)
                if line[start + i] == "":
                    line[start + i] = new
                else:
                    check_written(label, persons, line, start, i, new)

            label = "KII FI"
            start = 75
            for i in range(6):
                new = " ".join([aux_k2prat["werden"][i], aux_refl[refl][i], verb_inf])
                new = re.sub(r"\s+", " ", new)
                if line[start + i] == "":
                    line[start + i] = new
                else:
                    check_written(label, persons, line, start, i, new)

            label = "KII FII"
            start = 81
            for i in range(6):
                new = " ".join(
                    [aux_k2prat["werden"][i], aux_refl[refl][i], verb_p2, verb_aux]
                )
                new = re.sub(r"\s+", " ", new)
                if line[start + i] == "":
                    line[start + i] = new
                else:
                    check_written(label, persons, line, start, i, new)

            label = "Imperativ"
            start = 87
            for i in range(3):
                assert line[start + i] != ""

            """
            # this is not trivial, because it needs to know the
            # separable prefix of the verb. the other tenses don't

            label = "Imperativ Sie"
            start = 89
            new = " ".join(
                [verb_inf,"Sie!",sep_prefix]
            )
            if line[start + i] == "":
                line[start + i] = new
            else:
                check_written(label, persons, line, start-5, 5, new)
            """

            assert np.all(line != "")

    np.savetxt(output, table, delimiter=";", fmt="%s")

    with open(output, "r") as file:
        data = file.read()

    with open(output2, "w") as file:
        file.write(header)
        file.write(data)

    print("Conjugations finished!")


if __name__ == "__main__":
    main()
