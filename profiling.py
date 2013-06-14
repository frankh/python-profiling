def profile(func):
	import cProfile as profile
	from StringIO import StringIO
	import pstats
	import functools

	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		pr = profile.Profile()
		pr.enable()
		
		ret = func(*args, **kwargs)

		pr.disable()
		s = StringIO()
		ps = pstats.Stats(pr, stream=s)
		ps.sort_stats('time')
		ps.print_stats(30)

		ps.sort_stats('cumulative')
		ps.print_stats(10)

		s.seek(0)
		for l in s.readlines():
			print '@@@',l,

		return ret

	return wrapper
