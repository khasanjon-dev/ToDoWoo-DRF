from django.contrib.auth.models import User
from django.db.models import Model, CharField, TextField, BooleanField, DateTimeField, ForeignKey, CASCADE


class ToDoWoo(Model):
    title = CharField(max_length=300)
    description = TextField()
    # bool
    is_important = BooleanField(default=False)
    is_complete = BooleanField(default=False)
    # date
    created_at = DateTimeField(auto_now_add=True, blank=True)
    updated_at = DateTimeField(auto_now=True, null=True, blank=True)
    completed_at = DateTimeField(null=True, blank=True)
    # relationship
    author = ForeignKey(User, CASCADE, 'todos')
