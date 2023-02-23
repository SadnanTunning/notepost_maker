from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notepostapp', '0002_notepost_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notepost',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='notepost',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
