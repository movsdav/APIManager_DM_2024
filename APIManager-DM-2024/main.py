import requests
import logging
import os


class APIManager:
    def __init__(self, base_url):
        self.base_url = base_url
        self.__logger = logging.getLogger(__name__)

        if not os.path.isdir("../logs"):
            os.mkdir("../logs")
        with open("../logs/logger_info.log", "a"):
            pass

        logging.basicConfig(format='%(asctime)s %(message)s', datefmt="%m/%d/%Y %I:%M:%S",
                            filename="../logs/logger_info.log",
                            encoding="utf-8", level=logging.INFO, filemode="a")

    def request_get(self, endpoint, headers=None):
        url = f"{self.base_url}/{endpoint}"

        try:
            self.__logger.info(f"Sending GET request to: {url}")
            response_object = requests.get(url, headers=headers)
            response_object.raise_for_status()
            return response_object
        except requests.RequestException as e:
            self.__logger.error(f"Error during GET request to {url}: {e}")

    def request_post(self, endpoint, data, headers=None):
        url = f"{self.base_url}/{endpoint}"

        try:
            self.__logger.info(f"Sending POST request to: {url}")
            response_object = requests.post(url, json=data, headers=headers)
            response_object.raise_for_status()
            return response_object
        except requests.RequestException as e:
            self.__logger.error(f"Error during POST request to {url}: {e}")


if __name__ == "__main__":
    manager = APIManager("https://jsonplaceholder.typicode.com")
    response = manager.request_get("posts")
    # response_json = response.json()

    # for item in response_json:
    #     print(item)

    send_obj_status = manager.request_post("psts", {
        "name": "David",
        "age": 20,
    })
    #
    # print(send_obj_status)
