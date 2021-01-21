import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Env:
    def __init__(self, env):
        self.env = env

    def get_dummy_rest_api_version(self):
        return os.environ.get("DUMMY_REST_API_V1") if self == "/api/v1" else None

    def get_employee_id(self):
        return os.environ.get("EMPLOYEE_ID") if self == "id" else None
