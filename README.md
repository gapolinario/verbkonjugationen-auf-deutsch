
These programs reads an incomplete CSV table of conjugated verbs in German and fills it in with entries that are easily computed (past and future forms, except Präteritum).

Usage: `python complete-table.py`

If a required entry is missing, an assertion error is thrown.

The other two executables generate output formatted for Anki.

With `python export-full.py`, the full table is converted to a .txt file.

With `python export-abridged.py`, a shorter .txt file is generated. It contains only basic examples, from which the conjugations for other pronouns can be derived.

It is impractical to study the full .txt file. Instead, it is meant as a source for self assessment, by randomly drawing cards from it. To learn the conjugations for new verbs, the shorter version is preferred.

Both .txt files can be imported to anki. The abridged file can be imported with the standard Cloze card template. I have not yet added the card templates for the full table  to this repository.

## TODO

1. Add anki card template
2. Some verbs are impersonal. 