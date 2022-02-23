$(document).ready(function(){
    //code to be added here
    $('#likes').click(function(){
    var sportid;
    sportid = $(this).attr("data-catid");
    $.get('/like/', {sport_id: sportid}, function(data){
    $('#like_count').html(data);
    $('#likes').hide();
    });
});

})












