# replagex
Use replagex to easily replace massive strings on any text using regex.

## Install

Currently downloadable from [TestPyPI](https://test.pypi.org/project/replagex-pkg/)

## Example usage

1. Using JSON file

    ### example.json:
    ``` json
    {
        "patterns": [
            {
                "regex": "(\\d{3} \\d{3} \\d{4})",
                "replace": "xxx xxx xxxx"
            },
            {
                "regex": "(\\d{3}-\\d{3}-\\d{4})",
                "replace": "xxx-xxx-xxxx"
            },
            {
                "regex": "(\\(\\d{3}\\) \\d{3} \\d{4})",
                "replace": "(xxx) xxx xxxx"
            },
            {
                "regex": "(\\d{10})",
                "replace": "xxxxxxxxxx"
            }
        ]
    }
    ```
    > ### Warning
    > You have to escape the **\\** character on the JSON file, like this:  
    > \d -> \\\\d 

    ### script.py
    ``` python
    from replagex import Replagex

    rg = Replagex('example.json') # JSON file location

    # This is just a text example. It could be a text file content.
    text = '''
    555 513 4154
    555-513-4154
    (555) 513 4154
    5555134154
    '''

    # Apply regex
    print(rg.apply_regex(text))
    ```

    > ### Script Output:  
    > 
    > xxx xxx xxxx  
    > xxx-xxx-xxxx  
    > (xxx) xxx xxxx  
    > xxxxxxxxxx  

---  

2. Without JSON file

    ### script.py
    ``` python
    from replagex import Replagex
    from replagex.pattern import Pattern

    rg = Replagex()

    # It's just a text example. It could be text file content.
    text = '''
    555 513 4154
    555-513-4154
    (555) 513 4154
    5555134154
    '''

    # Add regex pattern using Pattern Class.
    rg.add_pattern(
        Pattern(
            "(\\d{3} \\d{3} \\d{4})",
            "xxx xxx xxxx"
        )
    )

    # Apply regex
    print(rg.apply_regex(text))
    ```

    > ### Script Output:  
    > 
    > xxx xxx xxxx  
    > 555-513-4154  
    > (555) 513 4154  
    > 5555134154  

***
## Extra parameters for patterns
You could use some extra parameters on every regex pattern:

 - [dotall](https://docs.python.org/3/library/re.html#re.DOTALL)
 - [ignore_case](https://docs.python.org/3/library/re.html#re.IGNORECASE)
 - [multiline](https://docs.python.org/3/library/re.html#re.MULTILINE)

> By default are ***False***.

Usage on a JSON file:

``` json
{
    "regex": "(\\d{3} \\d{3} \\d{4})",
    "replace": "xxx xxx xxxx",
    "dotall": true,
    "ignore_case": true,
    "multilne": true
},
```
Using *Pattern Class*:
``` python
rg.add_pattern(
    Pattern(
        "(\\d{3} \\d{3} \\d{4})",
        "xxx xxx xxxx",
        dotall=True,
        ignore_case=True,
        multiline=True
    )
)
```
