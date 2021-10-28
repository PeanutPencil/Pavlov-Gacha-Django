# 0 9,21 * * * python /home/reimus/workspace/Pavlov-Gacha-Django/pgserv/libs/rest>

from django.conf import settings

from users.models import User

for user in User.objects.all():
    user.claims = settings.MAX_CLAIMS
