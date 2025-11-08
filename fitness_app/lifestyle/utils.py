
class DataMixin:

    def get_mixin_context(self, context, **kwargs):
        context['selected_menu'] = 'Life Style'
        context.update(kwargs)
        return context

