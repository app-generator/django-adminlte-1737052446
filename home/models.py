# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    user = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Lga(models.Model):

    #__Lga_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Lga_FIELDS__END

    class Meta:
        verbose_name        = _("Lga")
        verbose_name_plural = _("Lga")


class State(models.Model):

    #__State_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__State_FIELDS__END

    class Meta:
        verbose_name        = _("State")
        verbose_name_plural = _("State")


class Nationality(models.Model):

    #__Nationality_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Nationality_FIELDS__END

    class Meta:
        verbose_name        = _("Nationality")
        verbose_name_plural = _("Nationality")


class Student_Information(models.Model):

    #__Student_Information_FIELDS__
    first_name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    other_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.BooleanField()
    date_of_birth = models.BooleanField()
    phone = models.IntegerField(null=True, blank=True)
    capture_image = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    matrix_no = models.CharField(max_length=255, null=True, blank=True)
    enrollment_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Student_Information_FIELDS__END

    class Meta:
        verbose_name        = _("Student_Information")
        verbose_name_plural = _("Student_Information")


class Course(models.Model):

    #__Course_FIELDS__
    course_code = models.CharField(max_length=255, null=True, blank=True)
    course_name = models.CharField(max_length=255, null=True, blank=True)
    credit = models.IntegerField(null=True, blank=True)
    course_description = models.CharField(max_length=255, null=True, blank=True)

    #__Course_FIELDS__END

    class Meta:
        verbose_name        = _("Course")
        verbose_name_plural = _("Course")


class Enrollment(models.Model):

    #__Enrollment_FIELDS__
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Enrollment_FIELDS__END

    class Meta:
        verbose_name        = _("Enrollment")
        verbose_name_plural = _("Enrollment")


class Result(models.Model):

    #__Result_FIELDS__
    enrolment = models.ForeignKey(enrollment, on_delete=models.CASCADE)
    semester = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=255, null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)

    #__Result_FIELDS__END

    class Meta:
        verbose_name        = _("Result")
        verbose_name_plural = _("Result")


class Feespayment(models.Model):

    #__Feespayment_FIELDS__
    amount = models.IntegerField(null=True, blank=True)

    #__Feespayment_FIELDS__END

    class Meta:
        verbose_name        = _("Feespayment")
        verbose_name_plural = _("Feespayment")


class Chatroom(models.Model):

    #__Chatroom_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    participants = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Chatroom_FIELDS__END

    class Meta:
        verbose_name        = _("Chatroom")
        verbose_name_plural = _("Chatroom")


class Message(models.Model):

    #__Message_FIELDS__
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.CharField(max_length=255, null=True, blank=True)

    #__Message_FIELDS__END

    class Meta:
        verbose_name        = _("Message")
        verbose_name_plural = _("Message")



#__MODELS__END
