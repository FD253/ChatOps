from mongoengine import Document, EmbeddedDocument, fields


class Answer(EmbeddedDocument):
    letter = fields.StringField(required=True, max_length=1)
    answer = fields.StringField(required=True, max_length=50)
    active = fields.BooleanField(default=True)


class Question(EmbeddedDocument):
    related_theme = fields.StringField(required=True, max_length=20)
    number = fields.IntField(required=True)
    question = fields.StringField(required=True, max_length=100)
    answers = fields.ListField(
        fields.EmbeddedDocumentField(Answer, required=True), required=True
    )


class Questionnaire(Document):
    questionnaire = fields.StringField(required=False, max_length=50)
    questions = fields.ListField(
        fields.EmbeddedDocumentField(Question, required=True), required=True
    )


class AnsweredQuestion(EmbeddedDocument):
    question_number = fields.IntField(required=True)
    answer_letter = fields.StringField(required=True, max_length=1)


class User(Document):
    user = fields.StringField(required=True, max_length=25, unique=True)
    charge_code = fields.StringField(max_length=6, required=True)


class Petition(Document):
    user = fields.ReferenceField(User, required=True)
    questionnaire = fields.ListField(
        fields.EmbeddedDocumentField(AnsweredQuestion, required=True)
    )


class AMI(Document):
    ami = fields.StringField(required=True, max_length=8, min_length=8)
    description = fields.StringField(required=True, max_length=50)
    summary = fields.StringField(required=True, max_length=15)
