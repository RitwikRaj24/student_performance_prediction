# For the purpose of 'logging' anything that happens in a file , so that we can track the progress or track any errors that might occur 

import logging
import os 
from datetime import datetime 

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 
# filename : datetime.now() 
# date and time  
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # whatever logs created will be w.r.t the cwd .
os.makedirs(log_path, exist_ok=True) # exist_ok -> even if a file exists , keep on appending the folder 

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH, 
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Testing 

# if __name__ == "__main__": 
#     logging.info("Logging has started")


