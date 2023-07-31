class Browser:
    def __init__(self, url: str):
        # Url of the website
        self.url = url

    def find_object(self, object_name: str):
        # TODO: return the specified object of the website DOM
        # For the sake of this example, let's just return a mock list of users
        # with one administrator user.
        return {
            "user_list": [
                {
                    "last_name": "Doe",
                    "first_name": "John",
                    "email": "john.doe@example.com",
                    "confirmed": True,
                    "role": "admin",
                    "other_permissions": "read",
                    "social": "linkedin",
                    "last_updated": 1234567890
                },
                {
                    "last_name": "Smith",
                    "first_name": "Jane",
                    "email": "jane.smith@example.com",
                    "confirmed": False,
                    "role": "user",
                    "other_permissions": "write",
                    "social": "facebook",
                    "last_updated": 1234567890
                }
                # Add more users if needed
            ],
            "total_counter": 2
        }

    class API:
        def __init__(self, url: str):
            # Url of the API
            self.url = url

        def request(self, http_method: str, endpoint: str):
            # TODO: return the HTTP RESTful API response
            # For the sake of this example, let's just return a mock API response.
            return {
                "data": [
                    {
                        "last_name": "Doe",
                        "first_name": "John",
                        "email": "john.doe@example.com",
                        "confirmed": True,
                        "role": "admin",
                        "other_permissions": "read",
                        "social": "linkedin",
                        "last_updated": 1234567890
                    },
                    {
                        "last_name": "Smith",
                        "first_name": "Jane",
                        "email": "jane.smith@example.com",
                        "confirmed": False,
                        "role": "user",
                        "other_permissions": "write",
                        "social": "facebook",
                        "last_updated": 1234567890
                    }
                    # Add more users if needed
                ],
                "Meta": {
                    "total": 2,
                    "limit": 10,
                    "offset": 0
                }
            }