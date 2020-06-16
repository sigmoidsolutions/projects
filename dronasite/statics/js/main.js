function myfunction(text){
    alert(text + " Selected");
}
$(document).ready(function(){
    $(window).scroll(function(){
        var positiontop = $(document).scrollTop();
        console.log(Math.ceil(positiontop))

        if((positiontop > 10) && (positiontop < 213)){
            $('#stream').addClass('animated bounceInLeft');
        }
        
    });
});