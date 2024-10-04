
def before_all(context):
    context.driver_path = context.config.userdata.get('driver_path')


def before_feature(context, feature):
    ...


def before_scenario(context, scenario):
    ...


def before_step(context, step):
    ...


def after_step(context, step):
    ...


def after_scenario(context, scenario):
    ...


def after_feature(context, feature):
    ...


def after_all(context):
    ...
