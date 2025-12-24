We seized a professor's laptop. It looks like his drive started
failing or he ran a wiper script right before we caught him. 
The source challenge.tex is full of corrupted data blocks.

However, he forgot to clear his build cache. The artifacts from
his last successful compilation are still in this folder.

OBJECTIVE:
Recover the flag from the build artifacts.

WARNING:
The source code is corrupted. If you try to recompile it,
the compiler will overwrite the valid artifacts with the
corrupted data from the source file, destroying the flag forever.