It’s common in bash scripts to create a directory and immediately cd to the directory, if the creations succeeded. Use conditional the `&&` operator to create the dir and cd into it only if the creation succeeded. 
<details>
  <summary>
     Solution
  </summary>

```bash
mkdir newdir && cd newdir
```

</details>