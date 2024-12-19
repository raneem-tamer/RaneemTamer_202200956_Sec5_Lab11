from seleniumbase import BaseCase

class ToDoListTest(BaseCase):
    def test_add_and_verify_task(self):
        # Start the Flask app
        self.open("http://127.0.0.1:5000/")

        # Add a task
        self.type("input[name='task']", "Finish homework")
        self.click("button[type='submit']")

        # Verify the task is displayed
        self.assert_text("Finish homework", "ul")
