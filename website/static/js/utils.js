/**
 * Created by yumendy on 2015/10/23.
 */
function showModal(state, msg) {
    if(state == 'success') {
        $('.modal-content').html("<h3 class='text-success'>" + msg +"</h3>");
    } else if(state == 'muted') {
        $('.modal-content').html("<h3 class='text-muted'>" + msg +"</h3>");
    } else if(state == 'warning') {
        $('.modal-content').html("<h3 class='text-warning'>" + msg +"</h3>");
    } else if(state == 'primary') {
        $('.modal-content').html("<h3 class='text-primary'>" + msg +"</h3>");
    } else if(state == 'info') {
        $('.modal-content').html("<h3 class='text-info'>" + msg +"</h3>");
    } else if(state == 'danger') {
        $('.modal-content').html("<h3 class='text-danger'>" + msg +"</h3>");
    } else {
        $('.modal-content').html("<h3 class='text-danger'>错误！</h3>");
    }
    $('#modal').modal();
}