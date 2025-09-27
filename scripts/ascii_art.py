# /// script
# dependencies = [
#   "pyfiglet",
# ]
# ///

# See: https://github.com/microsoft/pylance-release/discussions/6522
# Currently pylance does not recognise scripts with declared dependencies 
import pyfiglet  # pyright: ignore[reportMissingImports]

if __name__ == "__main__":
    result = pyfiglet.figlet_format("Modernist Python")
    print(result)