from django.db import models


# Create your models here.
class Policy(models.Model):

    CS_CHOICES = [
        ('MS', 'M.S.'),
        ('MEng', 'M.Eng.'),
        ('PhD', 'Ph.D.'),
    ]
    Program = models.CharField(max_length=12, choices=CS_CHOICES, default='MS')

    Breadth_Requirement = models.TextField(blank=True, verbose_name='Breadth Requirement')
    Depth_Requirement = models.TextField(blank=True, verbose_name='Depth Requirement')
    Theoretical_Computer_Science = models.CharField(blank=True, max_length=120, verbose_name='Theoretical Computer Science')
    Blanket_Credits = models.TextField(blank=True, verbose_name='Blanket Credits')
    Thesis_or_Project = models.TextField(blank=True, verbose_name='Thesis or Project')
    Responsible_Conduct_of_Research_Training = models.TextField(blank=True,
                                                                verbose_name='Responsible Conduct of Research Training')
    EECS_Colloquium = models.TextField(blank=True, verbose_name='EECS Colloquium')
    Total_Graduate_Credits = models.CharField(blank=True, max_length=120, verbose_name='Total Graduate Credits')
    Basic_Requirement = models.TextField(blank=True, verbose_name='Basic Requirement')

    class Meta:
        verbose_name = 'requirement'
        verbose_name_plural = 'CS_policy'



