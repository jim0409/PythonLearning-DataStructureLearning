from ansible_subprocess import run_playbook


status, stdout, stderr = run_playbook('testplaybook.yml', 'inventory/inventory')

print("the return status: {}".format(status))

print("the return stdout: {}".format(stdout))

print("the return stderr: {}".format(stderr))