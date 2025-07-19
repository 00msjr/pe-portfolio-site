import unittest
import os

os.environ["TESTING"] = "true"

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        # TODO: Add more tests for homepage

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_post" in json
        assert len(json["timeline_post"]) == 0
        # TODO: add more tests to timeline get/post, ad timeline page

    def test_malformed_timeline_post(self):
        # missing name
        response = self.client.post(
            "/api/timeline_post",
            data={"email": "john@example.com", "content": "Hello World, I'm John!"},
        )
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid Name" in html

        response = self.client.post(
            "/api/timeline_post",
            data={"name": "John Doe", "email": "john@example.com", "content": ""},
        )
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid Content" in html

        response = self.client.post(
            "/api/timeline_post",
            data={
                "name": "John Doe",
                "email": "not-an-email",
                "content": "Hello World, I'm John!",
            },
        )
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid Email" in html
