Functions should be written all **lowercase** with words separated by **underscores** as necessary to improve readability:

```
def calculate():
  pass
def add_item():
  pass 
```

Use one **leading underscore** only for private methods and instance variables

```
def _delete_row():
  pass 
```

It is considered a best practice and a clean code principle for function names to be a **verb**, an **action**.

So instead of `message_parser` use `parse_message`

Here are some examples:

```
def get_store_name():
  pass
def add_student():
  pass
def restore_product():
  pass
```