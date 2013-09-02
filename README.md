# djangox-route
[Django said tying URLs to Python functions is Bad thing.](https://docs.djangoproject.com/en/dev/misc/design-philosophies/#id8) But registering every view functions in urls.py is not so cool. Even django admin uses autodiscover, what's the reason we don't use autodiscover for normal view functions?

## Install

	pip install djangox-route

## discover_controllers
Register all controller functions to urlpatterns.

    url(r'', discover_controllers(your_app.controllers))

Recommended controller directory structure is like this:

* your_project
  * your_app
    * controllers
      * \__init__.py
      * hello.py
  * your_project
    * urls.py
    
\__init__.py

	def index(request):
		...	

hello.py

	def index(request):
		...
		
	def world(request):
		...

	def show(request, resource_id):
		...		

	def great(request, resource_id):
		...

Now urls will be dispatched like these:

* / -> controllers.__init__.index(request)
* /hello -> controllers.hello.index(request)
* /hello/great -> controllers.hello.great(request)
* /hello/5 -> controllers.hello.show(request, 5)
* /hello/5/world -> controllers.hello.world(request, 5)

You can also use string of package name.

    url(r'', discover_controllers('your_app.controllers'))
    
Other features of django url system are available, too.

    url(r'api/', discover_controllers(your_app.controllers))

url above will dispatch /api/hello to hello.index(request)


## Notes
* `discover_controllers` doesn't intercept django's url dispatching. It just registers every controllers to urlconf. So every decorators for django views works fine.

* I don't like the naming, `views`. Every other web frameworks are consist of MVC(model, view, controller), but only django uses the concept of model-view-template. The view of MVC and the view of django are different. It's more like controller in MVC, but not exactly same. Django intend template should be dull, and views should supply all data template needed. View in django are abstract layer for view in MVC. However I didn't find any advantages in django's approach, so I prefer MVC. This is why I name the autodiscover function as `discover_controllers`, not `discover_views`.

* As I said above, I don't like powerless template engine in django. I think template should have full functionality as programming language. Therefore I recommend mako rather than django template. With [djangox-mako](https://github.com/youngrok/djangox-mako) you can use mako easily.