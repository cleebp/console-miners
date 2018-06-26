from src import main
import platform

if __name__ == "__main__":
    current_platform = platform.system()
    print("Running on: " + str(current_platform))
    main.run(current_platform)
