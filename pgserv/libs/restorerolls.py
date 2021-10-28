# 0 * * * * python /home/reimus/workspace/Pavlov-Gacha-Django/pgserv/libs/restorerolls.py

from django.conf import settings

from users.models import User

for user in User.objects.all():
    user.rolls = settings.MAX_ROLLS
