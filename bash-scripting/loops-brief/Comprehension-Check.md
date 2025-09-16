Given the following script, answer the following 3 questions:
```bash
[elvis@station elvis]$ cat script
#!/bin/bash
for i in $*
do
  if [ -r $i ]
  then
    gzip $i
  else
    echo "cannot compress $i"
  done
fi
[elvis@station elvis]$ ./script rotate_cw
./script: line 10: syntax error near unexpected token `done'
./script: line 10: `
done'
```
{Check It!|assessment}(multiple-choice-3411777103)
{Check It!|assessment}(multiple-choice-3765629814)
{Check It!|assessment}(multiple-choice-225909242)
{Check It!|assessment}(multiple-choice-906881319)
{Check It!|assessment}(multiple-choice-1765813243)
{Check It!|assessment}(multiple-choice-3161492858)