function run($) {
  if(!$("#id_featured").is(':checked')) {
    $(".field-quote").hide();
  }

  $("#id_featured").click(function() {
    $(".field-quote").toggle(this.checked);
  });
}

django.jQuery(run.bind(django.jQuery));
