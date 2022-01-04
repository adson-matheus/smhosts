function ConfirmarDeleteHost(valor) {
    swalWithBootstrapButtons = swal.mixin({
        confirmButtonClass: 'btn btn-danger',
        cancelButtonClass: 'btn btn-success',
        confirmButtonColor: '#d33',
        cancelButtonColor: '#17a2b8',
        buttonsStyling: true,
    })
    swalWithBootstrapButtons({
        title: 'Você tem certeza?',
        text: "Você não poderá reverter isso!",
        type: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sim, Deletar!',
        cancelButtonText: 'Não, Cancelar!',
        reverseButtons: true
    }).then((result) => {
        if (result.value) {
            swalWithBootstrapButtons(
                'Deletado!',
                'REGISTRO DELETADO COM SUCESSO!',
                'success'
            )
            var url;
            var urlAtual = window.location.href;
            var urlAtual = urlAtual.split('/');
            if (urlAtual.length > 6) {
                url = '../../DeletarHost/' + valor;
            } else {
                url = '../DeletarHost/' + valor;
            }
            location.href = url;
        } else if (
            result.dismiss === swal.DismissReason.cancel
        ) {
            swalWithBootstrapButtons(
                'Cancelado!',
                'O REGISTRO NÃO FOI DELETADO!',
                'error'
            )
        }
    })
}

function ConfirmarDeletePorta(valor) {
    const swalWithBootstrapButtons = Swal.mixin({
        confirmButtonClass: 'btn btn-danger',
        cancelButtonClass: 'btn btn-success',
        confirmButtonColor: '#d33',
        cancelButtonColor: '#17a2b8',
        buttonsStyling: true,
    })
    swalWithBootstrapButtons({
        title: 'Você tem certeza?',
        text: "Você não poderá reverter isso!",
        type: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sim, Deletar!',
        cancelButtonText: 'Não, Cancelar!',
        reverseButtons: true
    }).then((result) => {
        if (result.isConfirmed) {
            swalWithBootstrapButtons(
                'Deletado!',
                'REGISTRO DELETADO COM SUCESSO!',
                'success'
            )
            var url;
            var urlAtual = window.location.href;
            var urlAtual = urlAtual.split('/');
            if (urlAtual.length > 6) {
                url = '../../DeletarPorta/' + valor;
            } else {
                url = '../DeletarPorta/' + valor;
            }
            location.href = url;
        } else if (
            result.dismiss === swal.DismissReason.cancel
        ) {
            swalWithBootstrapButtons(
                'Cancelado!',
                'O REGISTRO NÃO FOI DELETADO!',
                'error'
            )
        }
    })
}

function alertaAddPorta(){
    Swal.fire({
        icon: 'warning',
        title: 'Host Salvo!',
        text: 'Adicione uma porta ao host!',
    })
}

function temPortaCadastrada(){
    Swal.fire(
        'Ops...',
        'Você precisa adicionar uma porta antes!',
        'error'
      )
}

function temHostOffline(){
    Swal.fire({
        position: 'center',
        icon: 'error',
        title: 'Há host(s) offline(s)',
        width: 600,
        showConfirmButton: false,
        timer: 10000
      })
}