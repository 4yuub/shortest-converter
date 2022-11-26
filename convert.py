import sys

code = "".join(sys.stdin.readlines())
code += "\n" * (len(code)&1)

encoded = code.encode('u8').decode('u16')

template = "exec(bytes('%s','u16')[2:])"

print(template % (encoded, ))
