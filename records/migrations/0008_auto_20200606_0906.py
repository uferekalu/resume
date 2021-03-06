# Generated by Django 3.0.4 on 2020-06-06 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0007_auto_20200606_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesregistered',
            name='subjects_registered',
            field=models.CharField(choices=[('STATICS_MEC_101', 'Mechanical Engineering Science 1'), ('EEC_115', 'Electrical Engineering Science 1'), ('LOGIC_MTH_111', 'Logic and Linear Algebra'), ('MTH_101', 'Mathematics'), ('CALCULUS_MTH_201', 'Calculus'), ('TECHNICAL_DRAWING_MEC_102', 'Technical Drawing 1'), ('TECHNICAL_DRAWING_MEC_202', 'Technical Drawing 2'), ('MTH_202', 'Trigonometry'), ('EEC_201', 'Electrical Engineering Science 2'), ('STAT_101', 'Statistics'), ('PHY_101', 'Elementary Physics'), ('PHY_102', 'Atomic and Nuclear Physics'), ('CHEM_101', 'Inorganic Chemistry'), ('CHEM_102', 'Organic Chemistry'), ('BIO_101', 'Biology'), ('PMT_101', 'Pharmaceutical Calculation'), ('THERMO_MEC_203', 'Thermodynamics'), ('STRENGTH_MEC_222', 'Strength of Material'), ('FLUID_CEC_101', 'Fluid Mechanics'), ('STRUCTURAL_MECHANICS_CEC_101', 'Structural Mechanics')], max_length=28, null=True),
        ),
    ]
