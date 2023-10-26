from auto.models import Auto, Make


def run():
    Auto.objects.all().delete()
    Make.objects.all().delete()