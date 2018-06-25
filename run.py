from src import miners
import sys

if __name__ == "__main__":
	sys.path.append(str(sys.path[0] + "/src/"))
	print(sys.path)
	miners.run()
