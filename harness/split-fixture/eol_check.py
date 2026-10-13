"""Line endings of a split's output: every file one form, CRLF or LF, no lone carriage return.

python eol_check.py <dir-holding-the-doc> <DOC>.md

Prints one line per file (CRLF, bare LF, lone CR) and exits 1 when any file mixes forms or
carries a lone CR. A file-type tool that reports "CRLF line terminators" cannot stand in for
this: it says so when one CRLF is present, whatever else the file holds.
"""
import glob
import os
import sys

d, fname = sys.argv[1], sys.argv[2]
stem = fname[:-3]
bad = 0
for p in [os.path.join(d, fname)] + sorted(glob.glob(os.path.join(d, stem, '*.md'))):
    b = open(p, 'rb').read()
    crlf = b.count(b'\r\n')
    lf, cr = b.count(b'\n') - crlf, b.count(b'\r') - crlf
    ok = cr == 0 and (crlf == 0 or lf == 0)
    bad += not ok
    print(f'{"ok   " if ok else "MIXED"} {os.path.relpath(p, d)}: crlf {crlf}, bare lf {lf}, lone cr {cr}')
print(f'{bad} file(s) mixed')
sys.exit(1 if bad else 0)
