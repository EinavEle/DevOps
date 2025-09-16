# Exercise 1 - Rotating an Image
Create a script called `blur.sh`, which can be used to blur images. Use the `convert` command for the actual image processing.
The script should expect as arguments multiple filenames of the images to be blurred. You need to test that the file content is indeed an image (`file` or `stat`). The script should generate a new file of the blurred image, and if the new image is successfully generated, replace the original image with the blurred one.
<details>
  <summary>
     Solution
  </summary>

```bash
#!/bin/bash
for image in "$@"
do
  if file "$image" | grep "image data" && [ -f "$image" ]
  then
	convert "$image" -blur 0x8 "$image"_blurred
	if [[ $? -eq 0 ]]; then
  	  mv "$image"_blurred "$image"
  	  echo "Successfully blurred $image"
	else
  	  echo "Error: failed to blur $image"
	fi
  else
	echo "Error: $image is not a valid image file"
  fi
done
```

</details>

# Exercise 2 - Bad Elusive Command
Say you have a command that fails rarely. In order to debug it you need to capture its output but it can be time consuming to get a failure run. Write a bash script that runs the following script until it fails and captures its standard output and error streams to files and prints everything at the end. Report how many runs it took for the script to fail.
```bash
 #!/bin/bash

 n=$(( RANDOM % 100 ))

 if [[ n -eq 42 ]]; then
    echo "Something went wrong"
    exit 1
 fi

 echo "Everything went according to plan"
```
<details>
  <summary>
     Solution
  </summary>

```bash
let counter=0

while true
do
    bash script.sh 

    # Check if the command failed
    if [[ $? -eq 0 ]]; then
        echo "Run #$counter: Everything went according to plan"
        counter=$((counter+1))
    else
        echo "Run #$counter: Something went wrong"
        break
    fi
done
```

</details>