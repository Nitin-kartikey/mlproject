import logging
import os
from datetime import datetime

log_file=f"{datetime.now().strftime('%m_%d_%y_%H')}.log"
logs_path=os.path.joins(os.getcwd(),"logs",log_file)
os.makedirs(logs_path,exist_ok=True)

log_file_path=os.path.join(logs_path,log_file)

logging.basicConfig(
    filename=log_file_path,
    format="[ % (asctime)s ] %(line)d %(name)s - %(levelname)s - %(message)s " , 
    level=logging.info,
)

class CustomException(Exception):
    def __init__(self, message="An error occurred"):
        super().__init__(message)

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(str(e))
