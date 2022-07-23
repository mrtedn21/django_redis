from django.core.management.base import BaseCommand

from user_selection.models import User


class Command(BaseCommand):
    help = 'Create users of three types'

    def handle(self, *args, **options):
        user = User.objects.create_superuser(
            username='admin',
            email='admin@gmail.com',
            password='123',
            offer=True,
            role_choice=User.ADMIN,
        )
        user.avatar.save('test1.jpg', open('/app/default_images/admin.jpg', 'rb'))
        user.save()

        user = User.objects.create_user(
            username='user',
            email='user@gmail.com',
            password='123',
            offer=True,
            role_choice=User.USERNAME_FIELD,
        )
        user.avatar.save('test2.jpg', open('/app/default_images/user.png', 'rb'))
        user.save()

        user = User.objects.create_user(
            username='manager',
            email='manager@gmail.com',
            password='123',
            offer=True,
            role_choice=User.MANAGER,
        )
        user.avatar.save('test3.jpg', open('/app/default_images/manager.jpg', 'rb'))
        user.save()

