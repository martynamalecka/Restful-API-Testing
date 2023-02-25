import requests

url = "https://api.restful-api.dev/objects"
headers = {"content-type": "application/json"}


class APIClient:
    @staticmethod
    def get_all_objects():
        return requests.get(url, headers=headers)

    @staticmethod
    def get_single_object_by_id(object_id):
        return requests.get(f"{url}/{object_id}", headers=headers)

    @staticmethod
    def get_multiple_objects_by_ids(object_ids):
        object_ids_as_strings = list(map(str, object_ids))
        query_params = "&".join(
            "id=" + object_id for object_id in object_ids_as_strings
        )
        return requests.get(f"{url}?{query_params}")

    @staticmethod
    def delete_single_object_by_id(object_id):
        return requests.delete(f"{url}/{object_id}", headers=headers)

    @staticmethod
    def add_new_object(payload):
        return requests.post(url, json=payload)

    @staticmethod
    def update_object_by_id(object_id, payload):
        return requests.put(f"{url}/{object_id}", json=payload)

    @staticmethod
    def update_object_name_by_id(object_id, payload):
        return requests.patch(f"{url}/{object_id}", json=payload)
