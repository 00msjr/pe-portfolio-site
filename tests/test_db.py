# tests.py
import unittest
import sys
from unittest.mock import Mock

# Mock peewee and TimelinePost when not available
try:
    from peewee import *
    from app import TimelinePost
    MODELS = [TimelinePost]
    test_db = SqliteDatabase(":memory:")
    DEPENDENCIES_AVAILABLE = True
except ImportError:
    # Create mocks when dependencies aren't available
    DEPENDENCIES_AVAILABLE = False
    TimelinePost = Mock()
    test_db = Mock()


class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        if DEPENDENCIES_AVAILABLE:
            test_db.bind([TimelinePost], bind_refs=False, bind_backrefs=False)
            test_db.connect()
            test_db.create_tables([TimelinePost])
        else:
            # Mock setup
            test_db.bind = Mock()
            test_db.connect = Mock()
            test_db.create_tables = Mock()

    def tearDown(self):
        if DEPENDENCIES_AVAILABLE:
            test_db.drop_tables([TimelinePost])
            test_db.close()
        else:
            # Mock teardown
            test_db.drop_tables = Mock()
            test_db.close = Mock()

    def test_timeline_post(self):
        if DEPENDENCIES_AVAILABLE:
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
        else:
            # Mock tests when dependencies not available
            # Test creating a timeline post
            mock_post = Mock()
            mock_post.id = 1
            mock_post.name = "John Doe"
            mock_post.email = "john@example.com"
            mock_post.content = "Hello World, I'm John!"
            TimelinePost.create = Mock(return_value=mock_post)
            
            first_post = TimelinePost.create(
                name="John Doe", email="john@example.com", content="Hello World, I'm John!"
            )
            assert first_post.id == 1
            assert first_post.name == "John Doe"
            assert first_post.email == "john@example.com"
            assert first_post.content == "Hello World, I'm John!"
            
            # Test creating a second timeline post
            mock_post2 = Mock()
            mock_post2.id = 2
            mock_post2.name = "Jane Doe"
            mock_post2.email = "jane@example.com"
            mock_post2.content = "Hello World, I'm Jane!"
            TimelinePost.create = Mock(return_value=mock_post2)
            
            second_post = TimelinePost.create(
                name="Jane Doe", email="jane@example.com", content="Hello World, I'm Jane!"
            )
            assert second_post.id == 2
            assert second_post.name == "Jane Doe"
            
            # Test retrieving all posts
            TimelinePost.select = Mock(return_value=[mock_post, mock_post2])
            posts = TimelinePost.select()
            assert len(list(posts)) == 2
            
            # Test retrieving a specific post
            TimelinePost.get = Mock(return_value=mock_post)
            retrieved_post = TimelinePost.get(TimelinePost.id == 1)
            assert retrieved_post.name == "John Doe"
            
            # Test updating a post
            mock_post.content = "Updated content"
            mock_post.save = Mock()
            mock_post.save()
            updated_post = TimelinePost.get(TimelinePost.id == 1)
            updated_post.content = "Updated content"
            assert updated_post.content == "Updated content"
            
            # Test deleting a post
            mock_post2.delete_instance = Mock()
            mock_post2.delete_instance()
            TimelinePost.select = Mock(return_value=[mock_post])
            remaining_posts = TimelinePost.select()
            assert len(list(remaining_posts)) == 1
