from django.urls import reverse

class LogInTester:   
    def _is_logged_in(self):
        return '_auth_user_id' in self.client.session.keys()
    # def setUp(self):
    #     self.form_input = {
    #         'first_name': 'Jane',
    #         'last_name': 'Doe',
    #         'username': '@janedoe',
    #         'email': 'janedoe@example.org',
    #         'bio': 'My bio',
    #         'new_password': 'Password123',
    #         'password_confirmation': 'Password123'
    #     }