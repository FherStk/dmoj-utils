import os

DMOJ_DIR = "/etc/dmoj"

def main():		
	add_language(21)    # Java (latest installed)	
	add_language(24)    # Java 11
	add_language(23)    # Java 17
	add_language(9)     # Java8	
	add_language(20)    # CSharp v6 (Mono)
	add_language(22)    # GO

def add_language(id):
	command = f"from django.utils import timezone; from django.contrib.auth.models import User; from judge.models import Problem, Judge, Language; l = Language.objects.get(id={id}); for s in Problem.objects.all():exec('s.allowed_languages.add(l); s.save()')"
	os.system(f". {DMOJ_DIR}/dmojsite/bin/activate && echo \"{command}\" | python3 {DMOJ_DIR}/site/manage.py shell")

if __name__ == "__main__":
	main()