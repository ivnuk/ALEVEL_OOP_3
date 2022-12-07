try:
    # some code which may raise exception
    pass
except KeyError as err:
    # what should be done in case of KeyError
    pass
except (TypeError, ValueError, ZeroDivisionError) as err:
    # Multiple exception handling for similar behavior
    pass
except Exception as exc:
    # Broad exception handling, can be used in the case when
    # developer is not sure, what exception can be raised.
    # NOT RECOMMENDED.
    pass
else:
    # The code will be executed in the case if no exception was raised. OPTIONAL
    pass
finally:
    # This code will be executed in any case after exception handling or
    # if exception was not raised. OPTIONAL
    pass
