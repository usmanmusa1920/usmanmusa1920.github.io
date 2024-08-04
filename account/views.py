from django.shortcuts import (
	render,
	redirect)
from .default import (
	general_context,
	Viz)


def landing(request):
	"""Landing page view"""
	if request.user.is_authenticated:
		# escape adding authenticated user as a visitor (if login), only other who visit without login
		pass
	else:
		# who so ever visit the site without being logged in, will be added as a visitor, into the database, (the below called class method handle the functionalities)
		Viz.vizFun()
	return redirect('blog:blog')


def error_400(request, exception):
	"""This view handle 400 (bad request) error"""
	err_msg = {"code": 400, "status": "bad request"}
	return render(request, 'account/error_page.html', context={'general_context': general_context(), 'err_msg': err_msg})


def error_403(request, exception):
	"""This view handle 403 (forbidden (permission denied)) error"""
	err_msg = {"code": 403, "status": "forbidden (permission denied)"}
	return render(request, 'account/error_page.html', context={'general_context': general_context(), 'err_msg': err_msg})


def error_404(request, exception):
	"""This view handle 404 (not found) error"""
	err_msg = {"code": 404, "status": "not found"}
	return render(request, 'account/error_page.html', context={'general_context': general_context(), 'err_msg': err_msg})


def error_500(request):
	"""This view handle 500 (internal server) error"""
	err_msg = {"code": 500, "status": "internal server"}
	return render(request, 'account/error_page.html', context={'general_context': general_context(), 'err_msg': err_msg})
