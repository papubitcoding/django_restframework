from rest_framework.throttling import UserRateThrottle

class DemoRateThrottle(UserRateThrottle):
    scope = 'demo'
    