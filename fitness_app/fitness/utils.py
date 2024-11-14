class FitnessMixin:

    def get_mixin_context(self, context, **kwargs):
        context['selected_menu'] = 'Workout'
        context.update(kwargs)
        return context