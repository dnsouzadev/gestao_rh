const utilizouHoraExtra = (id) => {
    let token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function(response) {
            console.log('sucesso');
            $("#mensagem").text('Hora extra utilizada com sucesso!')
        }
    });
}