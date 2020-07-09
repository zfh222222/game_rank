from django.db import models
#create models
class Game(models.Model):
    g_client=models.CharField(max_length=24)
    g_score=models.IntegerField()
    class Meta:
        db_table="games"
