For communication in in combat we use false commands to distract enemies.
But our troops should have an algorithm to select real commands.
For this they have etalon set of commands.

You are given two string with words separated by commas.
Try to find what is common between these strings. The words are not repeated in the same string.

Your function should find all of the words that appear in both strings.
The result must be represented as a string of words separated by commas in **alphabetic order**.

**Input:** Two arguments as strings. 

**Output:** The common words as a string.

**Example:**

```python
common_words("hello,world", "hello,earth") == "hello"
common_words("one,two,three", "four,five,six") == ""
common_words("one,two,three", "four,five,one,two,six,three") == "one,three,two"
```
**How it is used:**

Here you can learn how to work with strings and sets.
This knowledge can be useful for linguistic analysis.

**Precondition:**

Each string contains no more than 10 words.
All words separated by commas.
All words consist of lowercase latin letters.

