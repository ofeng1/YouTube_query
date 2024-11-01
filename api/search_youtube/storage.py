import json
import os
from typing import Union

from dotenv import load_dotenv
from supabase import create_client

load_dotenv()


class Storage:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name
        self.client = create_client(
            os.environ["SUPABASE_URL"], os.environ["SUPABASE_KEY"]
        )

    def download(self, file_path: str, as_json: bool = False):
        try:
            result = self.client.storage.from_(self.bucket_name).download(file_path)
        except Exception:
            return None

        if as_json:
            result_str = result.decode("utf-8")
            return json.loads(result_str)

        return result

    def upload(self, file_path: str, data: Union[str, bytes], content_type: str):
        if isinstance(data, str):
            data = data.encode("utf-8")

        return self.client.storage.from_(self.bucket_name).upload(
            path=file_path,
            file=data,
            file_options={"content-type": content_type, "upsert": "true"},
        )

    def update(self, file_path: str, data: Union[str, bytes], content_type: str):
        if isinstance(data, str):
            data = data.encode("utf-8")

        return self.client.storage.from_(self.bucket_name).update(
            path=file_path,
            file=data,
            file_options={"content-type": content_type},
        )

    def move(self, source: str, destination: str):
        return self.client.storage.from_(self.bucket_name).move(source, destination)

    def remove(self, file_path: str):
        return self.client.storage.from_(self.bucket_name).remove(file_path)

    def create_signed_url(self, file_path: str, expires_in: int = 60):
        return self.client.storage.from_(self.bucket_name).create_signed_url(
            file_path, expires_in=expires_in
        )

    def get_public_url(self, file_path: str):
        return self.client.storage.from_(self.bucket_name).get_public_url(file_path)
