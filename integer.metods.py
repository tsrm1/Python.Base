int_value = -1234
print('int_value=                           -> ',int_value)
print('int_value.__abs__()                  -> ',int_value.__abs__())
print('abs(int_value)                       -> ',abs(int_value))
print('int_value.__ceil__()                 -> ',int_value.__ceil__())
# print('int_value.__divmod__(8)              -> ',int_value.__divmod__(8))
print('divmod(int_value, 8)                 -> ',divmod(int_value, 8))

print('float(int_value)                     -> ',float(int_value))
print('str(int_value)                       -> ',str(int_value))
print('int_value.__floor__()                -> ',int_value.__floor__())
print('int_value.__pow__(4)                 -> ',int_value.__pow__(4))
print('int_value.__radd__()                 -> ',int_value.__radd__(6))
print('round(3.14159, 2)                    -> ',round(3.14159, 2))
print('round(int_value, 2)                  -> ',round(int_value, 2))
print('int_value.__trunc__                  -> ',int_value.__trunc__())
print('int_value.as_integer_ratio()         -> ',int_value.as_integer_ratio())
print('int_value.bit_count()                -> ',int_value.bit_count())
print('int_value.bit_length()               -> ',int_value.bit_length())
print('int_value.denominator                -> ',int_value.denominator)
# print('int_value.bit_length()               -> ',int_value.from_bytes())
print('bin(int_value)                       -> ',bin(int_value))
print('hex(int_value)                       -> ',hex(int_value))
# print('int_value.__getattribute__           -> ',int_value.__getattribute__())
print('int_value.__doc__                    -> ',int_value.__doc__)

int_value = 2+3j
print('int_value=                           -> ',int_value)
print('int_value.imag                       -> ',int_value.imag)
print('int_value.real                       -> ',int_value.real)
print('int_value.conjugate()                -> ',int_value.conjugate())

print('int_value.__doc__                    -> ',int_value.__doc__)