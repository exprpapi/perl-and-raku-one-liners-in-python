# perl-and-raku-one-liners-in-python

I sympathize with the concept of perl, but let's stay within python shall we  
An effort to translate perl and raku one-liners into python.  
Inspired by the books by Peteris Krumins and by Andrew Shitov.

## The One-Liners
We expect to run these in a `bash` shell environment. Therefore all multiline code samples are `bash` syntax, leading `$` sigils are dropped.  
Using a shell redirection, a pipe or external commands, except heredocs, herestrings and process substitution of `cat` is considered cheating.  
The 'canonical' solution, if given, is how I would actually do it, if I had to. Cheating is embraced there.



---
### Replace all occurences of `you` by `me` in the file `file`

<details><summary>perl:</summary>

```bash
perl -pi -e 's/you/me/g' file
```
</details>

<details><summary>python:</summary>

```bash
python <(cat <<'EOF'
import sys, re
file, replaced = sys.argv[1], ''
with open(file, 'r') as f:
  replaced = re.sub('you', 'me', f.read())
with open(file, 'w') as f:
  f.write(replaced)
EOF
) file

```
</details>

<details><summary>canonical:</summary>

```bash
sed -i 's/you/me/g' file
```
</details>




---
### The same thing, just in several files and only in lines containing digits.

<details><summary>perl:</summary>

```bash
perl -pi -e 's/you/me/g if /\d/' file1 file2 file3
```
</details>




---
### Find all lines that occur more than once.

<details><summary>perl:</summary>

```bash
perl -ne 'print if $a{$_}++' file
```
</details>




---
### Print out the file with lines numbered.

<details><summary>perl:</summary>

```bash
perl -ne 'print "$. $_"' file
```
</details>



---
>Note: this file was machine generated

