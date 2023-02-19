# perl-and-raku-one-liners-in-python

I sympathize with the concept of perl, but let's stay within python shall we  
An effort to translate perl and raku one-liners into python.  
Inspired by the books by Peteris Krumins and by Andrew Shitov.

## The One-Liners
We expect to run these in a `bash` shell environment. Therefore all multiline code samples are `bash` syntax, leading `$` sigils are dropped.  
Using a shell redirection, a pipe or external commands, except heredocs, herestrings and process substitution of `cat` is considered cheating.  
The 'canonical' solution, if given, is how I would actually do it, if I had to. Cheating is embraced there.



---
### Replace patterns in file
Replace all occurences of `you` by `me` in the file `file`

<details><summary>perl:</summary>

```bash
perl -pi -e 's/you/me/g' file
```
</details>

<details><summary>python:</summary>

```bash
python <(cat <<'EOF'
import sys, re
replaced = ''
with open(sys.argv[1], 'r') as f:
  replaced = re.sub('you', 'me', f.read())
with open(sys.argv[1], 'w') as f:
  f.write(replaced)
EOF
) file

```
</details>



---
>Note: this file was machine generated

