from io import BytesIO

from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.base import File
from django.urls import reverse
from PIL import Image
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Like, Post


class PostListViewTests(APITestCase):
    """
    Test cases for the PostListView.
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)

    @staticmethod
    def get_image_file(name, ext='png', size=(50, 50), color=(256, 0, 0)):
        file_obj = BytesIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    def test_create_post(self):
        """
        Test creating a new post through the API.
        """
        url = reverse('post-list')
        image = self.get_image_file('test.png')
        data = {
            'image': image,
            'caption': 'Test content'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().user, self.user)

    def test_list_posts(self):
        """
        Test listing all posts through the API.
        """
        Post.objects.create(
            image='test1.jpg',
            caption='Content 1',
            user=self.user
        )
        Post.objects.create(
            image='test2.jpg',
            caption='Content 2',
            user=self.user
        )
        url = reverse('post-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(
            response.data['results'][0]['image'],
            'http://testserver/test1.jpg'
        )
        self.assertEqual(
            response.data['results'][1]['image'],
            'http://testserver/test2.jpg'
        )


class PostDetailViewTests(APITestCase):
    """
    Test cases for the PostDetailView.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.post = Post.objects.create(
            image='test.jpeg',
            caption='Test caption',
            user=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_retrieve_post(self):
        """
        Test retrieving a post through the API.
        """
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['image'], 'http://testserver/test.jpeg')

    def test_update_post(self):
        """
        Test updating a post through the API.
        """
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        data = {
            'image': 'tes4.jpeg',
            'caption': 'Updated caption'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.caption, 'Updated caption')

    def test_delete_post(self):
        """
        Test deleting a post through the API.
        """
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())


class LikeListViewTests(APITestCase):
    """
    Test cases for the LikeListView.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.post = Post.objects.create(
            image='test.jpeg',
            caption='Test caption',
            user=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_create_like(self):
        """
        Test creating a like for a post through the API.
        """
        url = reverse('like-post', kwargs={'pk': self.post.pk})
        data = {'post_id': self.post.pk}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Like.objects.count(), 1)
        self.assertEqual(Like.objects.get().user, self.user)

    def test_create_like_invalid_post_id(self):
        """
        Test creating a like with an invalid post_id through the API.
        """
        url = reverse('like-post', kwargs={'pk': self.post.pk})
        data = {'post_id': 999}  # Invalid post_id
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Like.objects.count(), 0)
