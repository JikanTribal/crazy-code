@type.__call__
class show: __lshift__ = print

main: lambda:\
        (
            show << "Hello, world"
        ) = "run"

if main == 'run':
    __annotations__["main"]()
else:
    print("Bruh")
