import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ser', '0002_category_quote_delete_picture_delete_product_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Quote',
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(serialize=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ser.category')),
            ],
        ),
    ]
