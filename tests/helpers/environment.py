import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Env:
    def __init__(self, env):
        self.env = env

    def get_dummy_rest_api_version(self):
        env = None
        if self == "/api/v1":
            env = os.environ.get("DUMMY_REST_API_V1")
        return env

    def get_employee_id(self):
        env = None
        if self == "id":
            env = os.environ.get("EMPLOYEE_ID")
        return env
