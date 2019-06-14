
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
});
