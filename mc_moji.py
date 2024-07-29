import os
import sys

# execution path for avatar generator
project_root = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.join(project_root, "app")
sys.path.insert(0, app_path)
from app.cli import main

if __name__ == "__main__":
    main()
