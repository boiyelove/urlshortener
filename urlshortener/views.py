from django.shortcuts import render
from django.views.generic import RedirectView, TemplateView, ListView
from .models import ShortLink, ShortLinkVisit
from .utils import get_client_ip, Crawler

# Create your views here.


class ShortlinkView(TemplateView):
	template_name = 'urlshortener/shortlinks.html'

	def post(self, request, *args, **kwargs):
		link = request.POST.get('link')
		author_ip = get_client_ip(request)
		try:
			short_link = ShortLink.objects.get(link = link)
		except:
			title = Crawler(link).get_title()
			description = Crawler(link).get_description()
			short_link = ShortLink.objects.create(link = link, author_ip= author_ip, title=title, description=description)
		context = {
		'short_link': short_link
		}
		return render(request, self.template_name, context)

class ShortLinkRedirect(RedirectView):

	def get_redirect_url(self, *args, **kwargs):
		shortcode = kwargs.get('shortcode')
		shortlink = ShortLink.get_id(shortcode)
		shortlinkvisit, created = ShortLinkVisit.objects.get_or_create(shortlink = shortlink,
			visitor_ip = get_client_ip(self.request) )
		if not created:
			shortlinkvisit.views  += 1
			shortlinkvisit.save()
		return shortlink.link


class ShortLinkListView(ListView):
	model =  ShortLink
	template_name = 'urlshortener/shortlinklist.html'
	context_object_name = 'shortlink_list'