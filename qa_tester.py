from mock_classes import Browser, API

class QATester:
    def __init__(self, website_url, api_url):
        self.browser = Browser(website_url)
        self.api = API(api_url)

    def verify_website_users(self):
        # TODO: Get the user list from the website and compare it with the expected list.
        # For now, let's just print the user list from the website for manual verification.
        user_list = self.browser.find_object("user_list")
        print("User List from Website:")
        print(user_list)

    def verify_api_users(self):
            # TODO: Get the user list from the API and compare it with the expected list.
            # For now, let's just print the user list from the API for manual verification.
            api_response = self.api.request("GET", "/api/v1/users")
            user_list = api_response["data"]
            print("User List from API:")
            print(user_list)

    if __name__ == "__main__":
        # Replace 'http://myweb.com' and 'http://api.myweb.com' with the actual URLs.
        tester = QATester(website_url='http://myweb.com', api_url='http://api.myweb.com')
        tester.verify_website_users()
        tester.verify_api_users()