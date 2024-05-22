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
            // console.log(response);
            sleep(1000).then(() => {
                $("#mensagem").hide();
                window.location.reload();
            });
            let horas = response.horas;
            if (horas == 0) {
                $("#horas_atualizadas").text('0 hora extra disponível')
            } else {
                $("#horas_atualizadas").text(response.horas + ' horas disponíveis')
            }
        }
    });
}

