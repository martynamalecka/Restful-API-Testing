class Payloads:

    @staticmethod
    def get_new_object_payload():
        return {
            'name': 'New Apple MacBook',
            'data': {
                'year': 2023,
                'price': 2999.99,
                'CPU model': 'Intel Core i9',
                'Hard disk size': '2 TB'
            }
        }

    @staticmethod
    def get_updated_object_payload():
        return {
            'name': 'New Apple MacBook',
            'data': {
                'year': 2023,
                'price': 2999.99,
                'CPU model': 'Intel Core i9',
                'Hard disk size': '2 TB',
                'color': 'silver'
            }
        }
