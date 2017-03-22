'''
from django.db import models

class Questionnaire(models.Model):
    description = models.TextField(null=True, blank=True)


class Question(models.Model):
    questionnaires = models.ManyToManyField(Questionnaire)
    question = models.CharField(max_length=100, null=False)

    class Meta:
        unique_together = (("questionnaire", "question"),)


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="inputs",
                                 on_delete=models.CASCADE)
    letter = models.CharField(max_length=1,  null=False)
    answer = models.CharField(max_length=100, null=False)

    class Meta:
        unique_together = (("question", "letter"),)
'''

from mongoengine import Document, EmbeddedDocument, fields


class Answer(EmbeddedDocument):
    letter = fields.StringField(required=True, max_length=1)
    answer = fields.StringField(required=True, max_length=50)


class Question(EmbeddedDocument):
    number = fields.IntField(required=True)
    question = fields.StringField(required=True, max_length=100)
    answers = fields.ListField(
        fields.EmbeddedDocumentField(Answer, required=True), required=True
    )


class Questionnaire(Document):
    questionnaire = fields.StringField(required=True, max_length=50)
    questions = fields.ListField(
        fields.EmbeddedDocumentField(Question, required=True), required=True
    )


class AnsweredQuestion(EmbeddedDocument):
    question_number = fields.IntField(required=True)
    answer_letter = fields.StringField(required=True, max_length=1)


class Petition(Document):
    user = fields.StringField(required=True, max_length=25)
    charge_code = fields.StringField(required=True, max_length=25)
    questionnaire = fields.ListField(
        fields.EmbeddedDocumentField(AnsweredQuestion, required=True)
    )
