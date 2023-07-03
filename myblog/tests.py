from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostUpdateTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.post = Post.objects.create(
            h1='Test Heading',
            title='Test Title',
            url='test-url',
            description='Test Description',
            content='Test Content',
            image='test.jpg',
            author = self.user,
            tag='test tag'
        )

    def test_post_update(self):
        # Определяем URL-адрес редактирования поста блога, замените 'post_update' на ваш фактический URL-шаблон
        url = reverse('post-update', args=[self.post.id])

        updated_data = {
            'h1': 'Updated Heading',
            'title': 'Updated Title',
            'url': 'updated-url',
            'description': 'Updated Description',
            'content': 'Updated Content',
            'tag': 'updated tag'
        }

        response = self.client.post(url, data=updated_data)

        # Проверяем, что код ответа равен 302 (перенаправление)
        self.assertEqual(response.status_code, 302)

        # Обновляем экземпляр объекта из базы данных
        self.post.refresh_from_db()

        # Проверяем, что поля объекта модели соответствуют обновленным данным
        self.assertEqual(self.post.h1, updated_data['h1'])
        self.assertEqual(self.post.title, updated_data['title'])
        self.assertEqual(self.post.url, updated_data['url'])
        self.assertEqual(self.post.description, updated_data['description'])
        self.assertEqual(self.post.content, updated_data['content'])
        self.assertEqual(self.post.tag, updated_data['tag'])


class PostDeleteTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.post = Post.objects.create(
            h1='Test Heading',
            title='Test Title',
            url='test-url',
            description='Test Description',
            content='Test Content',
            image='test.jpg',
            author = self.user,
            tag='test tag'
        )

    def test_post_delete(self):
      # Определяем URL-адрес удаления поста блога, замените 'post_delete' на ваш фактический URL-шаблон
      url = reverse('post-delete', args=[self.post.id])
      response = self.client.post(url)
      # Проверяем, что код ответа равен 302 (перенаправление)
      self.assertEqual(response.status_code, 302)
      # Проверяем, что пост был удален из базы данных
      self.assertFalse(Post.objects.filter(id=self.post.id).exists())