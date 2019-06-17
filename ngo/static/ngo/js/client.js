
  $(document).ready(function() { 
    console.log($('.number').text());
    var with0 = 0;
    $( "span.country_label" ).each(function( index ) {
      var w = $( this ).width();
      if (w > with0){
        with0=w;
      }
      console.log( index + ": " + $( this ).text() + with0);
    });

    $("span.country_label" ).css("width", with0+5).css("display", "inline-block")


    $('#id_start_date').datepicker({
    uiLibrary: 'bootstrap4'
    });

    $('#id_end_date').datepicker({
    uiLibrary: 'bootstrap4'
    });

      $('#id_start_time').timepicker();
      $('#id_end_time').timepicker();
    //  $('#id_image').after('<label for="id_image">Choose a file</label>')
     

     //$( "p" ).prepend( "<b>Hello </b>" );
});
