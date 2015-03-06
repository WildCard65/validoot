# validoot - 1.0

This module is designed to solve the most basic of argument validations:
type's, clauses, and combinations of clauses. It is meant to remove some of the
boiler plate code used to check the input types and checks such as between, or
string lengths.

#### Definitions

* Clause - A function that takes in the value as a parameter and returns `True` or `False`.
* Operator - Allows you to "and" and "or" clauses together.

## Basic example:

```python
@validates(is_instance(basestring), is_type(int), between(0, 100))
def do_something(name, id, age):
    pass
```

In the code above, a `validoot.ValidationError` will be thrown if the `name`
is not a string or unicode, if the `id` is not an integer, or if the `age`
is not between 0 and 100.

## Operators:

We can extend the first example by adding an additional check for the `name`:
it must be between 5 and 40 characters. For this we use the `validoot.And` operator
to combine the clauses.

```python
@validates(And(is_instance(basestring), len_between(5, 40)), is_type(int), between(0, 100))
def do_something(name, id, age):
    pass
```

An `Or` operator also exists. Both `And` and `Or` take in a variable number of
clauses and can be nested further.

## Keyword arguments:

There is also support for keyword arguments:

```python
@validates(is_instance(basestring), something=is_type(float))
def do_something(name, something=1.0, anotherthing=2):
    pass
```

Here the `something` value must pass the validation checks as specified in the decorator.
No checks exist for `anotherthing` so it has no restrictions.

## FAQ:

### What if I don't want validation for one of the position arguments?
Simple. Just use `None`.

```python
@validates(is_instance(basestring), None, between(0, 100))
def do_something(name, id, age):
    pass
```

### How do I create my own validation clauses?
The builtin clauses provided by Validoot are all subclasses of the `validoot.clauses.Clause`
object. Check out it's source code to see how they work.
