import sys
import recursion

print(sys.argv)

_, base, exp, *rest = sys.argv
print(rest)
result = recursion.our_pow(int(base), int(exp))
print(result)
