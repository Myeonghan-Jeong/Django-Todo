from django.db import models


class SurveyResponse(models.Model):
    name = models.TextField(null=True, blank=True)
    step1_data = models.JSONField(null=True, blank=True)
    step2_data = models.JSONField(null=True, blank=True)
    step3_data = models.JSONField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response by {self.user if self.user else 'Anonymous'} at {self.submitted_at}"
