import eadrax.data
import eadrax.user.login

import wipup.tools
import wipup.repositories.user

from wipup.views.static.homepage import Homepage
from eadrax.errors import AuthorisationError

def homepage(request):
    view = Homepage()

    if request.method == 'POST':
        view.was_told_stuff = True
        view.stuff = request.form['information']

    usecase = eadrax.user.login.load(
        user = eadrax.data.User(),
        repository = wipup.repositories.user.Login(),
        authenticator = wipup.tools.Authenticator(request),
        encryptor = wipup.tools.Encryptor()
    )

    try:
        usecase.run()
    except AuthorisationError:
        pass

    return view.render('static/homepage')
