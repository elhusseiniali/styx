from flask_admin.model import typefmt  # type: ignore

# Show null values instead of empty strings.
MY_DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
MY_DEFAULT_FORMATTERS.update({type(None): typefmt.null_formatter})
