from kiem_app.core.file_handler import FileHandler
from kiem_app.core.logger import Logger
from kiem_app.models.script_data import ScriptData
from kiem_app.services.checker_service import CheckerService

class MainController:
    def __init__(self, file_handler: FileHandler, logger: Logger, checker_service: CheckerService):
        self.file_handler = file_handler
        self.logger = logger
        self.checker_service = checker_service

    def run(self, filepath: str):
        try:
            content = self.file_handler.read_file(filepath)
            script_data = ScriptData(content)
            self.logger.info(f"Checking script: {filepath}")
            self.checker_service.check_all(script_data)
        except Exception as e:
            self.logger.error(f"Error checking {filepath}: {str(e)}")
