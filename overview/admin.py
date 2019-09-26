from django.contrib import admin
from movies_app.models import Movies
from series_app.models import Series
from series_episodes_app.models import Series_Episodes
from documentaries_app.models import Documentaries
from documentaries_episodes_app.models import Documentaries_Episodes

admin.site.register(Movies)
admin.site.register(Series)
admin.site.register(Series_Episodes)
admin.site.register(Documentaries)
admin.site.register(Documentaries_Episodes)