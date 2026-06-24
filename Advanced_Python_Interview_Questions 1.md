
# Advanced Python Interview Questions

## 1. How do you implement a Singleton design pattern in Python? - 3

The Singleton Pattern ensures that a class has only one instance throughout the program's lifecycle. When working with SQLAlchemy, this pattern can be useful for managing database connections or ensuring that a specific table (e.g., metadata) always has a single row.

The Singleton design pattern ensures that a class has only one instance and provides a global point of access to it. In Python, this can be implemented using a class variable to store the instance, and a class method to return this instance. Here's an example:

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
```

## 2. Explain the concept of metaclasses in Python.
Metaclasses are the 'classes of classes'. They define how classes behave. A class is an instance of a metaclass. In Python, `type` is the default metaclass, which can be overridden to customize class creation. Here's an example:

```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print("Creating class:", name)
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass
```

## 3. How does Python's memory management work?
Python uses automatic memory management through reference counting and a garbage collector for unused objects. The garbage collector handles circular references using the `gc` module. Memory for objects is allocated from a private heap.

## 4. Discuss the Global Interpreter Lock (GIL) in Python. - 1
The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode concurrently. It simplifies memory management but can be a bottleneck in CPU-bound applications. Alternatives like multiprocessing can be used to bypass GIL limitations.

## 5. What is asynchronous programming, and how is it handled in Python?
Asynchronous programming allows tasks to run concurrently, improving performance for I/O-bound tasks. Python uses the `asyncio` library for async programming, where `async` functions and `await` expressions are used to define coroutines.

```python
import asyncio

async def main():
    print('Hello')
    await asyncio.sleep(1)
    print('World')

asyncio.run(main())
```

## 6. Explain the concept of decorators in Python. - 2
Decorators are a form of metaprogramming that allow modification of functions or methods using other functions. They provide an easy way to apply reusable behaviors to functions.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

## 7. How can you optimize Python code for better performance?
Performance optimization can be achieved by using built-in functions, list comprehensions, generator expressions, and avoiding global variables. Profiling tools like `cProfile` can be used to identify bottlenecks.

## 8. Outline the strategies for effective testing in Python.
Effective testing includes writing unit tests and integration tests using frameworks like `unittest` and `pytest`. Mocking can be used to isolate code units, and continuous integration tools ensure tests run automatically.

## 9. Describe packaging in Python and the role of PyPI.
Packaging in Python involves structuring code into modules and packages, allowing distribution. `setuptools` and `wheel` are commonly used tools, and packages are published on the Python Package Index (PyPI) for public use.

## 10. What are context managers and how are they implemented in Python?
Context managers manage resources, ensuring acquisition and release using the `with` statement. They are implemented by defining `__enter__` and `__exit__` methods in a class.

```python
class FileOpener:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileOpener('myfile.txt') as f:
    content = f.read()
```

## 11. How do you manage dependencies in Python projects?
Dependencies are managed using `requirements.txt` files, specifying versions, or via `pipenv` and `poetry` for virtual environments and dependency management.

## 12. Explain the difference between 'deepcopy' and 'shallowcopy'.
A shallow copy creates a new object but inserts references to the objects found in the original. A deep copy creates a new object and recursively copies objects found in the original.

## 13. How does Python handle exceptions and what are best practices for exception handling?
Python handles exceptions using `try`, `except`, `else`, and `finally`. Best practices include catching specific exceptions and avoiding bare except clauses, using exception chaining, and cleaning up resources properly.

## 14. Discuss the observer design pattern and its implementation.
The observer design pattern involves objects (observers) monitoring a subject. When the subject changes, all observers are notified. This can be implemented using `Observable` and `Observer` classes.

## 15. What are Python's built-in data structures and their uses?
Python's built-in data structures include lists, tuples, sets, and dictionaries. Lists are dynamic arrays, tuples are immutable lists, sets are unordered collections of unique items, and dictionaries are key-value pairs.

## 16. How do you ensure code quality and readability in Python?
Code quality is ensured using PEP 8 guidelines for coding style, static analysis tools like `pylint`, and linters to adhere to best practices.

## 17. Explain the concept of generators and how they differ from normal functions.
Generators are functions that return an iterator using `yield` statements, allowing iteration over a sequence of values without holding all values in memory at once. They differ from normal functions by allowing lazy evaluation.

## 18. What is monkey patching and is it recommended?
Monkey patching refers to dynamic modification of a class or module at runtime. It is generally discouraged due to potential introduction of bugs and maintenance issues but can be useful for fixing or extending third-party code.

## 19. Describe the publish-subscribe design pattern in Python.
The publish-subscribe pattern involves publishers broadcasting messages to subscribers who listen for them. Libraries like `pynet` and `redis` can facilitate this pattern.

## 20. How do you handle concurrency in Python?
Concurrency in Python can be achieved using threading, multiprocessing, and async programming paradigms. The choice depends on whether the task is I/O-bound or CPU-bound due to GIL constraints.

## 21, How do you handle authentication and error handling?

## 22. Can you discuss challenges faced when deploying microservices-based systems using Python, and how you addressed them?

## 23. How do you profile Python code to detect bottlenecks?

## 24. Serverless & Lambda

Walk through how you have implemented automation tasks using AWS Lambda. What are some challenges or best practices you follow?
How would you manage dependencies and deployment packages for Python Lambda functions?

## 25. what is multithreading, mutli processing and asyncio and how do you select one among them? - 4

## How does Django work? Explain MVT. • 

Django follows MVT: Model‑View‑Template. • Model: Handles database structure and ORM. • View: Contains business logic, fetches data from models, returns HTTP response. • Template: Handles frontend presentation (HTML). • The request flow: Request → URL Dispatcher → View → Model → View → Template → Response.
## Difference between tuple and list? • 

List: Mutable, defined using [], can add/remove/update. • Tuple: Immutable, defined using (), faster than list, used for fixed data.

## What is mutable and immutable? Is string mutable? • 
Mutable objects: Can be changed after creation (list, dict, set). • Immutable objects: Cannot be changed (tuple, int, float, string). • String is immutable. Example: s = "hello" s[0] = "H" # Error → strings are immutable

## Can we configure multiple databases in Django? How? • 
Yes. Add multiple DB entries in settings.py under DATABASES. • Use database routers to control which model uses which database. • Use using('db_name') when performing queries.

## Difference between makemigrations and migrate? • 
makemigrations: Creates migration files based on model changes. • migrate: Applies migration files to the database to create/update tables.

## Do you know Django REST Framework? What are serializers? • 
Yes. DRF is used to build APIs quickly. • Serializers convert between: • Python objects ↔ JSON • Useful for data validation and transformation.

## Difference between GET, POST, PUT, DELETE? • 
GET: Retrieve data. • POST: Create new resource. • PUT: Update/replace a resource. • DELETE: Remove resource.

## How do you deploy Django? Which server? 
Typical pattern: • Use Gunicorn or uWSGI as the application server. • Use Nginx as a reverse proxy. • Deploy on AWS EC2, Elastic Beanstalk, Docker, or DigitalOcean.

## Why choose Django? Purpose? • 
Batteries‑included framework. • Built‑in admin, ORM, security features. • Follows DRY, rapid development, scalable for large applications.

## Difference between Flask and Django; when to choose? 
• Flask: Micro-framework, lightweight, minimal, more flexibility. Best for small services. • Django: Full-stack framework, built-in ORM, admin panel, auth, scalable. Best for large apps.

## What are middlewares in Django? Execution flow? 
• Middleware: Layer that processes request/response globally. • Execution order: Request → Middleware 1 → Middleware 2 → View → Middleware 2 → Middleware 1 → Response • Used for authentication, security, logging, sessions.

## Map, filter, reduce difference

## How do you throw exception from calling function

## inheritance - i want to pass variable from child to parent class

## how do you create abstract method? what is the use of abstract method

## what is solid principle? 

## how do you create a custom exception

## maximum time duration lambda can execute?

## what is the difference between synchronous and asynchronous? give real time examples

## difference between series and dataframe

------------------------------------------------------------ React / Frontend Questions (with Answers) ------------------------------------------------------------

## How does React render and update the DOM? 
• Uses Virtual DOM. • On state change: • React creates a new virtual tree. • Compares it with previous tree (diffing). • Applies minimal changes to the real DOM.

## When would you avoid useEffect? 
• When logic can run during render (e.g., derived data). • When updating state unnecessarily inside useEffect. • For synchronous calculations (useMemo/useCallback preferable).

## How to prevent unnecessary re-renders? 
• Use React.memo for components. • useCallback for stable function references. • useMemo for expensive computations. • Split large components. • Avoid passing new objects each render.

## What is a closure? Real React example? 
• Closure: Inner function accessing variables from outer function even after the outer function has executed. Example: const [count, setCount] = useState(0); useEffect(() => { const interval = setInterval(() => {

 setCount(prev => prev + 1); // using closure correctly
}, 1000); }, []);

## Redux vs Context? 
• Context: Good for low-frequency updates (theme, auth). • Redux: Good for large state, predictable, debugging tools, middleware, scalable apps.

## Lazy loading & code splitting? 
• Load component chunks only when needed. • Improves initial load performance. Example: const Component = React.lazy(() => import('./Component'));

## When does memoization hurt performance? 
• When computation is cheap but memoizing costs more. • When dependencies change often. • Overuse of useMemo/useCallback adds overhead.

## How to optimize large lists? 
• Virtualization using react-window or react-virtualized. • Pagination. • Infinite scrolling. • Memoized list items.

## When NOT to use ARIA? 
• When a native HTML element already has the semantic behavior built-in. • Example: Don’t add role="button" to an actual button.

## How do you test async API calls? 
• Use Jest + React Testing Library. • Mock API with jest.mock or MSW. • Use async/await with waitFor. Example: await waitFor(() => expect(screen.getByText("Data")).toBeInTheDocument());

## How do you prevent XSS in React? 
• React escapes content by default. • Avoid dangerouslySetInnerHTML unless sanitized. • Validate user input. • Use security libraries like DOMPurify when inserting HTML.

## Page re-renders excessively — how to debug? 
• Use React DevTools Profiler. • Check which props/state trigger re-renders. • Add console logs in components. • Investigate reference changes in objects/arrays. • Wrap child components in React.memo.

## What problems do hooks solve vs class components? 
• Avoid “this” confusion. • Share logic easily using custom hooks. • Reduce boilerplate. • Better code reuse. • Side-effect handling becomes cleaner with useEffect.

## How do you decide when to split components? 
• If the component: • Has too many responsibilities (violates SRP). • Re-renders frequently. • Contains reusable UI logic. • Becomes hard to test or maintain. Split for: • Reuse • Performance • Maintainability


## AWS related questions
how do create lambda
how do you manage data in dynamo db
what is sqs and type of queues
cloud watch, timestream db, dynamo streams etc..


## Summary and Resources

For effective Python interview preparation, focus on understanding concepts deeply and practicing coding problems. Key resources include:

- [Python's official documentation](https://docs.python.org/3/)
- Books like *Effective Python* by Brett Slatkin and *Fluent Python* by Luciano Ramalho.
- Online platforms like [LeetCode](https://leetcode.com/) and [HackerRank](https://www.hackerrank.com/) for coding problem practice.

Best practices for preparation:
- Regularly practice coding problems and focus on optimization.
- Deeply understand underlying principles, not just syntax.
- Participate in peer code reviews to gain insights into different coding styles.


str1 = "Hello World"
str1.replace("world, "Trane)
print(str1)

Solving Questions:
1. Merge Two Sorted Lists:

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Answer:

def merge_two_sorted_lists(list1, list2):
    i, j = 0, 0
    merged = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    # Append the rest of whichever list is not done
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

Time Complexity: O(n + m), where n and m are the lengths of the two lists.
Space Complexity: O(n + m) for the merged output list.
No unnecessary sorting or auxiliary data structures used.
Direct, readable, and efficient.

2. Two Sum
LeetCode 1
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

def two_sum(nums, target):
    prevMap = {}  #Map to store: {value: index}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in prevMap:
            # Found the solution
            return [prevMap[diff], i]
        prevMap[num] = i  # Store the index of the current number
    return []  # If there is no solution (problem guarantee says there is one)

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]

The indices for the input nums = [2, 7, 11, 15] and target = 9 are [0, 1]. This solution is optimal with a Time Complexity of \(O(n)\) and a Space Complexity of \(O(n)\)




3. Valid Parentheses
LeetCode 20
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false


def isValid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    return not stack

    

4. Remove Duplicates from Sorted Array
LeetCode 26

5. Reverse Linked List
LeetCode 206

6. Maximum Subarray
LeetCode 53

7. Intersection of Two Linked Lists
LeetCode 160

8. Linked List Cycle
LeetCode 141

9. Min Stack
LeetCode 155

10. Binary Tree Inorder Traversal
LeetCode 94




## 26. How Jango works
MVT - model view template
## difference tuple and list
## what is mutable and immutable. string is mutable or not. give below example and ask 

## 27. can we configure multiple database in jango, how to do that

## 28. Make Migration and Migrate difference

## 29. Do you aware of jango rest framework, if ans yes, what is seriliazers in rest framework

## 30. What is the diff between get, post, put, delete

## 31. how do you deploy jango and which server you deploy

## 31. Why you choosen jango and what is the purpose.

## 32. What is difference between Flask and Jango and when to choose ? Small scale Flask and Big Scale Jango

## 33. What is middlewares in Jango? how middle wares will execute

1. How does React render and update the DOM?
2. When would you avoid useEffect?
3. Prevent unnecessary re-renders?
4. Closures – real example
5. Redux vs Context
6. Lazy loading & code splitting
7. When memoization hurts?
8. Optimize large lists
9. When NOT to use ARIA?
10. How do you test async API calls?
11. How do you prevent XSS in React apps?
12. You notice a page re-renders excessively. How do you debug it?
 
 
13. What problems do hooks solve compared to class components?
14. How do you decide when to split components vs keeping them unified?



subnet - private and public subnet - can we access network in private subnet
VPC - virtual private cloud