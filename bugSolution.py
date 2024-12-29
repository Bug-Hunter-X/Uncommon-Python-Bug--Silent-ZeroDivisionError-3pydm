def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float('inf')  # Or handle it appropriately

result = function(10, 0)
print(result) # Output: inf