# Birds

IDIOT = lambda x : x
KESTREL = lambda p : lambda q : p
KITE = lambda p : lambda q : q

# Arithmetic

SUCCESSOR = lambda n : lambda f : lambda x : f(n(f)(x))
ADD = lambda m : lambda n : n(SUCCESSOR)(m)
MULTIPLY = lambda m : lambda n : m(SUCCESSOR)(n)

# Logic

TRUE = KESTREL
FALSE = KITE
AND = lambda p : lambda q : p(q)(FALSE)
OR = lambda p : lambda q : p(p)(q)
XOR = lambda p : lambda q : p(NOT(q))(q)
NOT = lambda c : c(FALSE)(TRUE)

# Church Numerals

ZERO = lambda f : IDIOT
ONE = SUCCESSOR(ZERO)
TWO = SUCCESSOR(ONE)
THREE = SUCCESSOR(TWO)
FOUR = SUCCESSOR(THREE)
FIVE = SUCCESSOR(FOUR)
SIX = SUCCESSOR(FIVE)
SEVEN = SUCCESSOR(SIX)
EIGHT = SUCCESSOR(SEVEN)
NINE = SUCCESSOR(EIGHT)
TEN = SUCCESSOR(NINE)
