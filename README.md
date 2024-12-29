# Uncommon Python Bug: Silent ZeroDivisionError

This repository demonstrates a subtle bug in Python that can lead to unexpected behavior when dealing with ZeroDivisionError exceptions.  The bug arises when the ZeroDivisionError occurs within a function that doesn't explicitly handle the exception, and the result of the function is not directly used or checked.