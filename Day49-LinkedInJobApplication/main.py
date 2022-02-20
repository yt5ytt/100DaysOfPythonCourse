import time
from Classes.linkedInLogin import LinkedInLogin

login = LinkedInLogin()
time.sleep(5)
login.get_python_jobs()
time.sleep(5)

for link in login.get_job_links():
    time.sleep(5)
    link.click()
    time.sleep(5)
    login.save_button()