>>> print(encode('Bond. James Bond.'.upper()))
-... --- -. -.. .-.-.-   .--- .- -- . ...   -... --- -. -.. .-.-.-
>>> print(encode('What makes you think this is my first time?.'.upper()))
.-- .... .- -   -- .- -.- . ...   -.-- --- ..-   - .... .. -. -.-   - .... .. ...   .. ...   -- -.--   ..-. .. .-. ... -   - .. -- . ..--.. .-.-.-
>>> print(encode('SOS'))
... --- ...

>>> print(decode('.-- .  .... .- ...- .  .- .-.. .-..  - .... .  - .. -- .  .. -.  - .... .  .-- --- .-. .-.. -.. .-.-.-'))
WEHAVEALLTHETIMEINTHEWORLD.
>>> print(decode('.-- . -....- .... .- ...- . -....- .- .-.. .-.. -....- - .... . -....- - .. -- . -....- .. -. -....- - .... . -....- .-- --- .-. .-.. -.. .-.-.-'))
WE-HAVE-ALL-THE-TIME-IN-THE-WORLD.
>>> print(decode('.-- . -....- .... .- ...- . -....- .- .-.. .-.. -....- - .... . -....- - .. -- . -....- .. -. -....- - .... . -....- .-- --- .-. .-.. -.. .-.-.-').replace('-', ' '))
WE HAVE ALL THE TIME IN THE WORLD.




# В терминале:
>>> pytest morse.py
======================================================== test session starts ===========================================================
platform win32 -- Python 3.9.12, pytest-7.4.3, pluggy-1.0.0
rootdir: C:\Users\User\Desktop\tests
plugins: anyio-3.5.0
collected 3 items

morse.py ...                                                                                                                                            [100%] 

========================================================== 3 passed in 0.08s ========================================================= 





# В терминале:
>>> python -m unittest -v ohe.py 
test_empty (ohe.TestOHE) ... ok
test_four_cities (ohe.TestOHE) ... ok
test_six_cities (ohe.TestOHE) ... ok
test_string (ohe.TestOHE) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK


# В терминале:
>>> pytest ohe.py
========================================================== test session starts =========================================================
platform win32 -- Python 3.9.12, pytest-7.4.3, pluggy-1.0.0
rootdir: C:\Users\User\Desktop\tests
plugins: anyio-3.5.0
collected 8 items

ohe.py ........                                                                                                                                         [100%]

========================================================== 8 passed in 0.10s ========================================================== 
