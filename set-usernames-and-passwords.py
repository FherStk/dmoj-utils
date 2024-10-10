import csv, os

DMOJ_DIR = "/etc/dmoj"
filename = 'group.csv'

def main():	
    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        next(datareader, None)  # skip the headers
        for row in datareader:            
            setup(row[2], row[3], row[4])

def setup(email, username, password):
	command = f"from django.contrib.auth.models import User; u = User.objects.get(email='{email}'); u.username = '{username}'; u.set_password('{password}'); u.save();"
	os.system(f". {DMOJ_DIR}/dmojsite/bin/activate && echo \"{command}\" | python3 {DMOJ_DIR}/site/manage.py shell")

if __name__ == "__main__":
	main()