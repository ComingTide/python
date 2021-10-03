import os
import shutil

new_catalog = 'my_project_new\\templates'
for root, dirs, files in os.walk('my_project'):
    for file in files:
        if file.endswith(".html"):
            templates_catalog = os.path.basename(root)
            if not os.path.exists(os.path.join(new_catalog, templates_catalog)):
                os.makedirs(os.path.join(new_catalog, templates_catalog))
                shutil.copy(os.path.join(root, file), os.path.join(new_catalog, templates_catalog))
            else:
                shutil.copy(os.path.join(root, file), os.path.join(new_catalog, templates_catalog))