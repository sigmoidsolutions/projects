function myfunction(text){
    window.location.href = "/"+text;
}
$(document).ready(function(){
    $(window).scroll(function(){
        var positiontop = $(document).scrollTop();
        console.log(Math.ceil(positiontop))

        if((positiontop > 10) && (positiontop < 213)){
            $('#stream-btn').fadeIn("slow");
        }
        
    });
});