That's all for OOP basics. Let's practice by making a **YouTubeLessonManager** class.
we'll take this step by step, but ultimately our code will run like this:


```python
lesson_manager = YouTubeLessonManager()
lesson_manager.save("For-Loops", "https://www.youtube.com/watch?v=OnDr4J2UXSA") 
lesson_manager.save("While-Loops", "https://www.youtube.com/watch?v=6TEGxJXLAWQ")
lesson_manager.save("Functions", "https://www.youtube.com/watch?v=NSbOtYzIQI0")
lesson_manager.save("Dictionaries", "https://www.youtube.com/watch?v=ZEZdys-fHDw")  
###--------------------------------------
lesson_manager.get("functions") # outputs: 'https://www.youtube.com/watch?v=NSbOtYzIQI0' 
lesson_manager.get("for loops") # outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA' 
```

In other words, this class will help us quickly get YouTube links to Python lessons by typing part of the lesson name - exciting!



## Exercise 1

Start by creating a plain class with a `constructor`.
The class doesn't receive anything from the outside, but it does have a lessons attribute, which at first should be an empty dict.

At this point, running this:

```python
lesson_manager = YouTubeLessonManager()
print(lesson_manager.lessons) 
```

Should output 
```python
{}
```


## Exercise 2

Create the `save` method. It should receive two parameters: name and url, and add these as a key-value pair to the class's lessons dict.


To check your work, here is how your code should work:

```python
lesson_manager = YouTubeLessonManager()
lesson_manager.save("For-Loops", "https://www.youtube.com/watch?v=OnDr4J2UXSA")
print(lesson_manager.lessons) # outputs: {"For-Loops": "https://www.youtube.com/watch?v=OnDr4J2UXSA"}  
print(lesson_manager.lessons["For-Loops"]) # outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA' 
```


## Exercise 3

Implement the `get` method. It should receive a `lesson name`, and return its `YouTube URL`:


```python
print(lesson_manager.get("For-Loops")) # outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA' 
```

## Exercise 4

Modify your methods such that you can search for the lesson with any casing, and it will still return the correct `URL`:


```python
print(lesson_manager.get("for-loops")) # outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA'
print(lesson_manager.get("fOr-LooPS")) # outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA'
```

**Hint:** you will probably have to modify more than just the get method


## Exercise 5

Modify your methods such that **punctuation** doesn't matter:

```python
print(lesson_manager.get("for-loops")) # outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA' 
print(lesson_manager.get("for loops")) # outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA'
```

## Exercise 6 (Bonus)

Modify your methods such that any part of the lesson's name will suffice to find the correct URL:

```python
print(lesson_manager.get("for loops")) # outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA'
print(lesson_manager.get("for")) # outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA'
print(lesson_manager.get("loops")) # outputs ['https://www.youtube.com/watch?v=OnDr4J2UXSA', 'https://www.youtube.com/watch?v=6TEGxJXLAWQ']
```

If more than one lesson matches, you should output all the matching lessons.

**Hint 1:** you can iterate over a dict's keys using the for...in loop

**Hint 2:** you can check whether a string is part of another string using the in keyword


## Extension 1

Instead of saving the entire **URL** in the save method, only save the unique lesson ID that comes at the end of the `?v=` in the URL

However, the get method should still return the **full URL**

For example:

```python
lesson_manager.save("For-Loops", "https://www.youtube.com/watch?v=OnDr4J2UXSA")
print(lesson_manager.get("For-Loops") # outputs: 'https://www.youtube.com/watch?v=OnDr4J2UXSA' 
```

## Extension 2

Add a `counter` attribute to the class.

This `counter` tracks how many times each lesson has been searched (how many times you used get to get it).

Use this to test your code:

```python
lesson_manager.get("For-Loops") lesson_manager.get("For-Loops")
lesson_manager.get("Dictionaries")
lesson_manager.get("For-Loops")
lesson_manager.get("Dictionaries") 
print(lesson_manager.get_counts('For-Loops')) # outputs: 3
print(lesson_manager.get_counts('Dictionaries')) # outputs: 2
```

But what happens if we have:

```python
lesson_manager.get("For-Loops")
lesson_manager.get("Loops")
print(lesson_manager.get_counts('For-Loops'))  
```

What will be the output?

This is something you need to think about and decide for yourself.


## Extension 3

Add a `get_most_popular_lesson` method that returns the most popular lesson based of counter:

```python
print(lesson_manager.get_most_popular_lesson()) # outputs: 'For-Loops'
```