const sleep = ms => new Promise(r => setTimeout(r, ms));

const utilizouHoraExtra = (id) => {
    let token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function(response) {
            console.log(response);
            $("#mensagem").text('Hora extra utilizada com sucesso!')
            sleep(4000).then(() => {
                $("#mensagem").hide();
            });
            $("#horas_atualizadas").text(response.horas)
        }
    });
}

