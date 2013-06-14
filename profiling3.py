def profile(func):
        import cProfile as profile
        from io import StringIO
        import pstats
        import functools

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
                pr = profile.Profile()
                pr.enable()

                ret = func(*args, **kwargs)

                pr.disable()
                s = StringIO()
                ps = pstats.Stats(pr)
                ps.sort_stats('time')
                ps.print_stats(20)

                ps.sort_stats('cumulative')
                ps.print_stats(10)

                return ret

        return wrapper
