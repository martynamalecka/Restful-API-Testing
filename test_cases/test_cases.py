from client_api.api_client import APIClient
from expected_data.expected_data import ExpectedData
from payloads.payloads import Payloads
import uuid


class TestAPI:
    @staticmethod
    def _get_random_id():
        return f"test_{uuid.uuid4().hex}"

    # Positive testing.

    def test_get_all_objects_200_expected(self):
        # get all objects to make sure they exist
        get_all_objects_response = APIClient.get_all_objects()
        assert get_all_objects_response.status_code == 200, "Objects NOT found."

        # check if the actual data of all objects matches the expected data
        expected_all_objects_data = ExpectedData.get_all_objects_data()
        actual_all_objects_data = get_all_objects_response.json()
        assert (
            expected_all_objects_data == actual_all_objects_data
        ), "The actual data for all objects should match the expected data."

    def test_get_single_object_by_id_200_expected(self):
        # get object with given id to make sure it exists
        get_object_response = APIClient.get_single_object_by_id(7)
        assert get_object_response.status_code == 200, "Object with given id NOT found."

        # check if the actual data of the object with given id matches the expected data
        expected_object_data = ExpectedData.get_object_with_id_7_data()
        actual_object_data = get_object_response.json()
        assert (
            expected_object_data == actual_object_data
        ), "The actual data for object with given id should match the expected data."

    def test_get_objects_by_ids_200_expected(self):
        # get multiple objects by ids
        get_objects_response = APIClient.get_multiple_objects_by_ids([3, 5, 10])
        assert (
            get_objects_response.status_code == 200
        ), "Objects with given ids NOT found."

        # check if the actual data of the objects matches the expected data
        expected_objects_data = ExpectedData.get_object_with_id_3_5_10_data()
        actual_objects_data = get_objects_response.json()
        assert (
            expected_objects_data == actual_objects_data
        ), "The actual data for objects with given ids should match the expected data."

    def test_add_new_object_200_expected(self):
        # create a new object
        new_object_payload = Payloads.get_new_object_payload()
        add_new_object_response = APIClient.add_new_object(new_object_payload)
        assert (
            add_new_object_response.status_code == 200
        ), "Object has NOT been created."

        # get a new object id and check if it exists
        new_object_id = add_new_object_response.json()["id"]
        get_new_object_response = APIClient.get_single_object_by_id(new_object_id)
        assert (
            get_new_object_response.status_code == 200
        ), "Object with given id does NOT exist."

        # get the creation date & time of the new object for the data comparison
        new_object_creation_date_and_time = add_new_object_response.json()["createdAt"]

        # check if the newly added object data matches the expected data
        expected_new_object_data = (
            {"id": new_object_id}
            | new_object_payload
            | {"createdAt": new_object_creation_date_and_time}
        )
        actual_new_object_data = add_new_object_response.json()
        assert (
            expected_new_object_data == actual_new_object_data
        ), "The actual data of the new object should match the expected data."

    def test_add_new_object_with_empty_data_200_expected(self):
        # create a new object with an empty dictionary
        new_object_payload = {}
        add_new_object_response = APIClient.add_new_object(new_object_payload)
        assert (
            add_new_object_response.status_code == 200
        ), "Object has NOT been created."

        # get a new object id and check if it exists
        new_object_id = add_new_object_response.json()["id"]
        get_new_object_response = APIClient.get_single_object_by_id(new_object_id)
        assert (
            get_new_object_response.status_code == 200
        ), "Object with given id does NOT exist."

    def test_update_object_200_expected(self):
        # create a new object prior to updating it
        new_object_payload = Payloads.get_new_object_payload()
        add_new_object_response = APIClient.add_new_object(new_object_payload)
        assert (
            add_new_object_response.status_code == 200
        ), "Object has NOT been created."

        # get the id for the newly created object and make sure it exist
        new_object_id = add_new_object_response.json()["id"]
        get_new_object_response = APIClient.get_single_object_by_id(new_object_id)
        assert (
            get_new_object_response.status_code == 200
        ), "Object with given id does NOT exist."

        # update an existing object with new data
        updated_object_payload = Payloads.get_updated_object_payload()
        updated_object_response = APIClient.update_object_by_id(
            new_object_id, updated_object_payload
        )
        assert updated_object_response.status_code == 200, "Update unsuccessful."

        # check if the object data has been updated with {'color': 'silver'}
        expected_object_color = "silver"
        actual_updated_object_color = updated_object_response.json()["data"]["color"]
        assert (
            expected_object_color == actual_updated_object_color
        ), "The actual data of the updated object should match the expected data."

    def test_update_object_name_200_expected(self):
        # create a new object prior to updating it
        new_object_payload = Payloads.get_new_object_payload()
        add_new_object_response = APIClient.add_new_object(new_object_payload)
        assert (
            add_new_object_response.status_code == 200
        ), "Object has NOT been created."

        # get a new object id and check if it exists
        new_object_id = add_new_object_response.json()["id"]
        get_new_object_response = APIClient.get_single_object_by_id(new_object_id)
        assert (
            get_new_object_response.status_code == 200
        ), "Object with given id does NOT exist."

        # update 'name' in the new object
        payload = {"name": "Apple MacBook Pro 16 (Updated Name)"}
        update_object_name_response = APIClient.update_object_name_by_id(
            new_object_id, payload
        )
        assert update_object_name_response.status_code == 200, "Update unsuccessful."

        # check if name has been updated
        assert (
            update_object_name_response.json()["name"] == payload["name"]
        ), "Actual data should match the expected data."

    def test_delete_object_200_expected(self):
        # create a new object prior to deleting it
        new_object_payload = Payloads.get_new_object_payload()
        add_new_object_response = APIClient.add_new_object(new_object_payload)
        assert (
            add_new_object_response.status_code == 200
        ), "Object has NOT been created."

        # get a new object id and check if it exists
        new_object_id = add_new_object_response.json()["id"]
        get_new_object_response = APIClient.get_single_object_by_id(new_object_id)
        assert (
            get_new_object_response.status_code == 200
        ), "Object with given id does NOT exist."

        # delete the created object
        delete_object_response = APIClient.delete_single_object_by_id(new_object_id)
        assert (
            delete_object_response.status_code == 200
        ), "Object with given id has NOT been deleted successfully."

        # get the deleted object to check if it has been successfully deleted
        get_deleted_object_response = APIClient.get_single_object_by_id(new_object_id)
        assert (
            get_deleted_object_response.status_code == 404
        ), "Object with given id has NOT been deleted."

    # Negative testing.

    def test_get_not_existing_object_by_id_404_expected(self):
        # get an object with a random id & check if it exists
        get_object_response = APIClient.get_single_object_by_id(self._get_random_id())
        assert get_object_response.status_code == 404, "Object with given id exists."

    def test_add_new_object_with_incorrect_payload_400_expected(self):
        # create a new object with an incorrect payload and check if it has been created
        incorrect_payload = "Incorrect payload"
        add_new_object_response = APIClient.add_new_object(incorrect_payload)
        assert (
            add_new_object_response.status_code == 400
        ), "Object should NOT have been created."

    def test_delete_object_that_does_not_exist_404_expected(self):
        # delete an object that does not exist using random id & check if it has been deleted successfully
        delete_object_response = APIClient.delete_single_object_by_id(
            self._get_random_id()
        )
        assert delete_object_response.status_code == 404, "Object with given id exists."

    def test_update_object_not_allowed_405_expected(self):
        # get an object and make sure it exists
        get_object_response = APIClient.get_single_object_by_id(2)
        assert get_object_response.status_code == 200, "Object with given id NOT found."

        # update the object, update should be not successful
        payload = {"data": "jhj"}
        update_object_response = APIClient.update_object_by_id(2, payload)
        assert update_object_response.status_code == 405, "Data has been updated."
