from locust import HttpUser, TaskSet, task, between
from locust.contrib.fasthttp import FastHttpUser

    
class WebsiteUser(FastHttpUser):
    """
    User class that does requests to the locust web server running on localhost,
    using the fast HTTP client
    """
    # some things you can configure on FastHttpUser
    # connection_timeout = 60.0
    # insecure = True
    # max_redirects = 5
    # max_retries = 1
    # network_timeout = 60.0
    min_wait = 0
    max_wait = 0
    
    @task
    def stats(self):
        self.client.get("/")
        # self.client.get("/stats/requests")


# http://127.0.0.1:8089

# or ...

# headless(no-web)
# locust -f locustfile.py --host=http://127.0.0.1 --headless -r 1000 -t 10s