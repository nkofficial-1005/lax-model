import os
import sys
import logging

#Logging string log level (information or bug), module (main.py or app.py), and message.
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#Creating a logs and running logs folder to store the logs
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), #Saves logs inside the logs folder
        logging.StreamHandler(sys.stdout) #Displays logs in terminal
    ]
)

logger = logging.getLogger("laxProjectLogger")