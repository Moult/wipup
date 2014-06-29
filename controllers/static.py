import eadrax.data
import eadrax.user.login.usecase

import wipup.tools
import wipup.repositories.user

from wipup.views.static.homepage import Homepage

def homepage(request):
    view = Homepage()

    if request.method == 'POST':
        view.was_told_stuff = True
        view.stuff = request.form['information']

    view.was_told_stuff = True
    view.stuff = 'foo'

    usecase = eadrax.user.login.usecase.load(
        user = eadrax.data.User(),
        repository = wipup.repositories.user.Login(),
        authenticator = wipup.tools.Authenticator(),
        encryptor = wipup.tools.Encryptor()
    )

    usecase.interact()

    return view.render('static/homepage')
