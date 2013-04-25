### 1) Define what a closure is. Give a simple closure example in a language of your choice.

A closure is a programming pattern which allows a function to call on variables outside it's local scope. Closures can be assigned to variables which allows calling the referenced function with the non-local variable.

A practical implementation of closures I've implemented is in jQuery, to make inline editing of table rows. 
The closures in this example are the .click functions, and the non-local variable being 'row'.

```javascript
$('tr').each(function(i, row) {
    $(row).find('a.edit').click(function() {
        // some code taken out which prepares edit field
        $(row).addClass('editmode');
    });
    $(row).find('a.save').click(function() {
        var newVal = $(row).find('input.edit').val();
        if (newVal != '') {
            $(row).find('form').submit(); 
        }
    }); 
});
```

### 2) Define a Python decorator that will cache the results of an expensive computation. Since you have no control over what methods can be decorated, make sure you are careful with the arguments that are passed around.

This is a very simple cache based on a dictionary. The only assumption for this decorator is that the args are hashable. Checks could be implemented to prevent this cache from breaking the code if a non-hashable set of arguments are received, or the args can be pickled down to hashable values.

Another interesting fact about this decorator is that it is also a closure.

```python
def memoize(function):
    memo = {}
    def cache(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return cache
```

### 3) Define a method that will return the Nth Fibonacci number. Print out the 10th - fib(10) . Can you think of different approaches to coding this in Python?

For the 10th fibonacci number, recursion is enough to calculate quickly. This recursive function is based on the mathematical formula F(n) = F(n-1) + F(n-2)

```python
def fib(a):
    if a == 0 or a == 1:
        return a
    else:
        return fib(a-1) + fib(a-2)

print fib(10)
```

### 3a) Print out the 100th Fibonacci number. Make sure this completes in less than a minute.

To find the 100th fibonacci number, plain recursion is a bad solution, since the amount of recursive calls escalates exponentially with the amount of fibonacci numbers it needs to calculate. We can fix this issue by simply adding the memoize decorator created in task 2.

```python
@memoize
def fib(a):
    if a == 0 or a == 1:
        return a
    else:
        return fib(a-1) + fib(a-2)
        
print fib(100)
```

### 3b) Print out the 1200th Fibonacci number. Make sure this completes in less than a minute.

The 1200th fibonacci number requires too many recursive steps and overflows the recursion depth that python allows. In order to calculate this number, I will just calculate the number iteratively.

Assuming python 2.x for this one, as xrange doesn't exist in Python 3, but xrange will consume less memory on larger ranges, and I have no need of the actual list of numbers when only iterating. 'i' could be used to construct a list or dict of the values as we go.

```python
def fib(a):
    x = 0
    y = 1
    for i in xrange(0,a):
        tmp = x + y
        y = x
        x = tmp
    return x

print fib(1200)
```

As a thought following these tasks on fibonacci, using a combination of iterative calculation and storing previously calculated numbers would be most efficient if we needed to calculate many different terms of fibonacci numbers in sequence.


### 4) Create a simple web application which allows you to upload a text file. The uploaded file(s) can be selected and upon selection a an analysis will be performed. A list of the top 20 words that occur the most in the text will be generated. Present this list as a Bar Graph rendered by the browser, to avoid rendering graphs on the server-side. Make sure that a large number of users can efficiently fetch the results.

I built the webapp using Bottle, CanvasJS and jQuery with the jQCloud plugin. I could have included bootstrap to provide better styling, but function above design for the simplicity.

The code for the webapp can be found in the webapp folder. All dependencies are included, just need to run app.py.

### 4a) We also challenge you to come up with other ways than bar-charts to present the data. While not required, can you come up with another interesting to analyze the data than "top 20 words" as well?

I've included code to produce a tag cloud focused around the top 20 words. The tag cloud uses the same data as the graph and renders with javascript.