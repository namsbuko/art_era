 jQuery(function(){
    var includes = $('[data-include]');
    jQuery.each(includes, function(){
      var file = 'views/' + $(this).data('include') + '.html';
       jQuery(this).load(file);
    });
  });