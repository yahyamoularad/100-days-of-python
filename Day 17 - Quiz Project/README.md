# Day 17: Quiz Project

## Folder structure

```text
Day 17 - Quiz Project/
├── main.py
├── question_model.py
├── quiz_brain.py
├── data.py
├── lessons/
│   └── user_class_examples.py
├── versions/
│   └── original_question_data.py
└── README.md
```

## Final project

The final quiz project keeps the original four-file structure:

```text
main.py
question_model.py
quiz_brain.py
data.py
```

The project logic has not been rewritten.

Only explanatory comments were added to the final project files.

## Earlier lesson code

The class examples from `Day17-start.py` are preserved in:

```text
lessons/user_class_examples.py
```

The earlier question-data version from `data.py` is preserved in:

```text
versions/original_question_data.py
```

This keeps the final project clean while preserving the learning process.

# Lessons learned

## 1. Naming conventions

Day 17 reviews three naming styles.

### PascalCase

Used for class names.

Examples:

```python
User
Question
QuizBrain
```

### camelCase

The first word starts with lowercase and later words begin with uppercase letters.

### snake_case

Words are lowercase and separated with underscores.

Examples from the project include:

```python
question_bank
question_number
question_list
user_answer
correct_answer
```

## 2. Creating a class

The basic syntax is:

```python
class User:
    pass
```

A class acts as a blueprint for creating objects.

An object can then be created with:

```python
user_1 = User()
```

## 3. Adding attributes to objects

The early lesson demonstrates adding attributes directly:

```python
user_1.id = "001"
user_1.username = "yahya"
```

These values belong to that particular object.

## 4. The constructor: `__init__`

The next version defines attributes when the object is created:

```python
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
```

Objects can then be created with:

```python
user_1 = User("001", "yahya")
user_2 = User("002", "jack")
```

This is more structured than manually adding every attribute after creating an object.

## 5. Understanding `self`

Inside a class, `self` refers to the current object.

For example:

```python
self.username = username
```

stores the supplied `username` inside the object being created.

In the Quiz project:

```python
self.question_number
self.score
self.question_list
```

belong to a particular `QuizBrain` object.

## 6. Creating methods

A method is a function defined inside a class.

The User lesson contains:

```python
def follow(self, user):
    user.followers += 1
    self.following += 1
```

This demonstrates objects interacting with other objects.

When:

```python
user_1.follow(user_2)
```

runs, `user_1` gains one following and `user_2` gains one follower.

## 7. Creating a model class

The final project introduces:

```python
class Question:
```

A Question object stores two attributes:

```python
self.text
self.answer
```

This models one quiz question as an object instead of working directly with separate strings.

## 8. Converting dictionary data into objects

The active data file contains dictionaries.

`main.py` loops through them:

```python
for question in question_data:
```

It extracts:

```python
question_text = question["question"]
question_answer = question["correct_answer"]
```

and creates a Question object:

```python
new_question = Question(
    q_text=question_text,
    q_answer=question_answer
)
```

The object is then added to:

```python
question_bank
```

This shows how raw dictionary data can be transformed into objects.

## 9. A list can contain objects

`question_bank` is a list of `Question` objects.

Each item contains its own:

```python
text
answer
```

The QuizBrain object receives that list:

```python
quiz = QuizBrain(question_bank)
```

## 10. A class can manage program state

`QuizBrain` stores the state of the quiz:

```python
self.question_number = 0
self.score = 0
self.question_list = q_list
```

The values change as the quiz progresses.

This keeps quiz-related state together inside one object.

## 11. Methods can use and update object attributes

`next_question()` reads:

```python
self.question_list
self.question_number
```

and then updates:

```python
self.question_number += 1
```

`check_answer()` can update:

```python
self.score += 1
```

The object remembers those values between method calls.

## 12. Returning a Boolean from a method

The method:

```python
still_has_questions()
```

returns:

```python
self.question_number < len(self.question_list)
```

This expression evaluates to either:

```python
True
```

or:

```python
False
```

The result controls the main loop:

```python
while quiz.still_has_questions():
    quiz.next_question()
```

## 13. One method can call another method

Inside `next_question()`:

```python
self.check_answer(
    user_answer,
    current_question.answer
)
```

calls another method belonging to the same `QuizBrain` object.

This separates:

```text
asking the question
```

from:

```text
checking the answer
```

## 14. Separating responsibilities into files

The final project is split into four responsibilities.

### `data.py`

Stores the quiz data.

### `question_model.py`

Defines what one question looks like.

### `quiz_brain.py`

Controls quiz behavior and score.

### `main.py`

Builds the Question objects, creates QuizBrain, and starts the quiz.

This structure makes each file responsible for one part of the program.

## 15. Importing your own classes

The project imports classes from your own Python files:

```python
from question_model import Question
from quiz_brain import QuizBrain
```

This is the same principle introduced with imported classes on Day 16, but Day 17 now uses classes created specifically for this project.

## Running the final project

From the root of the `100-days-of-python` repository:

```bash
python "Day 17 - Quiz Project/main.py"
```

## Running the class lesson

```bash
python "Day 17 - Quiz Project/lessons/user_class_examples.py"
```

## Dependencies

Day 17 uses only Python code from the project files and does not require an external package.
