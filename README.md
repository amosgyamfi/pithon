# πthon
Learn Python fundamental concepts
---

### 1. Combine Dictionaries {**fruit_emojis1, **fruit_emojis2}

```python
fruit_emojis1 = {    
    "apple": "🍎",    
    "banana": "🍌",    
    "cherry": "🍒" 
}

fruit_emojis2 = {
    "date": "🌴",
    "grapes": "🍇",
    "kiwi": "🥝"
}

fruit_emojis = {**fruit_emojis1, **fruit_emojis2}
print(fruit_emojis)
```
---

### Pretty printing a dictionary

```python
from pprint import pprint

emoji = {
    "animal": {
        "dog": "🐶",
        "cat": "🐱",
        "panda": "🐼"
    },
    "fruit": {
        "cherry": "🍒",
        "strawberry": "🍓",
        "grapes": "🍇"
    },
    "fish": {
        "fish": "🐟",
        "tropical fish": "🐠",
        "blowfish": "🐡"
    }
}
pprint(emoji)
```
