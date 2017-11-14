![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

# Learning Python

We're learning Python! Getting started with a totally new language doesn't have to be hard. The biggest key is to practice doing something that you *already know* in the context of the new language. This is called a *transfer task*. The more languages and computer science concepts you learn, the easier new ones become to pick up and its mostly syntax, quirks and language-specific tools that become the tricky part.

Now, your task is to *teach yourself* a bit of Python. The goal here isn't to become a Python master, but to explore and learn a bit about a new language.

## Goals:

By the end of this exercise, you should be able to:

- Create a simple python program
- Execute a simple python program
- Articulate basic differences between Python and other languages you know
- Feel comfortable understanding what is generally happening in most basic python programs

## Read: The Zen of Python

> The Zen of Python, by Tim Peters
>
> Beautiful is better than ugly.
> Explicit is better than implicit.
> Simple is better than complex.
> Complex is better than complicated.
> Flat is better than nested.
> Sparse is better than dense.
> Readability counts.
> Special cases aren't special enough to break the rules.
> Although practicality beats purity.
> Errors should never pass silently.
> Unless explicitly silenced.
> In the face of ambiguity, refuse the temptation to guess.
> There should be one-- and preferably only one --obvious way to do it.
> Although that way may not be obvious at first unless you're Dutch.
> Now is better than never.
> Although never is often better than *right* now.
> If the implementation is hard to explain, it's a bad idea.
> If the implementation is easy to explain, it may be a good idea.
> Namespaces are one honking great idea -- let's do more of those!

## Hello World

Write a program in `hello_world/hello_world.py` that prints 'Hello, World!' to the standard output (terminal).

## Fizzbuzz

Write a program in `fizzbuzz/fizzbuzz.py` that does the following:

For numbers 1 through 100, print `fizz` if the number is divisible by 3, `buzz` if the number is divisible by 5 and `fizzbuzz` if the number if the number is divisible by both 3 and 5. If the number isn't divisible by 3 or 5, just output the number itself.

The output should look something like `1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizz Buzz 16 17 Fizz...`

## Fibonacci

Write a program in `fibonacci/fib.py` that will output the N-th term of the [Fibonacci sequence](http://en.wikipedia.org/wiki/Fibonacci_number).

For example: `print fib(6)` should output `8`.

## Project Euler Problem 1

Project Euler's first problem is:

> If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
> Find the sum of all the multiples of 3 or 5 below 1000.

Write the code to complete this in `euler_1/sum_of_natural_numbers.py`

## Research: What is Python

Here are some general questions you might get asked about Python. Spend some time researching and answering these questions.

##### How does Python compare to other langauges you've used?
Python's syntax is a lot more straight forward and tends to require less code to achieve the same output as most other languages from what I have noticed. At the same time, it has a few crucial
rules, like all languages, that must be adhered to.  Having to pay close attention to spacing is an important aspect and it can add a layer to troubleshooting and debugging that usually isn't there with languages like javascript. However the simplified syntax of Python by far makes up for that. 

##### Is Python a high or low level language?
Python is a high level language, being that it is further removed from machine and assembly code and is more similiar to a human speaking language. 

##### Is it a compiled or interpeted language?
My research has shown me that this is a difficult question to answer because what makes Python compliled or interpreted would be the implementation method chosen rather than its native abilities. For normal Python, programs written in it are ran from the source code, leaning my answer towards it being interpreted.   However cPython implementations can be compiled, where as pypy implementation would be interpreted. 

##### What paradigms does Python support?
Python supports object-oriented, imperative, functional, and procedural programming paradigms.

##### Does it have built in memory management? garbage collection?
Yes, Python has both. 

##### Does it have strong support for functional programming?
Python suppports functional programming but not super well.  I am still in the process of understanding why but from my research it seems to lack concepts relating to pattern matching and doesn't really contain an extensive library, so many tasks enjoyed by developers of more suited functional programming languages have to be performed imperatively in Python and can take longer to accomplish. 

##### What's the deal with Python 2 vs Python 3?
Python 3 is considered to be current Python where as Python 2 is technically a legacy version though still widely used and supported.  Python 3 has several important differences such as the print statement is now a function and executed as print(), xrange is now simply range, and the map() and filter() methods return iterators. 

