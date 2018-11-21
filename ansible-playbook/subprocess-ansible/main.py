import subprocess
import os

cmd = "ansible-playbook -i inventory/inventory testplaybook.yml"
# my_env = os.environ.copy()
# my_env["TOKEN"] = _get_token()
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
output, error = process.communicate()

print(output)