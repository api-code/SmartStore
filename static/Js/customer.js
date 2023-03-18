console.log("inside Js")
$(document).ready(function () {
    $('#customer').DataTable({
        ajax: '../ajax/data/arrays.txt',
    });
});