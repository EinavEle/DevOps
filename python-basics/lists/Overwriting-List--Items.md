If you want to change a value in a list, all you have to do is access the index in the list, and reset the value:


```
modern_billionaires = ["Jeff Bezos", "Bill Gates", "Mark Zuckerberg", "Warren Buffett"]
modern_billionaires[2] = "Elon Musk"

print(modern_billionaires)﻿
```

Following our update operation, list will now look like this: `["Jeff Bezos", "Bill Gates", "Elon Musk", "Warren Buffett"]` - note that "Mark Zuckerberg" is completely gone! So make sure you don't need information you're overwriting, because it won't come back.