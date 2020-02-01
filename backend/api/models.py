from django.db import models


class FindClosingBracket(models.Model):
    string = models.TextField(blank=False, null=False)
    index = models.IntegerField(blank=False, null=False)
    closing_position_info = models.TextField(blank=True, null=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return f'{self.string}'
