import subprocess

# Spécifiez les chemins complets vers les scripts externes
Job01 = "calculette.py"
Job02 = "main.py"

# Utilisez subprocess pour exécuter les scripts externes
subprocess.run(["python3", Job01])
subprocess.run(["python3", Job02])
