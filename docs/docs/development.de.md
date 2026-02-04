# Entwicklung starten

Erstellen und aktivieren Sie eine Umgebung, indem Sie den folgenden Befehl ausführen:

```pyenv virtualenv 3.14.2 vatvalidation-venv```

```pyenv activate vatvalidation-venv```

Installieren Sie die erforderlichen Abhängigkeiten

```pip install -r src/requirements.txt```
```pip install -r icons/requirements.txt```
```pip install -r docs/requirements.txt```

Wenn Sie einige Änderungen an der Benutzeroberfläche vornehmen möchten, laden Sie den neuesten wxFormBuilder von der [wxFormBuilder Homepage] (https://github.com/wxFormBuilder/wxFormBuilder) herunter und installieren Sie ihn.

Sie können die VATValidation starten, indem Sie den folgenden Befehl ausführen:

```cd src && python vatvalidation.py```