import pytest
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from mtg_blog.models import Post, Topic

class TestTopicModel(TestCase):
    def test_topic_creation(self):
        """Test Topic model with the required fields"""
        topic = Topic.objects.create(
            name="Standard",
            slug="standard"
        )
        self.assertEqual(topic.name, "Standard")
        self.assertEqual(topic.slug, "standard")
        self.assertEqual(str(topic), "Standard")
    def test_topic_unique_name(self):
        """Test that topic has a unique name"""
        Topic.objects.create(name="Commander", slug="commander")
        with self.assertRaises(ValidationError):
            topic = Topic(name="Commander", slug="commander-edh")
            topic.full_clean()