The `ll` command is a commonly used alias for  `ls -l`. Try it yourself…

Open the `~/.bashrc` file using your favorite  text editor (e.g. `nano`) and search this alias definition. Add another alias of your own. 

<details>
  <summary>
     Solution
  </summary>

The alias is defined by:
```bash
alias ll='ls -alF'
```
An example for another alias is `ld`, which prints directories only:
```bash
alias ld='ls -d */'
```

</details>