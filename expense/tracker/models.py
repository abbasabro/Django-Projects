from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4 , primary_key=True,editable=False , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updatad_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Transaction(BaseModel):
    description = models.CharField(max_length=100)
    amount = models.FloatField(default=0)
    
    def isNegative(self):
        return self.amount < 0
    
