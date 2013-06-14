python-profiling
================

Profiling decorator for Python

Usage
=====

    @profile
    def func_that_you_want_to_profile():
        ...
    
Output:

    2 function calls in 0.000 seconds

    Ordered by: internal time

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 temp.py:27(test)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         2 function calls in 0.000 seconds

    Ordered by: cumulative time

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
         1    0.000    0.000    0.000    0.000 temp.py:27(test)
         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

