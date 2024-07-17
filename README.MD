# Intro
Author:     Armin Hünniger
Erstellt:   10.07.2024
Geändert:   12.07.2024 19:15 Uhr
     Was:   Web-Links ergänzt und Feinheiten noch bereinigt
git:        DTSL-20240711-v02

# Notwendige Grundbefehele aus dem vorherigen Tutorial v1

```Shell
python3 -m venv .env
source ./.env/bin/activate

python3 manage.py runserver
python3 manage.py shell
python3 manage.py createsuperuser

pip install -r requirements.text

python manage.py shell
- und in der Shell das Passwort zurücksetzen wenn z. B. Vergessen
my_user = DjangoTemplate-SQLite.objects.filter(email="info@itleichtgemacht.de").first()
my_user.set_password("NewPassword")
my_user.save()


```

## git Respository

```Shell
echo "# DjangoTemplate-SQLite" >> README.md
git init
git branch -M DTSL-20240711-v02
git remote add origin https://github.com/itleichtgemacht/DjangoTemplate-SQLite.git
git push -u origin DTSL-20240711-v02
```
# Intro
In dieser Version widmen wir uns den Templates im Django. Nur in sehr wenigen Ausnahmefällen kann auf die responsive Entwicklung verzichtet werden.
Daher schauten wir uns die Zusammenarbeit zwischen Templates und BootStrap 5.x genauer an.

# Installation
## Python
Hier ist keine Installation notwendig. Da BootStrap ein JavaScript Framework ist.

## index.html
Hier wird der Weg über CDN gezeigt. Im Projekt werden wir das BootStrap vom lokalen Static Verzeichnis laden.
Da ich diese Themenreihe noch fortführe und aus diesem Django Projekt ein PWA Anwendung machen möchte, ist dies notwendig.

```HTML
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
      crossorigin="anonymous" />

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    ...

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
      crossorigin="anonymous"
    ></script>
```





