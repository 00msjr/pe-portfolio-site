# tests.py
import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(":memory:")


class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        # Test creating a timeline post
        first_post = TimelinePost.create(
            name="John Doe", email="john@example.com", content="Hello World, I'm John!"
        )
        assert first_post.id == 1
        assert first_post.name == "John Doe"
        assert first_post.email == "john@example.com"
        assert first_post.content == "Hello World, I'm John!"
        
        # Test creating a second timeline post
        second_post = TimelinePost.create(
            name="Jane Doe", email="jane@example.com", content="Hello World, I'm Jane!"
        )
        assert second_post.id == 2
        assert second_post.name == "Jane Doe"
        assert second_post.email == "jane@example.com"
        assert second_post.content == "Hello World, I'm Jane!"
        
        # Test retrieving all posts
        posts = TimelinePost.select()
        assert len(list(posts)) == 2
        
        # Test retrieving a specific post
        retrieved_post = TimelinePost.get(TimelinePost.id == 1)
        assert retrieved_post.name == "John Doe"
        
        # Test updating a post
        first_post.content = "Updated content"
        first_post.save()
        updated_post = TimelinePost.get(TimelinePost.id == 1)
        assert updated_post.content == "Updated content"
        
        # Test deleting a post
        second_post.delete_instance()
        remaining_posts = TimelinePost.select()
        assert len(list(remaining_posts)) == 1
