from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.


@admin.register(Candidate, Python, Result, Machine, Dscience, Dstructure, Fullstack, Front, Aws, Test, Category, Angular,
                Java, Php, Accenture, Tcs, Infosys, Mahindra, Capgemini)
class ViewAdmin(ImportExportActionModelAdmin):
    pass
