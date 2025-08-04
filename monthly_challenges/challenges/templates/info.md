app_name/templates/app_name/template.html


this structure because Django under the hood merges all template folders from all apps into one big template folder

if multiple apps have same template name, this will create ambiguity

app_name/template.html will help identify uniquely in views

app_name/templates is the set structure for 'APP_DIRS': True auto template detection feature to work


Filter in DTL : Modify how content displays/looks
Tags in DTL : To control logic 