$(document).ready(function(){
    $("#actualizar").click(function(){
        $.get("https://intrumentos-musicales-default-rtdb.firebaseio.com/instrumentos.json", 
        function(data){
            $.each(data.instrumentos,function(i,item){
                $("#producto").append(
                    "<tr><td>" + item.id + "</td><td>" +
                    item.imagen + "</td><td><img src='" + 
                    item.nombre +"'></td><td>"+
                    item.precio + "</td></tr>"
                );
            });
        });
        
    });
});