from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.db.models import Q


class DetailsQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
            Q(name__icontains=query) | 
            Q(phone__icontains=query) | 
            Q(email__icontains=query) | 
            Q(payment__icontains=query) | 
            Q(balance__icontains=query) | 
            Q(dept__icontains=query)
        )
        return self.filter(lookup)

class DetailsManager(models.Manager):
    def get_queryset(self):
        return DetailsQuerySet(self.model, using=self._db)
    
    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class CoursesRegistered(models.Model):
    # MECHANICAL_ENGINEERING_SCIENCE_1 = 'STATICS_MEC_101'
    # ELECTRICAL_ENGINEERING_SCIENCE_1 = 'EEC_115'
    # LOGIC_AND_LINEAR_ALGEBRA = 'LOGIC_MTH_111'
    # MATHEMATICS = 'MTH_101'
    # CALCULUS = 'CALCULUS_MTH_201'
    # TECHNICAL_DRAWING_1 ='TECHNICAL_DRAWING_MEC_102'
    # TECHNICAL_DRAWING_2 ='TECHNICAL_DRAWING_MEC_202'
    # TRIGONOMETRY = 'MTH_202'
    # ELECTRICAL_ENGINEERING_SCIENCE_2 = 'EEC_201'
    # STATISTICS = 'STAT_101'
    # # ELEMENTARY_PHYSICS = 'PHY_101'
    # # ATOMIC_AND_NUCLEAR_PHYSIS = 'PHY_102'
    # # INORGANIC_CHEMISTRY = 'CHEM_101'
    # # ORGANIC_CHEMISTRY = 'CHEM_102'
    # # BIOLOGY = 'BIO_101'
    # # PHARMACEUTICAL_CALCULATION = 'PMT_101'
    # # THERMODYNAMICS = 'THERMO_MEC_203'
    # # STRENGTH_OF_MATERIAL = 'STRENGTH_MEC_222'
    # # FLUID_MECHANICS = 'FLUID_CEC_101'
    # # STRUCTURAL_MECHANICS = 'STRUCTURAL_MECHANICS_CEC_101'

    # SUBJECTS = (
    #     ('MECHANICAL_ENGINEERING_SCIENCE_1', 'Mechanical Engineering Science 1'),
    #     ('ELECTRICAL_ENGINEERING_SCIENCE_1', 'Electrical Engineering Science 1'),
    #     ('LOGIC_AND_LINEAR_ALGEBRA', 'Logic and Linear Algebra'),
    #     ('MATHEMATICS', 'Mathematics'),
    #     ('CALCULUS', 'Calculus'),
    #     ('TECHNICAL_DRAWING_1', 'Technical Drawing 1'),
    #     ('TECHNICAL_DRAWING_2', 'Technical Drawing 2'),
    #     ('TRIGONOMETRY', 'Trigonometry'),
    #     ('ELECTRICAL_ENGINEERING_SCIENCE_2', 'Electrical Engineering Science 2'),
    #     ('STATISTICS', 'Statistics'),
    #     ('ELEMENTARY_PHYSICS', 'Elementary Physics'),
    #     ('ATOMIC_AND_NUCLEAR_PHYSIS', 'Atomic and Nuclear Physics'),
    #     ('INORGANIC_CHEMISTRY', 'Inorganic Chemistry'),
    #     ('ORGANIC_CHEMISTRY', 'Organic Chemistry'),
    #     ('BIOLOGY', 'Biology'),
    #     ('PHARMACEUTICAL_CALCULATION', 'Pharmaceutical Calculation'),
    #     ('THERMODYNAMICS', 'Thermodynamics'),
    #     ('STRENGTH_OF_MATERIAL', 'Strength of Material'),
    #     ('FLUID_MECHANICS', 'Fluid Mechanics'),
    #     ('STRUCTURAL_MECHANICS', 'Structural Mechanics'),
    # )

    subjects_registered = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.subjects_registered)
    
    class Meta:
        verbose_name_plural = 'CoursesRegistered'

class Schools(models.Model):
    SCHOOL_OF_ENGINEERING_TECHNOLOGY = 'SET'
    SCHOOL_OF_INDUSTRIAL_AND_APPLIED_STUDIES = 'SIAS'
    SCHOOL_OF_MANAGEMENT_TECHNOLOGY = 'SMT'

    SCH = [
        (SCHOOL_OF_ENGINEERING_TECHNOLOGY, 'School of Engineering Technology'),
        (SCHOOL_OF_INDUSTRIAL_AND_APPLIED_STUDIES, 'School of Industrial and Applied Science'),
        (SCHOOL_OF_MANAGEMENT_TECHNOLOGY, 'School of Management Technology'),
    ]

    sch = models.CharField(max_length=4, null=True, choices=SCH)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.sch
    
    class Meta:
        verbose_name_plural = 'Schools'

class Faculty(models.Model):
    ENGINEERING = 'ENGINEERING'
    SCIENCE = 'SCIENCE'
    BUSINESS = 'BUSINESS'

    FACULTY = [
        (ENGINEERING, 'Engineering'),
        (SCIENCE, 'Science'),
        (BUSINESS, 'Business'),
    ]

    fac = models.CharField(max_length=11, null=True, choices=FACULTY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.fac
    
    class Meta:
        verbose_name_plural = 'Faculties'


class Levels(models.Model):
    NATIONAL_DIPLOMA_1 = 'ND_1'
    NATIONAL_DIPLOMA_2 = 'ND_2'
    HIGHER_NATIONAL_DIPLOMA_1 = 'HND_1'
    HIGHER_NATIONAL_DIPLOMA_2 = 'HND_2'

    LEVEL = [
        (NATIONAL_DIPLOMA_1, 'National Diploma 1'),
        (NATIONAL_DIPLOMA_2, 'National Diploma 2'),
        (HIGHER_NATIONAL_DIPLOMA_1, 'Higher National Diploma 1'),
        (HIGHER_NATIONAL_DIPLOMA_2, 'Higher National Diploma 2'),
    ]

    lev = models.CharField(max_length=5, null=True, choices=LEVEL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.lev
    
    class Meta:
        verbose_name_plural = 'Levels'


class Details(models.Model):
    MECHANICAL_ENGINEERING = 'ME'
    ELECTRICAL_ENGINEERING = 'EE'
    CIVIL_ENGINEERING = 'CE'
    AGRICULTURAL_ENGINEERING = 'AE'
    CHEMICAL_ENGINEERING = 'CHE'
    COMPUTER_SCIENCE = 'CS'
    COMPUTER_ENGINEERING = 'CTE'
    SCIENCE_LABORATORY_TECHNOLOGY = 'SLT'
    FOOD_SCIENCE_TECHNOLOGY = 'FST'
    PHARMACEUTICAL_TECHNOLOGY = 'PT'
    DISPENSARY_AND_OPTICIARY = 'DOP'

    DEPARTMENTS = [
        (MECHANICAL_ENGINEERING, 'Mechanical Engineering'),
        (ELECTRICAL_ENGINEERING, 'Electrical Engineering'),
        (CIVIL_ENGINEERING, 'Civil Engineering'),
        (AGRICULTURAL_ENGINEERING, 'Agricultural Engineering'),
        (CHEMICAL_ENGINEERING, 'Chemical Engineering'),
        (COMPUTER_SCIENCE, 'Computer Science'),
        (COMPUTER_ENGINEERING, 'Computer Engineering'),
        (SCIENCE_LABORATORY_TECHNOLOGY, 'Science Laboratory Technology'),
        (FOOD_SCIENCE_TECHNOLOGY, 'Food Science Technology'),
        (PHARMACEUTICAL_TECHNOLOGY, 'Pharmaceutical Technology'),
        (DISPENSARY_AND_OPTICIARY, 'Dispensary and Opticiary'),
    ]

    courses_registered = models.ManyToManyField(CoursesRegistered)
    school = models.ForeignKey(Schools, null=True, on_delete=models.SET_NULL)
    level = models.ForeignKey(Levels, null=True, on_delete=models.SET_NULL)
    faculty = models.ForeignKey(Faculty, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    payment = models.FloatField(null=True)
    balance = models.FloatField(null=True)
    total = models.FloatField(null=True)
    dept = models.CharField(max_length=3, null=True, choices=DEPARTMENTS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(default="profile-pic.jpg", null=True, blank=True)

    objects = DetailsManager()

    class Meta:
        ordering = ['-date_created']
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Details'



class Profile(models.Model):
    detail = models.ForeignKey(Details, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    

    def __str__(self):
        return self.first_name



