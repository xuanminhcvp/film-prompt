#!/usr/bin/env python3
import sys
import os

# Add scripts directory to path to allow imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from kiem_app.core.file_handler import FileHandler
from kiem_app.core.logger import Logger
from kiem_app.services.checker_service import CheckerService
from kiem_app.controllers.main_controller import MainController

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 kiem.py <KICH-BAN.md>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        sys.exit(1)
        
    # Dependency Injection
    file_handler = FileHandler()
    logger = Logger()
    checker_service = CheckerService(logger)
    
    controller = MainController(file_handler, logger, checker_service)
    controller.run(filepath)

if __name__ == "__main__":
    main()
