### Flag
CTF{d0nt_0v3rwr1t3_th3_bu1ld_l0g5}

---

### Solution

Through analyzing each file in the `forensics_rubber` folder, you'll find 5 text fragments that come together to make the flag.


#### >Part 1

Open the PDF and you will see `CTF{d0nt_` directly in the document body.


#### >Part 2

Open [challenge.log](../problem/forensics_rubber/challenge.log#L237), on line 237 you'll find: `>>> SYSTEM LOG: Part 2: 0v3rwr1t3\_ <<<`


The underscore appears directly as `_` in the output. This is because `\_` is the LaTeX macro for a text underscore, while `_` on it's own is a subscript character (catcode 8) and cannot be used in text mode. Thus, the second part is `0v3rwr1t3_`


#### >Part 3

Open [challenge.aux](../problem/forensics_rubber/challenge.aux#5), on line 5 you'll find: 

`\newlabel{backup_key}{{1}{1}{Part 3: th3\protect \unhbox \voidb@x \kern .06em\vbox {\hrule width.3em}}{}{}}`

In LaTeX, `\newlabel` stores cross-reference data, and the format in which it's written is: 

`\newlabel{<label-name>}{{<ref-text>}{<page>}{<caption>}{<hyperref>}{<extra>}}`


|    Field | Value                                                                      | Meaning             |
| -------: | -------------------------------------------------------------------------- | ------------------- |
| ref-text | `1`                                                                        | Reference number    |
|     page | `1`                                                                        | Page number         |
|  caption | `Part 3: th3\protect \unhbox \voidb@x \kern .06em\vbox{\hrule width .3em}` | Stored caption text |
| hyperref | ---                                                                        | Hyperref anchor     |
|    extra | ---                                                                        | Extra metadata      |

Only the first two fields are mandatory, the remaining fields are populated by packages such as hyperref, and the third field here contains a serialized representation of the label text.

Finally, we know that `\unhbox \voidb@x \kern .06em\vbox{\hrule width .3em}` are the raw instructions used to draw an underscore in LaTeX. Its glyph macro is `\textunderscore`, which can be confirmed by tracing macro expansion and by observing how LaTeX serializes the glyph into the `.aux` file.

So the third part would be `th3_`


#### >Part 4

Open [artifact.sh](../problem/forensics_rubber/artifact.sh), you'll find:

`echo "Part 4: bu1ld\protect \global \let \OT1\textunderscore \unhbox \voidb@x \kern .06em\vbox {\hrule width.3em}\OT1\textunderscore "`

`\global \let \OT1\textunderscore` globally binds the sequence `\OT1\textunderscore` to the proceeding box primitives, this is to make sure that the underscore glyph can be reused consistently in the OT1 encoding.

Again, `\unhbox \voidb@x \kern .06em\vbox{\hrule width .3em}` are the raw instructions used to draw an underscore.

And finally `\OT1\textunderscore` at the end invokes the prior bindiing and underscore glyph is printed.

Thus, the fourth part is `bu1ld_`

#### >Part 5

Finally, the 5th part can be found in the [metadata](./challenge.json-metadata.txt#26) of the PDF. The subject of the PDF is written as: `Part 5: l0g5`

Thus, the final part of the flag is `l0g5}`

---

### Notes

Mechanism of `\unhbox \voidb@x \kern .06em \vbox{\hrule width .3em}`

`\unhbox \voidb@x` emits the contents of `\voidb@x`, `\kern .06em` inserts a positive horizontal kern of .06 em to the right, and `\vbox{\hrule width .3em}` creates a vertical box whose reference point is on the text baseline and whose contents are a single horizontal rule .3 em wide which is then placed at that position

---
### Extra Resources

1. Display LaTeX online → https://www.quicklatex.com
2. View PDF metadata online → https://www.metadata2go.com/view-metadata
3. Info on `\newlabel` → https://tex.stackexchange.com/questions/512148/reference-for-newlabel