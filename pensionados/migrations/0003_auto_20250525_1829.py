from django.db import migrations

def add_unique_acreedor(apps, schema_editor):
    Pensionado = apps.get_model('pensionados', 'Pensionado')
    
    # Eliminar duplicados dejando solo el primero (por acreedor)
    seen = set()
    for p in Pensionado.objects.all():
        if p.acreedor in seen:
            p.delete()
        else:
            seen.add(p.acreedor)

    # Ahora sí, añadir unique=True
    field = Pensionado._meta.get_field('acreedor')
    field.unique = True

class Migration(migrations.Migration):

    dependencies = [
        ('pensionados', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_unique_acreedor),
    ]