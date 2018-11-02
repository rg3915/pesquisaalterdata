$(document).ready( function () {
    $('#myTable1').DataTable();

    $('#myTable2').DataTable( {
        "ajax": "/person/json/",

        "columns": [
          {"data":"cdalterdata"},
          {"data": "name"},
          {"data": "email"},
          {"data": "phone"},
        ],

        columnDefs: [
            {
                targets: [ 0, 1, 2 ],
                className: 'mdl-data-table__cell--non-numeric'
            }
        ],

        "language": {
            "lengthMenu": "Mostrar _MENU_ registros por página",
            "zeroRecords": "Nada encontrado - Sinto muito",
            "info": "Mostrando página _PAGE_ de _PAGES_",
            "infoEmpty": "Nenhum registro disponível",
            "infoFiltered": "(filtered from _MAX_ total records)",
            "paginate": {
              "previous": "Anterior",
              "next": "Próxima"
            },
            "search": "Procure aqui:"
        }

    } );
});


//CÓDIGO PARA INCLUIR BOTÕES EXPORTAR SALVAR E IMPRIMIR
//POR ALGUMMOTIVO ESCONDE A LISTA DE SHOW ENTIRES
//$(document).ready( function () {
//    $('#myTable1').DataTable();
//
//    $('#myTable2').DataTable( {
//        "ajax": "/person/json/",
//
//        "columns": [
//          {"data":"cdalterdata"},
//          {"data": "name"},
//          {"data": "email"},
//          {"data": "phone"},
//        ],
//
//        dom: 'Bfrtip',
//        buttons: [
//            'copy', 'csv', 'excel', 'pdf', 'print'
//        ]
//
//    } );
//});


//ARQUIVOSNECESSÁRIOS PARA MOSTRAR BOTÕES REFERENCIADOS ACIMA

//<script src="https://cdn.datatables.net/buttons/1.5.2/js/dataTables.buttons.min.js"></script>
//<script src="https://cdn.datatables.net/buttons/1.5.2/js/buttons.flash.min.js"></script>
//<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
//<script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.36/pdfmake.min.js"></script>
//<script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.36/vfs_fonts.js"></script>
//<script src="https://cdn.datatables.net/buttons/1.5.2/js/buttons.html5.min.js"></script>
//<script src="https://cdn.datatables.net/buttons/1.5.2/js/buttons.print.min.js"></script>