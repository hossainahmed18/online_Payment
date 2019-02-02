$(function(){
      $('#ajaxsubmit').click(function(){
             $.ajax({
                   type: 'POST',
                   url: "/ajaxbillshow",
                   data: {
                          'billno' : $('#billno').val(),
                          'accountno': $('#accountno').val(),
                           'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
                   },
                   success: showResult,
                   dataType: 'html'

             });
      });
});

function showResult(data, textStatus, jqXHR){
     $('#result').html(data);
}