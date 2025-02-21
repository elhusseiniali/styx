from flask_admin.contrib.sqla import ModelView  # type: ignore

from . import MY_DEFAULT_FORMATTERS


class UserView(ModelView):
    form_columns = (
        "username",
        "email",
        "password",
    )
    column_editable_list = ("username", "email")
    column_searchable_list = ("username", "email")
    column_type_formatters = MY_DEFAULT_FORMATTERS
