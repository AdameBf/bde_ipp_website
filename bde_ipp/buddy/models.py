from django.db import models
from django.db.models import BooleanField, CharField, EmailField, IntegerField

from multiselectfield import MultiSelectField

# Create your models here.

YEAR_CHOICES = (
    ('M1', 'Master 1'),
    ('M2', 'Master 2'),
    ('PhD', 'Doctorate')
)

STUDY_CHOICES = (
    ('advanced_materials', 'Advanced Materials'),
    ('life_sciences', 'Life Sciences'),
    ('chemistry_and_interfacts', 'Chemistry and Interfacts'),
    ('computer_science', 'Computer Science'),
    ('data_and_artificial_intelligence', 'Data and Artificial Intelligence'),
    ('economics', 'Economics'),
    ('electrical_engineering', 'Electrical Engineering'),
    ('energy_for_climate', 'Energy for Climate'),
    ('mathematics', 'Mathematics'),
    ('mechanics', 'Mechanics'),
    ('physics', 'Physics'),
    ('quantum_science_and_technologies', 'Quantum Science and Technologies'),
)

GENDER_CHOICES = (
    ('unknown', 'I\'d rather not say'),
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Non binary / Third gender')
)

GENDER_MATCHING_CHOICES = (
    ('no_preference', 'I don\'t have any preference.'),
    ('same', 'I prefer to match with the same gender.')
)

JUNG_PERSONALITY_TEST_CHOICES = (
    ('intj', 'Architect (INTJ)'),
    ('intp', 'Logician (INTP)'),
    ('entj', 'Commander (ENTJ)'),
    ('entp', 'Debater (ENTP)'),
    ('infj', 'Advocate (INFJ)'),
    ('infp', 'Mediator (INFP)'),
    ('enfj', 'Protagonist (ENFJ)'),
    ('enfp', 'Campaigner (ENFP)'),
    ('istj', 'Logistician (ISTJ)'),
    ('isfj', 'Defender (ISFJ)'),
    ('estj', 'Executive (ESTJ)'),
    ('esfj', 'Consul (ESFJ)'),
    ('istp', 'Virtuoso (ISTP)'),
    ('isfp', 'Adventurer (ISFP)'),
    ('estp', 'Entrepreneur (ESTP)'),
    ('esfp', 'Entertainer (ESFP)'),
)


# Be careful about how to proceed, what kind of relashionship between models ? etc.
class Buddlunteer(models.Model):
    data_privacy = BooleanField()
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    email = EmailField(unique=True)
    level = CharField(choices=YEAR_CHOICES, max_length=50)
    study = MultiSelectField(choices=STUDY_CHOICES)
    nb_buddies = IntegerField()
    gender = CharField(choices=GENDER_CHOICES, max_length=50)
    gender_matching = CharField(choices=GENDER_MATCHING_CHOICES, max_length=50)
    # Other fields such as :
    # "What would you do on Sunday evening",
    # "What do you have the most knowledge of ?"
    # "Favorite movie type"
    # "Living on campus or outside campus" ?
    jung_personality_test = CharField(choices=JUNG_PERSONALITY_TEST_CHOICES, max_length=50, blank=True)
    has_matched = BooleanField(default=False)  # Might not be needed


class Buddy(models.Model):
    data_privacy = BooleanField()
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    email = EmailField(unique=True)
    level = CharField(choices=YEAR_CHOICES, max_length=50)
    study = MultiSelectField(choices=STUDY_CHOICES)
    gender = CharField(choices=GENDER_CHOICES, max_length=50)
    gender_matching = CharField(choices=GENDER_MATCHING_CHOICES, max_length=50)
    # Other fields such as :
    # "What would you do on Sunday evening",
    # "What do you have the most knowledge of ?"
    # "Favorite movie type"
    # "Living on campus or outside campus" ?
    jung_personality_test = CharField(choices=JUNG_PERSONALITY_TEST_CHOICES, max_length=50, blank=True)
    associated_buddlunteer = models.ForeignKey(Buddlunteer, on_delete=models.CASCADE)  # One to many relationship
